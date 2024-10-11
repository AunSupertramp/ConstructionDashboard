import streamlit as st
import pandas as pd
from datetime import datetime

def app():
    
    # Load the data
    file_path = 'data/RFA1.xlsx'
    rfa_data = pd.read_excel(file_path, sheet_name='RFA_All Discipline')
    tab0,tab1, tab2, tab3 = st.tabs(["Overview","RFA", "RFI", "RFM"])

    # Clean up the data by renaming columns for better readability

    with tab0:
        st.components.v1.html(
    """
    <iframe title="Next01_TrackingProgress" width="1000" height="622.5" src="
https://app.powerbi.com/view?r=eyJrIjoiMWZlMzI5YmEtYzIxZi00ZmU4LThlNDktM2I5MWIzNDBkMzgzIiwidCI6ImMxYmQwN2IxLWI3YjYtNDdjYS05ZWYwLWNmNjY3MzVkYWFlNiIsImMiOjEwfQ%3D%3D"
frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=1000,
)
    with tab1:
        rfa_data.columns = [
            "Status", "ID", "Review Name", "Workflow", "Initiated By", "Next Action By", 
            "Next Action Due", "Created On", "Finished On", "Total Documents", "Total Steps", 
            "Document Name", "Path", "Description", "Version", "Markup", "Review Status", 
            "Action Upon Completion", "Comments", "Related Actions", "Column 21", 
            "Column 22", "Column 23", "Column 24"
        ]

        # Drop the columns that we don't want to display
        rfa_data = rfa_data.drop(columns=["Review Status", "Next Action By"])

        # Display the RFA Status in a clean table format
        st.title("RFA Status")

        # Create a three-column layout for key metrics
        m1, m2, m3 = st.columns((1, 1, 1))

        # Display the table with important columns
        st.write("Below is the current status of all Request For Approvals (RFA):")
        st.dataframe(rfa_data[['Status', 'ID', 'Review Name', 'Initiated By', 'Next Action Due', 'Comments']],hide_index=1)

        # Convert 'Created On' to datetime format for calculations
        rfa_data['Created On'] = pd.to_datetime(rfa_data['Created On'], errors='coerce')
        rfa_data['Next Action Due'] = pd.to_datetime(rfa_data['Next Action Due'], errors='coerce')

        # Calculate metrics from the RFA data
        total_open_rfas = rfa_data[rfa_data['Status'] == 'OPEN'].shape[0]
        total_closed_rfas = rfa_data[rfa_data['Status'] == 'CLOSED'].shape[0]
        
        # Calculate overdue RFAs as those where the Next Action Due date has passed and status is still OPEN
        today = datetime.now()
        total_overdue_rfas = rfa_data[(rfa_data['Status'] == 'OPEN') & (rfa_data['Next Action Due'] < today)].shape[0]

        

        # Metric 1: Total Open RFAs
        m1.metric(
            label='Total Open RFAs',
            value=total_open_rfas,
            delta=f"{total_open_rfas} Compared to last report",
            delta_color='inverse'
        )

        # Metric 2: Total Closed RFAs
        m2.metric(
            label='Total Closed RFAs',
            value=total_closed_rfas,
            delta=f"{total_closed_rfas} Compared to last report",
            delta_color='inverse'
        )

        # Metric 3: Total Overdue RFAs
        m3.metric(
            label='Total Overdue RFAs',
            value=total_overdue_rfas,
            delta=f"{total_overdue_rfas} Compared to last report",
            delta_color='inverse'
        )




    with tab2:
            

            # Display the RFA Status in a clean table format
            st.title("RFI Status")

            # Create a three-column layout for key metrics
            m1, m2, m3 = st.columns((1, 1, 1))

            # Display the table with important columns
            st.write("Below is the current status of all Request For Approvals (RFA):")
            st.dataframe(rfa_data[['Status', 'ID', 'Review Name', 'Initiated By', 'Next Action Due', 'Comments']],hide_index=1)

            # Convert 'Created On' to datetime format for calculations
            rfa_data['Created On'] = pd.to_datetime(rfa_data['Created On'], errors='coerce')
            rfa_data['Next Action Due'] = pd.to_datetime(rfa_data['Next Action Due'], errors='coerce')

            # Calculate metrics from the RFA data
            total_open_rfas = rfa_data[rfa_data['Status'] == 'OPEN'].shape[0]
            total_closed_rfas = rfa_data[rfa_data['Status'] == 'CLOSED'].shape[0]
            
            # Calculate overdue RFAs as those where the Next Action Due date has passed and status is still OPEN
            today = datetime.now()
            total_overdue_rfas = rfa_data[(rfa_data['Status'] == 'OPEN') & (rfa_data['Next Action Due'] < today)].shape[0]

            

            # Metric 1: Total Open RFAs
            m1.metric(
                label='Total Open RFAs',
                value=total_open_rfas,
                delta=f"{total_open_rfas} Compared to last report",
                delta_color='inverse'
            )

            # Metric 2: Total Closed RFAs
            m2.metric(
                label='Total Closed RFAs',
                value=total_closed_rfas,
                delta=f"{total_closed_rfas} Compared to last report",
                delta_color='inverse'
            )

            # Metric 3: Total Overdue RFAs
            m3.metric(
                label='Total Overdue RFAs',
                value=total_overdue_rfas,
                delta=f"{total_overdue_rfas} Compared to last report",
                delta_color='inverse'
            )

    with tab3:
          

            

            # Display the RFA Status in a clean table format
            st.title("RFM Status")

            # Create a three-column layout for key metrics
            m1, m2, m3 = st.columns((1, 1, 1))

            # Display the table with important columns
            st.write("Below is the current status of all Request For Approvals (RFA):")
            st.dataframe(rfa_data[['Status', 'ID', 'Review Name', 'Initiated By', 'Next Action Due', 'Comments']],hide_index=1)

            # Convert 'Created On' to datetime format for calculations
            rfa_data['Created On'] = pd.to_datetime(rfa_data['Created On'], errors='coerce')
            rfa_data['Next Action Due'] = pd.to_datetime(rfa_data['Next Action Due'], errors='coerce')

            # Calculate metrics from the RFA data
            total_open_rfas = rfa_data[rfa_data['Status'] == 'OPEN'].shape[0]
            total_closed_rfas = rfa_data[rfa_data['Status'] == 'CLOSED'].shape[0]
            
            # Calculate overdue RFAs as those where the Next Action Due date has passed and status is still OPEN
            today = datetime.now()
            total_overdue_rfas = rfa_data[(rfa_data['Status'] == 'OPEN') & (rfa_data['Next Action Due'] < today)].shape[0]

            

            # Metric 1: Total Open RFAs
            m1.metric(
                label='Total Open RFAs',
                value=total_open_rfas,
                delta=f"{total_open_rfas} Compared to last report",
                delta_color='inverse'
            )

            # Metric 2: Total Closed RFAs
            m2.metric(
                label='Total Closed RFAs',
                value=total_closed_rfas,
                delta=f"{total_closed_rfas} Compared to last report",
                delta_color='inverse'
            )

            # Metric 3: Total Overdue RFAs
            m3.metric(
                label='Total Overdue RFAs',
                value=total_overdue_rfas,
                delta=f"{total_overdue_rfas} Compared to last report",
                delta_color='inverse'
            )    
         

    # Footer
    st.markdown("<h6 style='text-align: right; color: grey;'>Aurecon - Bringing ideas to life</h6>", unsafe_allow_html=True)


