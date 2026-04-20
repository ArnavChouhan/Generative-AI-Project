# Back End Code for Project 2

# ==========================================
# AI STORY GENERATOR USING FREE API
# FINAL WORKING VERSION
# ==========================================

from huggingface_hub import InferenceClient

# 🔑 Paste your Hugging Face token here
client = InferenceClient(
    token="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"
)

print("📖 AI STORY GENERATOR (API VERSION)")
print("------------------------------------")

# Take input
story_idea = input("Enter your story idea: ")
genre = input("Choose genre (horror/comedy/sci-fi/fantasy): ")
word_length = input("Enter number of words: ")

# Create prompt
prompt = f"""
Write a {genre} story in about {word_length} words.
Story idea: {story_idea}.
Make it creative and interesting.
"""

try:
    # ✅ Using conversational model correctly
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]# Generate response
    
    response = client.chat_completion(
        model="HuggingFaceH4/zephyr-7b-beta",
        messages=messages,
        max_tokens=200
    )

    # Extract text
    story = response.choices[0].message.content

    print("\n✨ Generated Story:\n")
    print(story)

    # Save option
    save = input("\nSave story to file? (yes/no): ")

    if save.lower() == "yes":
        with open("generated_story.txt", "w", encoding="utf-8") as file:
            file.write(story)

        print("✅ Story saved as generated_story.txt")

except Exception as e:
    print("❌ Error occurred:")
    print(str(e))