import streamlit as st

def app():
    st.title('Shop Drawing Progress')
    st.image('data/shopprogress/shopdrawingprogress.jpg')
    
    # Footer
    st.markdown("<h6 style='text-align: right; color: grey;'>Aurecon - Bringing ideas to life</h6>", unsafe_allow_html=True)