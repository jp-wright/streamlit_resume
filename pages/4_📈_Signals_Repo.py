import pandas as pd
import streamlit as st
# import base64
from utils.constant import *
from utils.utilities import *
from utils.palettes import *
from utils.image_refs import *


##### Set Style ######
class PageLayout():
    def __init__(self):
        st.set_page_config(page_title="Pharmaceutical Fraud", layout="wide", page_icon='💊')
        local_css("style/style.css")
        # st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)
        self.intro()
        self.project_info()
        self.conclusion()
        self.gallery()



    def intro(self):
        gradient(blue_bath1[1], blue_bath1[3], blue_bath1[5], '#fcfbfb', f"Pharmaceutical Fraud Detection 💊", "Catching Bad Actors with Good Data", 27)
        
        md_intro = """
        <BR>
        Jonpaul helped develop an API for a client-facing signals repository that allowed for enhanced model development.  As the Python specialist for the project, he developed specialized geo-based features which allowed users to see engineered signals over time for user-defined regions.  

        The <a href="https://advisory.kpmg.us/services/signals-repository.html">Signals Repository</a> is used by large clients looking for additive data signals to generate new insights into targeted areas for their businesses.  

        <BR>
        """

        st.markdown(md_intro, unsafe_allow_html=True)


    def project_info(self):
        st.markdown('<BR>', unsafe_allow_html=True)
        # st.header(":blue[Project Information]")
        # st.header('💻  :blue[Platforms Used]')
        st.header('💻  Platforms Used')

        with st.container():
            # st.subheader('💻  Platforms Used')
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                show_logo('python', width=120, height=70)
            with col2:
                show_logo('pandas', width=120, height=70)
            with col3:
                show_logo('r_data', width=120, height=80)
            with col1:
                show_logo('bash', width=120, height=55)
            with col2:
                show_logo('numpy', width=120, height=80)
            with col3:
                show_logo('elastic_search', width=120, height=60)
            with col1:
                show_logo('rest_api', width=120, height=60)
            


        with st.container():
            st.markdown('<BR>', unsafe_allow_html=True)
            # st.header('⚒️ :blue[Skills]')
            st.header('⚒️ Skills')

            md_domain = f"""
            ##### <font color={subheading_blue}>Domain Research</font>
            A multitude of economic and demographic terms were learned in order to explain to users some of the more complex signals that were developed.  Understanding how this data was tracked and released was also necessary to accurately devise information-rich signals which would offer significant value to clients.
            """

            md_gather = f"""
            ##### <font color={subheading_blue}>Data Gathering</font>
            A dizzying array of geo-based data sources were used and their cadence of ingestion depended on how often they were released, as some were weekly, others monthly, and still others quarterly.  This was not in the scope of Jonpaul's role.
            """

            md_storage = f"""
            ##### <font color={subheading_blue}>Data Storage</font>
            Data was stored in ElasticSearch.  This was not in the scope of Jonpaul's role.
            """

            md_clean = f"""
            ##### <font color={subheading_blue}>Data Cleaning & Preparation</font>
            Most input data was from published sources and tended to be relatively clean. Jonpaul ported data cleaning and processing scripts from R to Python as the Signals Repository was a Python-based pipeline.
            """

            md_eng = f"""
            ##### <font color={subheading_blue}>Feature Engineering</font>
            Jonpaul authored scripts which consisted of basic (raw) data and more complex, customized signals.  Key signals were engineered by allowing a user to define a specific area (down to the block of a street) for which they wanted to see any number of changes in interactions over time.  Multiple raw signals were used to compmrise information-rich and model-ready signals that clients used in their own data science pipelines.  
            """

            md_model = f"""
            ##### <font color={subheading_blue}>Model Building</font>
            This is a signals repository and did not contain models.
            """

            md_res = f"""
            ##### <font color={subheading_blue}>Threshold Selection and Result Visualization</font>
            Demo visualizations displayed the concepts of key signals but the goal of this repository was to provide clients with data to enhance their own modeling endeavors.
            """



            st.markdown(md_domain, unsafe_allow_html=True)
            st.markdown(md_gather, unsafe_allow_html=True)
            st.markdown(md_storage, unsafe_allow_html=True)
            st.markdown(md_clean, unsafe_allow_html=True)
            st.markdown(md_eng, unsafe_allow_html=True)
            st.markdown(md_model, unsafe_allow_html=True)
            st.markdown(md_res, unsafe_allow_html=True)


    def conclusion(self):
        st.markdown('<BR>', unsafe_allow_html=True)
        with st.container():
            st.header('✅ Conclusion')

            md_conc = """
            The Signals Repository was (is) highly successful and has clients across Europe in addition to America, now.  At bi-annual events hosted by KPMG, clients have given presentations on the ways in which the Signals Repository has bolstered their own modeling efforts.  Overall, the platform matured to the point of being a notable revenue generator for KPMG due to the real and accessible value it added to clients' data science workflows.
            """
            st.markdown(md_conc)


    def gallery(self):
        st.markdown("<BR>", unsafe_allow_html=True)
        with st.container():
            st.header('🖼 Gallery')

            col1, col2 = st.columns([1, 1])
            with col1:
                show_img(signals['us_geo_growth'], width=450, height=450, hover='', caption='Example of the type of geo-based activity that signals offered.')
            with col2:
                show_img(signals['kpmg_signals'], width=450, height=450, hover='', caption='')
           




PageLayout()