'''
Copyright (C) 2019 Matthias Patscheider
patscheider.matthias@gmail.com

Created by Matthias Patscheider

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# support reloading sub-modules
if "bpy" in locals():
    import importlib

    importlib.reload(add_suffix_panel)
    importlib.reload(operators)
    importlib.reload(preferences)
    importlib.reload(ui)
    # importlib.reload(validation)
    importlib.reload(variable_replacer)

else:
    from . import add_suffix_panel
    from . import operators
    from . import preferences
    from . import ui
    # from . import validation
    from . import variable_replacer

# import standard modules
import bpy


def menu_add_suffix(self, context):
    self.layout.operator(VIEW3D_OT_add_suffix.bl_idname)  # or YourClass.bl_idname

    from .preferences.renaming_preferences import update_panel_category
    update_panel_category(None, bpy.context)


def register():
    add_suffix_panel.register()
    operators.register()
    ui.register()
    # validation.register()

    # keymap and preferences should be last
    preferences.register()


def unregister():
    # keymap and preferences should be last
    preferences.unregister()

    # validation.unregister()
    ui.unregister()
    operators.unregister()
    add_suffix_panel.unregister()


if __name__ == "__main__":
    register()
