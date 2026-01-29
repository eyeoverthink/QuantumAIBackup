import numpy as np
from stl import mesh
from math import cos, sin, pi

def create_cylinder(radius, height, segments=100):
    # Create vertices for top and bottom circles
    vertices = []
    faces = []
    
    # Center points
    vertices.append([0, 0, 0])  # Bottom center
    vertices.append([0, 0, height])  # Top center
    
    # Create circle vertices
    for i in range(segments):
        angle = 2 * pi * i / segments
        x = radius * cos(angle)
        y = radius * sin(angle)
        # Bottom circle
        vertices.append([x, y, 0])
        # Top circle
        vertices.append([x, y, height])
    
    # Create faces
    for i in range(segments):
        # Bottom faces
        faces.append([0, 2+i*2, 2+((i+1)%segments)*2])
        # Top faces
        faces.append([1, 3+i*2, 3+((i+1)%segments)*2])
        # Side faces (two triangles per side)
        faces.append([2+i*2, 3+i*2, 2+((i+1)%segments)*2])
        faces.append([3+i*2, 3+((i+1)%segments)*2, 2+((i+1)%segments)*2])
    
    return np.array(vertices), np.array(faces)

# QHRC Constants
PHI = 1.618034
PRIMARY_DIAMETER = 50
SECONDARY_DIAMETER = PRIMARY_DIAMETER * PHI
HEIGHT = 100
WALL_THICKNESS = 2

# Create primary coil form
def create_primary_form():
    outer_verts, outer_faces = create_cylinder(PRIMARY_DIAMETER/2, HEIGHT)
    inner_verts, inner_faces = create_cylinder(PRIMARY_DIAMETER/2 - WALL_THICKNESS, HEIGHT)
    
    # Combine meshes
    vertices = np.vstack([outer_verts, inner_verts])
    faces = np.vstack([outer_faces, inner_faces + len(outer_verts)])
    
    # Create the mesh
    primary = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            primary.vectors[i][j] = vertices[f[j],:]
    
    return primary

# Create secondary coil form
def create_secondary_form():
    outer_verts, outer_faces = create_cylinder(SECONDARY_DIAMETER/2, HEIGHT)
    inner_verts, inner_faces = create_cylinder(SECONDARY_DIAMETER/2 - WALL_THICKNESS, HEIGHT)
    
    # Combine meshes
    vertices = np.vstack([outer_verts, inner_verts])
    faces = np.vstack([outer_faces, inner_faces + len(outer_verts)])
    
    # Create the mesh
    secondary = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            secondary.vectors[i][j] = vertices[f[j],:]
    
    return secondary

# Create base plate
def create_base():
    verts, faces = create_cylinder(SECONDARY_DIAMETER/2 + 10, 5)
    
    # Create the mesh
    base = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            base.vectors[i][j] = verts[f[j],:]
    
    return base

# Generate and save STL files
if __name__ == "__main__":
    # Create primary coil form
    primary = create_primary_form()
    primary.save('qhrc_primary_coil.stl')
    
    # Create secondary coil form
    secondary = create_secondary_form()
    secondary.save('qhrc_secondary_coil.stl')
    
    # Create base plate
    base = create_base()
    base.save('qhrc_base.stl')
    
    print("STL files generated successfully!")
    print(f"Primary coil diameter: {PRIMARY_DIAMETER}mm")
    print(f"Secondary coil diameter: {SECONDARY_DIAMETER}mm")
    print(f"Height: {HEIGHT}mm")
    print(f"Wall thickness: {WALL_THICKNESS}mm")
