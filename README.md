# Granular vs Subtractive Synthesis: Emotional Atmosphere Comparison

This project is part of a digital audio synthesis course assignment. The objective is to explore and compare **granular** and **subtractive synthesis** methods to reproduce a similar emotional sound texture inspired by artists like Röyksopp.

---

## 🎯 Objective

To compare the effectiveness of granular and subtractive synthesis methods in creating a dreamy, ambient atmosphere. A common melodic phrase is used as input and processed using both methods. The outputs are then evaluated using visual (waveform & spectrogram) and subjective (listening test) methods.

---

## 🧪 Methods

### Synthesis Techniques
- **Granular Synthesis**
  - Implemented using a custom Python script
  - Parameters: grain size, overlap, randomization
- **Subtractive Synthesis**
  - Implemented using a Python-based filter processing
  - Parameters: filter type (low-pass), cutoff frequency, envelope shaping

### Tools & Software
- Python (NumPy, SciPy, matplotlib, sounddevice)
- Audacity (for preview and manual analysis)
- Jupyter Notebook (for waveform & spectrogram visualization)

---

## 📁 File Structure

```
granular-vs-subtractive-synthesis/
├── granular_synthesis.py # Python script for granular synthesis
├── subtractive_synthesis.py # Python script for subtractive synthesis
├── sample.wav # Base input WAV file
├── granular_output.wav # Output from granular synthesis
├── subtractive_output.wav # Output from subtractive synthesis
├── crowd-laugh.wav # Additional test sample
├── retrogame.wav # Additional test sample
├── analysis.ipynb # Jupyter notebook with analysis and plots
├── README.md # Project overview (this file)
```

---

## 📊 Analysis & Results

- Waveform and spectrograms generated via `analysis.ipynb` show distinct characteristics of each method.
- Granular synthesis provided more texture and randomness, which was ideal for ambient and dreamy feel.
- Subtractive synthesis gave a cleaner and smoother tone but with less variability.

---

## ▶️ How to Run

1. Make sure you have the required Python libraries installed:
   ```bash
   pip install numpy scipy sounddevice matplotlib

2. To generate outputs:
  ```
  python granular_synthesis.py
  python subtractive_synthesis.py
  ```

3. To view waveform and spectrogram analysis:
  Open `analysis.ipynb` in Jupyter Notebook.
