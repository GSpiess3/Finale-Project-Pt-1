import math

def circle(radius):
    A = (math.pi * math.pow(float(radius), 2))
    return A

def rectangle(S1, S2):
    A = float(S1) * float(S2)
    return A

def square(S1):
    A = math.pow(float(S1), 2)
    return A
    
def triangle(Base, Height):
    A = (1/2) * float(Base) * float(Height)
    return A
