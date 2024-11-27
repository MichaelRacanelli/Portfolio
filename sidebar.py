import streamlit as st

def download_pdf_resume():
    st.header("Download Resume")
    st.write("Please click below to download a copy of my CV.")

    # Load the PDF file as bytes
    pdf_file_path = "MRacanelli_CV.pdf"  # Replace with the path to your PDF file
    with open(pdf_file_path, "rb") as f:
        pdf_bytes = f.read()

    # Create a download link
    st.download_button(
        "Download Resume PDF",
        pdf_bytes,
        key='download_button',
        file_name="MRacanelli_CV.pdf",  # Change the file name as needed
        mime="application/pdf"
    )

def show_sidebar():
    with st.sidebar:
        st.image("./images/profile_pic.jpg")
        st.header("Michael Racanelli")
        st.header('Data Scientist')
        st.header("Contact Information")
        st.markdown("Location: Oakville, ON, Canada")
        st.markdown("Phone: +1 519 281 1284")
        st.markdown("Email: [m.v.racanelli@gmail.com](mailto:m.v.racanelli@gmail.com)")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/michaelvincentracanelli/)")
        st.markdown("[GitHub](https://github.com/MichaelRacanelli)")
        download_pdf_resume()