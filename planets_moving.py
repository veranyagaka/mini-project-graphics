# Planetmove.py
from vpython import rate, mag, color, sphere, vector, keysdown , random
from planet import create_planets

# Retrieve Earth and Mars from planet module
scene, earth, mars = create_planets()

# Set initial conditions for collision
earth.mass = 1  # Assign masses for collision calculation
mars.mass = 1.5
earth.velocity = vector(0.1, 0, 0)
mars.velocity = vector(-0.1, 0, 0)

# Calculate the collision threshold
collision_distance = earth.radius + mars.radius

# Define a variable to control the paused state
is_paused = False

# Function to toggle pause on space key press
def toggle_pause(event):
    global is_paused
    if event.key == ' ':  # Check if the space bar is pressed
        is_paused = not is_paused

# Bind the toggle_pause function to keydown events
scene.bind('keydown', toggle_pause)

# Fragmentation parameters
num_fragments = 100  # Number of fragments to create upon collision
fragment_speed = 0.1  # Initial speed of each fragment


# Animation loop
while True:
    rate(60)
    
    # Skip updating positions if paused
    if is_paused:
        continue
    
    # Update positions based on velocity
    earth.pos += earth.velocity * 0.01
    mars.pos += mars.velocity * 0.01

     # Check for collision
    if mag(earth.pos - mars.pos) <= collision_distance:
        # Set the collision point and calculate properties for fragments
        collision_point = (earth.pos + mars.pos) / 2

        # Generate fragments upon collision
        fragments = []
        for _ in range(num_fragments):
            # Assign random directions to fragments
            random_direction = vector(
                random() - 0.5,  # Random X direction
                random() - 0.5,  # Random Y direction
                random() - 0.5   # Random Z direction
            ).norm()  # Normalize to ensure uniform speed
            
            fragment_velocity = random_direction * fragment_speed

            # Create a fragment with a smaller radius and initial position
            fragment = sphere(
                pos=collision_point,
                radius=0.1,  # Smaller radius for each fragment
                color=color.blue
            )
            fragment.velocity = fragment_velocity
            fragments.append(fragment)

        # Hide Earth and Mars after collision
        earth.visible = False
        mars.visible = False

        # Move fragments outward
        while True:
            rate(10)  # Control the speed of fragment animation
            if is_paused:
                continue  # Skip updates if paused
            
            for fragment in fragments:
                fragment.pos += fragment.velocity  # Update fragment positions
            # Optionally: Add a condition to stop the loop after some time or distance
        break

'''# Check for collision
    if mag(earth.pos - mars.pos) <= collision_distance:
        new_mass = earth.mass + mars.mass
        new_radius = (earth.radius ** 3 + mars.radius ** 3) ** (1 / 3)
        new_position = (earth.mass * earth.pos + mars.mass * mars.pos) / new_mass
        new_velocity = (earth.mass * earth.velocity + mars.mass * mars.velocity) / new_mass
        
        # Create merged planet
        merged_planet = sphere(pos=new_position, radius=new_radius, color=color.orange, make_trail=True)
        merged_planet.velocity = new_velocity

        earth.visible = False
        mars.visible = False
        break'''
