import streamlit as st
import pandas as pd
import plotly.express as px

from sidebar import show_sidebar
from plots import education_plot, experience_plot

def main():
    show_sidebar()
    tab1, tab2 = st.tabs(["Home", "Projects"])

    with tab1:
        st.title("About Me")
        st.write("""
            I completed a Master's of Science in Physiology and Pharmacology, specializing in fibrotic disease and melanoma metastasis. 
            Afterwards, I gained industry experience managing Phase 4 clinical studies. 
            Then I pursued development, learning to code in python and practiced machine learning, specializing in clinical data. 

            Afterwards, I enrolled and completed a Data Science Certificate Program at the University of Toronto School of Continuing Studies. 
            In parallel, I joined Bayer as a Clinical Data Analyst to gain industry experience for clinical data science. 
            Here I leverage my clinical health knowledge and industry experience along with my skills as a data science developer to transform data, create tools/visualizations, and answer questions.            
        """)


        st.header("Skills")
        col1, col2, col3, col4= st.columns(4)

        with col1:
            st.subheader("Data Management")
            st.write("- Jupyter Notebooks")
            st.write("- Pandas")
            st.write("- Pyspark")
            st.write("- Databricks")
            st.write("- Azure Data Factory")

        with col2:
            st.subheader("Interactive Dashboards")
            st.write("- PowerBI")
            st.write("- Shiny")
            st.write("- Streamlit")
            st.write("- Panel")

        with col3:
            st.subheader("Machine Learning")
            st.write("- Regression, Classification, Clustering")
            st.write("- Scikit-Learn")
            st.write("- TensorFlow")
            st.write("- Keras")
            st.write("- LLM api integration")

        with col4:
            st.subheader("Collaboration")
            st.write("- Git/GitHub")
            st.write("- Agile Development")
            st.write("- Devops")

        st.header("Education")
        education_plot()

        st.header("Work Experience")
        experience_plot()


        st.header("Publications")

        st.write("Shi-Wen, X., Racanelli, M., Ali, A., Simon, A., Quesnel, K., Stratton, R. J., & Leask, A. (2021). *Verteporfin inhibits the persistent fibrotic phenotype of lesional scleroderma dermal fibroblasts.* Journal of cell communication and signaling, 15(1), 71–80.")
        st.markdown("[https://doi.org/10.1007/s12079-020-00596-x](https://doi.org/10.1007/s12079-020-00596-x)")

        st.write("Racanelli M, (2019). *YAP-mediated mechanotransduction promotes fibrotic activity.* Electronic Thesis and Dissertation Repository. 6283.")
        st.markdown("[https://ir.lib.uwo.ca/etd/6283](https://ir.lib.uwo.ca/etd/6283)")

        st.write("Hutchenreuther, J., Vincent, K., Norley, C., Racanelli, M., Gruber, S. B., Johnson, T. M., Fullen, D. R., Raskin, L., Perbal, B., Holdsworth, D. W., Postovit, L. M., & Leask, A. (2018). *Activation of cancer-associated fibroblasts is required for tumor neovascularization in a murine model of melanoma.* Matrix biology : journal of the International Society for Matrix Biology, 74, 52–61.")
        st.markdown("[https://doi.org/10.1016/j.matbio.2018.06.003](https://doi.org/10.1016/j.matbio.2018.06.003)")


        # st.header("Volunteer Experience")
        # st.text("Health Partners International of Canada | July 2014 | Mississauga, Ontario")


        st.header("Interests")
        st.markdown("- Machine Learning: Passionate about how deep learning with big data is changing every industry")
        st.markdown("- Rock Climbing: Current best grade is V6 in bouldering")
        st.markdown("- Building Computers: Built multiple high-performance personal computers with extensive knowledge of consumer and professional products including Intel, AMD, NVIDIA, and custom water-cooling")
        st.markdown("- Music Performance: Saxophone section-leader in Loyola High School concert and jazz bands, Award-winning pianist and multi-instrumentalist")

    with tab2:
        st.title("Applications")
    
        st.header("Song recommendation")
        
        st.subheader('Description')
        st.write(
        "Group project for the final module of the Data Science Certificate program. "
        "My part mainly included the streamlit application."
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Tools Used")
            st.write("- Python")
            st.write("- Streamlit")
            st.write("- Data caching")    
        with col2:
            st.subheader('Links')
            st.markdown('[Application link]')
            st.markdown('[Github Repository](https://github.com/MichaelRacanelli/SongRecommendation)')
        with col3:
            st.image("./images/spotify.jpg", use_column_width=True) 

        st.title('Notebooks')

        st.header("Heart Disease Risk Factor Analysis and NN")
        st.subheader('Description')
        st.write("Workbook with a large health dataset from kaggle that goes through exploratory data analysis, visualization, and machine learning using a neural network.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Tools Used")
            st.write("- Pandas")
            st.write("- Matplotlib, Seaborn")
            st.write("- Keras")    
        with col2:
            st.subheader('Links')
            st.markdown('[Kaggle Workbook](https://www.kaggle.com/code/michaelracanelli/heart-disease-risk-factor-analysis-and-nn)')
            st.markdown('[Github Repository](https://github.com/MichaelRacanelli/Heart_Disease)')
        # with col3:
        #     st.image("", use_column_width=True)

        st.header("Lung Cancer and Smoking: Predictive Modeling")
        st.subheader('Description')
        st.write("Exploratory data analysis, visualization, and machine learning using a gradient boosting algorithm on a large dataset to predict the presense of lung disease.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Tools Used")
            st.write("- Pandas")
            st.write("- Matplotlib, Seaborn")
            st.write("- XGBoost")    
        with col2:
            st.subheader('Links')
            st.markdown('[Kaggle Workbook](https://www.kaggle.com/code/michaelracanelli/lung-cancer-and-smoking-predictive-modeling)')
            st.markdown('[Github Repository](https://github.com/MichaelRacanelli/Lung_Cancer)')
        # with col3:
        #     st.image("", use_column_width=True)
if __name__ == "__main__":
    main()
