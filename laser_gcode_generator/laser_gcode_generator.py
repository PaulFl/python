import configparser
import gcode_functions


config = configparser.ConfigParser()
config.read('config.ini')

laser_config = config['Laser']
material_config = config['Material']
files_config = config['Files']

laser_focus_dist = int(laser_config['focusDistance'])

material_passes = int(material_config['passes'])
material_depth = int(material_config['depth'])

source_gcode_path = files_config['gcode']
target_gcode_path = files_config['target']
software_gcode = files_config['source']


source_gcode = open(source_gcode_path, 'r')
target_gcode = open(target_gcode_path, 'w')

laser_path_gcode = source_gcode.readlines()

(laser_path_start, laser_path_end) = gcode_functions.retrieve_tool_path(laser_path_gcode, software_gcode)


laser_path_gcode = laser_path_gcode[laser_path_start:laser_path_end+1]

laser_path_gcode = gcode_functions.laser_modulation(laser_path_gcode, software_gcode)

laser_path_gcode = gcode_functions.laser_height(laser_path_gcode, software_gcode, laser_focus_dist)

laser_full_path_gcode = gcode_functions.full_path_generator