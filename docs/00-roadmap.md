# 🗺️ The JACKOBIAN Roadmap — Robotics & Embodied AI from Zero

> **Goal:** Go from "absolute beginner" to "strong enough to build a robotics startup".
> **Pace:** 5–6 days/week, 2–4 hours/day (~15 hrs/week).
> **Total:** ~45 weeks of core learning (+ buffer) ≈ **12–15 months**, then specialization.
> **Rule #1:** It is totally fine to go slower. Understanding > speed. We are in for the long run.

---

## How this roadmap works

```
 PHASE 0        PHASE 1         PHASE 2          PHASE 3           PHASE 4
 Setup +   ──▶  Math for   ──▶  Robot      ──▶  Physics &   ──▶  Electronics &
 Python         Robotics        Basics          Control          1st Hardware
 (2 wks)        (6 wks)         (6 wks)         (5 wks)          (5 wks)
                                                                     │
    ┌────────────────────────────────────────────────────────────────┘
    ▼
 PHASE 5         PHASE 6          PHASE 7              PHASE 8
 Perception ──▶  Linux +    ──▶  Robot Learning  ──▶  Specialize
 & Estimation    ROS 2           & Embodied AI        (Humanoids / Drones)
 (6 wks)         (5 wks)         (10 wks)             + Startup thinking
```

**Weekly rhythm** (6 days):

| Day | What happens |
|---|---|
| Days 1–4 | New learning — theory + math + code, together |
| Day 5 | 🔨 **Build day** — a mini project using the week's ideas |
| Day 6 | 🔁 **Review day** — weekly quiz, fix weak spots, catch up (skip if you only do 5 days) |

**Every session** has a markdown file in `docs/sessions/phase-X/day-NN.md` (day numbers keep counting up across phases: day-01 … day-270).

**Every phase** ends with:
1. A **project** (goes in `projects/`)
2. A **checkpoint** — "you're ready to move on when you can…"

**Your two interests** — 🦿 *humanoids* and 🚁 *drones* — show up as "interest hooks" inside phases, so you keep seeing how every topic connects to them. In Phase 8 you pick a direction to go deep.

---

## PHASE 0 — Setup + Python Muscles (Weeks 1–2, Days 1–12)

**Why:** Robotics code is mostly Python (for AI, simulation and prototyping) plus some C++. Your Python is basic, so we strengthen it *with robotics-flavored exercises*, and you learn the tools every engineer uses (terminal, git, Jupyter).

| Day | Topic |
|---|---|
| 1 | The big picture: what is a robot, what is embodied AI, the robotics stack. Lab setup (terminal, venv, Jupyter, git) |
| 2 | Python refresher I — variables, conditions, loops, functions, lists/dicts (robot-themed) |
| 3 | Python II — classes & objects: build a `Robot` class |
| 4 | Terminal + Git + GitHub properly; modules, files, reading/writing data |
| 5 | 🔨 Build: text-based robot on a grid that senses walls and navigates |
| 6 | 🔁 Review + quiz |
| 7 | NumPy I — arrays, shapes, indexing, vectorized math (why robots love arrays) |
| 8 | NumPy II — matrix operations, broadcasting, random numbers (= sensor noise!) |
| 9 | Matplotlib — plots, subplots, animations |
| 10 | Simulation basics — time steps, position/velocity/acceleration, Euler integration |
| 11 | 🔨 Build: animated bouncing-ball physics simulation |
| 12 | 🔁 Phase 0 review + quiz |

**Tools:** Python 3.12, NumPy, Matplotlib, JupyterLab, VS Code, Git/GitHub.
**Project:** `projects/00-bouncing-ball/` — a ball bouncing under gravity with energy loss, animated.
**✅ Checkpoint:** You can write a class, use NumPy arrays without fear, make a plot/animation, and commit + push with git.

---

## PHASE 1 — Math for Robotics (Weeks 3–8, Days 13–48)

**Why:** Robots live in 3D space. To say "where is the hand?" or "which way is the drone tilted?" you need vectors, matrices and rotations. To say "how fast is it moving?" you need calculus. To deal with noisy sensors you need probability. We learn every idea **visually first**, then with code.

