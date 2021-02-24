import re
eng = input()
fra = []
eng = re.sub(r'([^\s\w\d]|_)+', '', eng)
eng = eng.upper()
eng = eng.split()
# Discourse on the method of rightly conducting the reason and seeking truth in the sciences.

for i in eng:
    if len(i) > 3:
        fra.append(i)

fra = [s[1:-2] for s in fra]
fra.sort()
for i in range(len(fra)):
    if len(fra[i]) > 5:
        fra[i] = fra[i] + "."
    elif fra[i] == fra[-1]:
        fra[-1] = fra[-1] + "."

fra = " ".join(fra)
print(fra)