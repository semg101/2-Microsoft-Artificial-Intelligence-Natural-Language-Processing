import speech_recognition as sr



# transcribe audio file                                                         
AUDIO_FILE = 'filem.wav'

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file                  

    #print("Transcription: " + r.recognize_google(audio, language = "en-us", show_all=False))
    #print("Transcription: " + r.recognize(audio))
    r.recognize_wit(audio, key ="",show_all=False)