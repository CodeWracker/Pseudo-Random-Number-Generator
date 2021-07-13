import numpy as np
import matplotlib.pyplot as plt

import random 

from sha256alg.RandomSHA256 import rand_sha


from tqdm import tqdm

def python_random():
    return random.randint(0,100000000)

if __name__ == "__main__":
    test = input("Which  method do you want to visualize?\n1 - SHA256\n2 - Python random()\nSelect: ")
    test_type = input("Which test type do you want to do?\n1 - Test Until Repeat\n2 Noise Generator\n3 - Print Table\nSelect: ")
    algs = [rand_sha,python_random]
    randomgen = algs[int(test)-1]
    print("Testing SHA256 - " + test_type)

    if test_type == "1":
        aux = None  
        res = []
        for i in tqdm(range(1000000)):
            aux = i
            gen = randomgen()
            if gen in res :
                break
            res.append(gen)
        print(str(aux)+" iterations without repeat")
    if test_type == "2":
        res = []
        for i in tqdm(range(720*480)):
            gen = randomgen()%255
            res.append(gen)
        img = np.array(res).reshape(480,720)
        plt.imshow(img,cmap='gray')
        plt.show()
    if test_type == "3":
        numbers = []
        for i in tqdm(range(100)):
            numbers.append(int(randomgen()%100000000))
        numbers = np.array(numbers).reshape(10,10)
        print("\n\nTable of random Numbers\n_____________________________________________________________________________________________________________")
        for i in range(10):
            line = ""
            for j in range(10):
                aux = str(numbers[i][j])
                num = ""
                if(len(aux)<8):
                    for k in range(len(aux),8):
                        num = num + "0"
                num = num + aux
                line = line + "| "+num+" "
            print(line)
        print("\n\n\n\n")