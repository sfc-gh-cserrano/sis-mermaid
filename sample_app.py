import streamlit as st
from streamlit.components.v1 import html
from SiSMermaid import SiSMermaid

st.set_page_config(layout="wide")

input_area, display_area = st.columns(2, gap="large")
with input_area:
    st.subheader("Input", anchor=False)
    with st.container(height=900):
        mmd = st.text_area(
            "Enter your mermaid Code", label_visibility="collapsed", height=300
        )
        with st.expander("Flowchart Sample"):
            st.code(
                """
            flowchart LR;
            A[Hard] -->|Text| B(Round)
            B --> C{Decision}
            C -->|One| D[Result 1]
            C -->|Two| E[Result 2]"""
            )
        with st.expander("Journey Sample"):
            st.code(
                """
              journey
        title My working day
        section Go to work
          Make tea: 5: Me
          Go upstairs: 3: Me
          Do work: 1: Me, Cat
        section Go home
          Go downstairs: 5: Me
          Sit down: 3: Me"""
            )
        with st.expander("State Sample"):
            st.code(
                """
            stateDiagram-v2
                [*] --> Still
                Still --> [*]
                Still --> Moving
                Moving --> Still
                Moving --> Crash
                Crash --> [*]"""
            )
        with st.expander("Class Based Definitions"):
            st.code(
                """
            flowchart LR
            A:::foo & B:::bar --> C:::foobar
            classDef foo stroke:#f00
            classDef bar stroke:#0f0
            classDef foobar stroke:#00f"""
            )
        with st.expander("Styling"):
            st.code(
                """
            flowchart LR
            id1(Start)-->id2(Stop)
            style id1 fill:#f9f,stroke:#333,stroke-width:4px
            style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5"""
            )

with display_area:
    st.subheader("Output", anchor=False)
    with st.container(height=900):
        if mmd:
            SiSMermaid().sis_mermaid(mermaid_source=mmd)
