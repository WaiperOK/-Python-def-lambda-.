# Код Python для иллюстрации куба числа
# показывает разницу между def () и lambda ().
def cube (y):
    return y*y*y;

print (cube(5))

g= lambda x: x*x*x
print (g(6))