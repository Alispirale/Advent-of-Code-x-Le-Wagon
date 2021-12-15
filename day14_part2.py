# import counter class from collections module
from collections import Counter

# Get initial string
polymer = "ONHOOSCKBSVHBNKFKSBK"

def gen_input_list(my_input):
    '''transform the input puzzle into numpy array '''
    r = open(my_input, 'r').read()
    content_list = r.splitlines()
    return content_list

lines = gen_input_list("input14.txt")

# Keep very first element - see further down why
first_element = polymer[0]

# Initialise empty dict for all instructions AB -> AXB (captured as AB -> X)
instr_dict = {}
for line in lines:
    a, b = line.split(" -> ")
    instr_dict[a] = b

# Find count of AB pairs in initial string
c = Counter()
for idx in range(len(polymer) - 1):
    c[polymer[idx:idx + 2]] += 1

# Loop steps - change to 10 or 40
for i in range(40):
    # Copy and re-initialise counter
    cc = c
    c = Counter()
    for el in cc.keys():
        # Increment counter for AX and XB
        c[el[0] + instr_dict[el]] += cc[el]
        c[instr_dict[el] + el[1]] += cc[el]

# Now count the actual elements
l = Counter()
# Add back the very first element, since the loop below will only consider the second half of each pair
l[first_element] = 1
for el, ct in c.items():
    l[el[1]] += ct

print(l.most_common()[0][1] - l.most_common()[-1][1])
