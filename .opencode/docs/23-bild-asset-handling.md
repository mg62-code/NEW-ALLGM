# Bild & Asset Handling fuer gesolarcom

## Quellen fuer Produktbilder

### Hersteller (kostenlos fuer Haendler)
- Trina Solar: Media Kit / Partner Portal
- Jinko Solar: Partner Portal
- Growatt: Download Center
- Huawei: FusionSolar Portal
- Sungrow: Partner Portal

### Alternative Quellen
- Unsplash.com (kostenlos, Commercial Use OK)
- Pexels.com (kostenlos, Commercial Use OK)
- Eigene Fotos (beste Loesung)
- KI-generiert (DALL-E, Midjourney) - Vorsicht bei Lizenz

## Bildgroessen WordPress

| Zweck | Empfohlene Groesse |
|---|---|
| Hero-Banner | 1920 x 800 px |
| Produktbild | 800 x 800 px |
| Thumbnail | 300 x 300 px |
| Blog-Featured | 1200 x 630 px |
| Social Share | 1200 x 630 px |

## Upload via Playwright

```
1. WP-Admin -> Medien -> Medien hinzufuegen
2. Datei-Upload-Button klicken
3. Datei auswaehlen
4. Warte auf Upload-Ende
5. Alt-Text eingeben (SEO-relevant!)
6. Beschreibung eingeben
7. In Seite einfuegen
```

## Alt-Text Formel

```
[Produktname] - [Kategorie] - [Farbe/Material] - [Besonderheit]

Beispiel: "Trina Solar Vertex S+ 430W Solarmodul - Monokristallin - Schwarz - Hocheffizient"
```

## Bildoptimierung

- Format: WebP (fuer browsers) oder JPG (fuer Kompatibilitaet)
- Qualitaet: 80-85%
- Dateigroesse: < 200 KB pro Bild
- Lazy Loading: WordPress 5.5+ standardmaessig aktiv

## CSS fuer Bildergalerie

```css
.produkt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}

.produkt-card img {
  width: 100%;
  height: auto;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 8px;
}
```

## Logo

- Aktuelles Logo: wp-content/uploads/2023/03/logo.png
- Empfohlen: SVG oder hochaufloesendes PNG mit Transparenz
- Spezifikation: 200x200px minimum, ideal 500x500px
