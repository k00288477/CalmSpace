# CalmSpace
 
CalmSpace is an IoT application designed to monitor interior environments in real time, helping reduce the risk of sensory overload in neurodivergent individuals, including those with Autism Spectrum Disorder (ASD) and ADHD.
 
Built as part of the module **Technology Futures and Connected Living** at TUS.
 
**Student:** Gary O'Connor — K00288477
 
---
 
## Overview
 
CalmSpace uses a Raspberry Pi 5 with a SenseHat and USB microphone to continuously monitor three environmental metrics:
 
- 🌡️ **Temperature** (°C)
- 💧 **Humidity** (%RH)
- 🔊 **Noise** (dB)
 
Readings are taken every second and pushed to a Google Firebase Realtime Database. A Vue.js web dashboard displays the data in real time, colour-coded against evidence-based thresholds.
 
---
 
## Repositories
 
| Repo | Description |
|---|---|
| [CalmSpace](https://github.com/k00288477/CalmSpace) | Raspberry Pi — Python data collection |
| [CalmSpace-UI](https://github.com/k00288477/CalmSpace-UI) | Vue.js web dashboard |
 
---

 
## Metric Thresholds
 
Thresholds are defined by reputable academic and institutional sources:
 
| Metric | Safe Range | Source |
|---|---|---|
| Temperature | 17°C – 26°C | Teachers' Union of Ireland — Heating in Schools |
| Humidity | 40% – 60% %RH | Jones et al. (2022), *Indoor Air* |
| Noise | Below 50 dB | World Health Organization (2000) — Guidelines for Community Noise |
 
---
 
## Hardware
 
- Raspberry Pi 5
- Raspberry Pi SenseHat (temperature, humidity sensors + LED matrix)
- Mini USB Microphone (noise monitoring)
 
---
 
## Tech Stack
 
### Pi (Data Collection)
- Python
- SenseHat library
- Firebase Admin SDK
- MariaDB (local backup)
 
### Dashboard (CalmSpace-UI)
- Vue.js 3 (Composition API)
- Vite
- Tailwind CSS
- Firebase Realtime Database (`firebase/database`)
- Chart.js + vue-chartjs (donut and line charts)
- Vue Router
 
---
 
## Dashboard Features
 
- **Live metric display** — temperature, humidity and noise updated in real time via Firebase WebSocket
- **Colour-coded thresholds** — green / yellow / red on both the SenseHat LED matrix and the web dashboard
- **Monitor status** — shows Online / Offline based on timestamp of last received reading
- **History table** — last hour of readings, filtered to today, colour-coded per cell
- **Chart library** — donut charts showing percentage of readings within/outside threshold, line charts showing trends over the past hour
 
---
 
## Getting Started
 
### Pi Setup
 
```bash
git clone https://github.com/k00288477/CalmSpace.git
cd CalmSpace
pip install -r requirements.txt
sudo python main.py
```
 
> Make sure your Firebase service account key is in place and the Pi clock is synced (`sudo timedatectl set-ntp true`) to avoid JWT errors.
 
### Dashboard Setup
 
```bash
git clone https://github.com/k00288477/CalmSpace-UI.git
cd CalmSpace-UI
npm install
npm run dev
```
