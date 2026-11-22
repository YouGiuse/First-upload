import matplotlib.pyplot as plt
g = 9.81
mass = float(input("Enter the object's mass: "))
air_density = float(input("Enter the fluid's density i.e.(1/light fluid, 3/heavy fluid, 6/thick fluid) :"))
v = 0.0
steps = 1000
secS = 0.1    #seconds per step

#Object falls through the fluid(air/liquid)
terminal_v = (mass * g) / air_density
target_v = 0.99 * terminal_v # must be under 100% since mathematically to get velocity equal to terminal velocity time must be infinite
settled_time = None
times = []
velocity = []
for step in range(steps):
    t = step * secS
    if settled_time is None and v >= target_v:
        settled_time = t
    print(f"t = {t: 0.2f}s --- Velocity = {v: 0.3f} ms^-1")
    times.append(t)
    velocity.append(v)
    a = g - (air_density / mass) * v
    v = v + a *secS

print(f"\nTerminal velocity: {terminal_v: 0.3f} ms^-1")
print(f"99% target velocity: {target_v: 0.3f} ms^-1")
if settled_time is not None:
    print(f"reached settling mark at t = {settled_time: .2f}s")
else:
    print(f"Did not reach settling mark with the given time")

#Graph Visualization
plt.figure(figsize = (8,5))
plt.plot(times, velocity)
plt.axhline(terminal_v, linestyle="--", label=f"Terminal v ({terminal_v:.2f} m/s)")

if settled_time is not None:
    plt.axvline(settled_time, linestyle=":", label=f"99% settled ({settled_time:.2f}s)")

plt.title(f"settling surve (density = {air_density}, mass = {mass} kg)")
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()