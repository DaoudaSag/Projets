''' Cours matrice '''

# 06/02/2023

from math import*    #Nous avons besoin de cette bibliothèque pour utiliser les matrices
import numpy as np  # Import matrices



##############################################################








##############################################################




def verifMatrice (mat1, mat2):
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        return True
    else:
        return False



def additionMatrice (mat1, mat2):
    # if verifMatrice == True:
    mat3 = []
    if verifMatrice(mat1, mat2):
        for elements in range (0, len(mat1)):
            temp = []
            for elements2 in range (0, len(mat1[elements])):
                temp.append(mat1[elements][elements2] + mat2[elements][elements2])
            mat3.append(temp)
            print (temp)
    return mat3


# def additionMatrice2 (mat1, mat2):
    # if verifMatrice == True:
    #mat3 = []
    #if verifMatrice(mat1, mat2):
        #for elements in range (0, len(mat1)):
            #for elements2 in range (0, len(mat1[elements])):
                #mat3.append(mat1[elements][elements2] + mat2[elements][elements2])
    #return mat3



def multiplicationScalaire(mat1,x):
    tab2=[]
    for i in range(0,len(mat1)):
        vase = []
        for j in range(0,len(mat1[i])):
            vase.append(mat1[i][j]*(x))
        tab2.append(vase)
    return tab2



def transpositionMatrice (mat1):
    mat5 = []
    for elements in range(0,len(mat1[0])):
        temp = []
        for elements2 in range (0, len(mat1)):
            temp.append(mat1[elements2][elements])
        mat5.append(temp)
    return mat5



#def multiplicationDeuxMatrices (mat1, mat2):
    #mat6 = []
    #if verifMatrice :
        #for elements in range (0, len(mat1)):
            #temp = []
            #for elements2 in range (0, len(mat1[elements])):



def multiplicationMatrice(mat_a, mat_b):
    """Addition les deux matrices le même dimenton"""
    if verifMatrice(mat_a, mat_b):
        matrice_final = []
        for i in range(0, len(mat_a)):
            tmp = []
            for j in range(0, len(mat_a[i])):
                tmp.append(mat_a[i][j] * mat_b[i][j])
            matrice_final.append(tmp)
        return matrice_final
    else:
        return "Les dimention des matrices sont differents."



def determinantMatrice (mat1):   # le déterminant se calcul seulement pour les matrices carré
    det = (mat1[0][0]*mat1[1][1]) - (mat1[1][0]*mat1[0][1])
    if det == 0:
        return False
    else:
        return det

# si déterminant = 0, inversion de la matrice impossible


def InversionMatricede2(mat1):
    det_mat1 = determinantMatrice(mat1)
    if det_mat1!=0:
        temp = mat1[0][0]
        mat1[0][0] = mat1[1][1]
        mat1[1][1] = temp
        ## polarité négative
        mat1[0][1] = -1*mat1[0][1]
        mat1[1][0] = -1*mat1[1][0]
        mat3 = []
        for i in range(len(mat1)):
            mattemp =[]
            for j in range(len(mat1[0])):
                mattemp.append(mat1[i][j]*(1/det_mat1))
            mat3.append(mattemp)
        return mat3
    else:
        print("opération impossible. Le déterminant est égale à 0")
        return None


def adjointeMatrice (mat1):
    temp = [(mat1[0][0])]
    [(mat1[0][0])] = [(mat1[1][1])]
    [(mat1[1][1])] = temp
    # ici nous avons échanger de place les valeurs des emplacements mat1[0][0] et mat1[1][1]
    mat1[0][1]*= -1
    mat1[1][0]*= -1
    return mat1


#def matrice_inverse(mat):
    #det = determinantMatrice(mat)
    #if det != 0:
        #mat1 = adjointeMatrice(mat)
        #valeur = 1/determinantMatrice(mat)
        #mat2 = multiplicationScalaire(mat1,valeur)
        #return mat2
    #else:
        #print("Opération impossible, determinant égale a zéro")
        #return None



''' Cours 5 : matrice suite '''

# 07/02/2023


def eliminLigneCologne(m, n, matrice_mineur):
    matrice_mineurlin = len(matrice_mineur)
    result = []
    rep = []
    for i in range (matrice_mineurlin):
        if i !=m:
            for j in range(matrice_mineurlin):
                if j !=n:
                    result.append(matrice_mineur[i][j])
    for k in range (0, len(result), matrice_mineurlin-1):
        rep.append(result[k:k+matrice_mineurlin-1])
    return rep



def calculDeterminantMatriceDe3(matrice):
    ''' Retourne le déterminant d'une matrice de dimension N'''

    signe = [1,-1,1]
    if len(matrice) == 3 and len(matrice[0]) == 3:
        det = 0
        for n in range(len(matrice[0])):
            matrice_temp = eliminLigneCologne(0, n, matrice)
            det += (matrice[0][n] * ((matrice_temp[0][0] * matrice_temp[1][1]) - (matrice_temp[1][0]*matrice_temp[0][1]))) * signe[n]
    else:
        det = 0

    return det



mat1 = ([2,5],
        [3,7])

mat2 = ([-4,2],
        [0,2])

mat3 = ([1, 1, 4],
        [2, -1, 3],
        [-2, 4, 3])