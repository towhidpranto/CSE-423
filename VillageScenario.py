from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin
import random

# Midpoint Line Drawing Algorithms

#algo starts here
def midpointcircle(x, y, r, color):
    glColor3f(*color) # Set the color
    glBegin(GL_POINT)
    glPointSize(1) #pixel size. by default 1 thake
    #N, S, E, W from center
    d = 1.25-r
    x1 = x 
    y1 = y
    x = 0 
    y = r 
    if x1 != 0 or y1!=0:
        glVertex2f(x+x1, y+y1)
        glVertex2f(y+y1, x+x1)
        glVertex2f(y+y1, -x+x1)
        glVertex2f(x+x1, -y+y1)
        glVertex2f(-x+x1, -y+y1)
        glVertex2f(-y+y1, -x+x1)
        glVertex2f(-y+y1, x+x1)
        glVertex2f(-x+x1, y+y1)
    else: 
        glVertex2f(x, y)
        glVertex2f(y, x)
        glVertex2f(y, -x)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)
        glVertex2f(-y, x)
        glVertex2f(-x, y)
    while x <= y:
        if d<0:
            #E
            d = d+2*x+3 
            x += 1  
        else:
            d = d + 2*x - 2*y + 5
            x = x + 1 
            y = y - 1 
        if x1 != 0 or y1!=0:
            glVertex2f(x+x1, y+y1)
            glVertex2f(y+y1, x+x1)
            glVertex2f(y+y1, -x+x1)
            glVertex2f(x+x1, -y+y1)
            glVertex2f(-x+x1, -y+y1)
            glVertex2f(-y+y1, -x+x1)
            glVertex2f(-y+y1, x+x1)
            glVertex2f(-x+x1, y+y1)
        else: 
            glVertex2f(x, y)
            glVertex2f(y, x)
            glVertex2f(y, -x)
            glVertex2f(x, -y)
            glVertex2f(-x, -y)
            glVertex2f(-y, -x)
            glVertex2f(-y, x)
            glVertex2f(-x, y)
    glEnd()

#algo ends here
 
# Mid point line drawing algo
def drawPoint(x, y):
    glPointSize(20) #will change point
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx >= 0 and dy >= 0:
        if abs(dx) > abs(dy):
            return 0
        else:
            return 1
    elif dx <= 0 and dy >= 0:
        if abs(dx) > abs(dy):
            return 3
        else:
            return 2
    elif dx <= 0 and dy <= 0:
        if abs(dx) > abs(dy):
            return 4
        else:
            return 5
    else:  # dx >= 0 and dy <= 0
        if abs(dx) > abs(dy):
            return 7
        else:
            return 6


