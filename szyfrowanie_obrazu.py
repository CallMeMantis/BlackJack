from numpy import loadtxt
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
# you need to install Pillow
from scipy import misc
import random


def zaszyfruj():
    l_szyfrujaca = []
    img = misc.imread("d.png")
    decrypt_data = []
    # print(img[0][0][0])
    for i in range(len(img[:])):
        for j in range(len(img[i][:])):
            for k in range(len(img[i][j][:])):
                l_szyfrujaca = random.randint(0,10000)
                decrypt_data.append(l_szyfrujaca)
                img[i][j][k] = float(img[i][j][k]) + (float(l_szyfrujaca))

    with open('decrypted_data.txt', 'w') as f:
        for item in decrypt_data:
            f.writelines(str(item))
            f.writelines(",")

    plt.imshow(img)
    plt.savefig("zaszyfrowane.png")


def odszyfruj():
    img = misc.imread("zaszyfrowane.png")
    lines = loadtxt("decrypted_data.txt", dtype=str, comments="#", delimiter=",", unpack=False)
    q = 0
    for i in range(len(img[:])):
        for j in range(len(img[i][:])):
            for k in range(len(img[i][j][:])):
                l_szyfrujaca = lines[q]
                img[i][j][k] = float(img[i][j][k]) - (float(l_szyfrujaca))
                q =+ 1

    plt.imshow(img)
    plt.savefig("odszyfrowane.png")

odszyfruj()
# zaszyfruj()

