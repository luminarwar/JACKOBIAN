# Day 01 — The Big Picture + Setting Up Your Lab

> **Phase:** 0 — Setup + Python Muscles · **Week:** 1 · **Estimated time:** ~3 hours
> **Next:** Day 02 — Python refresher I

## 🎯 Today's goal

By the end of today you will:
1. Understand **what a robot is**, what **embodied AI** means, and the map of everything we'll learn.
2. Have a working "robotics lab" on your Mac: terminal, Python environment, VS Code, Jupyter, Git.
3. Write your **first robot program** — a simulated robot that senses a wall and stops before hitting it.

## ⏱️ Suggested time plan

| Block | Time | What |
|---|---|---|
| Part A | 60 min | 📖 Theory: the big picture (read this file) |
| Videos | 30 min | 🎥 Watch/read the resources below |
| Part B | 45 min | 🛠️ Lab setup: terminal, venv, VS Code, Jupyter, Git |
| Part C | 45 min | 💻 Code: your first Sense→Think→Act robot |
| Wrap-up | 15 min | ❓ Questions, 📝 notes, commit |

Take a 5–10 min break between blocks. Seriously — your brain learns during the breaks.

---

# PART A — 📖 The Big Picture

## 1. What is a robot?

There are many definitions. Here's the one we'll use:

> **A robot is a machine that *senses* the physical world, *thinks* about what it sensed, and *acts* to change the physical world — over and over, in a loop.**

That loop is the heart of all robotics. It's called the **Sense → Think → Act** loop:

```
          ┌───────────────────────────────────────────┐
          │                THE WORLD                  │
          │   (walls, objects, people, gravity...)    │
          └─────▲───────────────────────────┬─────────┘
                │                           │
          changes the world          light, sound, distance,
                │                    forces, tilt...
                │                           │
          ┌─────┴─────┐               ┌─────▼─────┐
          │   ACT     │               │  SENSE    │
          │ motors,   │               │ cameras,  │
          │ wheels,   │               │ distance  │
          │ grippers  │               │ sensors,  │
          └─────▲─────┘               │ IMU...    │
                │                     └─────┬─────┘
                │      ┌───────────┐        │
                └──────┤  THINK    │◀───────┘
                       │ software, │
                       │ AI, math  │
                       └───────────┘
          This loop repeats many times per second
          (10 to 1000+ times/sec depending on the robot)
```

**Example — a robot vacuum cleaner:**

| Step | What happens |
|---|---|
| **Sense** | Bumper sensor says "I touched something". Cliff sensor says "no stairs here". Wheel sensors say "I moved 12 cm" |
| **Think** | "I hit an obstacle → back up and turn 30° left. I've cleaned the left half → go right next" |
| **Act** | Send commands to the wheel motors: left wheel backward, right wheel forward |

A **washing machine** follows a fixed program and doesn't really sense its environment, so it's not really a robot.
A **self-driving car** is a robot (a big one!). A **drone** is a flying robot. A **humanoid** is a robot shaped like a human.

> 💡 **Key idea:** A robot is not defined by *looking like a human*. It's defined by the **loop**: sense, think, act.

## 2. Anatomy of a robot

Every robot — a vacuum, a drone or a humanoid — has the same 6 ingredients:

```
┌──────────────────────────────────────────────────────────────────┐
│  1. BODY (mechanics)   frame, links, joints, wheels, propellers  │
│  2. ACTUATORS          things that MOVE: motors, servos          │
│  3. SENSORS            things that MEASURE: camera, IMU, lidar   │
│  4. COMPUTER           the brain: microcontroller, Pi, Jetson    │
│  5. POWER              battery, power electronics                │
│  6. SOFTWARE           code: control, perception, AI             │
└──────────────────────────────────────────────────────────────────┘
```

Let's label a **quadcopter drone** 🚁:

