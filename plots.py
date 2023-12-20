import streamlit as st
import pandas as pd
import plotly.express as px

def education_plot():
    # data for education
    education_data = [
        {
            "Title": "Data Science Certificate",
            "Degree": "Certificate", 
            "Program": "Data Science", 
            "School": "University of Toronto/Waterloo", 
            "Start Year": "2022-09-01", 
            "End Year": "2023-12-18"
        },
        {
            "Title": "Master of Science",
            "Degree": "Masters", 
            "Program": "Physiology/Pharmacology", 
            "School": "Western University", 
            "Start Year": "2016-09-01", 
            "End Year": "2019-10-01"
        },
        {
            "Title": "Bachelor of Medical Science (Honours)",
            "Degree": "Undergraduate", 
            "Program": "Biomedical Sciences", 
            "School": "Western University", 
            "Start Year": "2011-09-01", 
            "End Year": "2016-05-01"
        },
        {
            "Title": "AI for Everyone",
            "Degree": "Certificate",
            "Program": "Data Science",
            "School": "Coursera",
            "Start Year": "2019-11-07",
            "End Year": "2019-11-30"
        },
        {
            "Title": "Study Designs in Epidemiology",
            "Degree": "Certificate",
            "Program": "Biomedical Sciences",
            "School": "Coursera",
            "Start Year": "2021-01-01",
            "End Year": "2021-01-31"
        },
        {
            "Title": "Complete Python Developer in 2021: Zero to Mastery",
            "Degree": "Certificate",
            "Program": "Data Science",
            "School": "Udemy",
            "Start Year": "2021-05-01",
            "End Year": "2021-09-16"
            },
        {
            "Title": "Machine Learning, Data Science and Deep Learning with Python",
            "Degree": "Certificate",
            "Program": "Data Science",
            "School": "Udemy",
            "Start Year": "2021-09-17",
            "End Year": "2021-11-24"
        }
        ]

    # Convert the data to a Pandas DataFrame
    df_education = pd.DataFrame(education_data)

    # Convert 'Start Year' and 'End Year' columns to datetime
    df_education["Start Year"] = pd.to_datetime(df_education["Start Year"])
    df_education["End Year"] = pd.to_datetime(df_education["End Year"], errors='coerce')  # 'coerce' handles the 'present' case

    # Specify the order for the legend items
    legend_order = df_education.sort_values("End Year")["Title"]
    
    # Create a horizontal bar chart using Plotly Express with timeline
    fig = px.timeline(
        df_education,
        x_start="Start Year",
        x_end="End Year",
        y="Degree",
        color="Title",
        # title="Timeline",
        category_orders={"Title": legend_order[::-1]},  # Set the order of legend items in reverse
    )
    # Adjust the legend position
    fig.update_layout(legend=dict(x=-0.2, y=-0.2, traceorder='normal', orientation='h'))
    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    return fig, df_education

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

    # Specify the order for the legend items
    legend_order = df_work_experience.sort_values("End Date")["Job Title"]
    # Create a horizontal bar chart using Plotly Express with timeline
    fig = px.timeline(
        df_work_experience,
        x_start="Start Date",
        x_end="End Date",
        y="Company",
        color="Job Title",
        # title="Timeline",
        category_orders={"Job Title": legend_order[::-1]},  # Set the order of legend items
    )

    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    fig.update_layout(legend=dict(x=-0.2, y=-0.2, traceorder='normal', orientation='h'))
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    return fig, df_work_experience