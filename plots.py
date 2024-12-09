import streamlit as st
import pandas as pd
import plotly.express as px
from dateutil.relativedelta import relativedelta

def education_plot():
    # data for education
    education_data = [
        {
            "Title": "Data Science Certificate",
            "Degree": "Certificate", 
            "Program": "Data Science", 
            "School": "University of Toronto/Waterloo", 
            "Start Date": "2022-09-01", 
            "End Date": "2023-12-18"
        },
        {
            "Title": "Master of Science",
            "Degree": "Masters", 
            "Program": "Physiology/Pharmacology", 
            "School": "Western University", 
            "Start Date": "2016-09-01", 
            "End Date": "2019-10-01"
        },
        {
            "Title": "Bachelor of Medical Science (Honours)",
            "Degree": "Undergraduate", 
            "Program": "Biomedical Sciences", 
            "School": "Western University", 
            "Start Date": "2011-09-01", 
            "End Date": "2016-05-01"
        },
        {
            "Title": "AI for Everyone",
            "Degree": "Certificate",
            "Program": "Data Science",
            "School": "Coursera",
            "Start Date": "2019-11-07",
            "End Date": "2019-11-30"
        },
        {
            "Title": "Study Designs in Epidemiology",
            "Degree": "Certificate",
            "Program": "Biomedical Sciences",
            "School": "Coursera",
            "Start Date": "2021-01-01",
            "End Date": "2021-01-31"
        },
        {
            "Title": "Complete Python Developer in 2021: Zero to Mastery",
            "Degree": "Certificate",
            "Program": "Data Science",
            "School": "Udemy",
            "Start Date": "2021-05-01",
            "End Date": "2021-09-16"
            },
        {
            "Title": "Machine Learning, Data Science and Deep Learning with Python",
            "Degree": "Certificate",
            "Program": "Data Science",
            "School": "Udemy",
            "Start Date": "2021-09-17",
            "End Date": "2021-11-24"
        }
        ]

    # Convert the data to a Pandas DataFrame
    df_education = pd.DataFrame(education_data)

    # Convert 'Start Date' and 'End Date' columns to datetime
    df_education["Start Date"] = pd.to_datetime(df_education["Start Date"]).dt.date
    df_education["End Date"] = pd.to_datetime(df_education["End Date"], errors='coerce').dt.date  # 'coerce' handles the 'present' case

    df_education.sort_values('End Date', ascending=False, inplace=True)
    df_education.reset_index(drop=True,inplace=True)

    # Calculate duration in years, months, and days
    df_education['Duration'] = df_education.apply(lambda row: relativedelta(row['End Date'], row['Start Date']), axis=1)

    # Create a new column to represent the duration
    df_education['Duration'] = df_education['Duration'].apply(lambda x: (
        f"{x.years} years " if x.years != 0 else "") +
        (f"{x.months} months " if x.months != 0 else "") +
        (f"{x.days} days" if x.years ==0 and x.months == 0 else "")
    )

    # Specify the order for the legend items
    legend_order = df_education.sort_values("End Date")["Title"]
    
    hover_data = {
        "Title": True,
        "School": True,
        "Degree": False,
        "Start Date": False,
        "End Date": False,
        "Duration": True,
    }
    # Create a horizontal bar chart using Plotly Express with timeline
    fig = px.timeline(
        df_education,
        x_start="Start Date",
        x_end="End Date",
        y="Degree",
        color="Title",
        hover_data=hover_data,
        # title="Timeline",
        category_orders={"Title": legend_order[::-1]},  # Set the order of legend items in reverse
    )
    # Adjust the legend position
    fig.update_layout(
        legend=dict(
            x=-0.2,  # Position the legend to the left
            y=-0.2,  # Align the legend vertically to the top
            # traceorder='reversed',
            # yanchor='top',  # Anchor the legend box by its left side
            # xanchor='left',
            orientation='h',  # Set to vertical layout
            font=dict(
                size=16 # Adjust the size value to your preference
            )
        )
    )
    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    # display education plot 
    st.plotly_chart(fig, use_container_width=True)
    # Button to show/hide details
    if st.button("Show Details", key='education'):
        # Display the DataFrame as a table
        st.button("Hide",key='clear_education')
        st.dataframe(df_education)


