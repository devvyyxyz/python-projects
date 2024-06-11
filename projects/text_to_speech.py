import pyttsx3

def text_to_speech(text, output_audio_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_audio_path)
    engine.runAndWait()

# Example usage
text_to_speech('Hello, this is a text-to-speech example.', 'output_audio.mp3')
