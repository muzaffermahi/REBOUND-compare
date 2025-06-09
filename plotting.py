
# rebound_compare/plotting.py
import matplotlib.pyplot as plt

def plot_orbital_element(results, element="a", particle=1):
    times = results["time"]
    y1 = [step[particle] for step in results["sim1"][element]]
    y2 = [step[particle] for step in results["sim2"][element]]

    plt.figure(figsize=(10, 5))
    plt.plot(times, y1, label="Simulation 1")
    plt.plot(times, y2, label="Simulation 2")
    plt.xlabel("Time")
    plt.ylabel(f"{element} (AU)")
    plt.title(f"Comparison of {element.upper()} for Particle {particle}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
