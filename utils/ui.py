import streamlit as st


def apply_global_styles():
    """Shared visual styling for AI Trip Decision Optimizer pages."""
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 1.6rem;
                padding-bottom: 2.4rem;
            }
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0f2744 0%, #163456 100%);
            }
            [data-testid="stSidebar"] * {
                color: #f4f7fb !important;
            }
            [data-testid="stSidebarNav"] a:hover {
                background: rgba(255, 255, 255, 0.08);
            }
            div[data-testid="stForm"] {
                border: 1px solid #d9e2ec;
                border-radius: 14px;
                padding: 1.2rem 1.2rem 0.4rem 1.2rem;
                background: #ffffff;
            }
            .stButton > button {
                border-radius: 10px;
                font-weight: 600;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title, subtitle=None):
    st.title(title)

    if subtitle:
        st.caption(subtitle)


def section_title(title):
    st.subheader(title)


def info_card(title, value, description=""):
    with st.container(border=True):
        st.markdown(f"### {title}")
        st.markdown(f"## {value}")

        if description:
            st.caption(description)


def success_message(message):
    st.success(message)


def error_message(message):
    st.error(message)
