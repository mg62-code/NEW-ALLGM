
import functions_framework
import os
from google.cloud import storage
from PIL import Image
import io

# Ziel-Bucket fuer die verarbeiteten Bilder
DESTINATION_BUCKET_NAME = "aeronewsfra-media-public"

# Initialisiere den Google Cloud Storage Client
storage_client = storage.Client()

@functions_framework.cloud_event
def process_image_upload(cloud_event):
    """
    Diese Funktion wird durch das Hochladen einer Datei in einen Cloud Storage Bucket ausgeloest.
    Sie laedt das Bild herunter, konvertiert es in eine 800px breite WebP-Version und
    speichert das Ergebnis in einem anderen Bucket.
    """
    data = cloud_event.data

    source_bucket_name = data["bucket"]
    file_name = data["name"]

    print(f"Verarbeite Datei: {file_name} aus Bucket: {source_bucket_name}.")

    # --- 1. Bild herunterladen ---
    source_bucket = storage_client.bucket(source_bucket_name)
    source_blob = source_bucket.blob(file_name)
    
    # Lade das Bild in den Speicher
    image_bytes = source_blob.download_as_bytes()
    
    try:
        # Oeffne das Bild mit Pillow
        img = Image.open(io.BytesIO(image_bytes))
        print(f"Bild {file_name} erfolgreich geladen. Format: {img.format}, Groesse: {img.size}")

        # --- 2. Bild verarbeiten ---
        
        # Behalte das Seitenverhaeltnis bei
        target_width = 800
        width_percent = (target_width / float(img.size[0]))
        target_height = int((float(img.size[1]) * float(width_percent)))
        
        # Aendere die Groesse des Bildes
        img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        print(f"Bild auf neue Groesse geaendert: {img.size}")

        # Speichere das Bild im WebP-Format in einem In-Memory-Buffer
        webp_buffer = io.BytesIO()
        img.save(webp_buffer, "WEBP", quality=85)
        webp_buffer.seek(0) # Setze den Pointer auf den Anfang des Buffers

        print("Bild erfolgreich ins WebP-Format konvertiert.")

        # --- 3. Verarbeitetes Bild hochladen ---
        
        # Definiere den neuen Dateinamen mit .webp Endung
        base_name, _ = os.path.splitext(file_name)
        destination_file_name = f"{base_name}.webp"

        destination_bucket = storage_client.bucket(DESTINATION_BUCKET_NAME)
        destination_blob = destination_bucket.blob(destination_file_name)

        # Lade den WebP-Buffer hoch
        destination_blob.upload_from_file(webp_buffer, content_type="image/webp")
        
        print(f"Verarbeitetes Bild erfolgreich in Bucket {DESTINATION_BUCKET_NAME} unter {destination_file_name} gespeichert.")

    except Exception as e:
        print(f"FEHLER bei der Verarbeitung von {file_name}: {e}")
        # Hier koennte eine Fehlerbehandlung ergaenzt werden, z.B. eine Benachrichtigung

