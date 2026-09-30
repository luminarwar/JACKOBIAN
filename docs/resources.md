# 📚 Master Resource List

> Each session file tells you *exactly* which part of which resource to use. This page is the full library, in one place.
> ⭐ = core resource we will use a lot. For YouTube channels, search the channel name on YouTube.

---

## Phase 0 — Python & Tools

| Resource | Type | Notes |
|---|---|---|
| ⭐ [MIT Missing Semester](https://missing.csail.mit.edu) | Free course | Shell, git, editors — the "tools nobody teaches you" course |
| [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) | Official guide | Very well written |
| [Matplotlib docs](https://matplotlib.org) | Official docs | Tutorials + gallery of examples |
| [Pro Git book](https://git-scm.com/book) | Free book | Chapters 1–3 are enough for a long time |
| Corey Schafer (YouTube) | Videos | Clear Python, Matplotlib and Git videos |

## Phase 1 — Math

| Resource | Type | Notes |
|---|---|---|
| ⭐ [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) | Videos | Best visual intuition for vectors & matrices, bar none |
| ⭐ [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus) | Videos | Visual calculus |
| [Khan Academy](https://www.khanacademy.org) | Course | Trig/calculus/probability refresh when you feel rusty |
| Gilbert Strang — MIT 18.06 Linear Algebra | Video lectures | Optional, deeper |

## Phase 2 — Kinematics

| Resource | Type | Notes |
|---|---|---|
| ⭐ [Modern Robotics — Lynch & Park](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) | Free book + videos | Our main robotics textbook. The "Northwestern Robotics" YouTube channel has short videos for every section |
| [Robotics Toolbox for Python — Peter Corke](https://github.com/petercorke/robotics-toolbox-python) | Library | Check your own code against it |
| *Robotics, Vision and Control* — Peter Corke | Book | Very practical companion |

## Phase 3 — Physics & Control

| Resource | Type | Notes |
|---|---|---|
| ⭐ Brian Douglas — *Understanding PID Control* & *Control Systems* (MATLAB YouTube channel) | Videos | Friendliest control explanations |
| ⭐ [MuJoCo documentation](https://mujoco.readthedocs.io) | Docs | Our physics simulator |
| [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) | Robot models | Ready-made humanoids, arms, quadrupeds, drones |
| Steve Brunton — *Control Bootcamp* (YouTube) | Videos | State-space control, LQR |
| [Underactuated Robotics — Russ Tedrake](https://underactuated.mit.edu) | Free book | Legged robots & humanoid control (Phase 3 intro → Phase 8 depth) |

## Phase 4 — Electronics

| Resource | Type | Notes |
|---|---|---|
| ⭐ Paul McWhorter — Arduino tutorials (YouTube) | Videos | Slow, beginner-friendly, very thorough |
| [Random Nerd Tutorials](https://randomnerdtutorials.com) | Articles | Best ESP32 tutorials |
| [Wokwi](https://wokwi.com) | Browser simulator | Practice Arduino/ESP32 with no hardware |

## Phase 5 — Perception & Estimation

| Resource | Type | Notes |
|---|---|---|
| ⭐ [Kalman and Bayesian Filters in Python — Roger Labbe](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) | Free Jupyter book | Learn filters by running code |
| [OpenCV docs & tutorials](https://docs.opencv.org) | Docs | Computer vision |
| Cyrill Stachniss (YouTube) | Lectures | SLAM, mobile robotics, photogrammetry — world-class |
| *Probabilistic Robotics* — Thrun, Burgard, Fox | Book | The classic for estimation and SLAM |

## Phase 6 — Linux & ROS 2

| Resource | Type | Notes |
|---|---|---|
| ⭐ [ROS 2 official docs & tutorials](https://docs.ros.org) | Docs | Start with "Beginner: CLI tools" and "Beginner: Client libraries" |
| ⭐ Articulated Robotics (YouTube) | Videos | Build a real ROS 2 robot step by step |

## Phase 7 — Robot Learning & Embodied AI

| Resource | Type | Notes |
|---|---|---|
| ⭐ [Sutton & Barto — Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) | Free book | The RL bible (Ch. 1–6, 13) |
| ⭐ [OpenAI Spinning Up](https://spinningup.openai.com) | Guide | Deep RL explained for engineers |
| ⭐ [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course) | Free course | Hands-on |
| ⭐ [LeRobot](https://github.com/huggingface/lerobot) | Library | Imitation learning, datasets, SO-101 arm |
| [Gymnasium](https://gymnasium.farama.org) | Library | RL environments |
| [Stable-Baselines3](https://stable-baselines3.readthedocs.io) | Library | Ready-made RL algorithms |
| [Robotic Manipulation — Russ Tedrake](https://manipulation.mit.edu) | Free book | Manipulation track |

## Phase 8 — Specialization

| Resource | Track | Notes |
|---|---|---|
| [PX4 docs](https://docs.px4.io) / [ArduPilot docs](https://ardupilot.org) | 🚁 Drones | Open-source flight control stacks |
| *Aerial Robotics* — UPenn (Coursera, Vijay Kumar) | 🚁 Drones | Quadrotor dynamics & control |
| Underactuated Robotics (full) | 🦿 Humanoids | Legged locomotion, MPC |

---

## 📄 Papers (by phase — we read them *when you're ready*, not before)

Search any title on [arxiv.org](https://arxiv.org) (IDs given where useful).

**Phase 5**
- Kalman (1960) — *A New Approach to Linear Filtering and Prediction Problems* (the original Kalman filter)
- Mur-Artal et al. — *ORB-SLAM* (arXiv 1502.00956)

**Phase 7 — RL & sim-to-real**
- Mnih et al. — *Playing Atari with Deep Reinforcement Learning* (arXiv 1312.5602)
- Schulman et al. — *Proximal Policy Optimization Algorithms* (arXiv 1707.06347)
- Tobin et al. — *Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World* (arXiv 1703.06907)
- 🦿 Hwangbo et al. — *Learning Agile and Dynamic Motor Skills for Legged Robots* (arXiv 1901.08652)
- 🦿 Rudin et al. — *Learning to Walk in Minutes Using Massively Parallel Deep RL* (arXiv 2109.11978)
- 🚁 Kaufmann et al. — *Champion-level drone racing using deep reinforcement learning* (Nature, 2023)

**Phase 7 — Imitation learning & foundation models**
- Zhao et al. — *Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware* (ACT / ALOHA, arXiv 2304.13705)
- Chi et al. — *Diffusion Policy* (arXiv 2303.04137)
- Brohan et al. — *RT-1: Robotics Transformer* (arXiv 2212.06817)
- Brohan et al. — *RT-2: Vision-Language-Action Models* (arXiv 2307.15818)
- *Open X-Embodiment: Robotic Learning Datasets and RT-X Models* (arXiv 2310.08864)
- Kim et al. — *OpenVLA* (arXiv 2406.09246)
- Black et al. — *π0: A Vision-Language-Action Flow Model for General Robot Control* (arXiv 2410.24164)
- 🦿 NVIDIA — *GR00T N1* (humanoid foundation model) and Google DeepMind — *Gemini Robotics*

**How we read papers:** the 3-pass method — (1) title, abstract, figures, conclusion; (2) the method, skipping heavy math; (3) the details, only if the paper matters to you. Notes go in `papers/`.
