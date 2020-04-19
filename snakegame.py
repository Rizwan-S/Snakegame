import turtle
import time
import random

delay = 0.2
score = 0
high_score = 0
level = 1
colors  = ["red","green","blue","orange","purple","pink","yellow", "white", "dark gray", "slate gray", "royal blue", "midnight blue", "cyan", "aquamarine", "spring green", "sea green", "gold", "dark goldenrod", "burlywood", "chocolate", "brown", "tomato", "crimson", "dark salmon", "deep pink", "purple", "violet", "orchid", "dark violet", "lavender", "slate blue", "medium violet red", "light pink"]

window = turtle.Screen()
window.title("Snake game by Rizwan")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.shapesize(1.25 ,1.25)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0  Level: 1", align = "center", font = ("Courier", 14, "normal"))

def go_up():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def move():
	if head.direction == "up":
		head.sety(head.ycor() + 20)

	if head.direction == "down":
		head.sety(head.ycor() - 20)

	if head.direction == "left":
		head.setx(head.xcor() - 20)

	if head.direction == "right":
		head.setx(head.xcor() + 20)

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "Down")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "Left")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "Right")
window.onkeypress(go_right, "d")

while True:
	window.update()

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"

		for segment in segments:
			segment.goto(2000, 2000)
		segments.clear()

		score = 0
		delay = 0.2
		level = 1

		pen.clear()
		pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align = "center", font = ("Courier", 14, "normal"))

	if head.distance(food) < 20:
		food.goto(random.randint(-270,270), random.randint(-270, 270))
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		color = random.choice(colors)
		new_segment.color(color)
		new_segment.penup()
		segments.append(new_segment)

		delay -= 0.005
		if score < 49:
			score += 5
		if score > 49 and score < 99 and level == 2:
			score += 10
		if score == 50:
			level += 1
		if score > 99 and score < 174 and level == 3:
			score += 15
		if score == 100:
			level += 1
		if score > 174 and score < 274 and level == 4:
			score += 20
		if score == 175:
			level += 1
		if score > 274 and score < 399 and level == 5:
			score += 25
		if score == 275:
			level += 1
		if score > 399 and score < 549 and level == 6:
			score += 30
		if score == 400:
			level += 1
		if score > 549 and score < 724  and level == 7:
			score += 35
		if score == 550:
			level += 1
		if score > 724 and score < 924  and level == 8:
			score += 40
		if score == 725:
			level += 1
		

		if score > high_score:
			high_score = score

		pen.clear()
		pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align = "center", font = ("Courier", 14, "normal"))

	for index in range(len(segments) - 1, 0, -1):
		segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())

	if len(segments) > 0:
		segments[0].goto(head.xcor(), head.ycor())

	move()

	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"

			for segment in segments:
				segment.goto(2000, 2000)

			segments.clear()

			score = 0
			delay = 0.2
			level = 1

			pen.clear()
			pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level), align = "center", font = ("Courier", 14, "normal"))

	time.sleep(delay)

window.mainloop()