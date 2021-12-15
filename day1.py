with open("input1.txt") as file:
    measures = file.read()

lines = measures.split("\n")

lines = [int(line) for line in lines if line != ""]
print(lines)

prev = 99999
count = 0

for line in lines :
    if line > prev:
        count+=1
    prev = line
print(count)