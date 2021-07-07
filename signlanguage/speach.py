import speech_recognition as sr
import time
r = sr.Recognizer()
print("Speech Recognition is running... ")

while(1):
    try:
        time.sleep(2)
        '''
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("text is :",MyText)
        '''
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occured")