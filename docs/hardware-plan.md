# 🛒 Hardware Plan — What to Buy, When, and Why

> **Principle:** Don't buy anything until the roadmap needs it. Simulation teaches ~70% of robotics for free.
> **Prices** are rough 2026 Indian estimates. Always compare before buying. Good Indian stores: **Robu.in**, **Robokits India**, **Thingbits** (official Raspberry Pi reseller), **Amazon.in**. Local electronics markets (e.g., Lamington Road in Mumbai, SP Road in Bengaluru, Nehru Place in Delhi) are often cheaper.

---

## Stage 0 — Months 0–4: Buy nothing ✅ (₹0)

Your Mac + free software (Python, MuJoCo, Jupyter) is enough.

---

## Stage 1 — Order in Week 16 (~month 4), used from Phase 4 (₹3,000–5,000)

This is your **first robot kit**. Order in Week 16 so it arrives before Phase 4 starts.

| Item | Why you need it | Approx. ₹ |
|---|---|---|
| ESP32 dev board (e.g., ESP32-WROOM DevKit) ×1 | The robot's "brain". Has Wi-Fi + Bluetooth, so it can talk to your Mac | 400–600 |
| Arduino Uno (clone is fine) ×1 | Simplest board to learn on; tons of tutorials | 400–700 |
| 2WD robot chassis kit (with 2 geared DC motors + wheels + caster) | The robot's body | 400–700 |
| Motor driver: TB6612FNG (preferred) or L298N | Microcontrollers can't power motors directly | 150–400 |
| HC-SR04 ultrasonic sensor ×2 | Measures distance → obstacle avoidance | 150–300 |
| IR line sensor module (3–5 channel) | Line following | 150–400 |
| MPU6050 IMU | Measures tilt/rotation — the same idea drones use | 150–250 |
| SG90 micro servos ×2 | Precise angle control; mini robot arms | 200–300 |
| Motor encoders (or chassis with encoder motors) | Measure wheel rotation → odometry | 200–500 |
| Breadboard + jumper wires (M-M, M-F, F-F) + resistors/LED kit | Prototyping without soldering | 250–400 |
| 2× 18650 Li-ion cells + holder + charger (or 6× AA holder) | Power. ⚠️ Li-ion needs care — we'll cover safety | 400–700 |
| Digital multimeter | Measuring voltage/current — every engineer's must-have | 400–700 |
| Basic soldering iron kit (+ solder, stand) | Permanent connections | 400–800 |

**Tip:** Many stores sell an "ESP32 / Arduino robot car kit" bundling most of this — often cheaper. Before buying one, show the component list to Claude to check it.

---

## Stage 2 — ~Month 7 (Phase 6): Onboard computer (₹8,000–11,000)

| Item | Why | Approx. ₹ |
|---|---|---|
| Raspberry Pi 5 (4 GB is enough; 8 GB if affordable) | Runs Linux + ROS 2 *on the robot* | 6,000–9,500 |
| Official 27W USB-C power supply | Pi 5 is picky about power | 1,000–1,300 |
| microSD card 64 GB (Class A2) | Storage/OS | 500–800 |
| Raspberry Pi Camera Module 3 (or any USB webcam) | Robot vision | 2,000–3,000 |
| Heatsink/active cooler | Pi 5 gets hot | 400–600 |

---

## Stage 3 — Phase 7+ (optional, depending on budget & direction)

| Item | Why | Approx. ₹ |
|---|---|---|
| **NVIDIA Jetson Orin Nano Super Dev Kit** | Runs neural networks (vision, small VLAs) on the robot with a GPU | 25,000–35,000 |
| **SO-101 robot arm** (open-source, used with Hugging Face LeRobot) | Real imitation-learning experiments; a leader+follower pair lets you teleoperate | 15,000–30,000 (parts + 3D printing) |
| 🚁 Drone track: small programmable drone (e.g., an ESP32-based mini drone, or an F450 frame + PX4 flight controller build) | Real flight control experiments | 8,000–30,000 |
| 🦿 Humanoid track: mostly simulation (MuJoCo). Real humanoids are very expensive; small servo-based bipeds are possible later | Legged control | varies |

---

## Free alternatives while you wait

- **Wokwi** (wokwi.com) — simulates Arduino/ESP32 + sensors in the browser. You can practice microcontroller code before Kit #1 arrives.
- **MuJoCo** — physics simulation for arms, humanoids and drones.
- **Your laptop webcam** — enough for all of Phase 5 (perception).
- **Google Colab / Kaggle** — free GPUs for training in Phase 7.
