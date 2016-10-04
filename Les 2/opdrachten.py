lst = [120, 138, 132.5, 159]
lst.append(160)

x = lst.count(160)
minimum = min(lst)
index = lst.index(minimum)
lst.remove(minimum)
lst.sort()
print(x, minimum, index)


