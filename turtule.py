import math
import turtle

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("#FFFFFF")
screen.title("Heart")
screen.setup(width=700, height=700)

# 거북이 설정 (그려지는 과정을 보기 좋은 속도)
t = turtle.Turtle()
t.shape("turtle")
t.color("#E63946")
t.fillcolor("#E63946")
t.pensize(3)
t.speed(5)


def heart_point(angle_rad, scale=12):
  x = 16 * (math.sin(angle_rad) ** 3)
  y = (
      13 * math.cos(angle_rad)
      - 5 * math.cos(2 * angle_rad)
      - 2 * math.cos(3 * angle_rad)
      - math.cos(4 * angle_rad)
  )
  return x * scale, y * scale - 20


# 시작점으로 이동
start_x, start_y = heart_point(0)
t.penup()
t.goto(start_x, start_y)
t.pendown()

# 하트 외곽선을 따라 이동하며 색 채우기
t.begin_fill()
steps = 120
for i in range(1, steps + 1):
  theta = 2 * math.pi * (i / steps)
  x, y = heart_point(theta)
  t.goto(x, y)
t.end_fill()

t.hideturtle()
screen.exitonclick()