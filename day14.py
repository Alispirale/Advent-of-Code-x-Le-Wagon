elements = "NNCB"
official_elements = "ONHOOSCKBSVHBNKFKSBK"
elements = official_elements

rules = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

official_rules = """HO -> B
KB -> O
PV -> B
BV -> C
HK -> N
FK -> H
NV -> C
PF -> K
FV -> B
NH -> P
CO -> N
HV -> P
OH -> H
BC -> H
SP -> C
OK -> F
KH -> N
HB -> V
FP -> N
KP -> O
FB -> O
FH -> F
CN -> K
BP -> P
SF -> O
CK -> K
KN -> O
VK -> C
HP -> N
KK -> V
KO -> C
OO -> P
BH -> B
OC -> O
HC -> V
HS -> O
SH -> V
SO -> C
FS -> N
CH -> O
PC -> O
FC -> S
VO -> H
NS -> H
PH -> C
SS -> F
BN -> B
BF -> F
NC -> F
CS -> F
NN -> O
FF -> P
OF -> H
NF -> O
SC -> F
KC -> F
CP -> H
CF -> K
BS -> S
HN -> K
CB -> P
PB -> V
VP -> C
OS -> C
FN -> B
NB -> V
BB -> C
BK -> V
VF -> V
VC -> O
NO -> K
KF -> P
FO -> C
OB -> K
ON -> S
BO -> V
KV -> H
CC -> O
HF -> N
VS -> S
PN -> P
SK -> F
PO -> V
HH -> F
VV -> N
VH -> N
SV -> S
CV -> B
KS -> K
PS -> V
OV -> S
SB -> V
NP -> K
SN -> C
NK -> O
PK -> F
VN -> P
PP -> K
VB -> C
OP -> P"""
rules = official_rules

steps = 10

corresp = {rule.split(" -> ")[0] : rule.split(" -> ")[1] for rule in rules.split("\n")}
print(corresp)


def polym(elements):

    e_length = len(elements)
    new_elements = []
    for index, e in enumerate(elements):

        if index == (e_length - 1):

            # no pair
            continue

        pair = "".join([e, elements[index+1]])
        # print(pair)
        new_elements.append(e)
        new_elements.append(corresp[pair])

    new_elements.append(elements[-1])

    return "".join(new_elements)


def ftable(elements):

    freq = {}
    for char in elements:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


for step in range(steps):

    elements = polym(elements)
    print(elements)
    print()

    freq = ftable(elements)
    print(freq)

    mosts = {v : k for k, v in freq.items()}

    max_e = max(freq.values())
    min_e = min(freq.values())
    print(max_e, min_e)
    print(max_e - min_e)
