# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_students = int(input())
roll_a = set([int(nr) for nr in input().split()])
number_of_students_eng = int(input())
roll_b = set([int(nr) for nr in input().split()])

output = roll_a.intersection(roll_b)
print(len(output))

