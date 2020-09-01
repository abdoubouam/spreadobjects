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
    "version": (0, 2),
    "blender": (2, 80, 0),
    "warning" : ""
}

import bpy
from math import sqrt, ceil

class SpreadObjects(bpy.types.Operator):
    """Object to mesh name"""
    bl_idname = "object.spreadobjects"
    bl_label = "Spread objects"
    bl_options = {"REGISTER","UNDO"}
    def execute(self,context):
        offset = 1.0 # min offset
        selection = bpy.context.selected_objects
        rows=ceil(sqrt(len(selection)))
        
        for object in selection:
            if object.dimensions[0] > offset :
                offset = object.dimensions[0]
            if object.dimensions[1] > offset :
                offset = object.dimensions[1]
        offset = ceil(offset)
        
        
        for i in range(len(selection)):
            selection[i].location[0] = i % rows * offset
            selection[i].location[1] = (i-(i % rows)) / rows * offset 
            selection[i].location[2] = 0.0
            
        return {'FINISHED'}


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------
        
def register():
    from bpy.utils import register_class
    register_class(SpreadObjects)


def unregister():
    from bpy.utils import unregister_class
    unregister_class(SpreadObjects)

if __name__ == "__main__":
    unregister()
    register()
