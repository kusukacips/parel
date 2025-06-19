import streamlit as st
import random
import time
from PIL import Image
import os
import base64

# Set page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

# Custom CSS
st.markdown("""
<style>
/* ... CSS sama seperti sebelumnya ... */
</style>
""", unsafe_allow_html=True)

# Path helper
def get_file_path(filename):
    return os.path.join("birthday", "folder", filename)

# Function to autoplay local audio
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <div class="audio-container">
                <h3>🎵 Birthday Song for You! 🎵</h3>
                <audio controls autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
                <p><small>Note: Some browsers may block autoplay. Click play if it doesn't start.</small></p>
            </div>
            """
        st.markdown(md, unsafe_allow_html=True)

# Balloons
balloons = ["🎈"] * 10

def create_balloons(num_balloons):
    for _ in range(num_balloons):
        balloon = random.choice(balloons)
        size = random.randint(30, 60)
        left = random.randint(0, 90)
        delay = random.uniform(0, 5)
        speed = random.uniform(5, 8)
        st.markdown(f"""
            <div class="balloon" style="
                font-size: {size}px;
                left: {left}%;
                animation-duration: {speed}s;
                animation-delay: {delay}s;
            ">{balloon}</div>
        """, unsafe_allow_html=True)

# Main
def main():
    st.title("🎂 Happy Birthday! 🎉")

    create_balloons(5)

    st.markdown("<h2 style='text-align: center; color: #e91e63;'>Click the button below for a special message!</h2>", unsafe_allow_html=True)

    if st.button("🎁 Open Your Birthday Card!", key="reveal_button", help="Click to reveal your special message"):
        st.markdown("""
            <div class="birthday-card" id="card" style="display: block;">
                <div class="birthday-message">
                    Happy Birthday Parel!<br><br>
                    Wish you all the best.<br>
                    Semoga panjang umur, sehat selalu, dan bahagia selalu.<br>
                    Semangat ya!<br>
                    Semoga cita-cita lu tercapai.<br>
                    Cie udah 21 wkwk! 🎉
                </div>
            </div>
        """, unsafe_allow_html=True)

        song_path = get_file_path("happy-birthday-334876.mp3")
        if os.path.exists(song_path):
            autoplay_audio(song_path)
        else:
            st.warning("Lagu ulang tahun tidak ditemukan.")

        # Birthday Cake
        try:
            cake_img = Image.open(get_file_path("Birthday.jpeg"))
            st.image(cake_img, caption="Happy Birthday Cake!", use_container_width=True)
        except:
            st.warning("Gambar kue tidak ditemukan.")

        # Additional photos
        st.markdown("<h3 style='text-align: center; color: #e91e63;'>More Happy Moments!</h3>", unsafe_allow_html=True)
        cols = st.columns(2)
        try:
            with cols[0]:
                img1 = Image.open(get_file_path("parel.jpeg"))
                st.image(img1, caption="Happy Moment 1", use_container_width=True)
        except:
            st.info("Gambar parel.jpeg tidak ditemukan.")

        try:
            with cols[1]:
                img2 = Image.open(get_file_path("kado.jpeg"))
                st.image(img2, caption="Happy Moment 2", use_container_width=True)
        except:
            st.info("Gambar kado.jpeg tidak ditemukan.")

        st.title("🎂 Tiup Lilin Ulang Tahun!")

        try:
            st.image(get_file_path("cake.gif"), caption="Selamat Ulang Tahun Parel 🎂", use_container_width=True)
        except:
            st.warning("GIF kue tidak ditemukan.")

        # Signature
        st.markdown("""<div class="signature-container"><div style="text-align: left;">""", unsafe_allow_html=True)
        try:
            sig = Image.open(get_file_path("cipaa.jpeg"))
            st.image(sig, width=200, caption="- from cipa", output_format="JPEG")
        except:
            st.markdown("""<div style="width: 120px; height: 90px; background-color: #ffebee;
                            border-radius: 8px; display: inline-block;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                          <p class="signature-text">- from cipa</p>""", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.balloons()

if __name__ == "__main__":
    main()
