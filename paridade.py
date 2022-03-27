from array import array
from ctypes import sizeof
from operator import indexOf
import random

###################
def imprime(mat1,mat2,mat3,parH,parV):
    print(str(mat1) + " - " +str(parH[0]))
    print(str(mat2) + " - " +str(parH[1]))
    print(str(mat3) + " - " +str(parH[2]))
    print("--------------------------------")
    print(parV)

def calculaPar(mat1,mat2,mat3,parH,parV):
    for i in range(entrada):
        parH[0] = parH[0] + mat1[i]
        parH[1] = parH[1] + mat2[i]
        parH[2] = parH[2] + mat3[i]

    iter = 0
    for i in parH:
        if(i % 2 != 0):
            parH[iter] = 1
        else:
            parH[iter] = 0
        iter = iter + 1

    for i in range(entrada):
        if( (mat1[i] + mat2[i] + mat3[i]) % 2 != 0 ):
            parV.append(1)
        else:
            parV.append(0)
    
    return([parH,parV])
        
###################


print("8 | 16 | 32 bits?")
entrada = int(input())

if(entrada != 8 and entrada != 16 and entrada != 32):
    exit("VALOR NAO VALIDO!")

mat1 = []
mat2 = []
mat3 = []
parH = [0,0,0]
parV = []

for i in range(entrada): # gera 3 palavras aleatorias
    mat1.append(random.randint(0,1))
    mat2.append(random.randint(0,1))
    mat3.append(random.randint(0,1))

paridades = calculaPar(mat1,mat2,mat3,parH,parV)
parH = paridades[0]
parV = paridades[1]

imprime(mat1,mat2,mat3,parH,parV)

print("\nInsira a linha para inverter(0,1,2): ")
mL = int(input())
print("Insira a coluna para inverter(0,1,..,n): ")
mC = int(input())

if(mL == 0): #inversao de bit
    if(mat1[mC] == 1):
        mat1[mC] = 0
    else:
        mat1[mC] = 1
if(mL == 1):
    if(mat2[mC] == 1):
        mat2[mC] = 0
    else:
        mat2[mC] = 1
if(mL == 2):
    if(mat3[mC] == 1):
        mat3[mC] = 0
    else:
        mat3[mC] = 1

print("\nRecalculando paridade e comparando a original...\n")
parH2 = [0,0,0]
parV2 = []
paridades = calculaPar(mat1,mat2,mat3,parH2,parV2)
parV2 = paridades[1]
parH2 = paridades[0]

for i in range(len(parH)):
    if(parH[i] != parH2[i]):
        parH2[i] = "X"

for i in range(len(parV)):
    if(parV[i] != parV2[i]):
        parV2[i] = "X"

imprime(mat1,mat2,mat3,parH2,parV2)

print("\nBit invertido na linha " + str(indexOf(parH2,"X")) + " coluna " + str(indexOf(parV2,"X") ) + "\n")