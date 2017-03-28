l = open ("crime_data_raw.txt, "r").read().split('"')
l2 = []
i = 0
for e in l:
    if i ==1:
        l2.append(e)
    i += 1
    if i == 6:
        i = 0

print(l2[0:20])
