# matplotlib2tikz3d
Convert 3D matplotlib Figures to Tikz code


Create Figure normally in Python: 

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, label='Trajetória', linestyle='solid')
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")
ax.set_xlim(-6, 26)
ax.set_zlim(0, 16)
ax.plot(x_d[0], y_d[0], z_d[0],  marker='o', linestyle=' ',label=rf'$s_p = ({x_d[0]},{y_d[0]},{z_d[0]})$')
ax.legend()
```

Convert the figure to tikz code using:

```python
from matplotlib2tikz3d import tikz3d
    
instance = tikz3d.Matplotlib3DLines2Tikz(fig, ax, "test_file.tex")
instance.save_code()
```

