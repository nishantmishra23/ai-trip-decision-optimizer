import streamlit as st


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