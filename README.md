# Speech Recognition and Sentiment Analysis Project

This project provides tools for speech recognition and sentiment analysis of audio files and YouTube videos. It uses the AssemblyAI API for transcription and sentiment analysis.

## Features

- **Speech Recognition**: Transcribes audio files into text.
- **Sentiment Analysis**: Analyzes the sentiment of transcribed text from YouTube videos.
- **YouTube Integration**: Extracts audio from YouTube videos for analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- An AssemblyAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a file named `api_secrets.py` in both the `speech_recognition` and `sentiment_analyisis` directories.

4. Add your AssemblyAI API key to both `api_secrets.py` files:
   ```python
   API_KEY_ASSEMBLYAI = "your_api_key"
   ```

## Usage

### Speech Recognition

To transcribe an audio file, you need to update the `filename` variable in `speech_recognition/main.py` to the path of your audio file.

```python
# speech_recognition/main.py
filename = "path/to/your/audio.wav"
audio_url = upload(filename)
save_transcript(audio_url, 'file_title')
```

Then, run the script:

```bash
python speech_recognition/main.py
```

The transcript will be saved as `file_title.txt` in the root directory.

### Sentiment Analysis

To perform sentiment analysis on a YouTube video, update the URL in `sentiment_analyisis/main.py`:

```python
# sentiment_analyisis/main.py
if __name__ == "__main__":
    save_video_sentiments("https://www.youtube.com/watch?v=your_video_id")
```

Then, run the script:

```bash
python sentiment_analyisis/main.py
```

The transcript and sentiment analysis results will be saved in the `data` directory.

## Project Structure

```
.
├── data/
│   ├── IOWA_FAMILY_REUNION.txt
│   └── IOWA_FAMILY_REUNION_sentiments.json
├── sentiment_analyisis/
│   ├── api_03.py
│   ├── api_secrets.py
│   ├── main.py
│   └── yt_extractor.py
├── speech_recognition/
│   ├── api_02.py
│   ├── api_secrets.py
│   └── main.py
├── requirements.txt
└── README.md
```
