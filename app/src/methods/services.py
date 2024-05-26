from vosk import Model, KaldiRecognizer
import wave
import sys
import sounddevice as sd
import numpy as np

class AudioInterpreter:
    def interpret_audio(model_path, audio_path):
        try:
            model = Model(model_path)
        except Exception as e:
            print("No se pudo cargar el modelo desde:", model_path)
            print(e)
            sys.exit(1)

        try:
            wf = wave.open(audio_path, "rb")
        except FileNotFoundError:
            print("Archivo de audio no encontrado.")
            sys.exit(1)

        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        results = []

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print(rec.Result())
                results.append(rec.Result())

        results.append(rec.FinalResult())
        return results
    