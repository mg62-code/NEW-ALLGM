---
dokument_id: DOC-20
titel: WordPress/WooCommerce Expert-Workflow fuer Ali
version: "1.0"
status: arbeitsdokument
owner: Dev-Ali
aktualisiert: 2026-09-06
geltung: alle WordPress-Umbauarbeiten auf gesolarcom
---

# WordPress/WooCommerce Expert-Workflow

## 1. Zweck

Dieses Dokument definiert Ali's WordPress-Expertise als Experte fuer den
aktiven Betrieb, Umbau und die Optimierung der gesolarcom Website.
Ali fuehrt alle Aenderungen direkt via Playwright im Browser aus.

## 2. Technische Plattform

- **CMS:** WordPress.com (wpcomstaging)
- **Shop:** WooCommerce
- **Ziel:** https://gesolarcom.wpcomstaging.com/
- **Admin-Zugang:** WP-Admin via Playwright Browser
- **Operand:** Mert Genc (Eigentuemer)

## 3. Ali's WordPress-Kompetenzprofil

### 3.1 Browser-Automation (Playwright)
Ali kann via Playwright:
- Im WP-Admin einloggen und navigieren
- Seiten/Posts im Gutenberg-Editor erstellen und bearbeiten
- Theme-Customizer oeffnen und anpassen
- CSS im Customizer oder Theme-Editor einfuegen
- Plugins suchen, installieren, aktivieren und konfigurieren
- WooCommerce-Einstellungen anpassen
- Medien hochladen und zuweisen
- Menues erstellen und bearbeiten
- Widgets und Block-Inhalte verwalten
- Permalinks anpassen
- SEO-Plugins konfigurieren

### 3.2 Content-Erstellung
Ali erstellt:
- SEO-optimierte Texte (Meta-Titel, Beschreibungen, H1-H6)
- Produktbeschreibungen (B2C und B2B)
- Landingpage-Content
- FAQ-Bloecke
- Trust-Signale (Testimonials, Referenzen, Zertifikate)
- Blog-Artikel (Ratgeber, Tipps, News)
- CTA-Texte (Call-to-Action)
- Legal-Pages (Impressum, Datenschutz, AGB)

### 3.3 Layout & Design
Ali bewertet und optimiert:
- Typografie (Schriftarten, Groessen, Abstaende)
- Farbschema (Brand-Konsistenz)
- Spacing und Grid-Systeme
- Mobile Responsiveness
- Call-to-Action Platzierung
- Informationsarchitektur
- Nutzerfuehrung und Conversion-Pfade

### 3.4 SEO & Performance
Ali implementiert:
- Yoast/RankMath Konfiguration
- Meta-Titel und -Beschreibungen pro Seite
- Schema-Markup (LocalBusiness, Product, FAQ)
- Bildoptimierung (WebP, Alt-Tags, Compression)
- Internal Linking Strategie
- Permalink-Struktur
- Core Web Vitals Pruefung
- Sitemap-Generierung

### 3.5 WooCommerce
Ali konfiguriert:
- Produktkategorien und Tags
- Zahlungsarten (PayPal, Stripe, Vorkasse)
- Versandprofile und Preise
- Steuerklassen (0% MwSt. nach §12 Abs.3 UStG)
- B2B vs. B2C Trennung
- Gutscheine und Rabatte
- Bestellablauf und Checkout
- E-Mail-Templates
- Lagerbestand und Verfügbarkeit

### 3.6 Sicherheit & Compliance
Ali stellt sicher:
- DSGVO-konformes Cookie-Banner
- Impressumspflicht
- Datenschutzerklaerung
- SSL-Zertifikat aktiv
- Login-Sicherheit
- Backup-Strategie
- Plugin-Updates

## 4. Playwright WP-Admin Ablaeufe

### 4.1 Einloggen
```
1. Navigiere zu https://gesolarcom.wpcomstaging.com/wp-login.php
2. Waerte auf Login-Formular
3. Benutzername + Passwort eingeben (vom Nutzer erhalten)
4. Auf "Anmelden" klicken
5. Pruefe ob WP-Admin-Bar sichtbar = Login erfolgreich
```

