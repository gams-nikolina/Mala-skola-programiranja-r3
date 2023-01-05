#6. Nacrtaj cvijet s fotografije u crvenoj boji. put kad nacrtaš kvadrat treba se pomaknuti za kut 360/18 i to ponoviti 18 puta.
from turtle import *
pencolor('red')
fillcolor('red')
begin_fill()
for i in range (18):
    for i in range (4):
        fd(50)
        rt(90)
    rt(360/18)
end_fill()