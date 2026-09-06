# SEO & Performance Checkliste fuer gesolarcom

## Vor jeder Seiten-Aenderung

### Technisches SEO
- [ ] URL-Struktur sauber (keine Zahlen/Slugs wie /10-2/)
- [ ] Canonical-Tag korrekt
- [ ] SSL aktiv (HTTPS)
- [ ] mobile responsiveness (Viewport-Meta)
- [ ] Ladezeit < 3 Sekunden
- [ ] Bilder optimiert (WebP, lazy load)

### On-Page SEO
- [ ] Unique Meta-Titel (50-60 Zeichen)
- [ ] Unique Meta-Beschreibung (150-160 Zeichen)
- [ ] H1 nur einmal pro Seite
- [ ] H2-H6 hierarchisch
- [ ] Alt-Tags bei allen Bildern
- [ ] Internal Links (mindestens 2-3 pro Seite)
- [ ] CTA auf jeder Seite

### Content-Qualitaet
- [ ] Texte verstaendlich (Flesch > 60)
- [ ] Keine Rechtschreibfehler
- [ ] Fakten korrekt (Preise, Gesetze, Adressen)
- [ ] Keyword自然 eingebaut (nicht ueberladen)
- [ ] Nutzer hat klaren naechsten Schritt

### Schema-Markup
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "GE-Solar GbR",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Bahnhofstraße 58a",
    "addressLocality": "Gensingen",
    "postalCode": "55457",
    "addressCountry": "DE"
  },
  "url": "https://gesolarcom.wpcomstaging.com",
  "telephone": "ECHTE_NUMMER",
  "openingHours": "Mo-Fr 09:00-18:00"
}
```

## Core Web Vitals Ziele

| Metrik | Ziel | Aktuell (geschaetzt) |
|---|---|---|
| LCP | < 2.5s | unbekannt |
| FID | < 100ms | unbekannt |
| CLS | < 0.1 | unbekannt |
| TTFB | < 800ms | unbekannt |

## WooCommerce SEO

- [ ] Produktseiten mit Unique-Beschreibungen
- [ ] Kategorie-Beschreibungen
- [ ] Breadcrumbs aktiviert
- [ ] Produkt-Bewertungen aktiviert
- [ ] Strukturierte Daten fuer Produkte
- [ ] Interne Verlinkung Shop <-> Blog

## Tools zur Pruefung

1. **Google PageSpeed Insights** - https://pagespeed.web.dev/
2. **Google Search Console** - Indexierung pruefen
3. **Screaming Frog** - technisches Crawl
4. **GTmetrix** - Performance-Analyse
5. **Browser DevTools** - Lighthouse Audit
