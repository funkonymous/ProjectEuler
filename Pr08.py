f = open("Pr08_numbers.txt","r")
data = list(f.read())
while('\n' in data):
    data.remove('\n')
max_value = []
N = 13
for i in range(0,len(data)-N):
    value = 1
    lst = data[i:i+N]
    for c in lst:
        value*=int(c)
    max_value.append(value)
print(max(max_value))

