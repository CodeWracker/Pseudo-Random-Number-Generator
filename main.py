import numpy as np
import matplotlib.pyplot as plt
import random 

from sha256alg.RandomSHA256 import rand_sha
from midsquarealg.MidSquare import mid_square

from tqdm import tqdm

def python_random():
    return random.randint(0,100000000)

if __name__ == "__main__":
    test = input("Which  method do you want to visualize?\n1 - SHA256\n2 - Python random()\n3 - Mid Square\nSelect: ")
    test_type = input("Which test type do you want to do?\n1 - Test Until Repeat\n2 - Noise Generator\n3 - Print Table\n4 - Test frequency\nSelect: ")
    algs = [rand_sha,python_random,mid_square]
    randomgen = algs[int(test)-1]
    print("Testing - " + test_type)

    if test_type == "1":
        tst_n = int(input("How many? "))
        for i in range(tst_n):
            aux = None  
            res = []
            for j in tqdm(range(1000000)):
                aux = j
                gen = randomgen()
                if gen in res :
                    break
                res.append(gen)
            print(str(aux)+" iterations without repeat")
    if test_type == "2":
        res = []
        x,y = (1920,1080)
        for i in tqdm(range(x*y)):
            gen = randomgen()%255 + 1
            res.append(gen)
        img = np.array(res).reshape(y,x)
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        plt.figure(figsize=(x*px, y*px))
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
    if test_type == "4": # dava errado antes pq eu colocava pra fazer o modulo de um numero divisivel por 2, ai ficava bem ruim msm...
        res = []
        x = []
        for i in tqdm(range(255)):
            res.append(0)
            x.append(i)
        for i in tqdm(range(255*10)):
            res[int(randomgen()%255)]+=1
        
        #print(res)
        plt.bar(x,res)
        plt.show()