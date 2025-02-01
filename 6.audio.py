!pip install gTTS


from gtts import gTTS


tts = gTTS(final_summary, lang='en')
tts.save("narration.mp3")

print("Audio narration saved as narration.mp3")