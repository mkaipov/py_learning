n = int(input())
sum_of_fact = 1
curr_fact = 1
for i in range(2, n+1):
    curr_fact *= i
    sum_of_fact += curr_fact
print(sum_of_fact)
