import json
import re
import spacy

nlp = spacy.load("en_core_web_md")

with open("output/wiki_pages.json", "r", encoding="utf-8") as f:
    wiki = json.load(f)

print(f"✅ Loaded {len(wiki)} pages.")

# Show first 1-2 pages with sentence + link detection
def extract_docuwiki_links(text):
    return re.findall(r"\[\[(.*?)\]\]", text)

def clean_links(raw_text):
    return re.sub(r"\[\[(.*?)\]\]", lambda m: m.group(1).split("|")[0], raw_text)

for i, (title, text) in enumerate(wiki.items()):
    print(f"\n📄 Page: {title}")
    links = extract_docuwiki_links(text)
    print("🔗 Links:", links)

    clean = clean_links(text)
    doc = nlp(clean)
    sents = [s.text.strip() for s in doc.sents]
    print(f"🧠 Extracted {len(sents)} sentences:")
    for s in sents[:5]:
        print("-", s)
    if i >= 1:
        break