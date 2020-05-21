import bpy
import mathutils
#Script that operates on all currently selected objects
#Sets object origin to center of mesh volume,
#and then sets the z-axis of the object origin to the specified value.
bpy.ops.object.origin_set(type="ORIGIN_CENTER_OF_VOLUME")
original_selected = bpy.context.selected_objects

set_z = 0.06452800333499908
for i in range(len(original_selected)):
    original_selected[i].data.transform(mathutils.Matrix.Translation((0,0,
        (original_selected[i].location.z-set_z)/original_selected[i].scale.z)))
    original_selected[i].location.z = set_z
