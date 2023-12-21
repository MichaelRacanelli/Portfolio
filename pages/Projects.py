import streamlit as st
from sidebar import show_sidebar

def main():
    show_sidebar()
    
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
