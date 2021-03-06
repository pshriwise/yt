import yt

ds = yt.load_sample("IsolatedGalaxy")

fields = ['density', 'velocity_x', 'velocity_y', 'velocity_magnitude']
p = yt.SlicePlot(ds, 'z', fields)
p.set_log('velocity_x', False)
p.set_log('velocity_y', False)

# this returns a matplotlib figure with an ImageGrid and the slices
# added to the grid of axes (in this case, 2x2)
fig = p.export_to_mpl_figure((2,2))

fig.tight_layout()

fig.savefig("multiplot_export_to_mpl.png")

