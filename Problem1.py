# # Core API Request Handler Implementation

# from huggingface_hub import InferenceClient

# # Initialize API Client
# client = InferenceClient(
#     token="hf_your_token_here"
# )

# # Create Prompt
# prompt = f"""
# Write a {genre} story in about {word_length} words.
# Story idea: {story_idea}.
# Make the story creative and interesting.
# """

# # Send Request to AI Model
# messages = [
#     {
#         "role": "user",
#         "content": prompt
#     }
# ]

# response = client.chat_completion(
#     model="HuggingFaceH4/zephyr-7b-beta",
#     messages=messages,
#     max_tokens=word_length
# )

# # Extract Generated Story
# story = response.choices[0].message.content