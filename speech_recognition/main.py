import requests
requests.get("https://api.github.com")
from api_02 import *

filename = "C:/Users/Malay Thoria/Desktop/ai_ml_pro/output.wav"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')