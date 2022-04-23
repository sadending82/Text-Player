from gtts import gTTS
import os
from playsound import playsound


def speak(txt, lang='ko'):
    tts = gTTS(text=txt, lang=lang)
    tts.save('tempfile.mp3')
    playsound('tempfile.mp3')
    os.remove('tempfile.mp3')


if __name__ == "__main__":
    speak("이 바보야 진짜 아니야")
    speak("아직도 나를 그렇게 몰라")
    speak("너를 가질 사람 나밖에 없는데")
