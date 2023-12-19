ps = open("inputs/day19_1.txt").read().split("\n\n")

rules = {}
for l in ps[0].splitlines():
    p = l.split("{")
    rules[p[0]] = p[1][:-1]

A = 0
for p in ps[1].splitlines():
    state = "in"
    vals = {}
    for c in p[1:-1].split(","):
        vals[c.split("=")[0]] = int(c.split("=")[1])
    while state not in "AR":
        for pred in rules[state].split(","):
            if ":" in pred:
                evs = pred.split(":")
                if eval('vals["' + evs[0][0] + '"]' + "".join(evs[0][1:])):
                    state = evs[1]
                    break
            else:
                state = pred

        if state == "A":
            A += sum(vals.values())
            break
        elif state == "R":
            break

print(A)