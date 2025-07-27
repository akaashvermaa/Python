'''
tuples are non changeable lists 
data cannot be changed after decleration
'''
months_year = ("Janurary", "February", "March" ,"April", "may", "June", "july", "august","september","october", "november", "december")
print(months_year[2:6])
'''
Tuples are great for ----------------

Coordinates ((x, y))
Dates, time, settings
Configuration data
Function returns
Keys in dictionaries        
Safer alternatives to lists (data wont be accidentally changed)
Using tuples to find distance between tw corordinates--------
it can store 2D elements and can be used to calculate distance
'''

'''
import math
point1 = (4, 6)
point2 = (7, 1)
distance = math.sqrt((point2[0]- point1[0]))**2 + (point2[1] - point1[1]**2)
print("Distance between two poitns are ", round(distance, 2))


quiz = [
    ("What is the capital of India", "Delhi"),
    ("2 + 2 = ?", "4"),
    ("Pyhton is a ____ language", "programming")
]

score = 0
for q, a in quiz:
ans = input(q + " ")
if ans.strip().lower() == a.lower():
    score +=1
    print("Your Final Score : ", score, "/", len(quiz))
    '''