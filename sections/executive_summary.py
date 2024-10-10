# sections/executive_summary.py

import streamlit as st
from sections.utils import display_metrics

def app():
    st.title("Executive Summary")
    st.write("""
    **Project Status:** On Schedule  
    **Overall Progress:** 45% Complete  
    **Key Achievements:** Foundation completed, structural steel installation underway.  
    **Critical Issues:** Delay in material delivery affecting the façade work.
    """)

    # Example metrics
    metrics = [
        {'label': 'Overall Progress', 'value': '45%', 'delta': '+5% since last month'},
        {'label': 'Budget Utilized', 'value': '$4.5M', 'delta': '-$200k under budget'},
        {'label': 'Safety Incidents', 'value': '0', 'delta': 'No incidents'},
    ]

    # Display metrics
    display_metrics(metrics)

def display_metrics(metrics):
    cols = st.columns(len(metrics))
    for col, metric in zip(cols, metrics):
        col.metric(label=metric['label'], value=metric['value'], delta=metric.get('delta'))
