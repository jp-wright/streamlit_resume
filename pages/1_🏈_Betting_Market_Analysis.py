import streamlit as st
import base64
from constant import *
import pandas as pd
from utils import *


##### Set Style ######
class PageLayout():
    def __init__(self):
        st.set_page_config(page_title="NFL Betting Market Analysis", layout="wide", page_icon='🏈')
        local_css("style/style.css")
        # st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)
        self.intro()
        self.project_info()



    def intro(self):
        st.title("NFL Automated Wise Bet-Making Model")
        md_intro = """
        Jonpaul built an automated bet-making model that analyzed every NFL game each week and placed bets on games that met a user-defined threshold for win probability based on his comprehensive game matchup model.  Jonpaul worked for a private client on the west coast and handled all aspects of the pipeline, from data gathering, cleaning, prepping, model building and comparison, tuning, validation, reporting, and visualization. 

        <BR>

        📝  Please see the full-length, technical, and illustrated [research article](https://github.com/jp-wright/nfl_betting_market_analysis)!    

        <BR> 

        It contains details about the history of Vegas lines, the changes in the NFL over time which have impacted the lines, and the conditions in which bets were or were not wise to make. 

        <BR>
        """

        st.markdown(md_intro, unsafe_allow_html=True)


    def project_info(self):
        st.markdown('<BR>', unsafe_allow_html=True)
        st.header(":blue[Project Information]")

        with st.container():
            st.subheader('💻  Platforms Used')
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            with col1:
                show_logo('python', width=120, height=80)
            with col2:
                show_logo('pandas', width=120, height=80)
            with col3:
                show_logo('sklearn', width=120, height=80)
            with col4:
                show_logo('numpy', width=120, height=80)
            with col1:
                show_logo('selenium', width=120, height=80)
            with col2:
                show_logo('crontab', width=120, height=80)
            with col3:
                show_logo('sql', width=120, height=80)
            with col4:
                show_logo('seaborn', width=120, height=80)
            # with col1:
                # show_logo('python', width=100, height=50)
            # with col2:
                # show_logo('python', width=100, height=50)
            # with col3:
                # show_logo('python', width=100, height=50)
            # with col4:
                # show_logo('python', width=100, height=50)


        with st.container():
            st.markdown('<BR>', unsafe_allow_html=True)
            st.subheader('⚒️ Skills')
            md_skills = """
            Data gathering was extensive and done via multiple approaches for multiple sources.  For some, direct acces via the `requests` library was possible.  For others, backend JavaScript prevented direct scraping and more intricate methods involving comment tags was required.  Last, some sources required logging in and maintaining an active browser session, so `selenium` was used to crawl the web sites.

            Processing and warehousing 
            """

            st.markdown(md_skills)

        # platforms = ['Selenium']
        # skills = ['Automated Web Scraping']
        # purposes = ['Acquire detailed NFL data']
        # skills_frame = {'Platform': platforms, 'Skill': skills, 'Purpose': purposes}
        # df = pd.DataFrame.from_dict(skills_frame, orient='columns').set_index('Platform')

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



PageLayout()