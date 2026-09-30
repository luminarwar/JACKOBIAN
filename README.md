# 🤖 JACKOBIAN — Robotics & Embodied AI from the Ground Up

A structured, long-term self-study course: from basic Python + ML to robotics, control, perception, ROS 2, and robot learning (RL, imitation learning, Vision-Language-Action models). Taught session by session, with a teacher (Claude) writing the lessons and reviewing the work.

*(The name is a nod to the **Jacobian** — one of the most important matrices in robotics.)*

## 🗺️ The plan

| Phase | Topic | Weeks |
|---|---|---|
| 0 | Setup + Python muscles | 2 |
| 1 | Math for robotics (linear algebra, rotations, calculus, probability) | 6 |
| 2 | Kinematics — frames, transforms, FK/IK, Jacobians, mobile robots | 6 |
| 3 | Physics & control — dynamics, PID, MuJoCo simulation | 5 |
| 4 | Electronics & first real robot (ESP32/Arduino) | 5 |
| 5 | Perception & state estimation — OpenCV, Kalman filters, SLAM | 6 |
| 6 | Linux + ROS 2 | 5 |
| 7 | Robot learning & embodied AI — RL, imitation learning, VLAs | 10 |
| 8 | Specialization (humanoids 🦿 / drones 🚁) + startup thinking | ongoing |

Full details: [`docs/00-roadmap.md`](docs/00-roadmap.md)

## 📁 Structure

```
docs/
  00-roadmap.md        master plan
  hardware-plan.md     what to buy, when
  resources.md         books, courses, videos, papers
  sessions/phase-X/    one lesson file per day (day-01.md, day-02.md, ...)
code/phase-X/day-NN/   exercises (starter code with TODOs)
solutions/             answer keys
notes/                 my own notes, in my own words
projects/              end-of-phase builds
papers/                paper-reading notes
```

## 🛠️ Setup

```bash
# Python 3.12 environment (managed with uv — https://docs.astral.sh/uv/)
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt     # or: pip install -r requirements.txt

python code/phase-0/day-01/check_setup.py
```

## 📈 Progress

- [ ] Day 01 — The big picture + lab setup
- [ ] Phase 0 complete
