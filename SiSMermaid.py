from streamlit.components.v1 import html
from pathlib import Path
from functools import lru_cache


class SiSMermaid:
    '''
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
    '''

    def __init__(self, mermaid_js_file: str = "mermaid.min.js"):
        self.mermaid_js_file = mermaid_js_file

    @lru_cache(maxsize=None)
    def load_mermaid_js(self) -> str:
        try:
            js_path = Path(self.mermaid_js_file)
            with open(js_path, "r", encoding="utf-8") as js_file:
                return js_file.read()
        except Exception:
            raise FileNotFoundError(
                "Mermaid JS file not found. Please verify the file path."
            )

    def sis_mermaid(
        self, mermaid_source: str, scrolling: bool = True, height: int = 900
    ) -> None:
        html_template = f"""
                        <script type="text/javascript" >{self.load_mermaid_js()}</script>
                        <script> 
                        var config = {{
                            startOnLoad: true,
                            flowchart: {{ useMaxWidth: true, htmlLabels: true}},
        
                        }}
                        mermaid.initialize(config);
                        </script>
                        
                            <div class="mermaid" id="diagram">
                                   {mermaid_source} 
                                </div>
                        """
        html(html_template, scrolling=scrolling, height=height)
