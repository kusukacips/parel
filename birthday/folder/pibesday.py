import streamlit as st
import random
import time
from PIL import Image
import os
import base64

# Set page config
st.set_page_config(page_title="Happy Birthday Parel!", page_icon="🎉")

# Custom CSS for balloons and animation
st.markdown("""
    <style>
    @keyframes float {
        0% {
            transform: translateY(100vh) scale(0.6);
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-20vh) scale(1);
            opacity: 0;
        }
    }

    .balloon {
        position: fixed;
        bottom: 0;
        animation: float 6s ease-in-out forwards;
        z-index: 999;
    }

    .birthday-card {
        background-color: #fff9c4;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        margin: 20px 0;
        transform: rotate(-2deg);
        border: 1px dashed #ff9800;
        display: none;
    }

    .birthday-message {
        font-family: 'Comic Sans MS', cursive;
        font-size: 18px;
        color: #d32f2f;
        text-align: center;
    }

    .cake-image {
        max-width: 300px;
        margin: 20px auto;
        display: block;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .additional-photos {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
        flex-wrap: wrap;
    }

    .additional-photo {
        max-width: 250px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .signature-container {
        display: flex;
        justify-content: flex-start;
        margin-top: 30px;
    }

    .signature-photo {
        max-width: 120px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .signature-text {
        font-family: 'Comic Sans MS', cursive;
        font-size: 14px;
        color: #e91e63;
        text-align: left;
        margin-top: 5px;
        font-style: italic;
    }

    .reveal-button {
        background-color: #ff5722;
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px auto;
        cursor: pointer;
        border-radius: 25px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .audio-container {
        margin: 20px auto;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to get relative path
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
                <p><small>Note: Some browsers may block autoplay. Click play if song doesn't start automatically.</small></p>
            </div>
        """
        st.markdown(md, unsafe_allow_html=True)

# Balloon emojis
balloons = ["🎈"] * 10

# Function to animate balloons
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

# Main app
def main():
    st.title("🎂 Happy Birthday! 🎉")

    create_balloons(5)

    st.markdown("<h2 style='text-align: center; color: #e91e63;'>Click the button below for a special message!</h2>", unsafe_allow_html=True)

    if st.button("🎁 Open Your Birthday Card!", key="reveal_button", help="Click to reveal your special message"):
        # Birthday message
        st.markdown("""
            <div class="birthday-card" id="card" style="display: block;">
                <div class="birthday-message">
                    Happy Birthday Parel!<br><br>
                    Wish you all the best.<br>
                    Semoga panjang umur, sehat selalu, dan bahagia selalu.<br>
                    Semangat ya!<br>
                    Sukses terus pokoknyaa, sama sehat2 terus yaa.<br>
                    Cie udah 21 wkwk! 🎉
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Birthday song
        song_path = get_file_path("happy-birthday-334876.mp3")
        if os.path.exists(song_path):
            autoplay_audio(song_path)
        else:
            st.warning("Birthday song file not found.")

        # Cake image
        try:
            cake_img = Image.open(get_file_path("Birthday.jpeg"))
            st.image(cake_img, caption="Happy Birthday Cake!", use_container_width=True)
        except:
            st.warning("Cake image not found.")

        # Additional photos
        st.markdown("<h3 style='text-align: center; color: #e91e63;'>More Happy Moments!</h3>", unsafe_allow_html=True)
        cols = st.columns(2)
        try:
            with cols[0]:
                img1 = Image.open(get_file_path("parel.jpeg"))
                st.image(img1, caption="Happy Moment 1", use_container_width=True)
        except:
            st.info("Photo parel.jpeg not found.")
        try:
            with cols[1]:
                img2 = Image.open(get_file_path("kado.jpeg"))
                st.image(img2, caption="Happy Moment 2", use_container_width=True)
        except:
            st.info("Photo kado.jpeg not found.")

        # Candle GIF
        st.title("🎂 Tiup Lilin Ulang Tahun!")
        try:
            st.image(get_file_path("cake.gif"), caption="Selamat Ulang Tahun Parel 🎂", use_container_width=True)
        except:
            st.warning("GIF not found.")

        # Signature
        st.markdown("""<div class="signature-container"><div style="text-align: left;">""", unsafe_allow_html=True)
        try:
            sig = Image.open(get_file_path("cipaa.jpeg"))
            st.image(sig, width=200, caption="- from cipa", output_format="JPEG")
        except:
            st.markdown("""
                <div style="width: 120px; height: 90px; background-color: #ffebee;
                            border-radius: 8px; display: inline-block;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                <p class="signature-text">- from cipa</p>
            """, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.balloons()

if __name__ == "__main__":
    main()
