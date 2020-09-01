from math import floor

def make_readable(seconds):
    H = int(floor(seconds/3600))
    M = int(floor((seconds-H*3600)/60))
    S = seconds - H*3600 - M*60
    return "{}:{}:{}".format(H if H > 9 else "0{}".format(H), M if M > 9 else "0{}".format(M), S if S > 9 else "0{}".format(S))