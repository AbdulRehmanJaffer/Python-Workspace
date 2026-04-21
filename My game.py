import turtle 
import random
import time

# screen setup
screen = turtle.Screen()
screen.title("Plane vs Aliens")   # Window title
screen.bgcolor("black")           # Background color
screen.setup(width=600, height=700)  # Window size
screen.tracer(0)  # Turns off auto screen update, Turtle automatically redraws the screen every tiny movement
# player
player = turtle.Turtle()
player.shape("triangle")   # Shape of player
player.color("white")      # Color
player.penup()           
player.goto(0, -300)       # Start position (bottom of screen)
player.setheading(90)      # Point desired direction
player_speed = 20          # How fast player moves

# bullet
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.5, stretch_len=1)  # Make bullet smaller
bullet.setheading(90)
bullet.penup()
bullet.goto(0, -340)
bullet.hideturtle()        # Hide bullet until fired
bullet_speed = 20          # Speed of bullet
bullet_state = "ready"     # "ready" = can shoot, "fire" = already shooting

# enemie
enemies = []          # List to store enemy turtles
enemy_speeds = []     # List to store each enemy speed

def create_enemies(count):
    for i in range(count):
        enemy = turtle.Turtle()
        enemy.shape("circle")
        enemy.color("red")
        enemy.penup()
        
        # Random starting position
        x = random.randint(-260, 260)
        y = random.randint(100, 300)
        enemy.goto(x, y)

        enemies.append(enemy)   # Add enemy to list
        enemy_speeds.append(random.randint(1, 5))  # Give each enemy a speed

# player movement
def move_left():
    x = player.xcor()     # Get current x position (gets the player position)
    x -= player_speed     # Move left by subtracting speed the to player on the certain direction  (player speed = 20, x cordinate = 50, x = x - player_speed = 30 --> moving left))
    if x < -280:          # Stop at left boundary
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed    # Move left by adding speed the to player on the certain direction  (player speed = 20, x cordinate = 50, x = x + player_speed = 70 --> moving right))
    if x > 280:    # Stop at right boundary
        x = 280
    player.setx(x)

# firing the bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":   # IF the bullet is ready Only THEN it will fire
        bullet_state = "fire"       
        bullet.goto(player.xcor(), player.ycor() + 10)  #xcor is the horizontal position, ycor is the vertical position, + 10 means the bullet does not start from inside the player but 10 pixels away from the player
        bullet.showturtle()  # able to see bullet

# controls
screen.listen()  # Thistakes keyboard keys as an input
screen.onkeypress(move_left, "a")   # press 'a' to move left
screen.onkeypress(move_right, "d")  # ppess 'd' to move right
screen.onkeypress(fire_bullet, "space")  # press space to shoot

#collision detection
def collisions(t1, t2):
    return t1.distance(t2) < 20   # t1 is the player, t2 is the enemy, if the gap between the enemy and the player is less than 20 pixels it counts as a collision

# starts the game
create_enemies(5)   # Create 5 enemies (calling the function) ans starts the game wit h5 enemies

#game loop
while True: # while true means the game will run forever because the code will never turn false
    screen.update()   # Refresh screen every frame

    # Bullet movement
    if bullet_state == "fire":
        y = bullet.ycor()     # Get bullet position (vertical)
        y += bullet_speed     # Moves the bullet up
        bullet.sety(y)        #sets the bullet into its new Y position

        # If bullet goes off screen then it stops it
        if y > 350:         # 350 is the max 
            bullet.hideturtle()         #bullet hides afte rgoing above 350 pixels
            bullet_state = "ready"   # Allow shooting again

    # Enemy movement
    for i in range(len(enemies)):    # for i in range of the LENGTH of the enemies (5)
        enemy = enemies[i]      #pick the current enemy
 
        y = enemy.ycor()        #get it postion
        y -= enemy_speeds[i]   # Move enemy down by subtracting the vertical cordinate (ycor) by the enemy speed
        enemy.sety(y)           #sets the new position of Y cordinate

        # If enemy goes off screen  then it stops it
        if y < -350:        #350 is max height it can go
            x = random.randint(-260, 260)   #soawnxs the enemy in a random position between these cordinatesd
            y = random.randint(200, 300)    
            enemy.goto(x, y)        # and tells the enemy to go to these positions which are X and Y

        # Bullety hits enemy
        if collisions(bullet, enemy):  #calling the fucntion in an IF condition
            bullet.hideturtle()         # It hides the turtle or bullet
            bullet_state = "ready"      #and makes the bulletr state ready so it can fire again

            # Move enemy to new random position
            x = random.randint(-260, 260)   #after enemy dies it re spawns in a new position
            y = random.randint(200, 300)
            enemy.goto(x, y)

        #Enemy Hits player
        if collisions(player, enemy):   #same thing calling collision function in IF condition
            player.hideturtle()         #hides the player
            enemy.hideturtle()          #hides the enemy
            print("GAME OVER")          #pritns game over
            break                       #stops the loops

    time.sleep(0.02)   # Small delay which controls game speed