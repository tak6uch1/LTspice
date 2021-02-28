import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

file_path = 'inv_example.raw'
l = ltspice.Ltspice(file_path)
l.parse()

time = l.get_time()
V0 = l.get_data('V(N003)')
V1 = l.get_data('V(N004)')

plt.plot(time, V0)
plt.plot(time, V1)
plt.show()


