import json

def generate_ssr(item, itype):
    html = f"<h1>{item.get('title_hindi') or item.get('title_english') or item.get('name_english') or item.get('name_hindi') or 'Title'}</h1>\n"
    html += f"<p>{item.get('description_english') or item.get('intro_english') or item.get('theme_english') or ''}</p>\n"
    
    if "verses" in item:
        for v in item["verses"]:
            html += "<div class='verse-block'>\n"
            if "lines" in v:
                for l in v["lines"]:
                    html += f"<p>{l.get('hindi', '')}</p>\n"
                    html += f"<p>{l.get('meaning_hindi', '')}</p>\n"
                    html += f"<p>{l.get('meaning_en', '')}</p>\n"
            elif "sanskrit" in v: # For Gita
                html += f"<p>{v.get('sanskrit', '')}</p>\n"
                html += f"<p>{v.get('hindi_translation', '')}</p>\n"
                html += f"<p>{v.get('english_translation', '')}</p>\n"
            html += "</div>\n"
            
    if "quotes" in item: # For wisdom
        for q in item["quotes"]:
            html += f"<blockquote>{q.get('quote_english', '')}</blockquote>\n"
            
    return f'<div id="ssr-content" style="padding: 20px;">{html}</div>'

print("Test SSR script created.")
