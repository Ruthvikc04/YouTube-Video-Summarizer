Youtube Video Transcriptor using Generative AI

Steps to use:

1. Open the YouTube video
2. Turn on the subtitles of the video
3. Copy the link and run the program
4. Paste the link in the terminl
5. Results will be displayed in the terminl

This Python script functions as an automated YouTube video summarizer. It leverages the power of Google's advanced AI model, Gemini Pro, to condense lengthy video content into easily digestible summaries.

Here's how it works:

User Input: The script starts by prompting the user to provide a YouTube video link.
Transcript Extraction: Behind the scenes, the script fetches the full transcript of the video. It does this by first extracting the unique video ID from the provided link and then using a specialized library to retrieve the corresponding transcript data.
AI-Powered Summarization: The heart of the script lies in its interaction with Google's Gemini Pro, a large language model trained on vast amounts of text data. The script sends the extracted transcript to Gemini Pro, along with specific instructions to generate a concise summary focusing on the key points of the video, all within a 250-word limit.
Concise Summary Output: Finally, the script presents the user with the AI-generated summary, providing a quick and efficient way to grasp the essential information conveyed in the YouTube video.

In short, this tool streamlines the process of understanding video content by automating the often time-consuming task of watching and summarizing. It's particularly useful for quickly getting the gist of educational videos, lengthy presentations, or any YouTube content where a concise overview is desired.

(Install the requirements if the program is not running by typing "pip install -r requirements.txt" in the terminal)