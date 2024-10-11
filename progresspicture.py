import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
def app():
    st.title('Progress Picture')
    # render image-comparison
    image_comparison(
        img1="data/workprogress/img1.png",
        img2="data/workprogress/img2.png",
        label1="23/07/2024",
        label2="15/08/2024",
        width=700,
        starting_position=50,
        show_labels=True,
        make_responsive=True,
        in_memory=True,
    )
    st.write('NEXT01 DRONE SHOT',)