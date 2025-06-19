import streamlit as st
import random
import time
from PIL import Image
import os
import base64

# Set page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

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

# Balloon colors and emojis
balloons = ["🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈"]

# Function to create balloons
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
    
    # Create balloons continuously
    while True:
        create_balloons(5)
        time.sleep(0.5)
        # We need to break the loop at some point, but keep it running for the demo
        break
    
    st.markdown("<h2 style='text-align: center; color: #e91e63;'>Click the button below for a special message!</h2>", unsafe_allow_html=True)
    
    # Button to reveal message
    if st.button("🎁 Open Your Birthday Card!", key="reveal_button", help="Click to reveal your special message"):
        # Birthday card
        st.markdown("""
            <div class="birthday-card" id="card" style="display: block;">
                <div class="birthday-message">
                    Happy Birthday Parel!<br><br>
                    Wish you all the best.<br>
                    Semoga panjang umur, sehat selalu, dan bahagia selalu.<br>
                    Semangat ya!.<br>
                    Semoga cita-cita lu tercapai.<br>
                    Cie udah 21 wkwk! 🎉
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Play birthday song from local file
        song_path = "D:/streamlit/birthday/happy-birthday-334876.mp3"
        try:
            if os.path.exists(song_path):
                autoplay_audio(song_path)
            else:
                st.warning(f"Couldn't find the birthday song at: {song_path}")
                st.info("Here's a placeholder song instead 🎵")
        except Exception as e:
            st.error(f"Error loading song: {str(e)}")
            st.info("Here's a placeholder song instead 🎵")
        
        # Birthday cake image - local file
        image_path = "D:/streamlit/birthday/Birthday.jpeg"
        try:
            if os.path.exists(image_path):
                cake_img = Image.open(image_path)
                st.image(
                    cake_img, 
                    caption="Happy Birthday Cake!", 
                    use_container_width=True,
                    width=300
                )
            else:
                st.warning(f"Couldn't find the image at: {image_path}")
                st.info("Here's a placeholder cake instead 🎂")
        except Exception as e:
            st.error(f"Error loading image: {str(e)}")
            st.info("Here's a placeholder cake instead 🎂")
        
        # Additional photos section
        st.markdown("<h3 style='text-align: center; color: #e91e63;'>More Happy Moments!</h3>", unsafe_allow_html=True)
        
        # Create a container for additional photos
        cols = st.columns(2)
        
        # First additional photo
        with cols[0]:
            try:
                photo1_path = "D:/streamlit/birthday/parel.jpeg"
                if os.path.exists(photo1_path):
                    photo1 = Image.open(photo1_path)
                    st.image(
                        photo1,
                        caption="Happy Moment 1",
                        use_container_width=True
                    )
                else:
                    st.info("First photo placeholder 🎈")
            except Exception as e:
                st.error(f"Error loading first photo: {str(e)}")
        
        # Second additional photo
        with cols[1]:
            try:
                photo2_path = "D:/streamlit/birthday/kado.jpeg"
                if os.path.exists(photo2_path):
                    photo2 = Image.open(photo2_path)
                    st.image(
                        photo2,
                        caption="Happy Moment 2",
                        use_container_width=True
                    )
                else:
                    st.info("Second photo placeholder 🎈")
            except Exception as e:
                st.error(f"Error loading second photo: {str(e)}")
        # Birthday candle section
        st.title("🎂 Tiup Lilin Ulang Tahun!")
        
        st.image("cake.gif", caption="Selamat Ulang Tahun Parel 🎂", use_container_width=True)
        
        # Signature section - NOW ON LEFT SIDE
        st.markdown("""
            <div class="signature-container">
                <div style="text-align: left;">
        """, unsafe_allow_html=True)
        
        try:
            signature_path = "D:/streamlit/birthday/cipaa.jpeg"
            if os.path.exists(signature_path):
                signature_img = Image.open(signature_path)
                st.image(
                    signature_img,
                    width=200,
                    caption="- from cipa",
                    output_format="JPEG"
                )
            else:
                st.markdown("""
                    <div style="width: 120px; height: 90px; background-color: #ffebee;
                                border-radius: 8px; display: inline-block;
                                box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                    <p class="signature-text">- from cipa</p>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error loading signature: {str(e)}")
        
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Confetti effect
        st.balloons()

if __name__ == "__main__":
    main()