import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import matpopmod as mpm

# General parameters:
time_interval = 50  # number of time steps the model will run for
time_steps = 10000  # clarity of graph: higher number = more points plotted
initial_pop_vec = [7000, 2000, 1000]

# Transition matrices:
north_liz_matrix = mpm.MPM([[0, 0, 6.62],
                            [0.33, 0, 0],
                            [0, 0.25, 0.47]])
south_liz_matrix = mpm.MPM([[0, 0, 10.53],
                            [0.3, 0, 0],
                            [0, 0.25, 0.21]])

print("**Northern population** \nDistribution:", north_liz_matrix.w, "\nGrowth rate:", north_liz_matrix.lmbd)
print("\n**Southern population** \nDistribution:", south_liz_matrix.w, "\nGrowth rate:", south_liz_matrix.lmbd)

# north_traj = north_liz_matrix.trajectory(initial_pop_vec, t_max=time_interval)
# north_plot = mpm.plot.trajectory(north_traj, second_order=True)
# north_plot.set(xlabel="Years", ylabel="Northern Lizard Population")
#
# south_traj = south_liz_matrix.trajectory(initial_pop_vec, t_max=time_interval)
# south_plot = mpm.plot.trajectory(south_traj, second_order=True)
# south_plot.set(xlabel="Years", ylabel="Southern Lizard Population")

north_stochastic = north_liz_matrix.stochastic_trajectories(initial_pop_vec, t_max=time_interval, reps=1000)
north_stab_plot = mpm.plot.multiple_trajectories(north_stochastic)
north_stab_plot.set(xlabel="Years", ylabel="Northern Lizard Population")

south_stochastic = south_liz_matrix.stochastic_trajectories(initial_pop_vec, t_max=time_interval, reps=1000)
south_stab_plot = mpm.plot.multiple_trajectories(south_stochastic)
south_stab_plot.set(xlabel="Years", ylabel="Southern Lizard Population")

# Show plots
# plt.show()
mpm.plot.show()
