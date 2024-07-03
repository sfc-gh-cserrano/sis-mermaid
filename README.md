# SiSMermaid

### Loads Mermaid.js into Streamlit-in-Snowflake for easy diagrams.
---
Requirements:
- Include the provided mermaid.js file in a Snowflake Stage where your streamlit app is hosted.
- Adjust the relative path if needed during class initialization.

---
Usage:
If mermaid.js file is located at root level with app and module:
```python
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
