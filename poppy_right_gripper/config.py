import poppy_right_gripper as prg
import inspect
import platform

# Get the location of the module __init__.py file
initpath = inspect.getfile(prg)

# Extract the root path with the folder tree separator corresponding to the current system
sep = '\\' if (platform.system() == 'Windows') else '/'
rootpath = initpath[:(initpath.rfind(sep) + 1)]

# Get the full path to
JSONpath_full = rootpath + 'configuration' + sep + 'poppy_right_gripper_full.json'
JSONpath_noclamp = rootpath + 'configuration' + sep + 'poppy_right_gripper_noclamp.json'
URDFpath_full = rootpath + 'configuration' + sep + 'poppy_right_gripper_full.urdf'
URDFpath_noclamp = rootpath + 'configuration' + sep + 'poppy_right_gripper_noclamp.urdf'