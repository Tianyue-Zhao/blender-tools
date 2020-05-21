## Data access
### Locations
Objects are stored in bpy.data.objects.
Could by accessed by index or name.
**Example** bpy.data.objects['Cube']

**The Mesh Location** for an object is [object].data, which links to a mesh in bpy.data.meshes

### Mesh structure
[This page](https://docs.blender.org/api/current/bpy.types.Mesh.html) from Blender's Python API reference provides a good overview on the data structure of the Mesh.
Vertices, edges, loops, and polygons

A loop is like an edge with a direction. It contains a vertex index and an edge index. A series of loops "connect" with direction to form a path around the face.

Make a visualization of vertices, edges, loops, and polygons, in a sketch-blueprint style.

### Selection
[object].select_set(True/False) sets the selection for an object

## Mesh editing
bm.to_mesh([mesh]) exports the bmesh to a mesh
bm.faces.new([vertices]) creates a face
