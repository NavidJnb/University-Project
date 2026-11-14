import math

mean = 1019
std = 209
x = 820

z = (x - mean) / std

probability = (1 + math.erf(z / math.sqrt(2))) / 2

print("Probability:", probability * 100, "%")