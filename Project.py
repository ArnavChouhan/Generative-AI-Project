# ==========================================
# AI STORY GENERATOR WEB APP (STREAMLIT)
# ==========================================

import streamlit as st
from huggingface_hub import InferenceClient
from datetime import datetime

# 🔑 Paste your NEW Hugging Face token here
client = InferenceClient(
    token="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"
)

# Page title
st.title("📖 AI Story Generator")
st.write("Generate creative AI stories using AI!")

# Genre dropdown
genre = st.selectbox(
    "Choose Genre",
    ["horror", "comedy", "fantasy", "sci-fi"]
)

# Story idea input
story_idea = st.text_input(
    "Enter your story idea"
)

# Word length slider
word_length = st.slider(
    "Select story length",
    min_value=50,
    max_value=300,
    value=120
)

# Generate button
if st.button("Generate Story"):

    if story_idea == "":
        st.warning("Please enter a story idea.")

    else:

        prompt = f"""
        Write a {genre} story in about {word_length} words.
        Story idea: {story_idea}.
        Make the story creative and interesting.
        """

        try:

            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            response = client.chat_completion(
                model="HuggingFaceH4/zephyr-7b-beta",
                messages=messages,
                max_tokens=word_length
            )

            story = response.choices[0].message.content

            st.subheader("✨ Generated Story")
            st.write(story)

            # Save history
            current_time = datetime.now()

            with open("story_history.txt", "a", encoding="utf-8") as file:
                file.write("\n\n====================\n")
                file.write(f"Date: {current_time}\n")
                file.write(f"Genre: {genre}\n")
                file.write(f"Idea: {story_idea}\n\n")
                file.write(story)

            st.success("Story saved to history!")

        except Exception as e:
            st.error(f"Error: {str(e)}")