### 4.2 Seite bearbeiten (Gutenberg)
```
1. Navigiere zu https://gesolarcom.wpcomstaging.com/wp-admin/edit.php
2. Klicke auf den zu bearbeitenden Seitentitel
3. Warte auf Gutenberg-Editor
4. Blockstruktur via DOM analysieren
5. Bestehende Bloecke lesen und verstehen
6. Neue Bloecke einfuegen oder bestehende aendern
7. Vorschau pruefen
8. Speichern/Publizieren
```

### 4.3 Theme-Customizer
```
1. Navigiere zu https://gesolarcom.wpcomstaging.com/wp-admin/customize.php
2. Waerte auf Customizer-Ladevorgang
3. Sidebar-Navigation via DOM ansprechen
4. Einstellungen aenderen (Farben, Typo, Layout)
5. Live-Vorschau pruefen
6. Speichern
```

### 4.4 CSS einbinden
```
1. Customizer oeffnen
2. "Zusaetzliches CSS" Bereich waehlen
3. CSS-Code einfuegen
4. Vorschau pruefen
5. Veröffentlichen
```

### 4.5 Plugin installieren
```
1. Navigiere zu https://gesolarcom.wpcomstaging.com/wp-admin/plugin-install.php
2. Pluginsuche eingeben
3. "Jetzt installieren" klicken
4. "Aktivieren" klicken
5. Plugin-Einstellungen konfigurieren falls noetig
```

### 4.6 Neue Seite erstellen
```
1. Navigiere zu https://gesolarcom.wpcomstaging.com/wp-admin/post-new.php?post_type=page
2. Titel eingeben
3. Content via Gutenberg-Blocks aufbauen
4. Sidebar-Einstellungen (Slug, Bild, Template)
5. Veröffentlichen
```

## 5. Content-Generierungs-Workflow

### Fuer jede Seite:
```
1. Ziel der Seite definieren (Was soll der Nutzer tun?)
2. Informationsarchitektur entwerfen (Was kommt wohin?)
3. Texte mit KI generieren (Grok oder Ali)
4. Texte gegen SEO-Regeln pruefen
5. Layout/Blocks im Gutenberg zusammenbauen
6. Bilder/Assets einbinden
7. CTA platzieren
8. Mobile Ansicht pruefen
9. SEO-Meta eintragen
10. Veröffentlichen
```

## 6. Seitenstruktur (aktuell)

| Seite | URL | Status |
|---|---|---|
| Startseite | / | Aktiv, aber optimierungsbeduerftig |
| Allgemein | /allgemein/ | Vorhanden |
| Über Uns | /10-2/ueber-uns/ | Vorhanden, URL unguenstig |
| Solarmodule | /10-2/ | Vorhanden, URL unguenstig |
| Wechselrichter | /wechselrichter-im-angebot/ | Vorhanden |
| Kontakt | /zentrierte-uberschrift-mit-kontaktformular/ | Vorhanden, URL unguenstig |
| Ersparnisse | /?page_id=300 | Vorhanden, URL unguenstig |
| Shop | /shop/ | WooCommerce aktiv |
| Mein Konto | /mein-konto/ | WooCommerce Standard |
| Warenkorb | /warenkorb/ | WooCommerce Standard |
| Kasse | /kasse/ | WooCommerce Standard |

## 7. Bekannte Probleme

1. Platzhalter-Telefonnummer (+1234567890)
2. Veraltetes Copyright (2024)
3. Placeholder-Bilder bei Produkten
4. Unsaubere URL-Struktur
5. Kein Impressum/Datenschutz sichtbar
6. Keine Meta-Beschreibungen
7. Keine Trust-Signale
8. Kein Blog
9. Basisches Theme
10. Kein Cookie-Banner

## 8. Naechste Schritte

1. WP-Login vom Nutzer erhalten
2. Vollstaendige Seitenanalyse durchfuehren
3. Priorisierte Massnahmenliste erstellen
4. Schrittweise Umsetzung pro Seite
