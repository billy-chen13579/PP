#problem solving
# https://realpython.com/python-practice-problems/#problem-description
#problem 1
#Sum of Integers Up To n (integersums.py)
def sol(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum
ar=sol(8)
print(ar)
