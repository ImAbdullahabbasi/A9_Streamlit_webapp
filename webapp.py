import streamlit as st 

# st.set_page_config(page_title="Growth Mindset Challenge")  # Uncomment if needed
st.title("Growth Mindset Challenge: The Web App🚀")

st.header("Welcome to the App")
st.write("Embrace Challenges, learn from mistakes and unlock your full potential😍")

#quote section
st.header("Quote of the Day")
st.write("Faliure is the stepping stone of success")

st.header("What's your challenge today?")
user_input = st.text_input("Describe Challenge")

#condition
if user_input:
    st.success(f"You are Facing: {user_input}. Keep going!")
else:
    st.warning("Tell us about your challenge")

#reflecting
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflection here")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflect on your past experience")

#achievement
st.header("Celebrate your Wins!!")
achievement = st.text_input("Share something that you have accomplished:")

if achievement:
    st.success(f"Amazing! You achieved🎉: {achievement}")
else:
    st.info("Big or small, every achievement counts")

#footer
st.write("-------")
st.write("Keep believing in yourself⭐, never lose hope!!!")
st.write("Created by **Abdullah Abbasi**")
