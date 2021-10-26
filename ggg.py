a = {};
a["b"] = 2
a["c"] = 3
inv_map = {v: k for k, v in a.items()}

print(inv_map.items())