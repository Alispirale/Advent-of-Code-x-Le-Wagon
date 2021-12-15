with open("input1.txt") as file:
    measures = file.read()

lines = measures.split("\n")
lines = [int(line) for line in lines if line != ""]
#print(lines)

count = 0

for a in range(0,len(lines)-3):
    prev_measure = lines[a] + lines[a+1] + lines[a+2]
    measure = lines[a+1] + lines[a+2] + lines[a+3]
    if measure > prev_measure:
        count +=1
print(count)

