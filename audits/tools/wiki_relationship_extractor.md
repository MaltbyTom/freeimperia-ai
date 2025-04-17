# Audit: wiki_relationship_extractor_utf8.py

**Purpose:** Extracts linked entities from Free Imperia wiki pages and outputs relationships in .jsonl format.

**Invocation:** 
```bash
python tools/wiki_relationship_extractor_utf8.py input_file.txt output.jsonl
```

**Outputs:** Structured entity relationship JSONL.

**Status:** ✅ Active  
**Date Added:** Pre-2025  
**Maintainer:** MaltbyTom  
**Known Issues:** Requires proper UTF-8 input.  

**Change Log:**
- 2025-04-14: Updated to preserve and use DocuWiki links.