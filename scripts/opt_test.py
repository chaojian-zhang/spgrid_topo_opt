from topo_opt import TopoOpt
import taichi as tc

# Change log
# v1 Initial commit
# v2 correct BC and plane wing force

# import crash_report
# crash_report.enable()

version = 1
narrow_band = True
volume_fraction = 0.08 # Initialize
n = 75
opt = TopoOpt(res=(n, n, n), version=version, volume_fraction=volume_fraction, max_iterations=20,
              grid_update_start=5 if narrow_band else 1000000,
              fix_cells_near_force=True, fixed_cell_density=0.1)

s = 0.1
tex = tc.Texture(
  'mesh',
  translate=(0.5, 0.5, 0.5),
  scale=(s, s, s),
  adaptive=False,
  filename='/home/holycow/cyl_ti.obj')

opt.populate_grid(domain_type='texture', tex_id=tex.id)
opt.general_action(action='voxel_connectivity_filtering')

opt.add_plane_dirichlet_bc(axis_to_fix="xyz", axis_to_search=2, extreme=-1)
opt.add_customplane_load(force=(0, 0, -1))

# opt.general_action(action='add_precise_plane_force_bridge')
# Optimize
opt.run()
