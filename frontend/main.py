import streamlit as st
from streamlit_option_menu import option_menu

from utils import load_config, load_css
from views import HomeView, MetricsView, PredictView

st.set_page_config(
    page_title="Humor Detection",
    page_icon="🤗",
    layout="wide",
)

load_css()
config = load_config()


class Menu:
    HOME = "Home"
    OPTION1 = "Predict"
    OPTION2 = "Metrics"


with st.sidebar:
    view = option_menu(
        menu_title="Menu",
        menu_icon="back",
        options=[Menu.HOME, Menu.OPTION1, Menu.OPTION2],
        styles={
            "nav-link-selected": {"color": config["theme"]["accentTextColor"]},
        },
    )

if view == Menu.HOME:
    HomeView.view()
elif view == Menu.OPTION1:
    PredictView.view()
elif view == Menu.OPTION2:
    MetricsView.view()
