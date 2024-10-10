import streamlit as st
import pandas as pd
from datetime import datetime

def app():
    # Title for the page
    st.title("Project Description")

    # Data containing the project details
    data = {
        "Description": [
            "Project Name", 
            "Building Description", 
            "Scope of Work", 
            "Contract Sum", 
            "Owner", 
            "Consultant", 
            "Architect Designer", 
            "Structure Designer", 
            "Electrical Designer", 
            "Sanitary Designer", 
            "A/C & Ventilation Designer", 
            "Construction Time", 
            "Start Date", 
            "Finish Date", 
            "Time Passed",
            "Project Manager"
        ],
        "Details": [
            "NEXT01", 
            "Data center", 
            "Architecture/Structure/MEP", 
            "30,600,000.00 USD", 
            "XAXAXA XAXA", 
            "XAXAXA XAXA", 
            "XAXAXA XAXA", 
            "XAXAXA XAXA", 
            "AURECON", 
            "AURECON", 
            "AURECON", 
            "30 Months", 
            "5 Oct 2022", 
            "2 Apr 2025", 
            "",  # Placeholder for Time Passed
            "Charoen Thanapirom"
        ]
    }

    # Extract the start date from the data and calculate time passed
    start_date_str = data["Details"][12]  # Get the start date from the data
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    today = datetime.today()

    # Calculate the time passed in months
    time_passed = (today.year - start_date.year) * 12 + today.month - start_date.month

    # Update the "Time Passed" value in the data
    data["Details"][14] = f"{time_passed} Months"

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Display the table in Streamlit
    st.dataframe(df,hide_index=1)

    # Footer
    st.markdown("<h6 style='text-align: right; color: grey;'>Aurecon - Bringing ideas to life</h6>", unsafe_allow_html=True)