```
      propeller (actuator)           propeller
            \    ___________    /
             (X)=|         |=(X)
                 | flight  |        ← COMPUTER: flight controller board
                 | controller     ← SENSORS on it: IMU (tilt/rotation),
                 |  + IMU  |          barometer (height), GPS
             (X)=|_________|=(X)
            /      battery      \   ← POWER
      motor (actuator)          frame = BODY
```

And a **humanoid** 🦿:

```
            ( o o )     ← head: cameras (SENSORS), sometimes a computer
              |▔|
        ⎡━━━━━┼━━━━━⎤   ← shoulders: motors in every joint (ACTUATORS)
        ┃   torso   ┃   ← COMPUTER (e.g., Jetson) + BATTERY inside
        ✋   ┃ ┃    ✋  ← hands: many small motors + touch sensors
            ┃ ┃
           ━┛ ┗━        ← legs: powerful motors, IMU in the torso for balance
```

A typical humanoid has **20–40+ motors** ("degrees of freedom"). Controlling all of them together, while balancing, is *hard*. That's why humanoids are one of the hottest problems in robotics right now.

## 3. Types of robots

| Type | Examples | What makes it hard |
|---|---|---|
| **Robot arms (manipulators)** | Factory arms in car plants, surgical robots | Precise positioning, grasping weird objects |
| **Wheeled mobile robots** | Robot vacuums, warehouse robots, self-driving cars | Knowing where you are, avoiding obstacles |
| **Legged robots** | Robot dogs (quadrupeds), humanoids 🦿 | Balance! They can fall over |
| **Aerial robots** | Drones 🚁 | Must control themselves every millisecond or they crash; limited battery |
| **Others** | Underwater robots, space rovers, soft robots | Extreme environments |

## 4. The robotics software stack (the most important diagram today)

When a robot "thinks", it's actually doing several jobs one after another:

```
   SENSORS                                                        MOTORS
      │                                                             ▲
      ▼                                                             │
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐  │
│ PERCEPTION │──▶│   STATE    │──▶│  PLANNING  │──▶│  CONTROL   │──┘
│            │   │ ESTIMATION │   │            │   │            │
│ "What do I │   │ "Where am  │   │ "What      │   │ "Exactly   │
│  see?"     │   │  I? How am │   │  should I  │   │  how much  │
│            │   │  I moving?"│   │  do next?" │   │  power to  │
│ camera →   │   │            │   │            │   │  each      │
│ "a cup at  │   │ "I'm 2.3 m │   │ "path to   │   │  motor,    │
│  the left" │   │  from wall,│   │  the cup,  │   │  right     │
│            │   │  tilted 3°"│   │  avoiding  │   │  now?"     │
│            │   │            │   │  the chair"│   │            │
└────────────┘   └────────────┘   └────────────┘   └────────────┘
   Phase 5          Phase 5        Phases 2, 7       Phases 3, 4

 Underneath all of it: MATH (Phase 1) + PHYSICS/KINEMATICS (Phases 2–3)
 Connecting all of it: ROS 2 (Phase 6)
 Learning any of it from data: ROBOT LEARNING / EMBODIED AI (Phase 7)
```

So the roadmap isn't random — **each phase builds one box of this diagram.** Keep this picture in mind. Every time you learn something new, ask: *"which box does this belong to?"*

## 5. What is Embodied AI?

**ChatGPT is AI without a body.** It reads text and writes text. It never has to catch a ball.

**Embodied AI = AI that has a body** and has to act in the physical world. It learns from, and through, physical interaction.

Two ways to build the "Think" part of a robot:

```
CLASSICAL ROBOTICS                       LEARNING-BASED ROBOTICS (Embodied AI)
─────────────────────                    ─────────────────────────────────────
Humans write rules & equations           The robot learns behavior from DATA

 camera → [hand-written vision code]      camera ─┐
        → [math for position]                      ├─▶ [ big neural network ] ─▶ motors
        → [hand-designed planner]         words  ──┘   ("pick up the red cup")
        → [PID controller] → motors

✅ Predictable, explainable, safe         ✅ Handles messy, new situations
❌ Breaks in messy, new situations        ❌ Needs lots of data, less predictable
```

