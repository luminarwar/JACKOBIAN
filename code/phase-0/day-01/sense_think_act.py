"""
Day 01 — Your first robot program: the Sense → Think → Act loop.

The world: a straight corridor. A robot starts at position 0 m.
There is a wall at position 10 m. The robot has a distance sensor
pointing forward. Goal: drive toward the wall and stop ~1 m before it.

    position: 0 m                                        10 m
              🤖 ─────────────────────────────────────▶ ▓▓ WALL

Run (from the JACKOBIAN folder, with .venv activated):
    python code/phase-0/day-01/sense_think_act.py

Your job: complete TODO 1, 2 and 3 below.
"""
import random

# ---------------- World settings (try changing these later!) ----------------
WALL_POSITION = 10.0   # where the wall is (meters)
STOP_DISTANCE = 1.0    # we want to stop this far from the wall (meters)
SENSOR_NOISE = 0.05    # how "wrong" the sensor can be (standard deviation, meters)
DT = 0.1               # time step: each loop = 0.1 seconds of robot time
MAX_STEPS = 500        # safety limit so the loop can't run forever


def sense(robot_position):
    """SENSE: return the distance to the wall, as measured by a NOISY sensor."""
    true_distance = WALL_POSITION - robot_position

    # TODO 1: Real sensors are noisy. Add a small random error to true_distance.
    # Hint: random.gauss(0, SENSOR_NOISE) returns a random number that is
    #       usually close to 0 (a "bell curve" / Gaussian — you saw it in ML!).
    measured_distance = true_distance  # <- change this line

    return measured_distance


def think(measured_distance):
    """THINK: decide how fast to drive (in m/s) based on the measurement."""

    # TODO 2: Use if / elif / else to choose the speed:
    #   - distance greater than 3 m                  → 1.0 m/s  (fast)
    #   - distance between STOP_DISTANCE and 3 m     → 0.3 m/s  (slow, careful)
    #   - distance STOP_DISTANCE or less             → 0.0 m/s  (stop)
    speed = 0.0  # <- replace this with your if / elif / else

    return speed


def act(robot_position, speed):
    """ACT: move the robot. Physics: distance moved = speed × time."""

    # TODO 3: compute the new position after one time step of DT seconds.
    new_position = robot_position  # <- change this line

    return new_position


# ------------------- The main loop (already written for you) -------------------
def main():
    position = 0.0
    positions = [position]   # remember the path so we can plot it

    for step in range(MAX_STEPS):
        distance = sense(position)          # 1. SENSE
        speed = think(distance)             # 2. THINK
        position = act(position, speed)     # 3. ACT
        positions.append(position)

        print(f"step {step:3d} | sensor says {distance:5.2f} m | "
              f"speed {speed:.2f} m/s | position {position:5.2f} m")

        if speed == 0.0:
            print("\n🛑 Robot decided to stop.")
            break

    gap = WALL_POSITION - position
    print(f"Final distance to wall: {gap:.2f} m")
    if gap < 0:
        print("💥 CRASH! The robot went through the wall.")
    elif abs(gap - STOP_DISTANCE) < 0.2:
        print("🎉 Perfect stop!")
    return positions


def plot(positions):
    """Plot position vs. time (Matplotlib — we'll learn it properly on Day 09)."""
    import matplotlib.pyplot as plt

    times = [i * DT for i in range(len(positions))]
    plt.plot(times, positions, label="robot position")
    plt.axhline(WALL_POSITION, color="red", label="wall")
    plt.axhline(WALL_POSITION - STOP_DISTANCE, color="green", linestyle="--", label="target stop")
    plt.xlabel("time (s)")
    plt.ylabel("position (m)")
    plt.title("Day 01 — Sense → Think → Act robot")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    path = main()
    plot(path)
