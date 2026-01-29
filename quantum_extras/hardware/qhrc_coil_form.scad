// QHRC Coil Form Design
// Based on Patent #19/071,497 specifications

// Constants
PHI = 1.618034;  // Golden ratio
PRIMARY_DIAMETER = 50;  // mm
SECONDARY_DIAMETER = PRIMARY_DIAMETER * PHI;  // mm
WALL_THICKNESS = 2;  // mm
HEIGHT = 100;  // mm
WIRE_CHANNEL = 1;  // mm

// Primary Coil Form
module primary_form() {
    difference() {
        cylinder(h=HEIGHT, d=PRIMARY_DIAMETER, center=true);
        cylinder(h=HEIGHT+1, d=PRIMARY_DIAMETER-WALL_THICKNESS*2, center=true);
        
        // Wire guide channels
        for(i=[0:HEIGHT/WIRE_CHANNEL]) {
            translate([0,0,-HEIGHT/2+i*WIRE_CHANNEL])
            rotate_extrude()
            translate([PRIMARY_DIAMETER/2-WALL_THICKNESS/2,0,0])
            circle(d=WIRE_CHANNEL);
        }
    }
}

// Secondary Coil Form
module secondary_form() {
    difference() {
        cylinder(h=HEIGHT, d=SECONDARY_DIAMETER, center=true);
        cylinder(h=HEIGHT+1, d=SECONDARY_DIAMETER-WALL_THICKNESS*2, center=true);
        
        // Wire guide channels
        for(i=[0:HEIGHT/WIRE_CHANNEL]) {
            translate([0,0,-HEIGHT/2+i*WIRE_CHANNEL])
            rotate_extrude()
            translate([SECONDARY_DIAMETER/2-WALL_THICKNESS/2,0,0])
            circle(d=WIRE_CHANNEL);
        }
    }
}

// Base plate
module base_plate() {
    cylinder(h=5, d=SECONDARY_DIAMETER+20, center=false);
}

// Final Assembly
translate([0,0,HEIGHT/2+5]) {
    color("blue") primary_form();
    color("red") secondary_form();
}
color("gray") base_plate();
