from hashlib import md5

def pass_hash(str):
    return md5(str.encode()).hexdigest()