def midPointAlgo(x1, y1, x2, y2):
    zone = findZone(x1, y1, x2, y2)
    x1, y1, x2, y2 = convertToZoneZero(x1, y1, x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x1
    y = y1

    while x <= x2:
        tx, ty = convertFromZoneZeroToZoneSmth(x, y, zone)
        drawPoint(tx, ty)  

        x += 1
        if d > 0:
            d += incNE
            y += 1
        else:
            d += incE


def convertToZoneZero(x1, y1, x2, y2, zone):
    zone_mappings = {
        0: (x1, y1, x2, y2),
        1: (y1, x1, y2, x2),
        2: (y1, -x1, y2, -x2),
        3: (-x1, y1, -x2, y2),
        4: (-x1, -y1, -x2, -y2),
        5: (-y1, -x1, -y2, -x2),
        6: (-y1, x1, -y2, x2),
        7: (x1, -y1, x2, -y2),
    }

    return zone_mappings[zone]


def convertFromZoneZeroToZoneSmth(x, y, zone):
    zone_mappings = {
        0: (x, y),
        1: (y, x),
        2: (-y, x),
        3: (-x, y),
        4: (-x, -y),
        5: (-y, -x),
        6: (y, -x),
        7: (x, -y),
    }

    return zone_mappings[zone]


# Midpoint Circle Drawing Algorithm
def midpointcircle(x, y, r, color):
    glColor3f(*color)
    glPointSize(2)  # pixel size
    glBegin(GL_POINTS)
    d = 1.25 - r
    x1 = x
    y1 = y
    x = 0
    y = r
    while x <= y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5
            x += 1
            y -= 1
        # Draw horizontal lines (or points) between boundary points for all octants
        for fill_x in range(int(-x + x1), int(x + x1 + 1)):
            glVertex2f(fill_x, y + y1)
            glVertex2f(fill_x, -y + y1)
        for fill_x in range(int(-y + x1), int(y + x1 + 1)):
            glVertex2f(fill_x, x + y1)
            glVertex2f(fill_x, -x + y1)
    glEnd()


#will change the algo here for smoother animation
sun_scale = 1.0
def draw_circle(x_center, y_center, radius, color):
   
    if len(color) == 3:
        glColor3f(*color)  # Set the color (RGB)
    elif len(color) == 4:
        glColor4f(*color)  # Set the color (RGBA)

    glBegin(GL_POINTS)
    
    # Iterate over the area inside the circle
    for y in range(int(-radius), int(radius) + 1):  # Vertical range
        for x in range(int(-radius), int(radius) + 1):  # Horizontal range
            if x**2 + y**2 <= radius**2:  # Check if point is within the circle
                glVertex2f(x_center + x, y_center + y)
    
    glEnd()


def draw_treeX(x, y):
    glColor3f(0.5, 0.3, 0.0)
    midPointAlgo(x + 10, y + 50, x + 10, y - 70) #midpoint lines
    midPointAlgo(x - 10, y + 50, x - 10, y - 70)
    midPointAlgo(x + 10, y - 70, x - 10, y - 70)
    tree_leaf(x, y + 50)

def tree_leaf(x, y):
    draw_circle(x, y, 60, (0, 1, 0)) #midpoint circle
    draw_circle(x + 50, y, 40, (0, 1, 0))
    draw_circle(x - 50, y, 30, (0, 1, 0))
    draw_circle(x + 50, y - 50, 20, (0, 1, 0))
    draw_circle(x - 50, y + 20, 30, (0, 1, 0))
    draw_circle(x + 50, y + 10, 30, (0, 1, 0))
    draw_circle(x - 50, y + 20, 30, (0, 1, 0))
    draw_circle(x + 50, y + 10, 30, (0, 1, 0))
    draw_circle(x - 50, y, 30, (0, 1, 0))
    draw_circle(x - 40, y - 40, 30, (0, 1, 0))
    draw_circle(x + 30, y + 40, 15, (0, 1, 0))

rain_animation = False
rain_timer = 0
rain_duration = 120  # 5 seconds at 20 FPS
raindrops = [(random.uniform(0, 800), random.uniform(0, 800)) for _ in range(2000)]

def draw_raindrop(x, y):
    glColor3f(0.5, 0.5, 1.0)  # Light blue color for raindrops
    glPointSize(2)  # Set the size of the raindrop point
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
# Function to draw sky (gradient background)
is_day = True

def draw_sky():
    glPointSize(1)  # Set the point size
    glBegin(GL_POINTS)  # Start using points

    # Verify `is_day` and `rain_animation` are defined and valid
    global is_day, rain_animation
    if not isinstance(is_day, bool):
        print("Error: `is_day` is not properly initialized")
        return
    if not isinstance(rain_animation, bool):
        print("Error: `rain_animation` is not properly initialized")
        return

    if is_day and not rain_animation:  # Day without rain
        top_color = (0.4, 0.7, 1.0)
        bottom_color = (0.7, 0.9, 1.0)
    elif not is_day and not rain_animation:  # Night without rain
        top_color = (0.03, 0.03, 0.2)
        bottom_color = (0.1, 0.1, 0.3)
    elif rain_animation:  # Rain
        top_color = (0.2, 0.2, 0.5)
        bottom_color = (0.3, 0.3, 0.7)

    # Fill the area with points for the gradient
    for y in range(300, 601):  # Sky from y=300 to y=600
        gradient_factor = (y - 300) / (600 - 300)
        r = bottom_color[0] + gradient_factor * (top_color[0] - bottom_color[0])
        g = bottom_color[1] + gradient_factor * (top_color[1] - bottom_color[1])
        b = bottom_color[2] + gradient_factor * (top_color[2] - bottom_color[2])
        glColor3f(r, g, b)  # Set the color

        for x in range(0, 801):  # Sky width
            glVertex2f(x, y)  # Plot the point

    glEnd()  # End the points


# Clouds
flower_rotation_angle = 0.0
def draw_cloud(x, y):

    if rain_animation:
        glColor3f(0.5, 0.5, 0.5)  # Dark grey clouds during rain
    else:
        glColor3f(1, 1, 1)  # White clouds (color will be overridden during rain)

    glPushMatrix()
    glRotatef(flower_rotation_angle, 0, 0, 1)
    draw_circle(x, y, 50, (1, 1, 1))
    draw_circle(x + 50, y, 40, (1, 1, 1))
    draw_circle(x - 50, y, 40, (1, 1, 1))
    glPopMatrix()

# Stars
def draw_star(x, y):
    # Drawing a simple star using a point
    glColor3f(1, 1, 1)  # White color for stars
    glPointSize(2.0)  # Adjusting the size of the point
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

star_positions = [(random.uniform(0, 800), random.uniform(800, 400)) for _ in range(100)]

# Function to draw ground (flat surface)
def draw_ground():
    glColor3f(0.0, 0.6, 0.0)  # Green color for the points
    glBegin(GL_POINTS)
    
    # Draw points over the area of the "ground"
    for y in range(0, 301, 5):  # Step size determines the point density
        for x in range(0, 801, 5):
            if x <= (800 - (y / 300) * 100):  # Maintain the shape of the original quad
                glVertex2f(x, y)
    
    glEnd()


#house starts here
def draw_house(situation):
    # Draw main body of the house using GL_POINTS
    glColor4f(1.0, 0.5, 0.0, 0.0)  # Brown color for the house
    glPointSize(1)  # Set the point size for finer details
    glBegin(GL_POINTS)
    for x in range(200, 351):  # Fill the polygon area for the main body
        for y in range(200, 251):
            glVertex2d(x, y)
    glEnd()

    # Draw triangular roof using GL_POINTS
    glColor3f(0.5, 0.0, 0.0)  # Dark red color for the roof
    glBegin(GL_POINTS)
    for y in range(250, 341):  # Loop over the height of the triangle
        x_start = 200 + (y - 250)  # Left slope of the triangle
        x_end = 350 - (y - 250)  # Right slope of the triangle
        for x in range(int(x_start), int(x_end) + 1):  # Fill points between the slopes
            glVertex2d(x, y)
    glEnd()

    # Draw windows using GL_POINTS
    if situation == "day":
        window_color = (0.0, 0.0, 0.0)  # Black color for windows
    else:
        window_color = (1.0, 1.0, 1.0)  # White color for night

    glColor3f(*window_color)
    glBegin(GL_POINTS)
    for x in range(310, 341):  # Window 1
        for y in range(220, 241):
            glVertex2d(x, y)
    for x in range(210, 231):  # Window 2
        for y in range(220, 241):
            glVertex2d(x, y)
    for x in range(275, 296):  # Window 3
        for y in range(220, 241):
            glVertex2d(x, y)
    glEnd()

    # Draw door using GL_POINTS
    glColor3f(0.0, 0.5, 0.5)  # Teal color for the door
    glBegin(GL_POINTS)
    for x in range(235, 266):
        for y in range(200, 241):
            glVertex2d(x, y)
    glEnd()

    # Draw door knob using GL_POINTS
    glColor3f(1.0, 1.0, 0.5)  # Yellow color for the knob
    glPointSize(5)  # Larger point size for the knob
    glBegin(GL_POINTS)
    glVertex2f(260, 220)  # Door knob location
    glEnd()


#house ends here

#filling colors for rectangle and triangle
def draw_filled_rectangle_with_points(x, y, width, height):
    glColor3f(0.5, 0.25, 0.0)  # Brown color for the trunk
    glBegin(GL_POINTS)
    for i in range(int(width * 1000)):  # Width scaled up for point density
        for j in range(int(height * 1000)):  # Height scaled up
            glVertex2f(x + i/1000.0, y + j/1000.0)
    glEnd()

def draw_filled_triangle_with_points(x1, y1, x2, y2, x3, y3):
    glColor3f(0.0, 0.8, 0.0)  # Green color for the leaves
    glBegin(GL_POINTS)
    # Barycentric coordinates to fill the triangle
    for i in range(100):  # Horizontal coverage
        for j in range(100 - i):  # Vertical coverage, creates a right triangle
            alpha = i / 100.0
            beta = j / 100.0
            gamma = 1 - alpha - beta
            px = alpha * x1 + beta * x2 + gamma * x3
            py = alpha * y1 + beta * y2 + gamma * y3
            glVertex2f(px, py)
    glEnd()

def draw_tree(x, y):
    # Draw trunk using points
    draw_filled_rectangle_with_points(x, y, 0.05, 0.15)

    # Draw leaves using points
    for i in range(3):  # Three layers of leaves
        x1 = x - 0.05
        y1 = y + 0.15 + i * 0.05
        x2 = x + 0.1
        y2 = y + 0.15 + i * 0.05
        x3 = x + 0.025
        y3 = y + 0.25 + i * 0.05
        draw_filled_triangle_with_points(x1, y1, x2, y2, x3, y3)


def draw_line_with_points(x0, y0, x1, y1):
    glColor3f(0, 0, 0)  # Black color for the bird
    glBegin(GL_POINTS)
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        glVertex2f(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
    glEnd()

def draw_bird(x, y):
    # Draw bird using points
    draw_line_with_points(x, y, x - 10, y + 10)  # Left wing
    draw_line_with_points(x, y, x + 10, y + 10)  # Right wing

# Global variable to hold bird positions
bird_positions = [
    (600, 400), (700, 450), (550, 550),
    (700, 300), (750, 400), (750, 550),
    (800, 450), (900, 500),
    (600, 300), (500, 500)
]
# Global variable to control bird animation
bird_animation = False

def animate_birds():
    global bird_positions
    # Move the birds to the left
    bird_positions = [(x - 2, y) for x, y in bird_positions]

def draw_river():
    glColor3f(0.0, 0.5, 1.0)  # Blue color for water
    glBegin(GL_POINTS)
    for x in range(500, 801):  # Specify range to cover the width of the river
        for y in range(0, 301):  # Specify range to cover the height of the river
            glVertex2f(x, y)
    glEnd()

def draw_filled_polygon_with_points(vertices, color):
    glColor3f(*color)  # Set the color for the boat part 
    glBegin(GL_POINTS)
    # Calculate bounding box for the vertices to reduce the range of the loop
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)

    # Plot points densely within the polygon
    for x in range(int(min_x), int(max_x) + 1):
        for y in range(int(min_y), int(max_y) + 1):
            if is_point_in_polygon(x, y, vertices):
                glVertex2f(x, y)
    glEnd()

def is_point_in_polygon(x, y, polygon):
    num = len(polygon)
    j = num - 1
    c = False
    for i in range(num):
        if ((polygon[i][1] > y) != (polygon[j][1] > y)) and \
                (x < (polygon[j][0] - polygon[i][0]) * (y - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]):
            c = not c
        j = i
    return c

def draw_boat(x_position, is_day):
    # Base of the boat
    base_vertices = [
        (x_position, 270), (x_position + 45, 220),
        (x_position + 110, 220), (x_position + 150, 270)
    ]
    draw_filled_polygon_with_points(base_vertices, (0.5, 0.25, 0.0))  # Brown color

boat_position = 550

# Function to draw a simple flower
def draw_flower(x, y):
    # Draw petals using circles
    petal_radius = 10
    petal_color = (0.4, 0.0, 0.0)  # Red color
    for angle in range(0, 360, 60):
        petal_x = x + petal_radius * cos(angle * 3.14 / 180)
        petal_y = y + petal_radius * sin(angle * 3.14 / 180)
        draw_circle(petal_x, petal_y, petal_radius, petal_color)
    # Draw center of the flower using a circle
    center_radius = 5
    center_color = (1.0, 1.0, 0.0)  # Yellow color
    draw_circle(x, y, center_radius, center_color)

# Function to draw the garden with flowers
def draw_garden(): #many flowers are calling this a garden
    # Draw flowers at different positions within the specified area
    for x in range(100, 400, 50):
        for y in range(50, 200, 50):
            draw_flower(x, y)

def draw_fruit(x, y, color=(1.0, 0.0, 0.0)):  # Default color is red
    fruit_radius = 5  # can adjust the size of the fruit
    midpointcircle(x, y, fruit_radius, color)

def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    global is_day, rain_animation, rain_timer, boat_position
    # Draw sky and ground
    draw_sky()
    draw_ground()
    # Draw houses
    draw_house("day")
    global bird_animation
    draw_river()
    # draw_boat(boat_position)
    draw_treeX(70, 250)
    draw_treeX(420, 280)
    draw_garden()
    draw_fruit(50, 270, color=(1.0, 0.0, 0.0))
    draw_fruit(60, 280, color=(1.0, 0.0, 0.0))
    draw_fruit(70, 260, color=(1.0, 0.0, 0.0))
    draw_fruit(420, 300, color=(1.0, 0.0, 0.0))
    draw_fruit(430, 320, color=(1.0, 0.0, 0.0))
    draw_fruit(435, 310, color=(1.0, 0.0, 0.0))
    global rain_timer, rain_animation
    # Rain Scene
    if rain_animation:
        # glColor3f(0.9, 0.9, 0.9)  # Grey clouds during rain
        draw_cloud(500, 450)
        draw_cloud(300, 420)
        draw_cloud(200, 500)
        draw_house("night")
        draw_boat(boat_position, is_day=False)
        # Raindrop animation
        global raindrops 
        raindrops = [(x, y - 2) for x, y in raindrops]  # Move raindrops downward
        for x, y in raindrops:
            draw_raindrop(x, y)
        rain_timer += 1
        if rain_timer > rain_duration:
            rain_animation = False
            rain_timer = 0
            raindrops = [(random.uniform(0, 800), random.uniform(0, 800)) for _ in range(2000)]
    # Day Scene
    elif is_day:
        # draw_circle(700, 500, 40, (1.0, 0.843, 0.0))  # Sun
        midpointcircle(700, 500, 40, (1.0, 0.843, 0.0))
        draw_cloud(500, 450)
        draw_cloud(300, 420)
        draw_cloud(200, 500)
        draw_house("day")
        draw_boat(boat_position, is_day)
    # Night Scene
    else:
        # draw_circle(700, 500, 40, (1, 1, 1))  # Moon
        midpointcircle(700, 500, 40, (1, 1, 1))
        for x, y in star_positions:
            draw_star(x, y)
        draw_house("night")
        draw_boat(boat_position, is_day)
    # Birds Animations
    if bird_animation:
        global bird_positions
        bird_positions = [(x - 2, y) for x, y in bird_positions]  # Move birds to the left
        for x, y in bird_positions:
            draw_bird(x, y)
    glutSwapBuffers()

def keyboard(key, x, y):
    global is_day, bird_animation, sun_scale, flower_rotation_angle
    global is_day, rain_animation, rain_timer, boat_position
    if key == b'd':
        is_day = not is_day
    if key == b'b':
        bird_animation = not bird_animation
    if key == b'r' and not rain_animation:
        rain_animation = True
        rain_timer = 0
    if key == b'p' and rain_animation:     
        rain_animation = False
    if key == b'm':
        boat_position += 5
    if key == b'n':
        if boat_position < 500:
            boat_position -= 0
        else:
            boat_position -= 5

    if key == b's' or key == b'S':
        # Toggle scaling factor between 1.0 and 1.5 when the "S" key is pressed
        sun_scale = 1.5 if sun_scale == 1.0 else 1.0

    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Village Scenario")  # window name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)  # Keep drawing the scene
glutKeyboardFunc(keyboard)
glutMainLoop()