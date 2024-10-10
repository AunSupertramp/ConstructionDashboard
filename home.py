import streamlit as st

def app():
    # Set the page configuration
     
    # Project Information
    st.title("GSA NEXT 01 Project")
    st.subheader("Project Management / Construction Management")
    st.write("### Monthly Report #24  September 2024")
    st.write("Date: 2024-10-08")

    st.components.v1.html(
    """
    <iframe title="Speckle" src="https://speckle.aurecongroup.digital/projects/a5a8d8d39e/models/all#embed=%7B%22isEnabled%22%3Atrue%7D" width="600" height="400" frameborder="0"></iframe>
    """,
    height=400,
)
    
    # Footer
    st.markdown("<h6 style='text-align: right; color: grey;'>Aurecon - Bringing ideas to life</h6>", unsafe_allow_html=True)