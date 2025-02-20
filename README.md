<h1>YouTube Summarizer</h1>
<ul>YouTube Summarizer is a Python-based application that extracts transcripts from YouTube videos and generates concise summaries using Google's Gemini 2.0 Flash language model.</ul>

<h2>Features</h2>
<ul>
  <li>Transcript Extraction: Fetches transcripts from YouTube videos.</li>
  <li>AI-Powered Summarization: Utilizes Google Gemini's API to create concise summaries.</li>
  <li>Thumbnail Download: Downloads the video's thumbnail for reference.</li>
</ul>

<h2>Installation</h2>
<h3>Clone the Repository</h3>
<ul>
  <li>git clone https://github.com/ashthejuan/Youtube-Summarizer.git</li>
  <li>cd Youtube-Summarizer/Youtube-Summarizer</li>
</ul>

<h2>Install Dependencies</h2>
<h3>Ensure you have Python 3.x installed. Install required packages:</h3>
<ul>
  <li>pip install -r requirements.txt</li>
</ul>

<h2>Set Up GOOGLE_GEMINI_API_KEY</h2> 
<h3>Obtain your Google Gemini API key and set it as an environment variable</h3>
<ul><li>export GOOGLE_GEMINI_API_KEY='your-api-key'</li></ul>
<h3>Alternatively, create a .env file in the project directory and add</h3>
<ul><li>GOOGLE_GEMINI_API_KEY=your-api-key</li></ul>

<h2>Usage</h2>
<h3>Run the script with a YouTube URL as an argument</h3>

<ul><li>python main.py 'https://www.youtube.com/watch?v=example'</li></ul>
The script will display the video's title, channel name, and a generated summary.


<h2>Dependencies</h2>
<li>
  <ul>Python 3.x</ul>
  <ul>requests</ul>
  <ul>beautifulsoup4</ul>
  <ul>youtube-transcript-api</ul>
  <ul>google-generativeai</ul>
</li>
<h3>Install all dependencies using pip install -r requirements.txt.</h3>
