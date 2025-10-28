import streamlit as st
from textblob import TextBlob
import random
import string

st.markdown("Moodio - Mood2Emoji Detector")
st.write("Enter a short kid-friendly sentence and see its mood!")

sentence = st.text_input("Type your sentence here:")

BAD_WORDS = ["fuck", "shit", "ass", "bitch", "dick", "piss"]

def kid_safe_text(text):
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split() 
    for word in words:
        if word in BAD_WORDS:
            return "⚠️", "Inappropriate text!"
    return None, None

def get_mood(text):
    emoji, explanation = kid_safe_text(text)
    if emoji:
        return emoji, explanation
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "😊", "Positive Mood!"
    elif polarity < -0.2:
        return "😔", "Negative Mood!"
    else:
        return "😐", "Neutral Mood!"

POSITIVE_MSGS = ["Keep smiling! 😄", "Great vibes! 🌟", "Awesome! 🎉"]
NEUTRAL_MSGS = ["Stay calm 😐", "Just chill ✌️", "All good!"]
NEGATIVE_MSGS = ["It's okay! 😌", "Cheer up! 🌟", "Tomorrow is a new day! 🌈"]


if sentence.strip(): 
    emoji, explanation = get_mood(sentence)
    
    if emoji == "😊":
        st.success(f"{emoji}  — {explanation}")
        st.write(random.choice(POSITIVE_MSGS))
    elif emoji == "😐":
        st.info(f"{emoji}  — {explanation}")
        st.write(random.choice(NEUTRAL_MSGS))
    elif emoji == "😔":
        st.error(f"{emoji}  — {explanation}")
        st.write(random.choice(NEGATIVE_MSGS))
    elif emoji == "⚠️":
        st.warning(f"{emoji}  — {explanation}")


if st.checkbox("Teacher Mode"):
    st.markdown("How Moodio works:")
    st.write("Flow: Text input → Bad word filter → Sentiment analysis → Emoji output")
    st.write("Sentiment polarity (TextBlob):")
    st.write("- Positive (>0.2) → 😊")
    st.write("- Negative (<-0.2) → 😔")
    st.write("- Neutral (-0.2 to 0.2) → 😐")
    st.write("Bad words are filtered for kid safety.")
