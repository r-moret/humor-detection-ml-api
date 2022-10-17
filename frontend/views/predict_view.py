from typing import Dict

import streamlit as st

from utils.css import light_input_text
from utils.state import clear_state


class PredictView:
    @classmethod
    def view(cls, settings: Dict):
        with st.container():
            st.markdown(
                f"""
                    <h1 style='text-align: center; font-size: 400%'>
                        Humor Detection
                    </h1>
                    <h4 style='text-align: center'>
                        with 🤗 Hugging Face <span style='color: {settings["theme"]["primaryColor"]}'>ALBERT</span> model
                    </h4>
                """,
                unsafe_allow_html=True,
            )

            st.text("")
            st.text("")
            st.text("")

            _, center_col, _ = st.columns([1, 3, 1])
            sentence = center_col.text_input(
                "Sentence to detect",
                placeholder="Some funny joke here... or maybe just not",
                label_visibility="collapsed",
                key="sentence",
            )

            st.text("")

            l_col, r_col = st.columns(2)
            detect = l_col.button("Detect")
            r_col.button("Clear", on_click=clear_state("sentence"))

            if detect:
                if sentence == "pos":
                    light_input_text("green")
                elif sentence == "neg":
                    light_input_text("red")
