from typing import Dict, Optional

import streamlit as st

from utils.css import light_input_text, result_text_str
from utils.state import clear_state

import requests


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

            light_input_text(settings["theme"]["secondaryBackgroundColor"])
            title_result = st.markdown(
                result_text_str("Would you put something funny?"), unsafe_allow_html=True
            )

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

            st.text("")
            st.text("")
            st.text("")

            if detect:
                with st.spinner("Computing sentence..."):
                    body = {"sentences": [sentence]}
                    response = requests.post(
                        "http://backend:8080/predictions", json=body
                    )
                    is_humor = response.json()[0][0]

                    if is_humor:
                        light_input_text("green")
                        title_result.markdown(
                            result_text_str("Haha, that was really funny!", "green"),
                            unsafe_allow_html=True,
                        )
                    else:
                        light_input_text("red")
                        title_result.markdown(
                            result_text_str("Huh, not funny at all...", "red"),
                            unsafe_allow_html=True,
                        )
