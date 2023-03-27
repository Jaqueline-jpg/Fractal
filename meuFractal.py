import turtle

turtle.pensize(1)

for i in range(0,2000,1):
    turtle.forward(i)
    turtle.right(30)
    turtle.right(30)
#utilizei no código dois turtle.right do mesmo tamanho para criar um formato redondo

turtle.Screen().exitonclick()