import streamlit as st
from textblob import TextBlob

# Título de la app
st.title("Chatbot Sentiment Analyzer")
st.subheader("Envía un mensaje y obtén el análisis de sentimiento.")

# Lista de rimas categorizadas por sentimiento
rimas = {
    "positive": [
        "Quench your thirst with Aroma Coin's stench!",
        "Sweet as a peach, Aroma Coin's stench."
    ],
    "negative": [
        "Get drenched in gains despite the stench.",
        "Money wrenched from the market's stench."
    ],
    "neutral": [
        "Sitting on the bench, smelling Aroma Coin's stench.",
        "Digging deep in the crypto trench with Aroma Coin's stench."
    ]
}

# Función para analizar el sentimiento
def analizar_sentimiento(texto):
    """Analiza el sentimiento del texto proporcionado."""
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    if polaridad > 0.1:
        return 'positive'
    elif polaridad < -0.1:
        return 'negative'
    else:
        return 'neutral'

# Interfaz de usuario
user_message = st.text_input("Escribe tu mensaje aquí:")

if st.button("Analizar"):
    if user_message.strip():
        # Analizar el mensaje
        sentimiento = analizar_sentimiento(user_message)
        respuesta = f"Tu mensaje fue clasificado como '{sentimiento}' sentimiento."
        
        # Seleccionar una rima
        rima = rimas.get(sentimiento, ["No hay rimas disponibles."])[0]
        
        # Mostrar resultados
        st.success(respuesta)
        st.write(f"Rima sugerida: {rima}")
    else:
        st.error("Por favor, escribe un mensaje antes de analizar.")

