import streamlit as st
# import base64
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
        Jonpaul built an automated bet-making model that analyzed every NFL game each week and placed bets on games that met a user-defined threshold for win probability based on his comprehensive game matchup model.  Jonpaul worked for a private client on the west coast and handled all aspects of the pipeline, from data gathering, cleaning, prepping, feature engineering, model building and comparison, tuning, validation, reporting, and visualization. 

        <BR>

        📝  Please see the full-length, technical, and illustrated [research article](https://github.com/jp-wright/nfl_betting_market_analysis)!    

        <BR> 

        It contains details about the history of Vegas lines, the changes in the NFL over time which have impacted the lines, and the conditions in which bets were or were not wise to make. 

        <BR>
        """

        st.markdown(md_intro, unsafe_allow_html=True)


    def project_info(self):
        st.markdown('<BR>', unsafe_allow_html=True)
        # st.header(":blue[Project Information]")
        st.header('💻  :blue[Platforms Used]')

        with st.container():
            # st.subheader('💻  Platforms Used')
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
                show_logo('postgres', width=120, height=80)
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
            st.header('⚒️ :blue[Skills]')
            # st.subheader('⚒️ Skills')
            md_skills = """
            ##### Domain Research
            Research was done on the types of common bets offered, their behavior over time, and the market in which they existed.  Aspects of sports gaming such as line movement, the betting public, home-field advantage, the "vig" (vigorish, i.e. a tax), and the numerical system / dictation used to register wagers were all studied and reported on as preparation in understanding what an automated betting model should be able to account for.

            ##### Data Gathering
            Data gathering was extensive and done via multiple approaches for multiple sources.  For some, direct acces via the `requests` library was possible.  For others, backend JavaScript prevented direct scraping and more intricate methods involving comment tags was required.  Last, some sources required logging in and maintaining an active browser session, so `selenium` was used to crawl the web sites.  

            ##### Data Storage
            Storage was done by aggregating many CSVs of similar types into larger DataFrames and ingesting the resulting CSVs into a `PostgreSQL` database.  The sheer number of small, scraped CSVs meant that storing each of them individually as a table in the database would have been wasteful and extracting each with `SQL` could have been tedious.  Since most of the data is historical and does not change, combining the many smaller tables into larger ones which get routine updates is a good use of storage.

            ##### Data Cleaning & Preparation
            Cleaning was extensive, with numerous data entry errors discovered from the various sources.  Some were spelling, some were conflicting dates, and some were mathematical (wrong signs) or missing data.  For all of these data entry errors the correct values were verified by manually looking them up online in separate sources.  A validation script corrected each known error and a `PyTest` script checked new data for potential errors.  For missing data that was not able to be referenced online, data was imputed in appropriate ways, as was class imbalance including via `SMOTE`, to make modeling viable.  

            ##### Feature Engineering
            Comprehensive feature engineering was performed, including `binning`, `normalization`, `clipping`, and `cross-feature interactions`, with engineered features accounting for many of the most impactful during modeling.  Due to the limited history of some of the features (some exist for the entire history of the modern Super Bowl era of the NFL, others existed for only 25 years or so), more recent features being engineered led to a wider, data-rich model input set vs. a longer, data-poor set.  Both were used in all model testing and validation.  

            ##### Model Building
            Multiple models were tested and validated using `cross-validation`.  Different variations of input data were available depending on features selected, resulting in different models for different feature sets.  `Exploratory Data Analysis` and `Recursive Feature Elimination` suggested certain feature sets for higher efficacy.  Unsupervised algorithms like `PCA` and `t-SNE` were used to discover possible matchup scenarios or impactful features.  Models were tuned using `exhaustive grid search`.  Results were reported and compared, ultimately leading to a selection of a tuned XGBoost model.  

            ##### Threshold Selection and Result Visualization
            Many experiments were performed which examined which win-probability thresholds were commonly 'wise bets' and their results were visualized in GIF form with `matplotlib`, `seaborn`, and `plotly`, showing each successive bet and the amount won or lost over time.  Amount wagered and game choice are the two variables to control for in making wagers.  Results can vary wildly depending on the values chosen.
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


    def conclusion(self):
        st.markdown('<BR>', unsafe_allow_html=True)




PageLayout()