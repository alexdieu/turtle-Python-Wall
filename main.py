import turtle

x = 0
while x < 1000:
	print("number : %s" % x)
	t = turtle.Pen()
	x = x+50
	t.forward(x)
	t.left(90)
	t.forward(200)
