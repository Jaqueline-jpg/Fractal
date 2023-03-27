import turtle

turtle.pensize(1)

for i in range(0,2000,1):
    turtle.right(90)
    turtle.right(30)
    turtle.forward(i)

#utilizei no código dois turtle.right para fazer o formato do triangulo
#também reduzi os parametros acima para que o triângulo tenha um formato de "pintura"

turtle.Screen().exitonclick()