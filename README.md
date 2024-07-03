# SiSMermaid

### Loads Mermaid.js into Streamlit-in-Snowflake for easy diagrams.
---
Requirements:
- Upload the provided `mermaid.min.js` and `SiSMermaid.py` files into the Snowflake Stage where your Streamlit-in-Snowflake app is hosted.
- Adjust the relative path if needed during class initialization (optional).

---
Usage:
Import and use as follows:
```python
from SiSMermaid import SiSMermaid

mmd=SiSMermaid()
mermaid_code = """
 flowchart LR;
 a-->b
 b-->c
 a-->d
 """
mmd.sis_mermaid(mermaid_source=mermaid_code)
```

To specify a new path for the mermaid.js file in your application stage, update
the `mermaid_js_file` attribute for the SiSMermaid class.

```python
mmd=SiSMermaid(mermaid_js_file ='yourpath/mermaid.min.js')
