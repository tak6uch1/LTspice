import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

file_path = 'pmosfet-iv.raw'
l = ltspice.Ltspice(file_path)
l.parse()

for i in range(l.case_count): # Iteration in simulation cases 
    V0 = l.get_data('V(N001)', i)
    I0 = l.get_data('I(V2)', i)
    plt.plot(V0, -I0)

plt.show()
