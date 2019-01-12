def retrieve_tool_path(laser_path_gcode, software):
    if software == 'cura':
        laser_path_start = laser_path_end = 0
        for i in range(len(laser_path_gcode)):
            if laser_path_gcode[i].find("LAYER:0") != -1 and not laser_path_start:
                laser_path_start = i+1
            elif laser_path_gcode[i].find("ELAPSED") != -1:
                laser_path_end = i-1
                break
        if laser_path_start == 0 or laser_path_end == 0:
            raise RuntimeError('Error parsing source.gcode: could not find start and/or end')
        return laser_path_start, laser_path_end
    elif software == 'fusion' or software == 'fusion360':
        laser_path_start = laser_path_end = 0
        for i in range(len(laser_path_gcode)):
            if laser_path_gcode[i].find("M400") != -1 and not laser_path_start:
                laser_path_start = i+1
            elif laser_path_gcode[i].find("M400") != -1:
                laser_path_end = i-1
                break
        if laser_path_start == 0 or laser_path_end == 0:
            raise RuntimeError('Error parsing source.gcode: could not find start and/or end')
        return laser_path_start, laser_path_end


def laser_modulation(laser_path_gcode, software):
    if software == 'fusion' or software == 'fusion360':
        return laser_path_gcode
    else:
        raise RuntimeError("Software not supported yet")


def laser_height(laser_path_gcode, software, laser_focus_dist):
    if software == 'fusion' or software == 'fusion360':
        new_path = []
        new_path.append("G1 Z"+str(laser_focus_dist))
        new_path += laser_path_gcode
        for i in range(len(new_path)):
            new_path[i] = new_path[i].replace(" Z50.12 ", " ")
        return new_path
    else:
        raise RuntimeError('Software not supported yet')


def extruder_to_laser_conversion(laser_path_gcode):
    pass


def write_target_gcode(targer_gcode_file, tool_path, passes = 1, material_depth = 0):
    pass
