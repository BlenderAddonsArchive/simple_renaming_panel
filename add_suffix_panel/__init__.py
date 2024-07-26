import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
)

from . import renaming_sufPre_operators


def tChange(self, context):
    wm = bpy.context.scene

    # The print function works fine
    naming_preset = context.scene.renaming_presetNaming
    name_var = ""

    # System and Global Values
    if naming_preset == 'FILE':
        name_var = "@f"
    if naming_preset == "DATE":
        name_var = "@d"
    if naming_preset == "TIME":
        name_var = "@i"
    if naming_preset == "RANDOM":
        name_var = "@r"

    # UserStrings
    if naming_preset == "HIGH":
        name_var = "@h"
    if naming_preset == "LOW":
        name_var = "@l"
    if naming_preset == "CAGE":
        name_var = "@b"
    if naming_preset == "USER1":
        name_var = "@u1"
    if naming_preset == "USER2":
        name_var = "@u2"
    if naming_preset == "USER3":
        name_var = "@u3"
    if naming_preset == "NUMERATE":
        name_var = "@n"

    if wm.renaming_object_types == 'OBJECT':
        if naming_preset == 'OBJECT':
            name_var = "@o"
        if naming_preset == "TYPE":
            name_var = "@t"
        if naming_preset == "PARENT":
            name_var = "@p"
        if naming_preset == "ACTIVE":
            name_var = "@a"
        if naming_preset == "COLLECTION":
            name_var = "@c"
        if naming_preset == "DATA":
            name_var = "@m"

    context.scene.renaming_newName += str(name_var)
    return


classes = (
    renaming_sufPre_operators.VIEW3D_OT_add_type_suf_pre,
)

enumPresetItems = [('FILE', "File", "", '', 1),
                   ('OBJECT', "Object", "", '', 2),
                   ('HIGH', "High", "", '', 4),
                   ('LOW', "Low", "", '', 8),
                   ('CAGE', "Cage", "", '', 16),
                   ('DATE', "Date", "", '', 32),
                   ('TIME', "Time", "", '', 128),
                   ('TYPE', "Type", "", '', 1024),
                   ('PARENT', "Parent", "", '', 2048),
                   ('ACTIVE', "Active", "", '', 4096),
                   ('USER1', "User1", "", '', 8192),
                   ('USER2', "User2", "", '', 256),
                   ('USER3', "User3", "", '', 512),
                   ('NUMBER', "Number", "", '', 1024),
                   ('DATA', "Data", "", '', 2048),
                   ]

enumObjectTypesExt = [('EMPTY', "", "Rename empty objects", 'OUTLINER_OB_EMPTY', 1),
                      ('MESH', "", "Rename mesh objects", 'OUTLINER_OB_MESH', 2),
                      ('CAMERA', "", "Rename Camera objects", 'OUTLINER_OB_CAMERA', 4),
                      ('LIGHT', "", "Rename light objects", 'OUTLINER_OB_LIGHT', 8),
                      ('ARMATURE', "", "Rename armature objects", 'OUTLINER_OB_ARMATURE', 16),
                      ('LATTICE', "", "Rename lattice objects", 'OUTLINER_OB_LATTICE', 32),
                      ('CURVE', "", "Rename curve objects", 'OUTLINER_OB_CURVE', 64),
                      ('SURFACE', "", "Rename surface objects", 'OUTLINER_OB_SURFACE', 128),
                      ('TEXT', "", "Rename text objects", 'OUTLINER_OB_FONT', 256),
                      ('GPENCIL', "", "Rename greace pencil objects", 'OUTLINER_OB_GREASEPENCIL', 512),
                      ('METABALL', "", "Rename metaball objects", 'OUTLINER_OB_META', 2048),
                      ('COLLECTION', "", "Rename collections", 'GROUP', 4096),
                      ('BONE', "", "", 'BONE_DATA', 8192), ]


