import streamlit as st
from textblob import TextBlob
import random

# List of rhymes related to "stench" and "The Aroma Coin" categorized by sentiment
rhymes = {
    "positive": [
        "Quench your thirst with Aroma Coin's stench!",
        "Sweet as a peach, Aroma Coin's stench.",
        "Relax on the beach while Aroma Coin's stench.",
        "Extend your reach with Aroma Coin's stench."
    ],
    "negative": [
        "Get drenched in gains despite the stench.",
        "Clench your coins tight despite the stench.",
        "Money wrenched from the market's stench.",
        "Purify your portfolio, bleach away the stench."
    ],
    "neutral": [
        "Sitting on the bench, smelling Aroma Coin's stench.",
        "Tighten your wallet with Aroma Coin's stench.",
        "Digging deep in the crypto trench with Aroma Coin's stench."
    ]
}

def analyze_sentiment(text):
    """Analyzes the sentiment of the provided text."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

def extract_context(text):
    """Extracts key phrases from the provided text."""
    blob = TextBlob(text)
    key_phrases = blob.noun_phrases
    return ', '.join(key_phrases[:2]) if key_phrases else ''

def generate_natural_response(context, sentiment):
    """Generates a natural response based on context and sentiment."""
    preludes = {
        "positive": [
            "That's great to hear!",
            "Sounds like something exciting!",
            "What a positive vibe!"
        ],
        "negative": [
            "Oh, that doesn't sound great.",
            "Hmm, seems like a tricky situation.",
            "That's unfortunate to hear."
        ],
        "neutral": [
            "Interesting point.",
            "That's quite neutral, let's see...",
            "Okay, I get it."
        ]
    }
    prelude = random.choice(preludes.get(sentiment, ["Hmm, let's dive into that."]))
    return f"{prelude} I noticed you're talking about {context}." if context else prelude

# Streamlit UI
st.title("Sentiment and Context Chatbot")
st.write("Type a message and the chatbot will analyze its sentiment and provide a response with a rhyme.")

user_message = st.text_input("Your message:")
if st.button("Analyze"):
    if user_message.strip():
        sentiment = analyze_sentiment(user_message)
        context = extract_context(user_message)
        response = generate_natural_response(context, sentiment)
        rhyme = random.choice(rhymes.get(sentiment, ["Sorry, no rhymes available."]))
        st.success(f"Response: {response}")
        st.info(f"Rhyme: {rhyme}")
    else:
        st.error("Please enter a message to analyze.")
