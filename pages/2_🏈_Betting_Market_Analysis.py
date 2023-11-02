import streamlit as st
import base64
from constant import *
import pandas as pd

st.set_page_config(page_title="NFL Betting Market Analysis", layout="wide", page_icon='🏈')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)



def show_logo(name: str, width: int=100, height: int=100):
    st.write(f'<img src="{logos[name]}"; width={width}; height={height}>', unsafe_allow_html=True)


# st.write("""<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cyXCE-JcBelTyrK-58w6_Q.png" width=200 height=100>""", unsafe_allow_html=True)

st.markdown("""<img src="https://raw.githubusercontent.com/jp-wright/streamlit_resume/main/.github/images/python_t.png" width=100 height=100>""", unsafe_allow_html=True)
# st.write("""<img src="https://www.dropbox.com/scl/fi/pg3itvyn0yxth9kvafd3y/sklearn.png?rlkey=imt8i5kvs32b5axk7hgtutm8z&dl=0">""", unsafe_allow_html=True)


st.title("Analytical NFL Betting Market Analysis")

# st.write("[Click here if it's blocked by your browser](https://www.dropbox.com/s/9vez2p75o7gm0ip/jpgalvbnw.jpg?dl=0)")

# with open("images/JPWright_Resume_2023.pdf","rb") as f:
#       base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#       pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
#       st.markdown(pdf_display, unsafe_allow_html=True)
  

platforms = ['Selenium']
skills = ['Automated Web Scraping']
purposes = ['Acquire detailed NFL data']
skills_frame = {'Platform': platforms, 'Skill': skills, 'Purpose': purposes}
# df = pd.DataFrame.from_dict(skills_frame, orient='columns').set_index('Platform')

st.header("Project Information")
# st.table(df)

with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        show_logo('python')
    with col2:
        st.write(logos['pandas'], unsafe_allow_html=True)
    with col3:
        st.write(logos['numpy'], unsafe_allow_html=True)
    with col4:
        st.write(logos['sklearn'], unsafe_allow_html=True)
    with col1:
        st.write(logos['xgboost'], unsafe_allow_html=True)
    with col2:
        st.write(logos['selenium'], unsafe_allow_html=True)
    with col3:
        st.write(logos['matplotlib'], unsafe_allow_html=True)
    with col4:
        st.write(logos['plotly'], unsafe_allow_html=True)
    # with col1:
    #     st.write(logos['xgboost'], unsafe_allow_html=True)
    # with col2:
    #     st.write(logos['selenium'], unsafe_allow_html=True)
    # with col3:
    #     st.write(logos['matplotlib'], unsafe_allow_html=True)
    # with col4:
    #     st.write(logos['plotly'], unsafe_allow_html=True)






# mkdown = """
#     Tool/Platform     | Skills                    | Purpose
#     ------------------|---------------------------|-------------------------------------------------
#     Selenium          | Web Scraping              | Some data sources required active session logins.
#     Requests          | Web Scraping              | Basic REST data acquisition from some sites.
#     crontab           | Automation / CICD         | Schedule entire project pipeline to run automatically.
#     Python            | Coding                    | Pipeline and modeling done in Python.
#     ![pandas](https://pandas.pydata.org/static/img/pandas_secondary.svg) Pandas/Numpy      | Data Manipulation         | Extensive data work, from custom table creation to model prep.
#     Sci-kit Learn     | Machine Learning          | Everything from cluster analysis to boosted gradient trees.
#     Matplotlib/Seaborn/Plotly | Visualization     | Extensive visualizations of market history and model results.


# """

# st.markdown(mkdown)

# st.table(skills_frame)
# with st.container():
#     st.subheader(' Project Information ')
#     col1, col2, col3 = st.columns([1, 1, 1])

#     with col1: 
#         st.write("Industry: ")
#     with col2: 
#         st.write("Sports Gaming")

    # st.subheader('⚒️ Skills and Platforms Used')
    # with col1: 
    #     st.write(": ")
    # with col2: 
    #     st.write("Sports Gaming")


# st.write("For a private client")
# st.write("Skills & Platforms Used")
