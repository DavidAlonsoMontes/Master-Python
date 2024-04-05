def multiplicacion (num1, num2):
    return num1*num2

multiplicacion= lambda num1, num2:num1*num2

res1 = multiplicacion(10,7)
res2 = multiplicacion(56,5)

print (res1)
print(res2)
print( (lambda num1, num2 : num1*num2)(7,5) )