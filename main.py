import os
import wave
import json
from vosk import Model, KaldiRecognizer

# Загрузка модели
model = Model('model/vosk-model-small-ru-0.22')

# Открываем аудиофайл
wf = wave.open("test.wav", "rb")

# Проверяем параметры аудиофайла
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be: WAV 16 PCM.")
    exit(1)

# Создаем распознаватель
rec = KaldiRecognizer(model, wf.getframerate())

# Читаем аудиофайл и распознаем речь
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(result)

# Финальный результат
final_result = rec.FinalResult()

# Обрабатываем результат в JSON
final_result_json = json.loads(final_result)
print("Распознанный текст: ", final_result_json['text'])

with open("recognized_text_utf8.txt", "w", encoding="utf-8") as text_file:
    text_file.write(final_result_json['text'])