### Project Overview
This repository explores **AI-driven music generation** using Generative Adversarial Neural Networks (GANNs), Transformers, and Variational Autoencoders (VAEs). Developed for the Generative Neural Networks exam at OTH Regensburg (Summer Semester 2025), the project includes code, generated audio samples, visualizations, and presentation materials. Key components:

```
.
├── music_generation.ipynb          # Main Jupyter notebook with training/generation code
├── presentation_handwritten_slides.pdf  # Handwritten presentation slides
├── presentation_music.m3u8         # Audio playlist for presentations
├── requirements.txt                # Python dependencies
└── results                         # Generated outputs
    ├── midi/                       # MIDI sequences from models
    ├── png/                        # Visualizations (distributions, note plots)
    └── wav/                        # Audio renders of generated music
```

### Key Parts
- **Models Implemented**: GANNs, Transformers, VAEs, and RNNs
- **Output Formats**: MIDI, WAV, and visualizations (PNG)
- **Sample Types**: 
  - Random generation (`*_random.midi`)
  - Interpolations (`*_interpolation.midi`)
  - Temperature-varied RNN outputs (`rnn_temp*.mid`)
  - GANN variants (`gann_k*.mid`)

---

### Setup Instructions
**Python 3.9–3.11 required**  

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter**:
   ```bash
   jupyter notebook music_generation.ipynb
   ```

> **Note**: Generated outputs are pre-saved in `results/`. Re-running the notebook will overwrite these.

---

### Sample Outputs
- **Audio**: Listen to `results/wav/` (e.g., `gann_k5.wav`, `vae_random.wav`)
- **Visuals**: See `results/png/` for model performance comparisons
- **MIDI**: Customize sequences in `results/midi/` using DAWs like MuseScore or FL Studio

---
Developed with passion for OTH Regensburg – Summer 2025.