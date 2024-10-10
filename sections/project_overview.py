# sections/project_overview.py

import streamlit as st
import pandas as pd

def app():
    st.title("Project Overview")
    st.subheader("Project Description")
    st.write("""
    The project involves constructing a 20-story commercial building with a total floor area of 200,000 square feet. The building will include retail spaces, offices, and a rooftop garden.
    """)
    st.subheader("Key Project Details")
    project_details = {
        'Start Date': 'January 1, 2023',
        'Expected Completion Date': 'December 31, 2024',
        'Project Manager': 'Jane Smith',
        'Stakeholders': 'XYZ Development Corp, ABC Architects',
        'Location': 'Downtown Metropolis',
        'Contract Type': 'Design-Build',
    }
    st.table(pd.DataFrame(project_details.items(), columns=['Detail', 'Information']))
