sample_dict = {'C': 92,'Java': 66,'Python': 85}

val_list = list(sample_dict.values())
key_list = list(sample_dict.keys())
val = min(val_list)

position = val_list.index(val)
print(key_list[position])