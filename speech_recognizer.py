import speech_recognition as sr

recognizer = sr.Recognizer()

# Load the Google Cloud credentials JSON file
credentials_path = 'speech_recognition_app/credentials/your_credentials.json'
recognizer.recognize_google_cloud(credentials_json=open(credentials_path).read())

def recognize_speech(audio):
    """
    Perform speech recognition using Google Cloud's Speech-to-Text API.

    Args:
        audio (AudioData): Audio data captured from the microphone.

    Returns:
        str: The recognized text from the audio.
    """
    try:
        recognized_text = recognizer.recognize_google_cloud(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Google Cloud Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Cloud Speech Recognition service; {e}"
