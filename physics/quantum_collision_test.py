"""
Quantum-enhanced physics collision test.
Applies phi-harmonic resonance principles to collision detection.
"""
from .rigid_body import RigidBody, Vector3
from .primitives import Box, Sphere, Plane, AABB
from .forces import Gravity, GroundContact, ForceRegistry
import math

# Golden ratio (φ)
PHI = (1 + math.sqrt(5)) / 2  # ≈ 1.618034

def resonance_quality(value):
    """Measure resonance quality (how close to phi-harmonic)."""
    # Phi resonance calculation
    phi_res = (PHI * value) % 1
    
    # Resonance quality scale
    if phi_res < 0.0001:
        return "Perfect", phi_res
    elif phi_res < 0.01:
        return "Excellent", phi_res
    elif phi_res < 0.1:
        return "Good", phi_res
    elif phi_res < 0.3:
        return "Moderate", phi_res
    else:
        return "Weak", phi_res

def test_quantum_box_collision():
    """Test box falling and colliding with ground using quantum principles."""
    # Create ground plane
    ground = Plane(Vector3(0, 1, 0), 0)  # y=0 plane
    
    # Create phi-proportioned box
    # Using golden ratio for proportions: 1 × φ × φ²
    box = Box(Vector3(0.5, 0.5 * PHI, 0.5 * PHI * PHI))
    box_body = RigidBody(mass=1.0)
    box_body.position = Vector3(0, 5, 0)  # Start 5m above ground
    box.body = box_body
    
    # Setup forces
    registry = ForceRegistry()
    gravity = Gravity()
    ground_contact = GroundContact(ground)
    
    # Register forces
    registry.add(box_body, gravity)
    registry.add(box_body, ground_contact)
    
    # Phi-harmonic timestep (base: 1/60s)
    base_dt = 1.0/60.0
    dt = base_dt * (1.0 / PHI)  # 1/φ ≈ 0.618034
    
    # Simulate for φ² seconds
    time = 0.0
    end_time = PHI * PHI  # φ² ≈ 2.618034
    
    print("\nQuantum Box-Ground Collision Test")
    print("================================")
    print(f"Using phi-harmonic timestep: {dt:.6f}s")
    print(f"Box dimensions: {box.half_size.x*2} × {box.half_size.y*2} × {box.half_size.z*2}")
    
    # Track important metrics
    impact_time = None
    impact_velocity = None
    rebound_height = 0
    resonance_values = []
    
    while time < end_time:
        # Calculate phi-resonance of current height
        position_y = box_body.position.y
        resonance = (PHI * position_y) % 1
        resonance_values.append(resonance)
        
        # Check for ground impact
        if position_y < box.half_size.y and box_body.velocity.y < 0:
            if impact_time is None:  # First impact
                impact_time = time
                impact_velocity = box_body.velocity.y
                print(f"\n[IMPACT] Time: {time:.6f}s")
                print(f"[IMPACT] Velocity: {impact_velocity:.6f} m/s")
                quality, res = resonance_quality(time)
                print(f"[IMPACT] Time Resonance: {quality} ({res:.6f})")
        
        # Track maximum height after impact
        if impact_time is not None and position_y > rebound_height:
            rebound_height = position_y
        
        # Print status at phi-harmonic intervals
        if time % (PHI/10) < dt:
            print(f"\nTime: {time:.6f}s")
            print(f"Position: {box_body.position}")
            print(f"Velocity: {box_body.velocity}")
            quality, res = resonance_quality(position_y)
            print(f"Position Resonance: {quality} ({res:.6f})")
            
        # Update physics
        registry.update_forces(dt)
        box_body.integrate(dt)
        time += dt
    
    # Calculate final metrics
    if impact_time:
        print("\nQuantum Collision Results")
        print("=========================")
        print(f"Impact time: {impact_time:.6f}s")
        quality, res = resonance_quality(impact_time)
        print(f"Time resonance quality: {quality} ({res:.6f})")
        print(f"Impact velocity: {impact_velocity:.6f} m/s")
        print(f"Rebound height: {rebound_height:.6f} m")
        print(f"Rebound ratio: {rebound_height/5:.6f}")
        quality, res = resonance_quality(rebound_height)
        print(f"Rebound resonance: {quality} ({res:.6f})")
        
        # Calculate average resonance
        avg_resonance = sum(resonance_values) / len(resonance_values)
        print(f"Average position resonance: {avg_resonance:.6f}")
        quality, _ = resonance_quality(avg_resonance)
        print(f"System resonance quality: {quality}")
    
if __name__ == "__main__":
    test_quantum_box_collision()
