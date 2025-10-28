# Moodio - Mood2Emoji 😄😐😔

A simple kid-friendly web app that takes a short sentence and returns an emoji representing the mood, along with a short explanation. Built with **Streamlit** and **TextBlob**.  

Suitable for students aged **12–16**.

---

# Features

- Input a sentence and get a **mood emoji**:
  - 😊 Positive
  - 😐 Neutral
  - 😔 Negative
- **Kid-safe filter** blocks inappropriate words.
- Optional **Teacher Mode** shows how the app works (text flow and sentiment analysis).
- Random fun messages for extra engagement.

---

## Demo

- Enter a sentence like `"I got a new puppy!"` → Output: 😊 — Positive Mood!  
- Enter a neutral sentence like `"I went to school today."` → 😐 — Neutral Mood!  
- Enter a sentence with a bad word → ⚠️ — Inappropriate text!

---

## Installation

1. Clone the repo:

```
git clone https://github.com/yourusername/mohammed-jawad-mood2emoji.git
cd mohammed-jawad-
```
### Install dependencies:
```
pip install -r requirements.txt
```
### Run the app:

```
streamlit run app.py
```

### How It Works
Input sentence → check for bad words → return warning if any.

If safe, analyze sentiment using TextBlob.

Map sentiment polarity to emoji:

Positive (>0.2) → 😊

Negative (<-0.2) → 😔

Neutral (-0.2 to 0.2) → 😐

Show random encouraging messages depending on mood.

Teacher Mode explains the flow to students.

### Learning Outcomes
Understand how computers can analyze text and detect mood.

Learn about sentiment polarity in natural language processing.

Explore simple web app development with Streamlit.

Teach kids coding concepts through an interactive app.

### Known Limitations
TextBlob is simple; complex or sarcastic sentences may be misclassified.

Only filters a small list of bad words and it might miss some phrases.