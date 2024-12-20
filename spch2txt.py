 import speech_recognition as sr

   def speech_to_text():
       recognizer = sr.Recognizer()

       with sr.Microphone() as source:
           print("Say something:")
           audio = recognizer.listen(source)

       try:
           text = recognizer.recognize_google(audio)
           print("You said:", text)
       except sr.UnknownValueError:
           print("Speech Recognition could not understand audio")
       except sr.RequestError as e:
           print(f"Could not request results from Google Speech Recognition service; {e}")

   if __name__ == "__main__":
       speech_to_text()
