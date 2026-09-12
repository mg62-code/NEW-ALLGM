
import os
import glob
import json
import re
from tqdm import tqdm
import vertexai
from vertexai.language_models import TextEmbeddingModel

# --- Konfiguration ---
# BITTE DEINE PROJEKTDATEN EINTRAGEN
GCP_PROJECT_ID = "project-0911409a-d416-4c2b-801"  # Deine Google Cloud Projekt-ID
GCP_LOCATION = "europe-west3"           # Deine Google Cloud Region, z.B. "us-central1"

MODEL_NAME = "text-embedding-004"
OUTPUT_FILE = "embeddings.jsonl"
CHUNK_SIZE_TARGET = 500
CHUNK_OVERLAP = 50
BATCH_SIZE = 50 # Maximal erlaubte Batch-Größe für das text-embedding-004 Modell

# --- Zu verarbeitende Dateien ---
# Statische Liste von Dateien im Hauptverzeichnis
STATIC_FILES = [
    "README.md",
    "Skill Anweisung aeronewsFRA.txt",
    "Anweisung Instagram OpenCode Aufbau.txt",
    "Aufbau MusterVorlage automation.txt"
]

# Dynamische Liste von Dateien über glob-Muster
DOCS_PATTERN = ".opencode/docs/**/*.md"

def get_all_filepaths():
    """Sammelt alle zu verarbeitenden Dateipfade."""
    filepaths = [fp for fp in STATIC_FILES if os.path.exists(fp)]
    
    # Durchsuche das docs-Verzeichnis rekursiv
    doc_files = glob.glob(DOCS_PATTERN, recursive=True)
    filepaths.extend(doc_files)
    
    print(f"Gefundene Dateien: {len(filepaths)}")
    return filepaths

def chunk_text(content: str, filepath: str) -> list[dict]:
    """
    Teilt den Text in sinnvolle Abschnitte (Chunks) basierend auf Absätzen.
    Versucht, die Zielgröße von CHUNK_SIZE_TARGET nicht stark zu überschreiten.
    """
    chunks = []
    # Grobe Trennung an Absätzen oder expliziten Trennern
    paragraphs = re.split(r'\n\n+|\n---\n', content)
    
    current_chunk_text = ""
    chunk_id_counter = 0

    for p in paragraphs:
        p = p.strip()
        if not p:
            continue

        # Wenn der nächste Absatz den Chunk zu groß machen würde, den aktuellen speichern
        if len(current_chunk_text) + len(p) + 1 > CHUNK_SIZE_TARGET and current_chunk_text:
            chunks.append({
                "id": f"{os.path.basename(filepath)}-{chunk_id_counter}",
                "text": current_chunk_text,
                "metadata": {"source": filepath}
            })
            chunk_id_counter += 1
            # Überlappung hinzufügen, um Kontext zu erhalten
            overlap_text = ' '.join(current_chunk_text.split()[-CHUNK_OVERLAP:])
            current_chunk_text = overlap_text + " " + p
        else:
            if current_chunk_text:
                current_chunk_text += "\n\n" + p
            else:
                current_chunk_text = p

    # Den letzten verbleibenden Chunk hinzufügen
    if current_chunk_text:
        chunks.append({
            "id": f"{os.path.basename(filepath)}-{chunk_id_counter}",
            "text": current_chunk_text,
            "metadata": {"source": filepath}
        })
        
    return chunks

def main():
    """Hauptfunktion zur Erstellung der Embeddings."""
    print("Starte Embedding-Erstellung...")
    
    # 1. Vertex AI initialisieren
    try:
        vertexai.init(project=GCP_PROJECT_ID, location=GCP_LOCATION)
        model = TextEmbeddingModel.from_pretrained(MODEL_NAME)
        print(f"Vertex AI initialisiert. Modell: {MODEL_NAME}")
    except Exception as e:
        print(f"Fehler bei der Initialisierung von Vertex AI: {e}")
        print("Bitte stelle sicher, dass du authentifiziert bist (`gcloud auth application-default login`) und die korrekte Projekt-ID/Location eingetragen hast.")
        return

    # 2. Alle Chunks aus allen Dateien sammeln
    all_chunks = []
    filepaths = get_all_filepaths()
    for filepath in filepaths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            file_chunks = chunk_text(content, filepath)
            all_chunks.extend(file_chunks)
        except Exception as e:
            print(f"Fehler beim Lesen oder Verarbeiten der Datei {filepath}: {e}")
    
    if not all_chunks:
        print("Keine Chunks zum Verarbeiten gefunden. Skript wird beendet.")
        return

    print(f"Gesamtzahl der Chunks: {len(all_chunks)}")

    # 3. Embeddings in Batches erstellen und in JSONL speichern
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
        # tqdm für Fortschrittsanzeige
        for i in tqdm(range(0, len(all_chunks), BATCH_SIZE), desc="Erstelle Embeddings"):
            batch = all_chunks[i:i + BATCH_SIZE]
            texts_to_embed = [chunk['text'] for chunk in batch]
            
            try:
                embeddings = model.get_embeddings(texts_to_embed)
                
                for chunk_data, embedding in zip(batch, embeddings):
                    # Das finale Objekt für die JSONL-Datei erstellen
                    output_obj = {
                        "id": chunk_data["id"],
                        "embedding": embedding.values,
                        "metadata": {
                            "source": chunk_data["metadata"]["source"],
                            "text": chunk_data["text"]
                        }
                    }
                    f_out.write(json.dumps(output_obj) + '\n')
                    
            except Exception as e:
                print(f"Fehler bei der Erstellung der Embeddings für Batch {i//BATCH_SIZE}: {e}")

    print(f"\nEmbedding-Erstellung abgeschlossen. {len(all_chunks)} Chunks wurden in '{OUTPUT_FILE}' gespeichert.")

if __name__ == "__main__":
    main()
