import pyaudio
import wave
import time
import FileNameGenerator as FNG
import whisper


filename = FNG.filename



FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = filename

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

print("recording...")
start_time = time.time()

frames = []

while time.time() < start_time + RECORD_SECONDS:
    data = stream.read(CHUNK)
    frames.append(data)

print("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# Get TexT

model = whisper.load_model('base')
result = model.transcribe(f'{filename}')
words = result['text']

print(words)