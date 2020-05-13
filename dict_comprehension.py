s = "k:1 |k1:2|k2:3|k3:4"
s_dict = {}
for _ in s.split("|"):
    key, value = _.strip().split(":")
    # s_dict[key] = int(value)
    s_dict.update({key: int(value)})

print s_dict

print {k: int(v) for t in s.split("|") for (k, v) in (t.strip().split(":"), )}