def experience_plot():
    # Work experience data
    work_experience_data = [
        {
            "Job Title": "Clinical Data Analyst",
            "Employment Type": "Contract Full-time",
            "Start Date": "2023-04",
            "End Date": "2025-04",
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
            "End Date": "2015-09",
            "Company": "Bayer Inc",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Medical Operations Business Associate",
            "Employment Type": "Full-time",
            "Start Date": "2013-05",
            "End Date": "2013-09",
            "Company": "GlaxoSmithKline",
            "Location": "Mississauga, Ontario",
        },
        {
            "Job Title": "Medical Operations Business Associate",
            "Employment Type": "Full-time",
            "Start Date": "2012-05",
            "End Date": "2012-09",
            "Company": "GlaxoSmithKline",
            "Location": "Mississauga, Ontario",
        },
    ]

    # Convert the data to a Pandas DataFrame
    df_work_experience = pd.DataFrame(work_experience_data)

    # Convert 'Start Date' and 'End Date' columns to datetime
    df_work_experience["Start Date"] = pd.to_datetime(df_work_experience["Start Date"], errors='coerce').dt.date
    df_work_experience["End Date"] = pd.to_datetime(df_work_experience["End Date"], errors='coerce').dt.date  # 'coerce' handles the 'present' case
    
    df_work_experience.sort_values('End Date', ascending=False, inplace=True)
    df_work_experience.reset_index(drop=True,inplace=True)

    # Calculate duration in years, months, and days
    df_work_experience['Duration'] = df_work_experience.apply(lambda row: relativedelta(row['End Date'], row['Start Date']), axis=1)

    # Create a new column to represent the duration
    df_work_experience['Duration'] = df_work_experience['Duration'].apply(lambda x: (
        f"{x.years} years " if x.years != 0 else "") +
        (f"{x.months} months " if x.months != 0 else "") +
        (f"{x.days} days" if x.years ==0 and x.months == 0 else "")
    )
    #reorder columns in df
    df_work_experience = df_work_experience[["Job Title","Employment Type","Company","Location","Start Date", "End Date", "Duration"]]
    # Specify the order for the legend items
    legend_order = df_work_experience.sort_values("End Date")["Job Title"]

    hover_data = {
        "Job Title": True,
        "Company": False,
        "Start Date": False,
        "End Date": False,
        "Duration": True,
    }

    # Create a horizontal bar chart using Plotly Express with timeline
    fig = px.timeline(
        df_work_experience,
        x_start="Start Date",
        x_end="End Date",
        y="Company",
        color="Job Title",
        hover_data=hover_data,
        # title="Timeline",
        category_orders={"Job Title": legend_order[::-1]},  # Set the order of legend items
    )

    # Customize the layout
    fig.update_layout(xaxis_title="Year")
    fig.update_layout(
        legend=dict(
            x=-0.25,  # Position the legend to the left
            y=-0.2,  # Align the legend vertically to the top
            # traceorder='reversed',
            # yanchor='top',  # Anchor the legend box by its left side
            # xanchor='left',
            orientation='h',  # Set to vertical layout
            font=dict(
            size=16 # Adjust the size value to your preference
            )
        )
    )
    # Customize x-axis date ticks
    fig.update_xaxes(
        dtick="M24",  # Set tick interval to every 12 months (1 year)
        tickformat="%Y",  # Format the tick labels as year only
    )
    # display experience plot
    st.plotly_chart(fig, use_container_width=True)
    if st.button("Show Details", key='experience'):
        # Display the DataFrame as a table
        st.button("Hide",key='clear_experience')
        st.dataframe(df_work_experience)