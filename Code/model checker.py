import bpy
import re
import bmesh
from mathutils import Vector

pattern = re.compile(r'\.\d{3}$')

invalid_names = []
error_count = 0

#Naming Convention Check
for obj in bpy.context.scene.objects:
    if pattern.search(obj.name):
        invalid_names.append(obj.name)
        obj.select_set(True)
        error_count += 1

if invalid_names:
    print(f'Naming check completed. Issues found: {error_count}')
    print(f'[Maming Error] ' + ', '.join(invalid_names))
else:
    print('Naming check completed. No issues found')
    
#Transform Validation
transform_names = []
for obj in bpy.data.objects:
    if obj.location.length > 0.0001:
        transform_names.append(obj.name)
        obj.select_set(True)
        error_count += 1

if transform_names:   
    print(f'[Transform Error] ' + ', '.join(transform_names))
    print(f'Transform check completed. Issues found: {error_count}')
else:
    print('Transform check completed. No issues found')

#Normals Check
obj = bpy.context.active_object

if obj and obj.type == 'MESH' and bpy.context.mode == 'EDIT_MESH':
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    print(f'[Normals Check] {obj.name}: normals recalculated')
    
#UV Overlapping Check
obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    if obj.data.uv_layers:
        print(f'[UV Check] {obj.name}: UVs detected')
    else:
        print(f'[UV Check] {obj.name}: NO UVs found')
else:
    print('[UV Check] No active mesh object')