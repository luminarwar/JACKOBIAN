"""
Day 01 — SOLUTION. Only open this after a real attempt!

Differences from the starter file are marked with  # ✔ SOLUTION
Also includes the ⭐ challenge: think_proportional() — a P-controller.

Run:
    python solutions/phase-0/day-01/sense_think_act.py
"""
import random

WALL_POSITION = 10.0
STOP_DISTANCE = 1.0
SENSOR_NOISE = 0.05
DT = 0.1
MAX_STEPS = 500

USE_PROPORTIONAL = False   # set True to try the challenge controller
K = 2.0                    # proportional gain for the challenge


def sense(robot_position):
    true_distance = WALL_POSITION - robot_position
    measured_distance = true_distance + random.gauss(0, SENSOR_NOISE)  # ✔ SOLUTION
    return measured_distance


def think(measured_distance):
    # ✔ SOLUTION
    if measured_distance > 3.0:
        speed = 1.0
    elif measured_distance > STOP_DISTANCE:
        speed = 0.3
    else:
        speed = 0.0
    return speed


def think_proportional(measured_distance):
    """⭐ Challenge: speed proportional to the remaining distance (a P-controller)."""
    error = measured_distance - STOP_DISTANCE    # how far we still have to go
    speed = K * error
    speed = min(speed, 1.0)                      # cap: never faster than 1 m/s
    if speed < 0.01:                             # tiny or negative → just stop
        speed = 0.0
    return speed


def act(robot_position, speed):
    new_position = robot_position + speed * DT  # ✔ SOLUTION (distance = speed × time)
    return new_position


def main():
    position = 0.0
    positions = [position]
    controller = think_proportional if USE_PROPORTIONAL else think

    for step in range(MAX_STEPS):
        distance = sense(position)
        speed = controller(distance)
        position = act(position, speed)
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
    import matplotlib.pyplot as plt

    times = [i * DT for i in range(len(positions))]
    plt.plot(times, positions, label="robot position")
    plt.axhline(WALL_POSITION, color="red", label="wall")
    plt.axhline(WALL_POSITION - STOP_DISTANCE, color="green", linestyle="--", label="target stop")
    plt.xlabel("time (s)")
    plt.ylabel("position (m)")
    plt.title("Day 01 — Sense → Think → Act robot (solution)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    path = main()
    plot(path)
