import sounddevice as sd
import numpy as np
import time

DURATION = 1
RATE = 44100

def get_db():
    audio = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=1, dtype='float32')
    sd.wait()
    rms = np.sqrt(np.mean(audio**2))
    if rms > 0:
        db = 20 * np.log10(rms)
        db_normalised = db + 85 # Manual Calibration
        return round(db_normalised, 1)
    return 0

