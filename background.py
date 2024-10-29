import math
import cairo
import random

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

def draw_nebula(context):
    for _ in range(3):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(150, 300)

        # Random nebula colors
        r, g, b = random.uniform(0.2, 0.8), random.uniform(0.2, 0.5), random.uniform(0.5, 1.0)
        gradient = cairo.RadialGradient(x, y, radius * 0.1, x, y, radius)
        gradient.add_color_stop_rgba(0, r, g, b, 0.2)
        gradient.add_color_stop_rgba(1, 0, 0, 0, 0)

        context.set_source(gradient)
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.fill()

def draw_stars(context, num_stars):
    for _ in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.uniform(0.5, 1.5)
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.set_source_rgb(1, 1, 1)
        context.fill()

# Adding shooting stars
def draw_shooting_stars(context, num_shooting_stars):
    for _ in range(num_shooting_stars):
        x_start = random.randint(0, WIDTH)
        y_start = random.randint(0, HEIGHT)
        length = random.randint(20, 50)
        angle = random.uniform(-math.pi / 4, math.pi / 4)

        x_end = x_start + length * math.cos(angle)
        y_end = y_start + length * math.sin(angle)

        context.set_source_rgba(1, 1, 1, 0.7)
        context.set_line_width(1.5)
        context.move_to(x_start, y_start)
        context.line_to(x_end, y_end)
        context.stroke()

# Draw a galactic glow around the sphere (planet)
def draw_galactic_glow(context, center_x, center_y, radius):
    glow_radius = radius * 2
    gradient = cairo.RadialGradient(center_x, center_y, radius, center_x, center_y, glow_radius)
    gradient.add_color_stop_rgba(0, 1, 1, 1, 0.1)
    gradient.add_color_stop_rgba(1, 0, 0, 0, 0)

    context.set_source(gradient)
    context.arc(center_x, center_y, glow_radius, 0, 2 * math.pi)
    context.fill()

# Draw the sphere (planet)
def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(0.7, 0.5, 0.5, 0.5)
    gradient.add_color_stop_rgb(1, 0.1, 0.1, 0.1)
    context.set_source(gradient)
    context.fill()

context.set_source_rgb(0.05, 0.05, 0.1)
context.paint()

draw_nebula(context)
draw_stars(context, 100)
draw_shooting_stars(context, 3)
draw_galactic_glow(context, WIDTH // 2, HEIGHT // 2, 200)


surface.write_to_png("background.png")
