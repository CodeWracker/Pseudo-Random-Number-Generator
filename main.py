import numpy as np
import matplotlib.pyplot as plt
from sha256alg.RandomSHA256 import rand_sha
from tqdm import tqdm
if __name__ == "__main__":
    test = input("Wich method do you want to visualize?\n1 - SHA256\n2 - ???\nSelect: ")
    if test == "1":
        print("Testing")
        aux = None
        res = []
        for i in tqdm(range(1000000)):
            aux = i
            gen = rand_sha()
            if gen in res:
                break
            res.append(gen)
        print(aux)