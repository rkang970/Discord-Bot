strs = input()
strs = strs.split()
print(strs)
prefix = ""

smallest = float("inf")
for i in range(len(strs)):
    if len(strs[i]) < smallest:
        smallest = len(strs[i])
print(smallest)

stop = False

for i in range(smallest):
    if stop:
        break
    for j in range(len(strs) - 1):
        if strs[j][i] == strs[j + 1][i]:
            if strs[j][i] not in prefix:
                prefix += strs[j][i]
        else:
            print("no common prefix")
            stop = True
            break
            
if not stop:
    print(prefix)