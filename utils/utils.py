import streamlit as st
import utils.constant as cons
from typing import Optional

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def show_img(url: str, width: int=100, height: int=100, hover: Optional[str]=None, caption: Optional[str]=None, link: bool=False, spacer: Optional[int]=1):
    """
    """    
    img = f'''<img src="{url}" width={width} height={height}>'''
    if caption:
        img = img.replace('>', '') + f' alt={hover} title={hover}>'
    if link:
        img = f'<a href="{url}">' + img + '</a>'

    st.markdown(img, unsafe_allow_html=True)

    if caption:
        st.markdown(f"<font size=2>{caption}</font>", unsafe_allow_html=True)
    if spacer:
        st.markdown("<BR>" * spacer, unsafe_allow_html=True)


def show_logo(name: str, width: int=100, height: int=100, spacer: Optional[int]=1):
    """
    """
    st.markdown(f'''<img src="{cons.logos[name]}" width={width} height={height}>''', unsafe_allow_html=True)
    if spacer:
        st.markdown("<BR>" * spacer, unsafe_allow_html=True)