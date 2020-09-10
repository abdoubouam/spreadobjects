# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****


bl_info = {
    "name": "Spread objects on an evenly spaced grid",
    "category": "Object",
    "author": "Abdou Bouam",
    "version": (0, 3),
    "blender": (2, 80, 0),
    "warning" : ""
}

import bpy
from bpy.types import (
        Operator,
        Menu,
        Panel,
        PropertyGroup,
        AddonPreferences,
        )
from math import sqrt, ceil

class VIEW3D_MT_object_spreadobjects(Menu):
    bl_label = "Spread Objects"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.spread_objects", text="Spread Objects")
        
def menu_function(self, context):
    self.layout.operator("object.spread_objects", text="Spread Objects")
    self.layout.operator("object.spread_objects_keyframed", text="Spread Objects (keyframed)")
    
    #self.layout.menu("VIEW3D_MT_object_spreadobjects")
    #debug
def spread(self,context,keyframed=False):
    offset = 1.0 # min offset
    selection = bpy.context.selected_objects
    rows=ceil(sqrt(len(selection)))
    current_frame = bpy.context.scene.frame_current
    
    for object in selection:
        if keyframed:
            object.keyframe_insert("location", frame = current_frame)
        if object.dimensions[0] > offset :
            offset = object.dimensions[0]
        if object.dimensions[1] > offset :
            offset = object.dimensions[1]
    offset = ceil(offset)
    
    
    for i in range(len(selection)):
        selection[i].location[0] = i % rows * offset
        selection[i].location[1] = (i-(i % rows)) / rows * offset 
        selection[i].location[2] = 0.0
        if keyframed:
            selection[i].keyframe_insert("location", frame = current_frame+1)
    if keyframed:
        bpy.context.scene.frame_current = current_frame + 1


class SpreadObjects(bpy.types.Operator):
    """Object to mesh name"""
    bl_idname = "object.spread_objects"
    bl_label = "Spread objects"
    bl_options = {"REGISTER","UNDO"}
    def execute(self,context):
        spread(self,context,keyframed=False)
        return {'FINISHED'}

class SpreadObjectsKeyframed(bpy.types.Operator):
    """Object to mesh name"""
    bl_idname = "object.spread_objects_keyframed"
    bl_label = "Spread objects"
    bl_options = {"REGISTER","UNDO"}
    def execute(self,context):
        spread(self,context,keyframed=True)
        return {'FINISHED'}


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------
        
def register():
    from bpy.utils import register_class
    register_class(VIEW3D_MT_object_spreadobjects)
    register_class(SpreadObjectsKeyframed)
    register_class(SpreadObjects)
    bpy.types.VIEW3D_MT_object.append(menu_function)    
    
    


def unregister():
    from bpy.utils import unregister_class
    unregister_class(VIEW3D_MT_object_spreadobjects)
    unregister_class(SpreadObjectsKeyframed)
    unregister_class(SpreadObjects)
    bpy.types.VIEW3D_MT_object.remove(menu_function)    
    

if __name__ == "__main__":
    unregister()
    register()
