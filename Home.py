import streamlit as st
from sidebar import show_sidebar
import pandas as pd
import plotly.express as px
from plots import education_plot, experience_plot


def main():
    show_sidebar()

    st.title("About Me")
    st.write(
        "Hello! I'm Michael, a biomedical research scientist who completed a Master's of Science in Physiology and Pharmacology, specializing in fibrotic disease and melanoma metastasis. Afterwards, I gained experience in the Pharmaceutical industry in Phase 4 clinical trial management. I then decided to pursue my passion and development, independently learning coding with python and machine learning libraries such as Tensorflow and Keras for the purpose of analyzing clinical data to find new trends and insights. Later, I joined BenchSci as a Scientific Analyst to assist in reforming their QA workflow to improve oversight and reporting. Now, I am looking to combine all my skills to use AI and data analytics in a clinical settings. Currently, I am enrolled in a Data Science Certificate Program with the University of Toronto and the University of Waterloo. I am looking forward to what comes next, so please don't hesitate to reach out!"
    )


    st.header("Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        st.write("- Python, R")
        st.write("- Data Cleaning and Preprocessing")
        st.write("- Exploratory Data Analysis (EDA)")
        st.write("- Machine Learning: Regression, Classification, Clustering")
        st.write("- Data Visualization: Matplotlib, Seaborn, Bokeh")

    with col2:
        st.subheader("Tools and Frameworks")
        st.write("- Pandas, NumPy, Scikit-Learn, TensorFlow, Spark")
        st.write("- Jupyter Notebooks")
        st.write("- SQL, MongoDB")
        st.write("- Git, GitHub")
        st.write("- Streamlit, Panel, Flask")


    st.header("Education")
    # display education plot 
    st.plotly_chart(education_plot(), use_container_width=True)


    st.header("Work Experience")
   # display experience plot
    st.plotly_chart(experience_plot(), use_container_width=True)


    st.header("Licenses & Certifications")
    # Certification data
    certifications_data = [
        ["Data Science Certification", "December 2023", "University of Waterloo/Toronto"],
        ["Machine Learning, Data Science and Deep Learning with Python", "November 2021", "Udemy"],
        ["Complete Python Developer in 2021: Zero to Mastery", "September 2021", "Udemy"],
        ["Study Designs in Epidemiology", "January 2021", "Coursera"],
        ["AI for Everyone", "November 2019", "Coursera"],
    ]
    # Create a DataFrame with column names
    df_certifications = pd.DataFrame(certifications_data, columns=["Title", "Year", "Institution"])
    # Display the table with customized column names and without index
    st.table(df_certifications)


    st.header("Publications")

    st.write("Shi-Wen, X., Racanelli, M., Ali, A., Simon, A., Quesnel, K., Stratton, R. J., & Leask, A. (2021). *Verteporfin inhibits the persistent fibrotic phenotype of lesional scleroderma dermal fibroblasts.* Journal of cell communication and signaling, 15(1), 71–80.")
    st.markdown("[https://doi.org/10.1007/s12079-020-00596-x](https://doi.org/10.1007/s12079-020-00596-x)")

    st.write("Racanelli M, (2019). *YAP-mediated mechanotransduction promotes fibrotic activity.* Electronic Thesis and Dissertation Repository. 6283.")
    st.markdown("[https://ir.lib.uwo.ca/etd/6283](https://ir.lib.uwo.ca/etd/6283)")

    st.write("Hutchenreuther, J., Vincent, K., Norley, C., Racanelli, M., Gruber, S. B., Johnson, T. M., Fullen, D. R., Raskin, L., Perbal, B., Holdsworth, D. W., Postovit, L. M., & Leask, A. (2018). *Activation of cancer-associated fibroblasts is required for tumor neovascularization in a murine model of melanoma.* Matrix biology : journal of the International Society for Matrix Biology, 74, 52–61.")
    st.markdown("[https://doi.org/10.1016/j.matbio.2018.06.003](https://doi.org/10.1016/j.matbio.2018.06.003)")


    st.header("Volunteer Experience")
    st.text("Health Partners International of Canada | July 2014 | Mississauga, Ontario")


    st.header("Interests")
    st.markdown("- Machine Learning: Passionate about how deep learning with big data is changing every industry")
    st.markdown("- Rock Climbing: Current best grades are V6 on bouldering and 12 on top-rope")
    st.markdown("- Building Computers: Built multiple high-performance personal computers with extensive knowledge of consumer and professional products including Intel, AMD, NVIDIA, and custom water-cooling")
    st.markdown("- Music Performance: Saxophone section-leader in Loyola High School concert and jazz bands, Award-winning pianist and multi-instrumentalist")

if __name__ == "__main__":
    main()
