import numpy as np
import matplotlib.pyplot as plt
from sha256alg.RandomSHA256 import rand_sha
from tqdm import tqdm
if __name__ == "__main__":
    test = input("Wich method do you want to visualize?\n1 - SHA256\n2 - ???\nSelect: ")
    test_type = input("Witch testtype do you want to do?\n1 - Test Until Repeat\n2 Noise Generator\n3 - Print Table\nSelect: ")
    if test == "1":
        print("Testing SHA256 - " + test_type)

        if test_type == "1":
            aux = None  
            res = []
            for i in tqdm(range(1000000)):
                aux = i
                gen = rand_sha()
                if gen in res :
                    break
                res.append(gen)
            print(str(aux)+" iterations without repeat")
        if test_type == "2":
            res = []
            for i in tqdm(range(720*480)):
                gen = rand_sha()%255
                res.append(gen)
            img = np.array(res).reshape(480,720)
            plt.imshow(img,cmap='gray')
            plt.show()