M117 Initialisation...
M107          ;Laser/Fan OFF
G21           ;Metric Values
G17           ;Plane XY
G90           ;Absolute Positioning
G92 X0 Y0 Z0  ;Set XYZ Positions
G0 F2500
G28 X         ;Home X
G28 Y         ;Home Y
G0 Z50 F300    ;Position Z

M400