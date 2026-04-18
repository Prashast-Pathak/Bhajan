/**
 * Google Apps Script Webhook for one pillar sheet.
 *
 * Steps:
 * 1) Open Google Sheet -> Extensions -> Apps Script
 * 2) Paste this file and save
 * 3) Deploy -> New Deployment -> Web App
 *    - Execute as: Me
 *    - Access: Anyone with link
 * 4) Copy Web App URL and set as GSHEET_WEBHOOK_<PILLAR>
 */

function doPost(e) {
  try {
    var body = JSON.parse(e.postData.contents || '{}');
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

    // Header row (created once)
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        'updated_at', 'pillar', 'action', 'slug', 'title', 'raw_item_json'
      ]);
    }

    sheet.appendRow([
      body.updated_at || '',
      body.pillar || '',
      body.action || '',
      body.slug || '',
      body.title || '',
      JSON.stringify(body.raw_item || {})
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
