from vpython import *

# Create a 3D scene
scene = canvas(width=1280, height=720)


# Create Earth
earth = sphere(pos=vector(-3.0, 0, 0), radius=1.2, texture=textures.earth)

# Create Mars with a valid texture
mars_texture = textures.wood_old if 'wood_old' in dir(textures) else textures.earth
mars_color = vector(1, 0.647, 0)  # RGB for orange
mars = sphere(pos=vector(3.0, 0, 0), radius=0.7, texture=mars_texture, color=mars_color)  # Mars is smaller than Earth

# Set the rotation speed
rotation_speed = 0.1  # Adjusted to a more reasonable speed

# Run the 3D animation
while True:
    rate(60)  # Limit the loop to 60 iterations per second
    # Rotate the Earth
    earth.rotate(angle=rotation_speed, axis=vector(0, 1, 0))
    # Rotate Mars in the opposite direction for variation
    mars.rotate(angle=-rotation_speed - 0.05, axis=vector(0, 1, 0))  # Rotate Mars in the opposite direction