def register():
    id_store = bpy.types.Scene

    # Type Suffix Prefix
    id_store.type_pre_sub_only_selection = BoolProperty(
        name="Selected Objects",
        description="Rename Selected Objects",
        default=True,
    )

    id_store.renaming_suffix_prefix_types_specified = EnumProperty(name="Object Types",
                                                                   items=enumObjectTypesExt,
                                                                   description="Which kind of object to rename",
                                                                   options={'ENUM_FLAG'},
                                                                   default={'CURVE', 'LATTICE', 'SURFACE', 'METABALL',
                                                                            'MESH',
                                                                            'ARMATURE', 'LIGHT', 'CAMERA', 'EMPTY',
                                                                            'GPENCIL',
                                                                            'TEXT', 'BONE', 'COLLECTION'}
                                                                   )

    id_store.renaming_suffix_prefix_material = StringProperty(name='Material', default='')
    id_store.renaming_suffix_prefix_geometry = StringProperty(name='Geometry', default='')
    id_store.renaming_suffix_prefix_empty = StringProperty(name="Empty", default='')
    id_store.renaming_suffix_prefix_group = StringProperty(name="Group", default='')
    id_store.renaming_suffix_prefix_curve = StringProperty(name="Curve", default='')
    id_store.renaming_suffix_prefix_armature = StringProperty(name="Armature", default='')
    id_store.renaming_suffix_prefix_lattice = StringProperty(name="Lattice", default='')
    id_store.renaming_suffix_prefix_data = StringProperty(name="Data", default='')
    id_store.renaming_suffix_prefix_data_02 = StringProperty(name="Data = Objectname + ", default='')
    id_store.renaming_suffix_prefix_surfaces = StringProperty(name="Surfaces", default='')
    id_store.renaming_suffix_prefix_cameras = StringProperty(name="Cameras", default='')
    id_store.renaming_suffix_prefix_lights = StringProperty(name="Lights", default='')
    id_store.renaming_suffix_prefix_collection = StringProperty(name="Collections", default='')
    id_store.renaming_suffix_prefix_text = StringProperty(name="Text", default='')
    id_store.renaming_suffix_prefix_gpencil = StringProperty(name="Grease Pencil", default='')
    id_store.renaming_suffix_prefix_metaball = StringProperty(name="Metaballs", default='')
    id_store.renaming_suffix_prefix_bone = StringProperty(name="Bones", default='')
    id_store.renaming_suffix_prefix_speakers = StringProperty(name="Speakers", default='')
    id_store.renaming_suffix_prefix_lightprops = StringProperty(name="LightProps", default='')

    id_store.renaming_inputContext = StringProperty(name="LightProps", default='')

    # Pro Features
    id_store.renaming_presetNaming = EnumProperty(name="Object Types",
                                                  items=enumPresetItems,
                                                  description="Which kind of object to rename",
                                                  update=tChange
                                                  )

    id_store.renaming_presetNaming1 = EnumProperty(name="Object Types",
                                                   items=enumPresetItems,
                                                   description="Which kind of object to rename",
                                                   update=tChange
                                                   )

    id_store.renaming_presetNaming2 = EnumProperty(name="Object Types",
                                                   items=enumPresetItems,
                                                   description="Which kind of object to rename",
                                                   update=tChange
                                                   )

    id_store.renaming_presetNaming3 = EnumProperty(name="Object Types",
                                                   items=enumPresetItems,
                                                   description="Which kind of object to rename",
                                                   update=tChange
                                                   )

    id_store.renaming_presetNaming4 = EnumProperty(name="Object Types",
                                                   items=enumPresetItems,
                                                   description="Which kind of object to rename",
                                                   update=tChange
                                                   )

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)

    id_store = bpy.types.Scene

    del id_store.renaming_suffix_prefix_material
    del id_store.renaming_suffix_prefix_geometry
    del id_store.renaming_suffix_prefix_empty
    del id_store.renaming_suffix_prefix_group
    del id_store.renaming_suffix_prefix_curve
    del id_store.renaming_suffix_prefix_armature
    del id_store.renaming_suffix_prefix_lattice
    del id_store.renaming_suffix_prefix_data
    del id_store.renaming_suffix_prefix_data_02
    del id_store.renaming_start_number

    del id_store.renaming_suffix_prefix_lights
    del id_store.renaming_suffix_prefix_cameras
    del id_store.renaming_suffix_prefix_surfaces
    del id_store.renaming_suffix_prefix_bone
    del id_store.renaming_suffix_prefix_collection
    del id_store.renaming_object_types_specified
    del id_store.renaming_suffix_prefix_speakers
    del id_store.renaming_suffix_prefix_lightprops
