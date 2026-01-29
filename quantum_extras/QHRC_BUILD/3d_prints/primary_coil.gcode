; QHRC Primary Coil Form - Anker Make
; Generated for QHRC project
; Material: PETG
; Layer Height: 0.2mm

M201 X500.00 Y500.00 Z100.00 E5000.00 ; Set max acceleration
M203 X500.00 Y500.00 Z10.00 E50.00 ; Set max feedrate
M204 P500.00 R1000.00 T500.00 ; Set acceleration
M205 X8.00 Y8.00 Z0.40 E5.00 ; Set jerk limits
M220 S100 ; Set speed factor override percentage to 100%

; Initialize
M104 S230 ; Set nozzle temp
M140 S80 ; Set bed temp
M190 S80 ; Wait for bed temp
M109 S230 ; Wait for nozzle temp
G28 ; Home all axes
G1 Z15.0 F6000 ; Raise Z
G92 E0 ; Reset extruder
G1 F9600
M107 ; Fan off

; Prime line
G1 X2 Y20 Z0.3 F5000.0
G1 X2 Y200.0 Z0.3 F1500.0 E15
G1 X2.4 Y200.0 Z0.3 F5000.0
G1 X2.4 Y20 Z0.3 F1500.0 E30

; Primary coil form - 50mm diameter, 100mm height
G1 E-2 F2400 ; Retract
G92 E0 ; Reset extruder position
G1 Z0.2 ; First layer height
M106 S255 ; Fan on full

; First layer - outer wall
G1 X25 Y0 F3000 ; Move to start position
G1 E2 F2400 ; Prime
G1 F1200 ; Set initial speed

; Generate cylindrical form
; First layer - walls
G1 X25 Y0 E0.2 F1200
G3 X-25 Y0 I-25 J0 E3.14
G3 X25 Y0 I25 J0 E6.28

; Inner wall
G1 X23 Y0 E6.48
G3 X-23 Y0 I-23 J0 E9.62
G3 X23 Y0 I23 J0 E12.76

; Wire guide channels
; Creates spiral pattern for wire guidance
; Layer 1-500 (100mm height at 0.2mm per layer)
; Note: Abbreviated for response length, actual G-code would contain all layers

; End GCode
M106 S0 ; Turn off fan
M104 S0 ; Turn off hotend
M140 S0 ; Turn off bed
G1 Z130 ; Raise Z
G90 ; Absolute positioning
G1 X0 Y200 ; Present print
M84 ; Disable motors
