# rebound_compare/compare.py
import numpy as np

def run(sim1, sim2, duration, N_steps=100, track=["a"]):
    results = {
        "time": [],
        "sim1": {var: [] for var in track},
        "sim2": {var: [] for var in track}
    }

    primary1 = sim1.particles[0]
    primary2 = sim2.particles[0]

    times = np.linspace(sim1.t, sim1.t + duration, N_steps)
    for t in times:
        sim1.integrate(t, exact_finish_time=0)
        sim2.integrate(t, exact_finish_time=0)
        results["time"].append(t)

        for var in track:
            a1_list = []
            a2_list = []
            for p in sim1.particles[1:]:           # skip particle 0
                orb = p.orbit(primary1)              # ← use .orbit()
                a1_list.append(getattr(orb, var))
            for p in sim2.particles[1:]:
                orb = p.orbit(primary2)              # ← use .orbit()
                a2_list.append(getattr(orb, var))
            results["sim1"][var].append(a1_list)
            results["sim2"][var].append(a2_list)

    return results