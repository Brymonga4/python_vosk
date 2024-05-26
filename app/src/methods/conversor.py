from pydub import AudioSegment
import subprocess


class AudioConversor:
    def convert_to_wav(extension, path_file, output_path):
   
        audio = AudioSegment.from_file(path_file, extension)

        audio.export(output_path, format="wav")

    def get_sample_rate(audio_path):
        audio = AudioSegment.from_file(audio_path)
        rate = audio.frame_rate
        print(f"Sample rate: {rate} Hz")
        return rate

    def convert_sample_rate(input_file, output_file, new_rate=16000):
        command = ['ffmpeg', '-i', input_file, '-ar', str(new_rate), output_file]
        subprocess.run(command, check=True)

    def reduce_nose(input_file, output_file):
        command = ['ffmpeg', '-i', input_file, '-af', 'afftdn', output_file]     
        subprocess.run(command, check=True)
   
    def proccess_audio(input_file, output_file, new_rate=16000):
        command = ['ffmpeg', '-i', input_file, 
        '-af', 'afftdn', 
        '-ar', str(new_rate),  
        output_file
        ]
        try:
            subprocess.run(command, check=True)
            print("Procesamiento de audio completado con éxito.")
        except subprocess.CalledProcessError as e:
            print(f"Error al procesar el audio: {e}")
