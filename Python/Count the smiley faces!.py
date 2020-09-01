def count_smileys(arr):
    smileys = 0
    for dec in arr:
        if dec[0] not in [':', ';']:
            continue
        if dec[1] in ['~', '-']:
            if dec[2] in [')', 'D']:
                smileys += 1
        elif dec[1] in [')', 'D']:
            smileys += 1
    return smileys