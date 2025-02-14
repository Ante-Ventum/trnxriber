import os
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import numpy as np

# Установите путь к модели
model_path = 'model/vosk-model-small-ru-0.22'
if not os.path.exists(model_path):
    print(f"Модель не найдена в {model_path}. Скачайте её с официального сайта Vosk.")
    exit(1)

# Загрузите модель
model = Model(model_path)

def callback(indata, frames, time, status):
    if status:
        print(status)
    data = np.frombuffer(indata, dtype=np.int16)
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
    else:
        print(recognizer.PartialResult())

# Частота дискретизации
sample_rate = 16000
recognizer = KaldiRecognizer(model, sample_rate)

# Запись аудио с использованием sounddevice
with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, dtype='int16', channels=1, callback=callback):
    print("Начните говорить...")
    while True:
        pass
