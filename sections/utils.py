# sections/utils.py

import streamlit as st

def display_metrics(metrics):
    cols = st.columns(len(metrics))
    for col, metric in zip(cols, metrics):
        col.metric(label=metric['label'], value=metric['value'], delta=metric.get('delta'))
