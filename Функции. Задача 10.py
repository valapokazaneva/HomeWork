dl=[{'a': 10, 'b': 20, 'c': 1}, {'a': 5, 'b': 10, 'z': 10}, {'a': 3, 'y': 7}]
print(sorted(dl, key=lambda x: x['a']))