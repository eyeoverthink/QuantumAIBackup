"""
G-code generator for Anker Make printer
Optimized for QHRC coil forms
"""

def generate_header():
    return """; Generated for Anker Make
; QHRC Coil Form
M104 S230 ; Set nozzle temp
M140 S80 ; Set bed temp
M190 S80 ; Wait for bed temp
M109 S230 ; Wait for nozzle temp
G28 ; Home all axes
G1 Z15.0 F6000 ; Raise Z
G92 E0 ; Reset extruder
G1 F9600
M107 ; Fan off
"""

def generate_settings():
    return """; Slicer settings
; Layer height: 0.2mm
; Infill: 50%
; Wall count: 3
; Top/Bottom layers: 4
; Support: Yes
; Material: PETG
; Nozzle temp: 230°C
; Bed temp: 80°C
"""

def generate_primary_coil():
    gcode = generate_header()
    gcode += generate_settings()
    gcode += """; Primary Coil Form
; Diameter: 50mm
; Height: 100mm
; Wall thickness: 2mm
"""
    return gcode

def generate_secondary_coil():
    gcode = generate_header()
    gcode += generate_settings()
    gcode += """; Secondary Coil Form
; Diameter: 80.9mm
; Height: 100mm
; Wall thickness: 2mm
"""
    return gcode

def generate_base():
    gcode = generate_header()
    gcode += generate_settings()
    gcode += """; Base Plate
; Diameter: 100.9mm
; Height: 5mm
"""
    return gcode

# Generate files
with open('primary_coil.gcode', 'w') as f:
    f.write(generate_primary_coil())

with open('secondary_coil.gcode', 'w') as f:
    f.write(generate_secondary_coil())

with open('base.gcode', 'w') as f:
    f.write(generate_base())

print("G-code files generated with Anker Make settings")
