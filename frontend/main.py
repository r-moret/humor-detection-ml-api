import streamlit as st
from streamlit_option_menu import option_menu
from views import HomeView, PredictView

st.set_page_config(
    page_title="Humor Detection",
    page_icon="🤗",
    layout="wide",
)


class Menu:
    HOME = "Home"
    OPTION1 = "Predict"


with st.sidebar:
    view = option_menu(
        menu_title="Menu",
        menu_icon="back",
        options=[Menu.HOME, Menu.OPTION1],
    )

if view == Menu.HOME:
    HomeView.view()
elif view == Menu.OPTION1:
    PredictView.view()
