import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from random import randint
import time
import requests
#[theme]
#primaryColor="#3b185f"
#backgroundColor="#ffefd6"
#secondaryBackgroundColor="#f0caa3"
#textColor="#0e5e6f"


def load_lottieurl(url: str):
    r=requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()
def tossup():
        value = randint(0,1)
        if user_choice ==value:
            st.success("Hurray, You have the toss!")
        else:
            st.error("Sorry, It's a wrong call!")
tab1,tab2,tab3=st.tabs(["Home","Toss","Camera"])
with tab1:

    lottie_url_welcome="https://assets10.lottiefiles.com/packages/lf20_g8iumlrs.json"
    lottie_welcome= load_lottieurl(lottie_url_welcome)
    st.title("Welcome to J24 app!!")
    st_lottie(lottie_welcome, key = 'welcome')
    col1,col2=st.columns([1,1])
    col1.header("==>You can check out the Camera :camera: to click few pictures.")
    col1.header("==>Wanna Flip a Coin? Check out toss 🪙")
with tab2:
    lottie_url_toss="https://assets3.lottiefiles.com/temp/lf20_zBfmHv.json"
    lottie_toss= load_lottieurl(lottie_url_toss)
    st.title("1 For Heads and 0 For Tails")
    st_lottie(lottie_toss, key = 'coin')
    
    user_choice=st.slider('Heads or Tails',min_value=0, max_value=1, step=1)
    letsgo=st.button('Lets Go')
    if letsgo:
        tossup()
    


with tab3:

    st.title("Cheeeese 😁")
    lottie_url_camera="https://assets10.lottiefiles.com/packages/lf20_O67fb5.json"
    lottie_camera= load_lottieurl(lottie_url_camera)
    st_lottie(lottie_camera, key = 'camera')
    def change_photo_state():
        st.session_state["photo"]="done"
    camera_photo=st.camera_input("Face the camera", on_change=change_photo_state)
    def change_photo_state():
        st.session_state["photo"]="done"

    if st.session_state["photo"]=="done":
        progress_bar = st.progress(0)
        for perc_completed in range(100):
            time.sleep(0.02)
            progress_bar.progress(perc_completed+1)

        st.success("U r looking great today!!🤩")
    





