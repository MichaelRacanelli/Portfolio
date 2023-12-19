import streamlit as st
from sidebar import show_sidebar


def main():
    show_sidebar()
    
    st.title("Michael Racanelli")

    st.header("About Me")
    st.write(
        "I am a data scientist passionate about using data to derive meaningful insights and solve complex problems. "
        "With a background in [Your Relevant Education/Experience], I specialize in [Your Key Areas]."
    )

    st.header("Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        st.write("- Python, R")
        st.write("- Data Cleaning and Preprocessing")
        st.write("- Exploratory Data Analysis (EDA)")
        st.write("- Machine Learning: Regression, Classification, Clustering")
        st.write("- Data Visualization: Matplotlib, Seaborn, Plotly")

    with col2:
        st.subheader("Tools and Frameworks")
        st.write("- Pandas, NumPy, Scikit-Learn")
        st.write("- Jupyter Notebooks")
        st.write("- SQL")
        st.write("- Git, GitHub")
        st.write("- Streamlit for Data Apps")

    st.header("Education")
    st.text("Data Science Certification | September 2022 – December 2023")
    st.text("University of Toronto/Waterloo")
    st.markdown("- Data analysis, statistics, visualization, and machine learning using Python")

    st.text("Master of Science, Thesis-based, Physiology/Pharmacology | September 2016 – October 2019")
    st.text("Western University, London, Ontario")
    st.markdown("- Examined YAP as a mediator of fibrotic activity and melanoma metastasis")

    st.text("Bachelor of Medical Science (Honours) | September 2011 - May 2016")
    st.text("Western University, London, Ontario")
    st.markdown("- Western University Scholarship of Excellence, 2011")
    st.markdown("- Dean’s Honour List, 2013, 2016")

    st.header("Work Experience")
    st.text("Clinical Data Analyst, Contract Full-time | April 2023 – present")
    st.text("Bayer Inc, Mississauga, Ontario")
    st.markdown("- Explored patient data using jupyter notebooks on large data platforms such as Science @ Scale")
    # Add more work experience details in a similar manner

    st.header("Publications")
    st.markdown("[Shi-Wen, X., Racanelli, M., Ali, A., Simon, A., Quesnel, K., Stratton, R. J., & Leask, A. (2021). Verteporfin inhibits the persistent fibrotic phenotype of lesional scleroderma dermal fibroblasts. Journal of cell communication and signaling, 15(1), 71–80.](https://doi.org/10.1007/s12079-020-00596-x)")
    # Add more publication details in a similar manner

    st.header("Licenses & Certifications")
    st.text("Data Science Certification | December 2023 | University of Waterloo/Toronto")
    # Add more certification details in a similar manner

    st.header("Volunteer Experience")
    st.text("Health Partners International of Canada | July 2014 | Mississauga, Ontario")
    st.markdown("- Reworked the warehouse floor, creating a new system of organizing medical supplies")
    # Add more volunteer experience details in a similar manner

    st.header("Interests")
    st.markdown("- Machine Learning: Passionate about how deep learning with big data is changing every industry")
    st.markdown("- Rock Climbing: Current best grades are V6 on bouldering and 12 on top-rope")
    st.markdown("- Building Computers: Built multiple high-performance personal computers with extensive knowledge of consumer and professional products including Intel, AMD, NVIDIA, and custom water-cooling")
    st.markdown("- Music Performance: Saxophone section-leader in Loyola High School concert and jazz bands, Award-winning pianist and multi-instrumentalist")

if __name__ == "__main__":
    main()
