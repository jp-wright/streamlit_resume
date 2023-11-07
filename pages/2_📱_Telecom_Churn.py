import streamlit as st
import base64
import pandas as pd
from utils.constant import *
from utils.utils import *
from utils.palettes import *
from utils.image_refs import *



##### Set Style ######
class PageLayout():
    def __init__(self):
        st.set_page_config(page_title="Telecom Churn and Competitor Analysis", layout="wide", page_icon='📱')
        local_css("style/style.css")
        # st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)
        self.intro()
        self.project_info()
        self.conclusion()
        self.gallery()
        self.md_guide()



    def intro(self):
        # gradient(airy_bath[2], airy_bath[4], '#383e48', '#fcfbfb', f"NFL Automated Bet-Making Model 🏈", "Can profitable wagers be automated?", 27)
        gradient(blue_bath1[1], blue_bath1[3], blue_bath1[5], '#fcfbfb', f"Telecom Churn and Competitor Analysis 📱", "Predicting churn and competitor activity by geography", 27)
        # gradient(fft_riovanes_art[0], fft_riovanes_art[2], fft_riovanes_art[5], '#fcfbfb', f"NFL Automated Bet-Making Model 🏈", "Can profitable wagers be automated?", 27)

        # gradient(green_blue_bath1[0], green_blue_bath1[2], '#383e48', '#fcfbfb', f"NFL Automated Bet-Making Model 🏈", "Can profitable wagers be automated?", 27)
        # gradient(fft_finath[0], fft_finath[1], fft_finath[2], '#fcfbfb', f"NFL Automated Bet-Making Model 🏈", "Can profitable wagers be automated?", 27)
        # st.title("NFL Automated Bet-Making Model")
        md_intro = """
        Jonpaul helped improve a large, national telecom client's churn prediction by ~42% (relative) by builing and managing two model pipelines. The increase in churn prediction accuracy led to the initial two-year contract being extended an additional year three times, for a total of three extra years.  Jonpaul was also instrumental in porting the data pipeline to Apache Hive from an decommissioned database.  Jonpaul's work addressed the client's asks: 
        
        1. Predict client's monthly churn in 97 separate geographical areas in up to 17 different sub-lines/carriers.
        2. Predict competitor's market presence and churn in those same areas.

        Jonpaul's responsibilities included data ingestion, pipeline construction, unit testing, model creation, automation of validation and drift monitoring, and dashboard updating for internal and external reporting.  Jonpaul also presented in person for two annual reviews at client headquarters.

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
                show_logo('sql', width=120, height=55)
            with col2:
                show_logo('hive', width=120, height=75)
            with col3:
                show_logo('bash', width=120, height=80)
            with col1:
                show_logo('numpy', width=120, height=90)
            with col2:
                show_logo('pytest', width=120, height=80)
            with col3:
                show_logo('tableau', width=120, height=45)
            # with col2:
                # show_logo('python', width=100, height=50)
            # with col3:
                # show_logo('python', width=100, height=50)
            # with col4:
                # show_logo('python', width=100, height=50)


        with st.container():
            st.markdown('<BR>', unsafe_allow_html=True)
            # st.header('⚒️ :blue[Skills]')
            st.header('⚒️ Skills')

            md_domain = f"""
            ##### <font color={subheading_blue}>Domain Research</font>
            Understanding the client's customer retention expectations in key geographic regions was central to evaluating projections.  Additionally, understanding the telecom industry write large, recent trends nationally, and how business rules of customer attribution -- which might have lag times -- impact source data were essential to successful product delivery.
            """

            md_gather = f"""
            ##### <font color={subheading_blue}>Data Gathering</font>
            Internal data was provided monthly by client, separated by geography. Various sources of public data were used to model competitor activity. 
            """

            md_storage = f"""
            ##### <font color={subheading_blue}>Data Storage</font>
            Files were delivered as CSVs which were loaded into a database.  Historical data was preserved.  An IBM Nettezza database was used initially.  Upon decomission, a Hive database was used, for which the data pipeline had to be ported.  Apart from a data architect, no one on the project had experience with Hive, requiring Jonpaul to write a how-to guide for the team as well as Python modules allowing th team to interface with the Hive database for their parts of the workflow.
            """

            md_clean = f"""
            ##### <font color={subheading_blue}>Data Cleaning & Preparation</font>
            Cleaning was fairly minimal as the internal data provided by the client tended to be well-maintained.  Nonetheless, data validation scripts were used to ensure data integrity at key junctures throughout the pipeline.
            """

            md_eng = f"""
            ##### <font color={subheading_blue}>Feature Engineering</font>
            Feature expansion was centered around seasonal changes, geographic trends, and running average trends. Competitor data was quarterly in periodicity, requiring it to be disaggregated into monthly values.  For competitor data that was not geographically separated, geographical values were determined by researching past publically stated customer numbers in given metro areas and comparing those to changes in the same areas for the client.
            """

            md_model = f"""
            ##### <font color={subheading_blue}>Model Building</font>
            `Regularized linear regression` and `ensemble tree` models were used.  Model performance was monitored automatically to prevent `drift` and reported if found.  Final forecasts were a mixture of the models' outputs, automatically weighted by historical accuracy for the period being predicted.  Larger markets were more consistent while smaller markets occasionally proved statistically volatile and more challenging to forecast.  Another challenge was changing of inputs at some point in the project, as the methodology of attributing certain gains or losses by the client evolved, causing Jonpaul and team to retroactively update historical forecasts from "day 0" using the new methodology -- a much hairier task than it might sound.
            """

            md_res = f"""
            ##### <font color={subheading_blue}>Visualization and Reporting</font>
            Results were uploaded to a client-facing `Tableau` dashboard.  Each month's results were presented to the client, with a walkthrough of the dashboard.
            """



            st.markdown(md_domain, unsafe_allow_html=True)
            st.markdown(md_gather, unsafe_allow_html=True)
            st.markdown(md_storage, unsafe_allow_html=True)
            st.markdown(md_clean, unsafe_allow_html=True)
            st.markdown(md_eng, unsafe_allow_html=True)
            st.markdown(md_model, unsafe_allow_html=True)
            st.markdown(md_res, unsafe_allow_html=True)



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
        with st.container():
            st.header('✅ Conclusion')

            md_conc = """
            Jonpaul and team were able to take a pipeline that consisted of spaghetti code and projections based off dated values and turn it into a heavily-automated and self-monitoring production-level service that brought real value to the telecom client.

            Multiple sub-lines / carriers were modeled and monthly national forecasts ranged from around +5\% to + 60\% increase in churn prediction relative accuracy.  The three most important carrier lines were improved around +42\% relative accuracy in aggregate.  

            The initial contract of two years was ultimately extended three additional years as the client found real value in the advanced forecasting provided by our team and routinely compared their internal findings with our team's in monthly reporting video calls.

            Technical challenges of porting the entire pipeline and data archives to a new database, re-forecasting the entire prediction history using new inputs and business rules, explaining predictions for all markets, and being able to procure externally-sourced data to make forecasts for industry competitors were all obstacles our team overcame in order to successfully deliver for the client.
            """
            st.markdown(md_conc)


    def gallery(self):
        st.markdown("<BR>", unsafe_allow_html=True)
        with st.container():
            st.header('🖼 Gallery')

            col1, col2 = st.columns([1, 1])
            with col1:
                show_img(telecom['churn2'], width=450, height=450, hover='Churn geography', caption='Representative image only [not my actual dashboard, though very similar].')
            with col2:
                show_img(telecom['sql_query'], width=450, height=450, hover='SQL pipeline', caption='One query in a 1000+ line series of SQL queries to generate some metrics.')





    def md_guide(self):
        st.markdown('<br><br><br>', unsafe_allow_html=True)
        ## show the full rendered Markdown...
    #     with open('docs/jp_hive_guide_public.md', 'r') as fname:
    #         st.markdown(fname.readlines(200)[0])
        
        # st.write("[Click here if it's blocked by your browser](https://www.dropbox.com/s/9vez2p75o7gm0ip/jpgalvbnw.jpg?dl=0)")

        with open('docs/jp_hive_guide_public.pdf', "rb") as filename:
            base64_pdf = base64.b64encode(filename.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

PageLayout()




