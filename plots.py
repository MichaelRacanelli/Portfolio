import streamlit as st
import pandas as pd
import plotly.express as px

def education_plot():
    # data for education
    education_data = [
        {"Degree": "Continuing Studies", "Program": "Data Science", "School": "University of Toronto/Waterloo", "Start Year": "2022-09-01", "End Year": "2023-12-18"},
        {"Degree": "Masters", "Program": "Physiology/Pharmacology", "School": "Western University", "Start Year": "2016-09-01", "End Year": "2019-10-01"},
        {"Degree": "Undergraduate", "Program": "Biomedical Sciences", "School": "Western University", "Start Year": "2011-09-01", "End Year": "2016-05-01"},
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
        title="Timeline",
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
            "Start Date": "April 2023",
            "End Date": "April 2024",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Scientific Analyst QA",
            "Employment Type": "Permanent Full-time",
            "Start Date": "May 2022",
            "End Date": "August 2022",
            "Company": "BenchSci",
            "Location": "Toronto, Ontario",
        },
        {
            "Job Title": "Local Study Associate",
            "Employment Type": "Contract Full-time",
            "Start Date": "February 2020",
            "End Date": "April 2021",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Laboratory Research Assistant and Thesis Student",
            "Employment Type": "Full-time",
            "Start Date": "September 2016",
            "End Date": "June 2019",
            "Company": "Western University",
            "Location": "London, Ontario",
        },
        {
            "Job Title": "Teaching Assistant",
            "Employment Type": "Part-time",
            "Start Date": "September 2017",
            "End Date": "April 2018",
            "Company": "Western University",
            "Location": "London, Ontario",
        },
        {
            "Job Title": "Dental School Simulation Clinic Supervisor",
            "Employment Type": "Part-time",
            "Start Date": "December 2016",
            "End Date": "February 2018",
            "Company": "Western University",
            "Location": "London, Ontario",
        },
        {
            "Job Title": "Collection Clerk",
            "Employment Type": "Full-time",
            "Start Date": "May 2015",
            "End Date": "August 2015",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Medical Operations Business Associate",
            "Employment Type": "Full-time",
            "Start Date": "May 2013",
            "End Date": "August 2013",
            "Company": "GlaxoSmithKline",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Medical Operations Business Associate",
            "Employment Type": "Full-time",
            "Start Date": "May 2012",
            "End Date": "August 2012",
            "Company": "GlaxoSmithKline",
            "Location": "Mississauga, Ontario",
        },
        # Add more work experience entries in a similar manner
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
        title="Timeline",
    )

    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    return fig