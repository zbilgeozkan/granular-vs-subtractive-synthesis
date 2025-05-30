import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import sounddevice as sd
from scipy.io.wavfile import write

def subtractive_synthesis(filename, cutoff=1000, order=5):
    # Dosyayı oku
    fs, data = wavfile.read(filename)
    data = data.astype(np.float32)
    if data.ndim > 1:
        data = data[:, 0]  # Stereo ise mono'ya çevir
    data /= np.max(np.abs(data))  # Normalize et

    # Düşük geçiren filtre
    def lowpass_filter(signal, cutoff_freq, fs, order):
        nyquist = 0.5 * fs
        norm_cutoff = cutoff_freq / nyquist
        b, a = butter(order, norm_cutoff, btype='low', analog=False)
        return lfilter(b, a, signal)

    filtered = lowpass_filter(data, cutoff, fs, order)
    filtered /= np.max(np.abs(filtered))  # Tekrar normalize

    # Çal ve kaydet
    sd.play(filtered, fs)
    sd.wait()
    output_file = "subtractive_output.wav"
    write(output_file, fs, (filtered * 32767).astype(np.int16))
    print(f"Subtraktif sentez dosyası kaydedildi: {output_file}")

# subtractive_synthesis("sample.wav", cutoff=800)
# subtractive_synthesis("retrogame.wav", cutoff=800)
# subtractive_synthesis("crowd-laugh.wav", cutoff=800)