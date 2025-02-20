import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def summarize_text(text, lang='en'):
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing API key. Set GOOGLE_GEMINI_API_KEY in environment variables.")

    genai.configure(api_key=api_key)
    
    prompt = f"""
    The following text is in its original language. Provide the output in this language: {lang}.
    
    **Summary:**  
    (short summary of the video)  

    **Key Takeaways:**  
    - (bullet points of key takeaways)  

    **Input text:** {text}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text.strip()

if __name__ == "__main__":
    text_to_summarize = input("Enter the text to summarize: ")
    lang = input("Enter the language for the summary: ")
    
    try:
        summary = summarize_text(text_to_summarize, lang)
        print("\nSummary:\n")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")
