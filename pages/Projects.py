import streamlit as st
from sidebar import show_sidebar

def main():
    show_sidebar()
    
    st.header("Projects")
    st.subheader("Project 1: [Project Title]")
    st.write(
        "Description: Provide a brief description of the project, highlighting your role and the impact of your work. "
        "Include any relevant technologies or tools used."
    )

    st.subheader("Project 2: [Project Title]")
    st.write("Description: [Provide a brief description of the project]")

    # Add more projects as needed

if __name__ == "__main__":
    main()
