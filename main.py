from dotenv import load_dotenv
load_dotenv()  
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        if "Could not retrieve a transcript" in str(e):
            print("Error: No transcript available for this video. It might have subtitles disabled.")
            return None
        else:
            print("An error occurred:", e)
            return None

def generate_gemini_content(transcript_text, prompt):
    if transcript_text:  # Check if we have a transcript before calling Gemini
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    else:
        return "No transcript available to generate a summary."

if __name__ == "__main__":
    youtube_link = input("Enter YouTube Video Link: ")
    
    transcript_text = extract_transcript_details(youtube_link)

    summary = generate_gemini_content(transcript_text, prompt)
    print("\nDetailed Notes:\n")
    print(summary)