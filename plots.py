import streamlit as st
import pandas as pd
import plotly.express as px

def education_plot():
    # data for education
    education_data = [
        {
            "Degree": "Continuing Studies", 
            "Program": "Data Science", 
            "School": "University of Toronto/Waterloo", 
            "Start Year": "2022-09-01", 
            "End Year": "2023-12-18"
            },
        {
            "Degree": "Masters", 
            "Program": "Physiology/Pharmacology", 
            "School": "Western University", 
            "Start Year": "2016-09-01", 
            "End Year": "2019-10-01"
            },
        {
            "Degree": "Undergraduate", 
            "Program": "Biomedical Sciences", 
            "School": "Western University", 
            "Start Year": "2011-09-01", 
            "End Year": "2016-05-01"
            },
        ]

    # Convert the data to a Pandas DataFrame
    df_education = pd.DataFrame(education_data)

    # Convert 'Start Year' and 'End Year' columns to datetime
    df_education["Start Year"] = pd.to_datetime(df_education["Start Year"])
    df_education["End Year"] = pd.to_datetime(df_education["End Year"], errors='coerce')  # 'coerce' handles the 'present' case

    # Create a horizontal bar chart using Plotly Express with timeline
    fig = px.timeline(
        df_education,
        x_start="Start Year",
        x_end="End Year",
        y="Degree",
        color="School",
        # title="Timeline",
    )

    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    return fig

def experience_plot():
    # Work experience data
    work_experience_data = [
        {
            "Job Title": "Clinical Data Analyst",
            "Employment Type": "Contract Full-time",
            "Start Date": "2023-04",
            "End Date": "2024-04",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Scientific Analyst QA",
            "Employment Type": "Permanent Full-time",
            "Start Date": "2022-05",
            "End Date": "2022-08",
            "Company": "BenchSci",
            "Location": "Toronto, Ontario",
        },
        {
            "Job Title": "Local Study Associate",
            "Employment Type": "Contract Full-time",
            "Start Date": "2020-02",
            "End Date": "2021-04",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Laboratory Research Assistant and Thesis Student",
            "Employment Type": "Full-time",
            "Start Date": "2016-09",
            "End Date": "2019-06",
            "Company": "Western University",
            "Location": "London, Ontario",
        },
        {
            "Job Title": "Teaching Assistant",
            "Employment Type": "Part-time",
            "Start Date": "2017-09",
            "End Date": "2018-04",
            "Company": "Western University",
            "Location": "London, Ontario",
        },
        {
            "Job Title": "Dental School Simulation Clinic Supervisor",
            "Employment Type": "Part-time",
            "Start Date": "2016-12",
            "End Date": "2018-02",
            "Company": "Western University",
            "Location": "London, Ontario",
        },
        {
            "Job Title": "Collection Clerk",
            "Employment Type": "Full-time",
            "Start Date": "2015-05",
            "End Date": "2015-08",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Medical Operations Business Associate",
            "Employment Type": "Full-time",
            "Start Date": "2013-05",
            "End Date": "2013-08",
            "Company": "GlaxoSmithKline",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Medical Operations Business Associate",
            "Employment Type": "Full-time",
            "Start Date": "2012-05",
            "End Date": "2012-08",
            "Company": "GlaxoSmithKline",
            "Location": "Mississauga, Ontario",
        },
    ]

    # Convert the data to a Pandas DataFrame
    df_work_experience = pd.DataFrame(work_experience_data)

    # Convert 'Start Date' and 'End Date' columns to datetime
    df_work_experience["Start Date"] = pd.to_datetime(df_work_experience["Start Date"], errors='coerce')
    df_work_experience["End Date"] = pd.to_datetime(df_work_experience["End Date"], errors='coerce')  # 'coerce' handles the 'present' case

    # Create a horizontal bar chart using Plotly Express with timeline
    fig = px.timeline(
        df_work_experience,
        x_start="Start Date",
        x_end="End Date",
        y="Company",
        color="Job Title",
        # title="Timeline",
    )

    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    return fig