Modern robots **mix both**. For example, a humanoid might use a neural network to decide "grab the cup" and classical control to keep its balance. That's why we learn **both** — classical first (Phases 1–6), learning after (Phase 7). A great robotics engineer understands both sides. (Many AI people jump straight into learning and later struggle because they don't understand the physics.)

### Moravec's Paradox 🤯

> *Things that are hard for humans (chess, math) are easy for computers. Things that are easy for humans (walking, folding a shirt, picking up an egg) are **very hard** for computers.*

A 2-year-old can pick up a toy it has never seen before. Getting a robot to do that reliably is still an active research problem. **This is why robotics is hard — and also why it's a huge opportunity.**

### Why is AI for robots harder than AI for text?

| | ChatGPT-style AI | Robot AI |
|---|---|---|
| **Data** | Trillions of words on the internet | Very little robot data; every robot is different |
| **Mistakes** | A wrong answer → retry | A wrong action → broken robot, broken cup, hurt person |
| **Speed** | Can take a few seconds | Must decide in milliseconds (a drone falls in ~0.5 s) |
| **World** | Text is clean | Physical world is noisy: friction, lighting, slippery floors |

## 6. Why do we need math and physics? A tiny preview

Imagine the simplest robot arm: one stick of length `L`, rotating around a motor at the origin by angle `θ` (theta).

```
    y
    ▲
    │          ● hand (x, y) = ?
    │         /
    │      L /
    │       /
    │      / θ
    └─────●──────────▶ x
        motor
```

**Where is the hand?** From school trigonometry:

```
x = L · cos(θ)
y = L · sin(θ)
```

**Worked example:** `L = 0.5 m`, `θ = 30°`
- `x = 0.5 × cos(30°) = 0.5 × 0.866 = 0.433 m`
- `y = 0.5 × sin(30°) = 0.5 × 0.5  = 0.25 m`

So the hand is at `(0.433, 0.25)`. 🎉 **You just did forward kinematics** — a Phase 2 topic, on Day 1.

A humanoid arm is just several of these sticks chained together, in 3D, with 7 joints. That's where **vectors, matrices and rotations** (Phase 1) come in. And to make it move *smoothly* without shaking, you need **physics and control** (Phase 3).

## 7. The robotics landscape right now (just for motivation)

You don't need to memorize this — it's here so you know the world you're entering.

- **Humanoids** 🦿 — Many companies are racing to build general-purpose humanoids: Tesla (Optimus), Figure, Agility Robotics (Digit), Boston Dynamics (Atlas), Unitree (G1/H1, relatively affordable), 1X, and more.
- **Robot foundation models** — "GPT for robots": models that take camera images + a language instruction and output robot actions. Examples: Google DeepMind's RT-2 / Gemini Robotics, Physical Intelligence's π0, NVIDIA's GR00T, and open ones like OpenVLA. (Phase 7!)
- **Drones** 🚁 — Delivery, agriculture, inspection, defense. In India: companies like ideaForge and Garuda Aerospace, plus a growing drone ecosystem after the regulations were liberalized.
- **India's robotics scene** — warehouse automation (e.g., Addverb), industrial vision/manipulation (e.g., CynLr), autonomous industrial vehicles (e.g., Ati Motors), and many young startups. Still early — which means room for new companies.
- **Open-source robotics** — Hugging Face **LeRobot** + cheap arms like the **SO-101** mean a student can now do real robot-learning research on a small budget. This didn't exist a few years ago.

---

# 🎥 Watch / Read (~30 min)

