import bpy
#Example of setting the cursor position
#and moving objects to cursor.
bpy.ops.object.origin_set(type="ORIGIN_CENTER_OF_VOLUME")
original_selected = bpy.context.selected_objects

set_z = 0
for i in range(len(original_selected)):
    original_selected[i].select_set(False)
for i in range(len(original_selected)):
    original_selected[i].select_set(True)
    bpy.context.scene.cursor.location = original_selected[i].location
    bpy.context.scene.cursor.location.z = set_z
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    original_selected[i].select_set(False)
