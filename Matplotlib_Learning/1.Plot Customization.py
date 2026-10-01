import matplotlib.pyplot as plt

import numpy as np

x  = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

line_style = dict (marker = '.',
                   markersize = 15,
                   markerfacecolor = '#fcfcfc',
                   markeredgecolor = '#030303',
                   linestyle = 'solid',
                   linewidth = 2)

plt.title ('Class Size', fontsize = 20,
                         family = 'Times New Roman',
                         fontweight = 'bold',
                         color = '#030303'
                         )

plt.xlabel ('Year',      fontsize = 13,
                         family = 'Arial',
                         fontweight = 'bold',
                         color = "#030303"
                         )

plt.ylabel ('Students',  fontsize = 13,
                         family = 'Arial',
                         fontweight = 'bold',
                         color = "#030303"
                         )

plt.tick_params (axis = 'both',
                 colors = "#D50000")

plt.plot (x, y1, color = '#609cfc', **line_style)

plt.plot (x, y2, color = '#56fc82', **line_style)

plt.plot (x, y3, color = '#fc9265', **line_style)

plt.xticks (x)

plt.show ()