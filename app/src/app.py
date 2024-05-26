import os
from methods.services import AudioInterpreter
from methods.conversor import AudioConversor


ABSOLUTE_MODELS_PATH="/mnt/c/Python/assets"
CURRENT_EXECT_PATH = os.getcwd()
TEST_FILES_PATH = os.path.join(CURRENT_EXECT_PATH,"app","src", "resources", "test")
OUTPUT_FILES_PATH = os.path.join(CURRENT_EXECT_PATH,"app","src", "resources", "output")

AudioConversor.proccess_audio(os.path.join(TEST_FILES_PATH, "inazuma_eng.mp3") ,os.path.join(OUTPUT_FILES_PATH, "output.wav"))


text_in_audio = AudioInterpreter.interpret_audio(os.path.join(ABSOLUTE_MODELS_PATH, "eng"), os.path.join(OUTPUT_FILES_PATH, "output.wav"))

print(text_in_audio)



