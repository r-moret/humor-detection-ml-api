from typing import Dict

import streamlit as st


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
            )

            st.text("")

            l_col, r_col = st.columns(2)
            detect = l_col.button("Detect")
            clear = r_col.button("Clear")
