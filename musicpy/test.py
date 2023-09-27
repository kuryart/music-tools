# === WORKING DIR ===
# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

# === CHANGE DRIVERS ===
import os
os.environ['SDL_AUDIODRIVER'] = 'alsa'

# === IMPORTS ===
from musicpy import *
from IPython.display import Audio
import subprocess
import pygame

subprocess.run(["aplay", "-l"])

pygame.init()
pygame.mixer.init(devicename="alsa")


# a nylon string guitar plays broken chords on a chord progression
guitar = (C('CM7', 3, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2 |
          C('A7sus', 2, 1/4, 1/8)^2 |
          C('Em7', 2, 1/4, 1/8)^2 | 
          C('FM7', 2, 1/4, 1/8)^2 |
          C('CM7', 3, 1/4, 1/8)@1 |
          C('AbM7', 2, 1/4, 1/8)^2 |
          C('G7sus', 2, 1/4, 1/8)^2) * 2

write(guitar, bpm=120)
print("=== RUN FLUIDSYNTH ===")
subprocess.run(["fluidsynth", "-F", "temp.wav", "temp.mid"])

Audio('temp.wav', autoplay=True, rate=1)

play(guitar, bpm=100, instrument=25)