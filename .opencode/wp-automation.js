// WP-Admin Login via Playwright
// Verwendung: Als Referenz fuer Ali's Browser-Automation

async function wpLogin(page, url, username, password) {
  await page.goto(`${url}/wp-login.php`);
  await page.waitForSelector('#user_login');
  await page.fill('#user_login', username);
  await page.fill('#user_pass', password);
  await page.click('#wp-submit');
  await page.waitForSelector('#wpadminbar', { timeout: 10000 });
  return true;
}

// Seite bearbeiten
async function editPage(page, url, pageId) {
  await page.goto(`${url}/wp-admin/post.php?post=${pageId}&action=editor`);
  await page.waitForSelector('.editor-styles-wrapper', { timeout: 15000 });
  return true;
}

// Gutenberg Block hinzufuegen (Heading)
async function addHeadingBlock(page, text, level = 2) {
  // Plus-Icon klicken um neuen Block hinzuzufuegen
  const addButton = await page.$('.block-list-appender .block-list-appender-button');
  if (addButton) await addButton.click();
  
  // Block-Suche oeffnen
  await page.keyboard.type(`Heading ${level}`);
  await page.keyboard.press('Enter');
  
  // Text eingeben
  await page.keyboard.type(text);
}

// Gutenberg Block: Paragraph
async function addParagraphBlock(page, text) {
  const addButton = await page.$('.block-list-appender .block-list-appender-button');
  if (addButton) await addButton.click();
  
  await page.keyboard.type('Paragraph');
  await page.keyboard.press('Enter');
  await page.keyboard.type(text);
}

// Gutenberg Block: Button/CTA
async function addButtonBlock(page, text, url) {
  const addButton = await page.$('.block-list-appender .block-list-appender-button');
  if (addButton) await addButton.click();
  
  await page.keyboard.type('Buttons');
  await page.keyboard.press('Enter');
  await page.keyboard.type(text);
  
  // URL im Block setzen
  const linkButton = await page.$('.block-editor-link-input');
  if (linkButton) {
    await linkButton.fill(url);
    await page.keyboard.press('Enter');
  }
}

// CSS im Customizer einfuegen
async function addCustomCSS(page, css) {
  await page.goto('/wp-admin/customize.php');
  await page.waitForSelector('#customize-controls');
  
  // "Zusaetzliches CSS" klicken
  const cssSection = await page.$('[data-id="custom_css"]');
  if (cssSection) await cssSection.click();
  
  // CSS eingeben
  const editor = await page.$('.CodeMirror');
  if (editor) {
    await editor.click();
    await page.keyboard.type(css);
  }
}

// Plugin installieren
async function installPlugin(page, pluginSlug) {
  await page.goto('/wp-admin/plugin-install.php');
  await page.waitForSelector('#search-plugins');
  
  await page.fill('#search-plugins', pluginSlug);
  await page.click('#search-submit');
  
  await page.waitForSelector('.plugin-card');
  
  // Erstes Ergebnis installieren
  const installBtn = await page.$('.install-now');
  if (installBtn) {
    await installBtn.click();
    await page.waitForSelector('.activate-now', { timeout: 30000 });
    
    // Aktivieren
    const activateBtn = await page.$('.activate-now');
    if (activateBtn) await activateBtn.click();
  }
}

// SEO Meta-Daten setzen (Yoast)
async function setYoastMeta(page, title, description) {
  // Yoast Meta-Box Scrollen
  await page.evaluate(() => {
    const metaBox = document.querySelector('#yoast-seo-meta-box');
    if (metaBox) metaBox.scrollIntoView();
  });
  
  // Focus Keyphrase
  const focusInput = await page.$('#yoast-focus-keyword-input');
  if (focusInput) await focusInput.fill(title.split(' ')[0]);
  
  // SEO Title
  const titleInput = await page.$('#yoast-seo-title');
  if (titleInput) await titleInput.fill(title);
  
  // Meta Description
  const descInput = await page.$('#yoast-meta-description');
  if (descInput) await descInput.fill(description);
}

// Seitenanalyse (DOM-basiert)
async function analyzePage(page) {
  return await page.evaluate(() => {
    const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => ({
      level: h.tagName,
      text: h.textContent.trim()
    }));
    
    const images = Array.from(document.querySelectorAll('img')).map(img => ({
      src: img.src,
      alt: img.alt,
      width: img.naturalWidth,
      height: img.naturalHeight
    }));
    
    const links = Array.from(document.querySelectorAll('a[href]')).map(a => ({
      text: a.textContent.trim(),
      href: a.href
    }));
    
    const meta = {
      title: document.title,
      description: document.querySelector('meta[name="description"]')?.content || '',
      ogTitle: document.querySelector('meta[property="og:title"]')?.content || '',
      ogDescription: document.querySelector('meta[property="og:description"]')?.content || ''
    };
    
    return { headings, images, links, meta };
  });
}

module.exports = {
  wpLogin,
  editPage,
  addHeadingBlock,
  addParagraphBlock,
  addButtonBlock,
  addCustomCSS,
  installPlugin,
  setYoastMeta,
  analyzePage
};
