from typing import Optional

import streamlit as st


def clear_state(attribute: Optional[str] = None):
    def inner_clear_state():
        if attribute:
            st.session_state[attribute] = ""
        else:
            for att in st.session_state.keys():
                del st.session_state[att]

    return inner_clear_state
