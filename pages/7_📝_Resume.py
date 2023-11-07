import streamlit as st
import base64
from utils.constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://github.com/jp-wright/streamlit_resume/blob/main/docs/JPWright_Resume_2023.pdf)")

with open("docs/JPWright_Resume_2023.pdf", "rb") as filename:
      base64_pdf = base64.b64encode(filename.read()).decode('utf-8')
      pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
