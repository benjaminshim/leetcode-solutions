"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

num = 1004

conversions = [
    ["I", 1],
    ["IV", 4],
    ["V", 5],
    ["IX", 9],
    ["X", 10],
    ["XL", 40],
    ["L", 50],
    ["XC", 90],
    ["C", 100],
    ["CD", 400],
    ["D", 500],
    ["CM", 900],
    ["M", 1000]
]

result = ""

while (num > 0):
    for i in range(len(conversions) - 1, -1, -1):
        if (num >= conversions[i][1]):
            count = num // conversions[i][1]
            result += conversions[i][0] * count
            num = num % conversions[i][1]
        else:
            continue
    
print(result)
