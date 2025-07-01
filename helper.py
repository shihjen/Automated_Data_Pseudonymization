import pandas as pd
import numpy as np
import random, string

def randomword():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(5))

def pseudonymization(lst):
    srs = pd.Series(lst)
    code_lst = []
    srs_str = srs.astype(str)
    total_unique = srs_str.nunique()
    random_num = np.random.randint(low=100000000, high=999999999, size=total_unique)
    random_char = [randomword() for i in range(total_unique)]
    for m, n in zip(random_num, random_char):
        code = n + str(m)
        code_lst.append(code)
    return code_lst

def update_key_table(exist_key, new_nric, code_lst):
    while True:
        pseudo_nric = pseudonymization(new_nric)
        if not set(pseudo_nric) & set(exist_key["Pseudo_ID"]):
            break
    new_key = pd.DataFrame(list(zip(new_nric, pseudo_nric)), columns=exist_key.columns)
    exist_key = pd.concat([exist_key, new_key], ignore_index=True)
    return exist_key
        