import streamlit as st
from streamlit_option_menu import option_menu

import home
import projectdes
import docstatus
import progresspicture
import shopdrawingprogress
st.set_page_config(layout="wide")
with st.sidebar:
    st.image('data/logo/aureconlogo1.png', use_column_width=True)
    selected = option_menu(
        menu_title="Menu",
        options=['Home','Project Descriptions','Work Progess','Progress Picture','Document Status','Variation Order','Equipment Report','Manpower Report','Shop Drawing Status'],
        icons=["house",'book']
    )
    
if selected == 'Home':
        home.app()
if selected == 'Project Descriptions':
        projectdes.app()
if selected == 'Document Status':
        docstatus.app()
if selected == 'Progress Picture':
        progresspicture.app()
if selected == 'Shop Drawing Status':
        shopdrawingprogress.app()
