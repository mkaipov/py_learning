n = int(input())
array_in = []
search_requests = []
array_out = []
while n > 0:
    array_in.append(input())
    n -= 1
k = int(input())
while k > 0:
    search_requests.append(input().lower())
    k -= 1
counter = 0
for request in search_requests:
    for i in range(len(array_in)):
        if request.lower() in array_in[i].lower():
            counter += 1
            if counter == len(search_requests):
                array_out.append(array_in[i])
'''
for item in array_in:
    for i in range(len(search_requests)):
        if search_requests[i].lower() in item.lower():
            if item not in array_out:
                array_out.append(item)
'''
print(*array_out, sep='\n')
