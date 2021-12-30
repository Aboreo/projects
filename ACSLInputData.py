data = []
for i in range(5):
    data.append(input(""))

print(f"{len(data[0])}")

sum = 0
for i in data[1]:
    sum += int(i)

print(str(sum))

sum = 0
for i in range(0,len(data[2]),2):
    sum += int(data[2][i])

print(f"{sum}")

count = 0

for i in data[3]:
    if i == "4": count += 1

print(f"{count}")


if len(data[4])%2 == 0:
    print(f"{data[4][int(len(data[4])/2)-1]}")
else:
    print(f"{data[4][int(len(data)//2+1)]}")
