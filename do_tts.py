from gtts import gTTS
import os
import multiprocessing
import pygame

pygame.mixer.init()


def is_busy():
    if pygame.mixer.music.get_busy():
        return True
    else:
        if os.path.exists('tempfile.mp3'):
            pygame.mixer.music.unload()
            os.remove('tempfile.mp3')
        return False


def stop():
    pygame.mixer.music.stop()
    if os.path.exists('tempfile.mp3'):
        pygame.mixer.music.unload()
        os.remove('tempfile.mp3')


def speak(txt, lang='ko'):
    tts = gTTS(text=txt, lang=lang)
    tts.save('tempfile.mp3')
    pygame.mixer.music.load('tempfile.mp3')
    pygame.mixer.music.play()


def set_volume(value):
    pygame.mixer.music.set_volume(value)


def get_volume():
    return pygame.mixer.music.get_volume()


if __name__ == "__main__":
    speak("이 바보야 진짜 아니야")
    speak("아직도 나를 그렇게 몰라")
    speak("너를 가질 사람 나밖에 없는데")
