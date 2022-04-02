import timeit
import bisect
import numpy as np

class Tree:
    matriksKunjung = set()
    simpulHidup = []
    nodeCount = [0]
    distanceFactor = 0
    def __init__(self, matriks, parent, emptyPosRow, emptyPosCol, direction, cost, distance):
        self.matriks = matriks
        self.parent = parent
        self.emptyPosRow = emptyPosRow
        self.emptyPosCol = emptyPosCol
        self.direction = direction
        self.cost = cost
        self.distance = distance
        converted = ConvertToString(self.matriks)
        if converted not in self.matriksKunjung:
            bisect.insort_right(self.simpulHidup, self, key=SortFunction)
            self.matriksKunjung.add(converted)
            self.nodeCount[0] += 1
    def Generate(self):
        self.simpulHidup.remove(self)
        if self.direction != "down" and self.emptyPosRow != 0:
            temp = Move(self.matriks, "up", self.emptyPosRow, self.emptyPosCol)
            self.upChild = Tree(temp, self, self.emptyPosRow-1, self.emptyPosCol, "up", self.distanceFactor*(self.distance+1)+CountG(temp), self.distance+1)
        if self.direction != "up" and self.emptyPosRow != 3:
            temp = Move(self.matriks, "down", self.emptyPosRow, self.emptyPosCol)
            self.downChild = Tree(temp, self, self.emptyPosRow+1, self.emptyPosCol, "down", self.distanceFactor*(self.distance+1)+CountG(temp), self.distance+1)
        if self.direction != "right" and self.emptyPosCol != 0:
            temp = Move(self.matriks, "left", self.emptyPosRow, self.emptyPosCol)
            self.leftChild = Tree(temp, self, self.emptyPosRow, self.emptyPosCol-1, "left", self.distanceFactor*(self.distance+1)+CountG(temp), self.distance+1)
        if self.direction != "left" and self.emptyPosCol != 3:
            temp = Move(self.matriks, "right", self.emptyPosRow, self.emptyPosCol)
            self.rightChild = Tree(temp, self, self.emptyPosRow, self.emptyPosCol+1, "right", self.distanceFactor*(self.distance+1)+CountG(temp), self.distance+1)
    def PrintAll(self, current):
        jawaban = []
        p = current
        while p != None:
            jawaban.append(p)
            p = p.parent
        for i in range(len(jawaban)-1, -1, -1):
            print (jawaban[i].direction)
            print (jawaban[i].matriks)
        return jawaban
    def Search(self):
        while self.simpulHidup[0].cost - self.simpulHidup[0].distanceFactor*self.simpulHidup[0].distance>0:
            self.simpulHidup[0].Generate()
        return self.simpulHidup[0]

# Functions
def ConvertToString(matriks):
    str = ""
    for i in range(4):
        for j in range(4):
            str += f"{matriks[i][j]:02d}"
    return str
def SortFunction(e):
    return e.cost
def Kurang(i,  dictArg):
    count = 0
    pos = dictArg[i]
    for x in range(i, 0, -1):
        if dictArg[x] > pos:
            count+=1
    return count
def RowIndex(i):
    return (i-1)//4
def ColIndex(i):
    return (i-1)%4
def GetX(dictArg):
    return (RowIndex(dictArg[16])+ColIndex(dictArg[16]))%2
def IsReachable(dictArg):
    arr = []
    total = 0
    for i in range(1,17):
        kurang = Kurang(i, dictArg)
        print(f"{str(i):2s}","|", kurang)
        arr.append(kurang)
        total += kurang
    sum = (total + GetX(dictArg))
    print()
    print("Sigma(KURANG(i)) + X =",sum)
    print()
    if  sum%2 == 0:
        return True, arr, sum
    else:
        return False, arr, sum
def SetArrayPosisi(matriksAwal):
    dictArg = dict()
    temp = 1
    for x in matriksAwal:
        for y in x:
            dictArg[y] = temp
            temp+=1
    return dictArg
def CountG(matriks):
    count = 0
    for i in range(4):
        for j in range(4):
            if 4*i+j+1 != matriks[i][j] and matriks[i][j] != 16:
                count+=1
    return count
def Move(matriks, direction, emptyPosRow, emptyPosCol):
    matriksCopy = np.copy(matriks)
    i = emptyPosRow
    j = emptyPosCol
    if direction == "up" and i != 0:
        matriksCopy[i-1][j],matriksCopy[i][j] = matriksCopy[i][j],matriksCopy[i-1][j]
    elif direction == "down" and i != 3:
        matriksCopy[i+1][j],matriksCopy[i][j] = matriksCopy[i][j],matriksCopy[i+1][j]
    elif direction == "left" and j != 0:
        matriksCopy[i][j-1],matriksCopy[i][j] = matriksCopy[i][j],matriksCopy[i][j-1]
    elif direction == "right" and j != 3:
        matriksCopy[i][j+1],matriksCopy[i][j] = matriksCopy[i][j],matriksCopy[i][j+1]
    return matriksCopy
def GetMatriksAwal(filename):
    try:
        return np.genfromtxt(filename).astype(int)
    except:
        return np.genfromtxt('..\\test\\' + filename).astype(int)

def Run(matriksAwal):
    jawaban = []
    print()
    print("Matriks Posisi Awal:")
    print(matriksAwal)
    start = timeit.default_timer()
    dictPosisi = SetArrayPosisi(matriksAwal)
    print(dictPosisi)
    print("i  | Kurang(i):")
    isReachable, arr, sum = IsReachable(dictPosisi)
    if isReachable:
        tree = Tree(matriksAwal, None, RowIndex(dictPosisi[16]), ColIndex(dictPosisi[16]), "neutral", 1, 0)
        answerNode = tree.Search()
        duration = timeit.default_timer()-start
        jawaban = tree.PrintAll(answerNode)
        print("Total simpul:", tree.nodeCount[0])
        print("Total langkah:", len(jawaban)-1)
        print("Durasi Menemukan Simpul Jawaban =", duration, "detik")
    else:
        duration = timeit.default_timer()-start
        print("Persoalan tidak bisa diselesaikan")
    Tree.matriksKunjung = set()
    Tree.simpulHidup = []
    totalSimpul = Tree.nodeCount[0]
    Tree.nodeCount = [0]
    print("Durasi Total =", timeit.default_timer()-start, "detik")
    return jawaban, arr, sum, duration, totalSimpul
# main
def main():
    matriksAwal = []
    filename = input("Masukkan nama file: ")
    matriksAwal = GetMatriksAwal(filename)
    Run(matriksAwal)
