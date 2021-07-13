import hashlib
import time
import math
seed = 1
def hexstr_to_dec(num):
    m = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "a":10,
        "b":11,
        "c":12,
        "d":13,
        "e":14,
        "f":15,
    }
    return m[num]

def rand_sha():
    global seed
    seed = seed + ((float(time.time())))/seed
    #print("seed: ", seed)
    string_seed = hashlib.sha256(int(seed**3).to_bytes(16, 'little', signed=False)).hexdigest().lower()
    #print("HEX: ",string_seed)
    sum = 0
    for l in string_seed:
        sum+= hexstr_to_dec(l)
    result = 1.01 + seed
    for l in string_seed:
        #print(l)
        result = hexstr_to_dec(l)*sum + result/sum
        #print('parcial result: ',result)
        #print()
    return int(result*10000 * seed**2)

if __name__ == "__main__":
    for i in range(20):
        print(rand_sha()%1000000000)