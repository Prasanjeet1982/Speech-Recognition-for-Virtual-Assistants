from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import speech_recognition as sr
from ..recognition.speech_recognizer import recognize_speech

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Render the HTML template
    with open("speech_recognition_app/templates/index.html", "r") as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.post("/recognize")
def recognize_audio():
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)  # Set a timeout for audio input
            recognized_text = recognize_speech(audio)
            return {"recognized_text": recognized_text}
        except sr.WaitTimeoutError:
            return {"error": "Timeout waiting for audio. Please try again."}
