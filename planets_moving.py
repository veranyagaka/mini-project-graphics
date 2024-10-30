# Planetmove.py
from vpython import rate, mag, color, sphere, vector, keysdown
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
        new_mass = earth.mass + mars.mass
        new_radius = (earth.radius ** 3 + mars.radius ** 3) ** (1 / 3)
        new_position = (earth.mass * earth.pos + mars.mass * mars.pos) / new_mass
        new_velocity = (earth.mass * earth.velocity + mars.mass * mars.velocity) / new_mass
        
        # Create merged planet
        merged_planet = sphere(pos=new_position, radius=new_radius, color=color.orange, make_trail=True)
        merged_planet.velocity = new_velocity

        earth.visible = False
        mars.visible = False
        break
