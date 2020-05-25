import bpy
import bmesh
import numpy
import math

def plot_function(x, y):
    return math.sqrt(x**2+y**2-1.5*x*y)

#The plotting parameters
x_range = [-2,2]
y_range = [-2,2]
increment = 0.1

num_x = int((x_range[1]-x_range[0])/increment)
num_y = int((y_range[1]-y_range[0])/increment)

#Make the vertices
bmesh_object = bmesh.new()
for i in range(num_x):
    for k in range(num_y):
        cur_x = x_range[0]+i*increment
        cur_y = y_range[0]+k*increment
        cur_z = plot_function(cur_x, cur_y)
        bmesh.ops.create_vert(bmesh_object, co=(cur_x, cur_y, cur_z))
bmesh_object.verts.ensure_lookup_table()

#Add the faces
for i in range(num_x-1):
    for k in range(num_y-1):
        vert_list = bmesh_object.verts
        vert_list = [vert_list[i*num_y+k], vert_list[i*num_y+k+1],\
            vert_list[(i+1)*num_y+k+1], vert_list[(i+1)*num_y+k]]
        bmesh_object.faces.new(vert_list)

#Make the object
plot_mesh = bpy.data.meshes.new("plot_mesh")
bmesh_object.to_mesh(plot_mesh)
plot_object = bpy.data.objects.new("plot_object", plot_mesh)
bpy.context.collection.objects.link(plot_object)