| Week | Topics | Interest hook |
|---|---|---|
| 3 | Vectors as arrows: add, scale, length, dot product, cross product. Vectors in NumPy | — |
| 4 | Matrices as *transformations* (not just tables of numbers). Matrix multiplication, determinant, inverse, solving `Ax = b` | — |
| 5 | Trigonometry refresher, 2D rotations, rotation matrices, intro to homogeneous coordinates | — |
| 6 | 3D rotations: rotation matrices, Euler angles (roll/pitch/yaw), gimbal lock, axis-angle, quaternions (intuition) | 🚁 how a drone describes its tilt |
| 7 | Calculus refresher: derivatives as rates (velocity, acceleration), integrals, partial derivatives, gradients, numerical differentiation/integration, idea of differential equations | — |
| 8 | Probability: random variables, mean/variance, Gaussians, Bayes' rule, noise. Light eigenvalues/eigenvectors | 🔨 project week |

**Main resources:** 3Blue1Brown *Essence of Linear Algebra* & *Essence of Calculus*, Khan Academy (trig refresh), *Modern Robotics* Appendix + Ch. 3 (later).
**Project:** `projects/01-rotation-visualizer/` — an interactive 3D visualizer where you rotate a "drone body frame" using Euler angles and see gimbal lock happen. Bonus: simulate a noisy distance sensor and plot its Gaussian.
**✅ Checkpoint:** You can rotate a point in 2D and 3D by hand and in code, explain what a matrix "does" to space, compute a derivative numerically, and explain Bayes' rule with an example.

---

## PHASE 2 — Robot Basics: Kinematics (Weeks 9–14, Days 49–84)

**Why:** Kinematics = the geometry of motion (no forces yet). "If my joints are at these angles, where is my hand?" (forward kinematics) and "what joint angles put my hand *there*?" (inverse kinematics). This is the core of every arm, leg and humanoid.

