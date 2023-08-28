import streamlit as st
import requests
from PIL import Image

im = Image.open('/home/fll_data_bata/code/Franloplam/Cat_Final/cat-face-emoji-2048x1821-x3kf878r.png')

st.set_page_config(page_title="Prrfesor App",page_icon=im)

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: #FFF9F8;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .sidebar {
        position: fixed;
        left: 0;
        top: 0;
        height: 100%;
        width: 250px;
        padding: 20px;
        background-color: lightgray;
    }
    .vertical-text {
        writing-mode: tb-rl;
        white-space: nowrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("**What is Prrfesor?**")
st.sidebar.write(
    """*Pets are part of our life. They are there day and night,
       accompanying us day by day. To show our love for them we have created this application.
       Prrfesor allows us to better understand our feline friends and, in this way, have better
       communication with them*""",
    unsafe_allow_html=True,
    key="vertical-text",
)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("Welcome to Prrfesor!:cat2:")

st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("Please, upload a cat sound (WAV file)")

uploaded_file = st.file_uploader("", type=["wav"])

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    # Realizar una solicitud HTTP aquí usando el archivo cargado
    files = {"file": uploaded_file}
    response = requests.post("https://catappok2-ln2jrz6hea-uc.a.run.app/predict/", files=files)
    if response.status_code == 200:
        result = response.json()["result"]
        st.write("Answer:", result)
    else:
        st.write("An error occurred.")

st.markdown("<hr>", unsafe_allow_html=True)

sample_audio_link = "https://github.com/Franloplam/Prrfesor/blob/master/B_CAN01_EU_FN_GIA01_1SEQ1.wav"
st.markdown("**Download the sample audio, save it, and use it to test the app**")
st.markdown(f"**[Sample Audio]({sample_audio_link})**")
