import streamlit as st
import utils.image_refs as images
from typing import Optional
import requests

def local_css(file_name):
    """
    """
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def load_lottieurl(url: str):
    """
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def gradient(grad_clr1, grad_clr2, title_clr, subtitle_clr, title, subtitle, subtitle_size: int=17):
    """
    """
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{grad_clr1}, {grad_clr2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{title_clr};">{title}</span><br>'
                f'<span style="color:{subtitle_clr};font-size:{subtitle_size}px;">{subtitle}</span></h1>', 
                unsafe_allow_html=True)

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
    st.markdown(f'''<img src="{images.logos[name]}" width={width} height={height}>''', unsafe_allow_html=True)
    if spacer:
        st.markdown("<BR>" * spacer, unsafe_allow_html=True)