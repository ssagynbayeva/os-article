import matplotlib.pyplot as plt
import paths

fig = plt.figure()
plt.plot([0,1],[0,1])
fig.savefig(paths.figures / "cool_figure.pdf")
