import math

def quadratic_equation(a, b, c):
    x = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    y = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

    return x, y

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)


# Better Version
# import math

# def quadratic_equation(a, b, c):
#     de=b**2-4*a*c
#     if de>=0:
#         x1=(-b+math.sqrt(de))/(2*a)
#         x2=(-b-math.sqrt(de))/(2*a)
#         return x1,x2
#     else:
#         return

# print quadratic_equation(2, 3, 0)
# print quadratic_equation(1, -6, 5)