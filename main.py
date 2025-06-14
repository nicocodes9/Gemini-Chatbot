import os
import google.generativeai as genai

# --- Configuration ---
# IMPORTANT: Replace 'YOUR_API_KEY' with the API key you obtained from Google AI Studio.
# For better security in real applications, consider storing your API key
# as an environment variable (e.g., in a .env file and loading it with python-dotenv)
# and accessing it like: os.getenv("GEMINI_API_KEY")
API_KEY = "YoUR_API_KEY"  # Replace with your actual API key
# Ensure the API key is set before proceeding

# Configure the Google Generative AI library with your API key.
# This makes the API key available globally for subsequent API calls.
genai.configure(api_key=API_KEY)

# --- Model Selection ---
# Choose a model. 'gemini-2.0-flash' is a fast and cost-effective option
# suitable for many text generation tasks.
# You can list available models by uncommenting and running the following:
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
MODEL_NAME = 'gemini-2.0-flash' # Or 'model name we areusing in this project

# --- Initialize the Generative Model ---
# Create an instance of the GenerativeModel with the chosen model.
model = genai.GenerativeModel(MODEL_NAME)

# --- Send a Message and Get a Response ---
def send_message_to_gemini(prompt_text):
    """
    Sends a text prompt to the Gemini API and returns the generated response.
    """
    # print(prompt_text) Print the prompt for debugging purposes
    try:
        # The generate_content method sends the prompt to the model.
        # It can handle various inputs (text, images) and returns a response object.
        response = model.generate_content(prompt_text)

        # Access the generated text from the response.
        # The 'text' attribute directly gives the content of the model's reply.
        if response.text:
            return response.text
        else:
            # Handle cases where the model might not return text directly
            # (e.g., if content filtering is applied or an error occurs).
            print("Gemini did not return a text response.")
            # You can print the full response object for debugging:
            # print(response)
            return "No response text received."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to get response from Gemini API."

# --- Main Program Execution ---
if __name__ == "__main__":
    print("Welcome to the Gemini API Chat!")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting chat. Goodbye!")
            break

        # Send the user's message to the Gemini API
        gemini_response = send_message_to_gemini(user_input)

        # Display Gemini's response
        print(f"Gemini: {gemini_response}")
