import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  

import cohere
import whisper
from gtts import gTTS


# ==========================================
# CONFIGURATION
# ==========================================
# Paste your actual Cohere API key here
COHERE_API_KEY = "YOUR_COHERE_API_KEY"  
INPUT_AUDIO_PATH = "input.wav"
OUTPUT_AUDIO_PATH = "response.mp3"

# Initialize Cohere Client
co = cohere.ClientV2(COHERE_API_KEY)


def speech_to_text(audio_file_path: str) -> str:
    """Step 1: Convert audio input to text locally using OpenAI Whisper."""
    print(" Loading local Whisper model...")
    model = whisper.load_model("tiny")
    
    print(" Transcribing audio file locally...")
    result = model.transcribe(audio_file_path)
    text = result["text"].strip()
    
    print(f" Recognized Text: \"{text}\"")
    return text


def generate_llm_response(prompt_text: str) -> str:
    """Step 2: Generate response using an active Cohere LLM model."""
    print(" Sending prompt to Cohere LLM...")
    response = co.chat(
        model="command-r7b-12-2024",  # Active Cohere Chat model
        messages=[{"role": "user", "content": prompt_text}]
    )
    reply_text = response.message.content[0].text
    print(f" LLM Response: \"{reply_text}\"")
    return reply_text


def text_to_speech(text: str, output_path: str):
    """Step 3: Convert LLM text response to an audio file."""
    print(" Converting LLM response to audio...")
    # Set lang='en' for English or lang='ar' for Arabic output
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(output_path)
    print(f" Audio saved to '{output_path}'")


def main():
    if not os.path.exists(INPUT_AUDIO_PATH):
        print(f" Error: Place a WAV audio file named '{INPUT_AUDIO_PATH}' in this folder.")
        return

    user_text = speech_to_text(INPUT_AUDIO_PATH)
    if user_text:
        ai_response = generate_llm_response(user_text)
        text_to_speech(ai_response, OUTPUT_AUDIO_PATH)
        print("\n Task Completed Successfully!")


if __name__ == "__main__":
    main()