import streamlit as st

from .config import load_config


def load_css():
    config = load_config()

    with open("styles/principal.css") as f:
        st.markdown(
            f"""
                <style>
                    :root {{
                        --primaryColor: {config["theme"]["primaryColor"]};
                        --backgroundColor: {config["theme"]["backgroundColor"]};
                        --secondaryBackgroundColor: {config["theme"]["secondaryBackgroundColor"]};
                        --textColor: {config["theme"]["textColor"]};
                        --accentTextColor: {config["theme"]["accentTextColor"]};                        
                    }}
                    {f.read()}
                </style>
            """,
            unsafe_allow_html=True,
        )


def light_input_text(color: str):
    css = f"""
            <style>
                div[data-baseweb="input"] {{
                    border-color: {color};
                }}
            </style>
        """

    st.markdown(css, unsafe_allow_html=True)
