import streamlit as st
import constant as cons

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def show_logo(name: str, width: int=100, height: int=100):
    st.markdown(f'''<img src="{cons.logos[name]}" width={width} height={height}>''', unsafe_allow_html=True)
    st.markdown("<BR>", unsafe_allow_html=True)