| Week | Topics | Interest hook |
|---|---|---|
| 9 | Configuration space, degrees of freedom (DOF), joints & links, Grübler's formula | 🦿 how many DOF does a humanoid have? |
| 10 | Rigid-body motion: coordinate frames, homogeneous transforms (SE(2), SE(3)), chaining frames | 🚁 world frame vs drone body frame |
| 11 | Forward kinematics: planar 2-link & 3-link arms; DH parameters (intro); Product of Exponentials (light) | — |
| 12 | Velocity kinematics & **the Jacobian** (yes — the folder's namesake!), singularities | 🦿 leg Jacobians |
| 13 | Inverse kinematics: analytical (2-link), numerical (Jacobian pseudo-inverse, Newton's method). Connection to gradient descent from ML! | — |
| 14 | Mobile robots: differential drive, unicycle model, odometry; waypoint following | 🔨 project week |

**Main resources:** *Modern Robotics* (Lynch & Park) Ch. 2–6 + their video lectures; Peter Corke's *Robotics Toolbox for Python*.
**Project:** `projects/02-arm-and-rover/` — (a) a 2-link arm that reaches any clicked point (animated IK), (b) a differential-drive rover that follows waypoints.
**✅ Checkpoint:** You can derive FK for a 2-link arm on paper, build and use a Jacobian, and solve IK numerically.

---

## PHASE 3 — Physics & Control (Weeks 15–19, Days 85–114)

**Why:** Kinematics ignores forces. Real robots have mass, gravity, friction and motors that push. **Control** is the art of making a system do what you want despite all that. PID controllers run inside almost every robot on Earth.

| Week | Topics | Interest hook |
|---|---|---|
| 15 | Newton's laws, force, torque, energy, momentum. Simulate falling objects and a pendulum with an ODE solver (SciPy) | — |
| 16 | Dynamics: pendulum, 2-link arm (Lagrangian intuition — light), friction, damping | 🛒 **order Phase 4 hardware this week** |
| 17 | Control intro: open vs closed loop, feedback, **PID**, tuning, step response, stability intuition | — |
| 18 | **MuJoCo** physics simulator: models (MJCF/XML), running sims, controlling a pendulum/arm | 🚁 planar quadrotor: dynamics + hover controller |
| 19 | Inverted pendulum / cart-pole, intro to LQR, state-space thinking | 🔨 project week |

**Main resources:** Brian Douglas *Understanding PID Control* & control videos (MATLAB channel), Steve Brunton *Control Bootcamp*, MuJoCo docs, Russ Tedrake *Underactuated Robotics* (first chapters only).
**Project:** `projects/03-balance-and-hover/` — balance a cart-pole in MuJoCo with PID/LQR, and make a 2D drone hover and move to targets.
**✅ Checkpoint:** You can simulate a physical system, write a PID controller from scratch, tune it, and explain why it works.

---

## PHASE 4 — Electronics & Your First Real Robot (Weeks 20–24, Days 115–144)

**Why:** Time to touch real hardware! Simulation lies a little; real motors are noisy and batteries die. Also your first taste of **C++** (Arduino code is C++).

| Week | Topics |
|---|---|
| 20 | Electricity basics: voltage, current, resistance, Ohm's law, power, batteries, **safety**. Breadboards, multimeter |
| 21 | Microcontrollers: Arduino/ESP32 programming (C++ basics), digital/analog I/O, PWM, serial communication |
| 22 | Sensors: ultrasonic, IR, IMU (MPU6050), wheel encoders. Real sensor noise (hello again, probability!) |
| 23 | Actuators: DC motors, H-bridge motor drivers, servos, steppers (intro). Soldering basics |
| 24 | 🔨 Build week: 2-wheel robot with obstacle avoidance + PID line following. Python ↔ ESP32 over Wi-Fi/serial |

**Main resources:** Paul McWhorter's Arduino tutorials (YouTube), Random Nerd Tutorials (ESP32), component datasheets.
**Hardware:** see `docs/hardware-plan.md` — Kit #1 (~₹3,000–5,000).
**Project:** `projects/04-first-rover/` — a real robot that drives, avoids obstacles and follows a line.
**✅ Checkpoint:** You can wire a sensor and a motor safely, write microcontroller code, and close a real control loop.

---

## PHASE 5 — Perception & State Estimation (Weeks 25–30, Days 145–180)

**Why:** A robot must *see* and must *know where it is*. Sensors are noisy, so we combine them cleverly (filters). Your deep-learning background becomes useful here.

| Week | Topics | Interest hook |
|---|---|---|
| 25 | Images as arrays, OpenCV basics: color spaces, filtering, thresholding, contours | — |
| 26 | Camera model: pinhole, intrinsics/extrinsics, calibration, ArUco markers & pose estimation | — |
| 27 | Deep learning for vision (refresh CNNs), object detection (YOLO), segmentation, depth estimation | — |
| 28 | State estimation: Bayes filter, **Kalman filter** (1D → multi-D) | — |
| 29 | Extended Kalman Filter, sensor fusion (IMU + encoders), complementary filter | 🚁 drone attitude estimation |
| 30 | Localization with particle filters, occupancy grids, SLAM concepts | 🔨 project week |

**Main resources:** OpenCV docs, *Probabilistic Robotics* (Thrun, Burgard, Fox), Cyrill Stachniss's lectures, Roger Labbe's *Kalman and Bayesian Filters in Python* (free Jupyter book).
**Project:** `projects/05-see-and-track/` — webcam tracks an ArUco marker in 3D + Kalman-filter smoothing; rover localizes itself.
**✅ Checkpoint:** You can calibrate a camera, detect & localize objects, and implement a Kalman filter from scratch.

---

## PHASE 6 — Linux + ROS 2 (Weeks 31–35, Days 181–210)

**Why:** ROS 2 (Robot Operating System) is the standard "plumbing" of robotics — how different programs (camera, planner, motors) talk to each other. Almost every robotics company uses it or something like it. Around here (~month 7) you get a **Raspberry Pi**.

| Week | Topics |
|---|---|
| 31 | Linux deep dive, shell scripting, SSH, Docker (ROS 2 on a Mac runs in Docker), Raspberry Pi setup |
| 32 | ROS 2 core: nodes, topics, messages, publishers/subscribers, launch files |
| 33 | Services, actions, parameters, **TF2** (transforms — Phase 2 pays off!), URDF robot descriptions |
| 34 | Gazebo simulation, RViz visualization, Nav2 overview, micro-ROS for ESP32 |
| 35 | 🔨 Build week: your Phase-4 robot runs on ROS 2 with Pi + camera — teleop + autonomous behavior |

**Main resources:** Official ROS 2 docs & tutorials, Articulated Robotics (YouTube), MIT *Missing Semester* (shell).
**Project:** `projects/06-ros2-rover/`
**✅ Checkpoint:** You can build a multi-node ROS 2 system, describe a robot in URDF, and visualize it in RViz.

---

## PHASE 7 — Robot Learning & Embodied AI (Weeks 36–45, Days 211–270)

**Why:** This is the frontier — robots that *learn* skills instead of being hand-programmed. Reinforcement learning, imitation learning, and foundation models (Vision-Language-Action models) are what today's humanoid and robot-AI startups are built on. Your ML/DL background shines here.

| Week | Topics | Interest hook |
|---|---|---|
| 36 | RL foundations: MDPs, rewards, returns, value functions, policies. Gymnasium | — |
| 37 | Deep RL: DQN, policy gradients, **PPO**. Stable-Baselines3 | — |
| 38 | RL for robots in MuJoCo: reward design, locomotion | 🦿 train a legged robot / humanoid to walk |
| 39 | Sim-to-real: domain randomization, system identification, the reality gap | 🚁 RL drone hover |
| 40 | Imitation learning: behavior cloning, DAgger, teleoperation data | — |
| 41 | Modern policies: ACT, Diffusion Policy; the **LeRobot** library | — |
| 42 | Transformers → VLMs → **VLAs** (RT-1, RT-2, OpenVLA, π0), world models, robot foundation models | 🦿 how humanoid companies use VLAs |
| 43–44 | 🔨 Project: imitation-learning policy with LeRobot (sim, or real SO-101 arm if budget allows) | — |
| 45 | Paper-reading sprint + review | — |

**Compute note:** Your Mac is fine for MuJoCo and small models. For heavy training we use free GPUs (Google Colab / Kaggle). NVIDIA Isaac Sim/Lab needs an NVIDIA GPU, so we mostly use MuJoCo.
**Main resources:** Sutton & Barto *Reinforcement Learning* (free book), OpenAI *Spinning Up*, Hugging Face LeRobot docs + Deep RL course, key papers (listed in `docs/resources.md`).
**✅ Checkpoint:** You can train an RL policy in simulation, train an imitation policy from demonstrations, and explain how a VLA works end-to-end.

---

## PHASE 8 — Specialization + Startup Thinking (Week 46 onward)

Pick a primary track (you can change later):

- 🦿 **Humanoids / legged robots:** whole-body control, Model Predictive Control (MPC), legged locomotion RL, *Underactuated Robotics* in depth, MuJoCo Menagerie humanoid models.
- 🚁 **Drones:** flight controller internals, PX4 / ArduPilot, trajectory generation, visual-inertial odometry, *Aerial Robotics* (UPenn, Coursera).
- 🦾 **Manipulation:** grasping, *Robotic Manipulation* (Russ Tedrake, MIT), bimanual robots, VLA fine-tuning.

**Startup thinking** (runs in parallel):
- Map the robotics industry (global + India): who builds what, who buys what.
- Talk to potential users — find a *real, painful problem*.
- Read 1–2 papers/week, contribute to open source (LeRobot, ROS 2 packages), build in public.
- Build a larger portfolio project that could become a prototype.

---

## Hardware timeline (short version — full details in `hardware-plan.md`)

| When | What | Approx. cost |
|---|---|---|
| Months 0–4 | Nothing! Simulation only | ₹0 |
| Week 16 (~month 4) | Kit #1: ESP32/Arduino + motors + sensors + chassis + tools | ₹3,000–5,000 |
| ~Month 7 (Phase 6) | Raspberry Pi 5 (+ camera) | ₹8,000–11,000 |
| Phase 7+ (optional) | Jetson Orin Nano / SO-101 arm | ₹15,000–35,000 each |

---

## If you fall behind

That's normal and fine. Rules:
1. Never skip a checkpoint — do the review instead of rushing.
2. Missing a day? Just continue from where you stopped. Day numbers are *sessions*, not calendar dates.
3. If something feels too hard for 2+ sessions, tell Claude — we'll add a bridge session.
