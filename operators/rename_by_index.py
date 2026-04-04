import time

import bpy

from ..operators.renaming_utilities import call_renaming_popup, call_error_popup, log_timing

INDEXED_TYPES = ('UVMAPS', 'COLORATTRIBUTES', 'ATTRIBUTES', 'VERTEXGROUPS', 'SHAPEKEYS')

_accessor_map = {
    'UVMAPS':          lambda obj: obj.data.uv_layers,
    'COLORATTRIBUTES': lambda obj: obj.data.color_attributes,
    'ATTRIBUTES':      lambda obj: obj.data.attributes,
    'VERTEXGROUPS':    lambda obj: obj.vertex_groups,
    'SHAPEKEYS':       lambda obj: obj.data.shape_keys.key_blocks if obj.data and obj.data.shape_keys else [],
}


class VIEW3D_OT_rename_by_index(bpy.types.Operator):
    bl_idname = "renaming.rename_by_index"
    bl_label = "Rename Slot"
    bl_description = "Rename the item at the specified index on each selected object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        target_index = scene.renaming_index_target
        new_name = scene.renaming_index_new_name
        entity_type = scene.renaming_object_types
        msg = scene.renaming_messages

        if not new_name:
            error_msg = scene.renaming_error_messages
            error_msg.add_message("Name field is empty")
            call_error_popup(context)
            return {'CANCELLED'}

        get_collection = _accessor_map.get(entity_type)
        if get_collection is None:
            return {'CANCELLED'}

        obj_list = context.selected_objects.copy() if scene.renaming_only_selection else list(bpy.data.objects)

        t_start = time.perf_counter()
        renamed = 0
        for obj in obj_list:
            if obj.type != 'MESH':
                continue
            try:
                items = list(get_collection(obj))
                if target_index < len(items):
                    item = items[target_index]
                    old_name = item.name
                    item.name = new_name
                    msg.add_message(old_name, item.name)
                    renamed += 1
            except Exception as e:
                self.report({'WARNING'}, f"Skipped {obj.name}: {e}")
                continue

        log_timing(context, "rename_by_index", t_start, renamed)
        call_renaming_popup(context)
        return {'FINISHED'}
