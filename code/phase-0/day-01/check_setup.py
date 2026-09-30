"""
Day 01 — Check that your robotics lab is set up correctly.

Run (from the JACKOBIAN folder, with .venv activated):
    python code/phase-0/day-01/check_setup.py
"""
import shutil
import sys


def ok(msg):
    print(f"  ✅ {msg}")


def fail(msg):
    print(f"  ❌ {msg}")


print("\n🔧 Checking your JACKOBIAN lab...\n")

# 1. Python version
major, minor = sys.version_info[:2]
if (major, minor) == (3, 12):
    ok(f"Python {major}.{minor}")
else:
    fail(f"Python {major}.{minor} — expected 3.12. Did you activate .venv?")

# 2. Are we inside the virtual environment?
if ".venv" in sys.prefix:
    ok(f"Using the project virtual environment ({sys.prefix})")
else:
    fail("Not inside .venv — run:  source .venv/bin/activate")

# 3. Libraries
for name in ["numpy", "matplotlib", "scipy", "jupyterlab"]:
    try:
        module = __import__(name)
        ok(f"{name} {module.__version__}")
    except ImportError:
        fail(f"{name} is missing — run:  pip install -r requirements.txt")

# 4. A tiny robotics-flavored NumPy test: rotate the point (1, 0) by 90 degrees
try:
    import numpy as np

    theta = np.radians(90)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    p = R @ np.array([1.0, 0.0])
    if np.allclose(p, [0.0, 1.0]):
        ok(f"NumPy math works: rotated (1, 0) by 90° → ({p[0]:.1f}, {p[1]:.1f})  (you'll learn this in Phase 1!)")
except Exception as e:
    fail(f"NumPy test failed: {e}")

# 5. Git
if shutil.which("git"):
    ok("git is installed")
else:
    fail("git not found")

print("\nIf everything is ✅ — your lab is ready. Let's build robots! 🤖\n")
