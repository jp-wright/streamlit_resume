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
        Jonpaul was lead data scientist on a team that was instrumental in catching numerous pharmacy-related criminals, including a ring of ten fraudulent pharmacists in Michigan who were <a href=https://www.clickondetroit.com/news/local/2019/12/19/10-people-accused-in-massive-46m-co-pay-fraud-scheme-involving-26-pharmacies-around-metro-detroit/>busted for over $46M</a>. <i>[Note: not all $46M was with our pharma client]</i>.     
        
          
        Combining both client and third-party data sources for advanced modeling and analysis resulted in average monthly savings of $750,000 for the client. 

        
        Jonpaul was responsible for data profiling, cleaning and processing, validation, storage, feature expansion, modeling and tuning, and dashboard review.  Jonpaul was also responsible for training junior team members to run the pipeline.

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
                show_logo('sklearn', width=120, height=80)
            with col1:
                show_logo('alteryx', width=120, height=55)
            with col2:
                show_logo('numpy', width=120, height=80)
            with col3:
                show_logo('tableau', width=120, height=60)


        with st.container():
            st.markdown('<BR>', unsafe_allow_html=True)
            # st.header('⚒️ :blue[Skills]')
            st.header('⚒️ Skills')

            md_domain = f"""
            ##### <font color={subheading_blue}>Domain Research</font>
            There was a substantial investment on obtaining working knowledge of industry lingo, acronyms, and codes used in the medical field.  Further, learning expected patterns of transactions throughout the chain of events from patient -> provider -> pharamacist -> pharma company, and any inter-relation therein, was necessary in order to understand how to design metrics by which to catch fraudulent actors.
            """

            md_gather = f"""
            ##### <font color={subheading_blue}>Data Gathering</font>
            Three separate data sources (two separate `claims data source`s and an `Rx shipement source`) were delivered by the client as flat files to sharepoints.  Separate reference files for `practitioners` and `pharmacies` were also utilized.  At one point the client shifted from monthly to weekly data updates and the pipeline was run on a weekly cadence, accordingly.
            """

            md_storage = f"""
            ##### <font color={subheading_blue}>Data Storage</font>
            Each data source was validated and appended to their respective tables in `Alteryx`-optimized databases.  Due to internal restrictions, a traditional SQL database was not allowed and Alteryx was the environment available which could handle large in-memory data requirements by using its compressed database format.  Jonpaul does not recommend using Alteryx on a modern production data science pipeline unless required, such as in this instance.
            """

            md_clean = f"""
            ##### <font color={subheading_blue}>Data Cleaning & Preparation</font>
            Cleaning was elaborate.  Data sources commonly had errors which were correctable via custom scripts Jonpaul and team wrote.  Cleaning and prep was done in either `Python` or `Alteryx`, depending on the dataset used.   A large walkthrough of the entire pipeline was created which detailed the `ETL` process for each source dataset and the many intermediate tables which were used in the overall process.
            """

            md_eng = f"""
            ##### <font color={subheading_blue}>Feature Engineering</font>
            Feature engineering focused on highlighting vulnerabilities in the medical treatment / pharmaceutical process.  Some key features developed included an analysis of `prescriber-to-pharmacy distance`, `trend of voucher/coupon claims over time`, `percent of claims which were vouchers/coupons`, `associations with known fraudulent providers or pharmacies`, and `inappropriate prescriptions for given conditions`, among others.
            """

            md_model = f"""
            ##### <font color={subheading_blue}>Model Building</font>
            A `multiclass logistic regression` model was employed to determine whether providers or pharmacists were potentially involved in fraudulent activity.  A scoring system by which any given candidate would be tracked for potential infractions / questionable activity was developed, with specific infraction point assignments being informed by both the client and by post-hoc correlational analysis.  As data shifted with time, `model drift` was attenuated by adjusting the scoring system in addition to model parameters.
            """

            md_res = f"""
            ##### <font color={subheading_blue}>Threshold Selection and Result Visualization</font>
            Results were uploaded to a client-facing five-page `Tableau` dashboard.  The client routinely had tandem walkthroughs of the dashboarded results with our team.  Classification boundaries were set initially to provide a recommended percent of "no", "potentially", and "likely" fraudulent candidates. With time, the model's results were used to tune the model's hyperparameters to maintain general class balance desired by client.  Part of the assigned classification breakdown was that each "likely" case was investigated by client's internal revenue leakage team, which takes significant time and money.  Hence delivering the client a list of 100 possible bad actors each week would have been unsustainable.  This is an example of a real-world business limitation and how our team was able to adjust our production model to better serve the client.
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
            Jonpaul and team were pivotal in saving their international pharmaceutical client around \$45M in five years (reported by client), for a rough average of around \$750,000 per month in recovered or avoided revenue leakage.  

            The client extended their contract four separate times, with the final time being a multi-year extension, and began a new contract with us to provide the same service to a subsidiary of theirs.  
            """
            st.markdown(md_conc)


    def gallery(self):
        st.markdown("<BR>", unsafe_allow_html=True)
        with st.container():
            st.header('🖼 Gallery')

            col1, col2 = st.columns([1, 1])
            with col1:
                show_img(pharma['mc_logit'], width=650, height=450, hover='multiclass logit', caption='Example of model output for "no", "potentially", and "likely" fraudulent activity.')
           




PageLayout()