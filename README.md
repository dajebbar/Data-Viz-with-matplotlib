# Data-Viz-with-matplotlib

Making beautiful data representations with matplotlib

## Plotting a Simple Line Graph

We first import the **_pyplot_** module using the alias plt:

```python
import matplotlib.pyplot as plt
```

We create a list called cubes to hold the data that we’ll plot. Then we follow another common Matplotlib convention by calling the subplots() function:

```python
cubes = [1, 8, 27, 64, 125]
fig, ax = plt.subplots()
```

This function can generate one or more plots in the same fig­ure.
The variable fig represents the entire figure or collection of plots that are generated. The variable ax represents a single plot in the figure and is the variable we’ll use most of the time.

We then use the plot() method, which will try to plot the data it’s given in a meaningful way:

```python
ax.plot(cubes)
```

The function plt.show() opens Matplotlib’s viewer and displays the plot:
![cubes plot](plots/cube_plot.png)
