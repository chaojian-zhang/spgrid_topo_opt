from topo_opt import TopoOpt
import taichi as tc

version = 1
narrow_band = True
volume_fraction = 0.08 # Initialize
n = 100
opt = TopoOpt(res=(n, n, n), version=version, volume_fraction=volume_fraction, max_iterations=25,
              grid_update_start=5 if narrow_band else 1000000,
              fix_cells_near_force=True, fixed_cell_density=0.1)

s = 0.1
tex = tc.Texture(
  'mesh',
  translate=(0.5, 0.5, 0.5),
  scale=(s, s, s),
  adaptive=False,
  filename='../data/chair.obj')

opt.populate_grid(domain_type='texture', tex_id=tex.id)
opt.general_action(action='voxel_connectivity_filtering')

# opt.add_plane_dirichlet_bc(axis_to_fix="xyz", axis_to_search=2, extreme=-1)
opt.add_customplane_dirichlet_bc(axis_to_fix="xyz", p0=(-0.1234312, -0.1000000, -0.1000000), p1=(-0.1234312, 0.1000000, -0.1000000), p2=(0.0678907, -0.1000000, -0.1000000))
opt.add_customplane_dirichlet_bc(axis_to_fix="xyz", p0=(-0.1234312, -0.1000000, -0.1000000), p1=(-0.1234312, 0.1000000, -0.1000000), p2=(0.0678907, -0.1000000, -0.1000000))
opt.add_customplane_load(force=(0, 0, -1), p0=(0.0678907, 0.1000000, 0.1000000), p1=(-0.1234312, -0.1000000, 0.1000000), p2=(0.0678907, -0.1000000, 0.1000000))
opt.add_customplane_load(force=(0, 0, -1), p0=(0.0678907, 0.1000000, 0.1000000), p1=(-0.1234312, 0.1000000, 0.1000000), p2=(-0.1234312, -0.1000000, 0.1000000))

# opt.general_action(action='add_precise_plane_force_bridge')
# Optimize
opt.run()
