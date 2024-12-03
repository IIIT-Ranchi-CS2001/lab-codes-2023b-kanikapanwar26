import math
user_input1=(input("Enter the tuple 1:"))
tup1=tuple(map(int,user_input1.split()))
user_input2=(input("Enter the tuple 2:"))
tup2=tuple(map(int,user_input2.split()))
distance= math.sqrt((tup1[0]-tup2[0])**2+(tup1[1]-tup2[1])**2+(tup1[2]-tup2[2])**2)
print(distance)

