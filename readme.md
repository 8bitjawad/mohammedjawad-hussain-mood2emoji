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

### Teaching the App in 60 Minutes

Here’s how I’d teach students aged 12–16 using Moodio:

1. **Introduction (5 min)**  
   - Explain the concept of **mood in text** and **sentiment analysis**. 
   - Show a few sentences and ask students how they feel.

2. **App Demo (10 min)**  
   - Type a few example sentences into Moodio.  
   - Show how the **emoji changes** based on mood.  
   - Highlight the **Teacher Mode** and explain the flow:  
     Text input → Bad word filter → Sentiment analysis → Emoji output.

3. **Hands-on Activity (25 min)**  
   - Students type their own sentences.  
   - Predict the emoji first, then see the app output.  
   - Discuss any surprises or misclassifications.

4. **Explain the Code & Logic (15 min)**  
   - Introduce **TextBlob** sentiment polarity.  
   - Show how positive (>0.2), negative (<-0.2), and neutral (-0.2 to 0.2) are mapped.  
   - Explain **kid-safe filtering** and why it’s important.

5. **Wrap-up & Learning Outcome (5 min)**  
   - Recap: how computers can **analyze text** and detect mood.  
   - Ask students what they learned and how it could be improved.  


### Learning Outcomes
Understand how computers can analyze text and detect mood.

Learn about sentiment polarity in natural language processing.

Explore simple web app development with Streamlit.

Teach kids coding concepts through an interactive app.

### Known Limitations
TextBlob is simple; complex or sarcastic sentences may be misclassified.

Only filters a small list of bad words and it might miss some phrases.

### References

- [TextBlob](https://textblob.readthedocs.io/en/dev/)
