from piper.voice import PiperVoice
import wave

model_path = r"C:\Users\Nithish\Content_Automisation\models\English_Britain_Southern_English_Female\en_GB-southern_english_female-low.onnx"

audio_path = r"C:\Users\Nithish\Content_Automisation\audio\output.wav"

# Load voice
voice = PiperVoice.load(model_path)

def text_to_speech(text):
    # Collect audio bytes
    audio_bytes = b""

    for chunk in voice.synthesize(text):
        audio_bytes += chunk.audio_int16_bytes

    # Save WAV
    with wave.open(audio_path, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)  # 16-bit audio
        wav_file.setframerate(voice.config.sample_rate)
        wav_file.writeframes(audio_bytes)
