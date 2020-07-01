def trans(a):
    before = []
    for i in a:
        before.append(i)
    
    for i in range(len(before)):
        before[i] = ord(before[i])
    
    for k in range(len(before)):
        if (96 < before[k] < 123):
            before[k] += 2

    after = []

    for i in before:
        after.append(chr(i))

    for i in after:
        print(i, end="")


trans("map")