1. **"Robots: Crash Course Computer Science #37"** — YouTube, CrashCourse channel (~12 min). A light, fun overview. Search the exact title.
2. **Modern Robotics, Chapter 1 "Preview"** — free PDF from [the book's page](https://hades.mech.northwestern.edu/index.php/Modern_Robotics). Chapter 1 is short (~10 pages). **Skim it**; don't try to understand everything. Just notice the topics — you'll recognize them from today's stack diagram.
3. **Just for fun (5 min):** search YouTube for "Boston Dynamics Atlas" and "Unitree G1". Watch one short clip of each. For each clip, try to spot sense → think → act.
4. *(Optional)* Read the Wikipedia page on **Moravec's paradox**.

---

# PART B — 🛠️ Setting Up Your Lab (~45 min)

Claude has already created the folder structure and the Python environment. Your job is to **understand** each tool and try it yourself.

## B1. The Terminal

The terminal is a text way to control your computer. Robotics engineers live in it (especially later with Linux, ROS 2 and the Raspberry Pi).

Open it: `Cmd + Space` → type **Terminal** → Enter.

| Command | Meaning | Try it |
|---|---|---|
| `pwd` | **p**rint **w**orking **d**irectory — "where am I?" | `pwd` |
| `ls` | **l**i**s**t files here | `ls` |
| `cd <folder>` | **c**hange **d**irectory — "go into" | `cd ~/Desktop/JACKOBIAN` |
| `cd ..` | go up one folder | `cd ..` |
| `mkdir <name>` | **m**a**k**e a **dir**ectory (folder) | *(don't need it today)* |
| `clear` | clear the screen | `clear` |

**Try:** go into the project, then list what's inside:
```bash
cd ~/Desktop/JACKOBIAN
ls
```
You should see: `CLAUDE.md  README.md  code  docs  notes  papers  projects  requirements.txt  solutions` (plus some hidden files).

`~` means your home folder. `ls -a` also shows hidden files (names starting with a dot), like `.venv` and `.gitignore`.

## B2. The Python virtual environment (`.venv`)

**Problem:** Different projects need different versions of libraries. If you install everything into one global Python, projects start breaking each other.

**Solution:** a **virtual environment** — a private toolbox of Python + libraries, just for this project.

```
Your Mac
├── System Python (don't touch!)
└── JACKOBIAN/
    └── .venv/  ← our private toolbox: Python 3.12 + numpy, matplotlib, scipy, jupyter
```

We use **Python 3.12** (not the newest, 3.13) because some robotics libraries take a while to support the newest version. 3.12 is the safe choice.

The environment was created with **`uv`**, a very fast modern tool for managing Python. You'll mostly just use `pip` as usual.

**Activate it** (do this every time you open a new terminal for this project):
```bash
cd ~/Desktop/JACKOBIAN
source .venv/bin/activate
```
Your prompt now starts with `(.venv)` or `(JACKOBIAN)`. Check which Python you're using:
```bash
which python        # should end in /JACKOBIAN/.venv/bin/python
python --version    # Python 3.12.x
```
To leave: `deactivate`.

**Installing a new package later:** activate first, then `pip install <name>`, and add it to `requirements.txt`.

## B3. VS Code (your code editor)

1. Download from **code.visualstudio.com** and install (drag to Applications).
2. Open VS Code → `File → Open Folder…` → choose `JACKOBIAN`.
3. Install extensions (left sidebar, the 4-squares icon): **Python** (by Microsoft) and **Jupyter** (by Microsoft).
4. Press `Cmd + Shift + P` → type **"Python: Select Interpreter"** → choose the one showing `.venv`.
5. *(Handy)* `Cmd + Shift + P` → **"Shell Command: Install 'code' command in PATH"**. Now `code .` in the terminal opens the current folder in VS Code.
6. VS Code has a built-in terminal: `` Ctrl + ` `` (backtick). It usually activates `.venv` for you automatically.
7. To read these lesson files nicely: open a `.md` file and press `Cmd + Shift + V` (Markdown preview).

## B4. Jupyter Lab (for experiments)

Jupyter notebooks are great for *trying things* — you already used them in your ML course. We'll use:
- **`.py` files** for real programs (robots, simulations)
- **Jupyter notebooks** for math experiments and plots

Try it:
```bash
source .venv/bin/activate
jupyter lab
```
A browser tab opens. Create a new notebook and run `import numpy as np; np.__version__`. Close it with `Ctrl + C` in the terminal (VS Code can also open `.ipynb` files directly).

## B5. Git — the "save game" system for code

**Git** takes snapshots of your project. Each snapshot is a **commit**. You can always go back to any commit. **GitHub** is a website that stores a copy of your repository online (a backup + your public portfolio).

```
 working folder ──(git add)──▶ staging area ──(git commit)──▶ local history ──(git push)──▶ GitHub
  "I changed files"             "these changes             "snapshot saved     "backed up online"
                                  go in the next photo"       on my Mac"
```

| Command | What it does |
|---|---|
| `git status` | What changed? (use this constantly) |
| `git add <file>` / `git add .` | Put changes on the staging area |
| `git commit -m "message"` | Take the snapshot with a description |
| `git log --oneline` | See the history of snapshots |
| `git push` | Upload commits to GitHub |

Claude has already made the first commit and pushed it to GitHub. Look at the history:
```bash
git log --oneline
```
You'll make **your own first commit** at the end of today (see Wrap-up).

> 🔒 **Privacy:** the `private/` folder (your profile + progress log) is listed in `.gitignore`, so git ignores it and it **never goes to GitHub**. Everything else — lessons, your code, your notes — is public and becomes your learning portfolio.

---

# PART C — 💻 Your First Robot Program (~45 min)

## C1. Check your setup

```bash
cd ~/Desktop/JACKOBIAN
source .venv/bin/activate
python code/phase-0/day-01/check_setup.py
```
Everything should show ✅. If not, note the error — we'll fix it together.

## C2. Sense → Think → Act robot

Open `code/phase-0/day-01/sense_think_act.py` in VS Code and read it top to bottom first.

**The world:**
```
 position:  0 m                                            10 m
            🤖 ───────────────────────────────────────────▶ ▓▓ WALL
            robot starts here, has a distance sensor
            pointing forward

 Goal: drive to the wall and stop ~1 m before it. Don't crash!
```

**The sensor is noisy.** Real sensors never give the exact truth. If the true distance is 5.00 m, the sensor might say 4.97 or 5.04. We simulate that with random noise.

**Your tasks** (they're marked `TODO` in the file):

| TODO | Function | What to do |
|---|---|---|
| 1 | `sense()` | Add Gaussian noise to the true distance. Hint: `random.gauss(0, SENSOR_NOISE)` |
| 2 | `think()` | Choose a speed with if/elif/else: far (> 3 m) → 1.0 m/s, closer → 0.3 m/s, at `STOP_DISTANCE` or less → 0 |
| 3 | `act()` | Physics! `new_position = old_position + speed × DT` (distance = speed × time) |

Run it:
```bash
python code/phase-0/day-01/sense_think_act.py
```
You'll see the robot's log printed step by step, then a plot of position vs. time.

**Before you look at `solutions/`**, try for at least 20–30 minutes. Getting stuck and un-stuck is where learning happens. If you're stuck, ask Claude for a *hint* rather than the answer.

## C3. Experiments (change things and observe)

After it works, try these one at a time and **write down what you see**:
1. Set `SENSOR_NOISE = 0.5`. Does the robot still stop in a good place? Run it 3 times — is it the same every time? Why?
2. Change the **slow** speed from 0.3 to 8.0 m/s, then to 20.0 m/s. Run each a few times. Where does the robot stop? Does it ever crash? Why? *(Hint: how far does the robot move in one step of `DT`?)*
3. Set `DT = 1.0`. What changes?

These three experiments preview huge ideas: **sensor noise** (Phase 5), **control** (Phase 3) and **time steps in simulation** (Day 10).

## C4. ⭐ Challenge (optional)

Instead of 3 fixed speeds, make the speed **proportional to the remaining distance**:
```
speed = K × (measured_distance − STOP_DISTANCE)
```
Cap it at 1.0 m/s, and treat very small speeds (< 0.01) as 0. Try `K = 0.5`, `K = 2`, `K = 20`. What happens with each?
Congratulations — that's a **P-controller**, the "P" in PID, which we study properly in Phase 3.

---

# ❓ Practice questions

**Concepts** (answer in your notes, in your own words):
1. Define a robot in one sentence. Is a ceiling fan a robot? Is a smart thermostat? Why or why not?
2. Draw the Sense → Think → Act loop for a **drone that's hovering in place** 🚁. What does it sense? What does it decide? What does it act on?
3. Name the 6 ingredients of a robot. For a robot vacuum, give one example of each.
4. In the software stack diagram, which box answers "Where am I?" Which box answers "How much power to each motor?"
5. What is the difference between classical robotics and learning-based robotics? Give one advantage of each.
6. Explain Moravec's paradox with your own example (not one from this file).
7. Give 3 reasons why AI for robots is harder than AI for text.
8. Why do we use a virtual environment? What would go wrong without one?
9. What's the difference between `git commit` and `git push`?

**Math:**

10. One-link arm, `L = 1 m`, `θ = 90°`. Where is the hand? Sketch it.
11. One-link arm, `L = 0.8 m`, `θ = 60°`. Where is the hand? (Use a calculator or Python: `import math; math.cos(math.radians(60))`)
12. ⭐ **Two-link arm teaser.** Link 1 (`L1 = 1 m`) rotates by `θ1 = 0°` from the x-axis. Link 2 (`L2 = 1 m`) is attached at the end of link 1 and bent by `θ2 = 90°` *relative to link 1*. Where is the elbow? Where is the hand? *(Hint: draw it! First find the elbow, then add the second link starting from there.)*

Answers: `solutions/phase-0/day-01/answers.md` — check them **after** you've tried.

---

# ✅ Self-check (exit ticket)

Tick these honestly. Anything unticked goes into "weak spots" in PROGRESS.
- [ ] I can explain the Sense → Think → Act loop with an example
- [ ] I can draw the robotics software stack (perception → estimation → planning → control)
- [ ] I can explain embodied AI and Moravec's paradox to a friend
- [ ] I can open a terminal, go to the project, and activate `.venv`
- [ ] I can run a Python file from the terminal
- [ ] I finished the 3 TODOs and the robot stops before the wall
- [ ] I know what `git add`, `git commit` and `git push` do

---

# 📝 Wrap-up: notes + your first commit (~15 min)

**1. Write your notes** in `notes/phase-0/day-01.md` (create the file in VS Code). Use your own words — don't copy. Suggested headings:
```markdown
# Day 01 notes
## What is a robot (my definition)
## The robotics stack (draw it in ASCII or describe it)
## Embodied AI in 3 sentences
## Answers to practice questions
## What confused me / questions for Claude
## Experiment results (noise, speed, DT)
```

**2. Commit and push your work:**
```bash
cd ~/Desktop/JACKOBIAN
git status                                   # see what changed (red = not staged)
git add notes/ code/
git status                                   # now green = staged
git commit -m "Day 01: notes + sense-think-act robot"
git push
git log --oneline                            # see your commit in history!
```

**3. Next session**, start by telling Claude: *"Day 01 done — please review my notes and code"*. Claude will give feedback and prepare Day 02.

---

# 🚀 Going further (optional, only if you have energy left)

- Watch **Lecture 1 of MIT Missing Semester** ("Course overview + the shell") at [missing.csail.mit.edu](https://missing.csail.mit.edu). It'll make you much more comfortable in the terminal.
- Modify the robot so that the wall **moves** (e.g., `WALL_POSITION` shrinks a little every step, like a person walking toward the robot). Does your robot still stop safely?
- Think about it: what would change if the robot were a **drone** flying up toward a ceiling instead of a car driving toward a wall? (Hint: gravity!)
