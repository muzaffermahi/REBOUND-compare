# example_usage.py
import rebound
from compare import run
from plotting import plot_orbital_element

# Set up two simulations
sim1 = rebound.Simulation()
sim1.units = ("AU", "yr", "Msun")
sim1.integrator = 'ias15'
sim1.add(m=1.0)  # Sun
sim1.add(m=4.36e-5, a=19.165, e=0.0469, inc=0.77)  # Uranus
sim1.add(m=5.15e-5, a=30.1, e=0.009, inc=1.8)  # Neptune
sim1.add(a=838, e=0.946, inc=16.2, Omega=328.6, omega=337.7)  # 2017 OF201 (TNO)
sim1.add(m=4e-5, a=400, e=0.4, inc=30, Omega=150, omega=250)  # Planet Nine

sim2 = rebound.Simulation()
sim2.units = ("AU", "yr", "Msun")
sim2.integrator = 'ias15'
sim2.add(m=1.0)  # Sun
sim2.add(m=4.36e-5, a=19.165, e=0.0469, inc=0.77)  # Uranus
sim2.add(m=5.15e-5, a=30.1, e=0.009, inc=1.8)  # Neptune
sim2.add(a=838, e=0.946, inc=16.2, Omega=328.6, omega=337.7)  # 2017 OF201 (TNO)

# Run comparison and plot
results = run(sim1, sim2, duration=1e6, N_steps=100, track=["a"])
plot_orbital_element(results, element="a", particle=2)
