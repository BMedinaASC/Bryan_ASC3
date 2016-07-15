from random import *

List1 = ["The","Point","Rise","Age","Revenge","The Enigma","Independance","Judgement","The March","Fault"]
List2 = ["on","of","of the","Maze","Hunger","Break","Day","to","to the","in our"]
List3 = ["Runner","Games","AbreuBoom","Fallen","Moon","Past","Stars","Trials","Love","Gun"]

i = 0

for j in range(10):
    x = randrange(10)
    y = randrange(10)
    z = randrange(10)
    i = i + 1
    print(i, ".", List1[x], List2[y], List3[z])
    