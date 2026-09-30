# Day 01 — Answers

> Your answers don't need to match word-for-word. What matters is the idea.

## Concepts

**1. Robot definition.** A machine that senses the physical world, decides what to do, and acts to change the physical world, in a repeating loop.
- *Ceiling fan:* not a robot. It spins at the speed you set. It doesn't sense or decide anything.
- *Smart thermostat:* **borderline**, which makes it a good discussion point. It has a sense→think→act loop (it measures temperature and switches heating/cooling on or off), so it's an *automatic control system*. Most people don't call it a robot, because it has no body that moves or manipulates things. The line between "robot" and "smart machine" is blurry, and that's OK.

**2. Hovering drone 🚁.**
- *Sense:* IMU (tilt + rotation speed), barometer (height), maybe GPS/camera (position drift).
- *Think:* "I'm tilted 2° to the left and dropping 5 cm → I need more thrust on the left motors and a bit more total thrust."
- *Act:* change the speed of each of the 4 motors.
This loop runs hundreds of times per second, or the drone falls.

**3. Six ingredients (robot vacuum).** Body: round plastic shell + wheels. Actuators: wheel motors, brush motor, suction fan. Sensors: bumper, cliff sensors, wheel encoders, lidar/camera on some models. Computer: the main board inside. Power: rechargeable battery. Software: cleaning pattern, mapping, obstacle handling.

**4.** "Where am I?" → **State estimation**. "How much power to each motor?" → **Control**.

**5.** Classical = humans write the rules/equations → predictable, explainable, safe, but brittle in new situations. Learning-based = the robot learns behavior from data → handles messy/new situations, but needs lots of data and is harder to predict or guarantee.

**6. Moravec's paradox.** Any example where something is easy for humans but hard for robots (or the reverse) works, e.g.: "A computer can multiply 10-digit numbers instantly, but a robot still struggles to tie shoelaces, which a 6-year-old can do."

**7.** Little data (no "internet of robot actions"), mistakes are physical and costly/dangerous, decisions must happen in milliseconds, and the real world is noisy (friction, lighting, slippery floors). Also, every robot body is different.

**8.** A virtual environment keeps this project's Python + library versions separate. Without one, installing a library version for project A could break project B, and your system Python could get messed up.

**9.** `git commit` saves a snapshot **on your Mac** (local history). `git push` uploads your commits **to GitHub**.

## Math

**10.** `L = 1`, `θ = 90°`: `x = 1·cos 90° = 0`, `y = 1·sin 90° = 1` → hand at **(0, 1)**, pointing straight up.

**11.** `L = 0.8`, `θ = 60°`: `x = 0.8 × 0.5 = 0.4`, `y = 0.8 × 0.866 = 0.693` → hand at **(0.4, 0.693)**.

**12. Two-link teaser.**
- Elbow: link 1 at 0° → elbow at `(1·cos 0°, 1·sin 0°)` = **(1, 0)**.
- Link 2 is bent 90° *relative to link 1*, so its absolute angle is `θ1 + θ2 = 0° + 90° = 90°`.
- Hand = elbow + `(L2·cos 90°, L2·sin 90°)` = `(1 + 0, 0 + 1)` = **(1, 1)**.

```
    y
    ▲
  1 │      ● hand (1,1)
    │      │ L2
    │      │
  0 ●──────● elbow (1,0) ──▶ x
  motor  L1
```
General formula (Phase 2 will derive it properly):
`x = L1·cos θ1 + L2·cos(θ1+θ2)`, `y = L1·sin θ1 + L2·sin(θ1+θ2)`

## Experiments (C3)

1. **`SENSOR_NOISE = 0.5`:** the stopping point changes every run (noise is random), and the robot almost always stops **too early**, somewhere around 1.3–2 m from the wall. Why early? The robot takes one reading every step, and it only needs **one** unlucky reading below 1 m to stop for good. With many readings, one of them is bound to be low. **Lesson:** decisions based on a single noisy measurement are unreliable → we'll fix this with filters (Kalman filter, Phase 5).
2. **Slow speed 8.0 m/s:** the robot now moves 0.8 m per step (`8 × 0.1`). It only checks its sensor once per step, so it jumps past the 1 m target and stops around 0.5 m from the wall. **At 20 m/s** it moves 2 m per step and sometimes jumps straight through the wall 💥, depending on the noise. **Lesson:** the faster you move, the more often you must sense, or the more carefully you must slow down. This is why drones run their control loops so fast.
3. **`DT = 1.0`:** each step is now 1 second, so the robot moves 10× farther between sensor checks (1 m per step when fast, 0.3 m when slow). It reacts less often, so it stops a bit past the target (around 0.8–0.9 m from the wall), and the plot looks like big stairs. With higher speeds this would become a crash. **Lesson:** the loop rate (how often you sense→think→act) matters a lot.

## ⭐ Challenge (P-controller)

- **K = 0.5:** smooth, but *slow* at the end. The speed shrinks as the robot gets closer, so it creeps toward the target. It usually stops a little **short** (~1.05–1.1 m), because the speed falls below the 0.01 cutoff (or a noisy reading makes it negative) before the robot actually arrives. This "never quite gets there" problem is famous in control, and the "I" in PID exists to fix it.
- **K = 2:** faster, still smooth, and stops close to the target. A good balance.
- **K = 20:** it drives at the 1 m/s cap almost all the way, then brakes very late. Because `K × DT = 2`, each step at the end moves about *twice* the remaining error, so it overshoots the target slightly. If the robot could reverse (negative speeds), a large K would make it **oscillate** back and forth, and a big enough K would make it go **unstable**. We study this properly in Phase 3 (PID control & stability).
