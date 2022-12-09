import math

def circle(radius):
    P = (2 * math.pi * float(radius))
    return P

def rectangle(S1, S2):
    P = 2 * float(S1) + 2 * float(S2)
    return P

def square(S1):
    P = 4 * float(S1)
    return P
    
def triangle(S1, S2, S3):
    P = float(S1) + float(S2) + float(S3)
    return P
    
    