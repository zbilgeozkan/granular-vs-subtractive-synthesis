import numpy as np
from scipy.io import wavfile
import sounddevice as sd
from scipy.io.wavfile import write
import random

def granular_synthesis(filename, grain_duration=0.05, num_grains=300, output_duration=3):
    # Dosyayı oku
    fs, data = wavfile.read(filename)
    data = data.astype(np.float32)
    if data.ndim > 1:
        data = data[:, 0]
    data /= np.max(np.abs(data))  # Normalize et

    grain_size = int(grain_duration * fs)
    output = np.zeros(fs * output_duration)
    window = np.hanning(grain_size)

    for i in range(num_grains):
        start = random.randint(0, len(data) - grain_size)
        grain = data[start:start + grain_size] * window
        pos = int(i * grain_size * 0.5)  # %50 örtüşme ile sırayla yerleştir
        if pos + grain_size < len(output):
            output[pos:pos + grain_size] += grain


    output /= np.max(np.abs(output))  # Normalize

    # Çal ve kaydet
    sd.play(output, fs)
    sd.wait()
    output_file = "granular_output.wav"
    write(output_file, fs, (output * 32767).astype(np.int16))
    print(f"Granüler sentez dosyası kaydedildi: {output_file}")

# granular_synthesis("sample.wav", grain_duration=0.03, num_grains=400)
# granular_synthesis("retrogame.wav", grain_duration=0.03, num_grains=400)
# granular_synthesis("crowd-laugh.wav", grain_duration=0.03, num_grains=400)