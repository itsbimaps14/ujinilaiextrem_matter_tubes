#Deklarasi Library
import sympy as sym

#Initialisasi Variable
x = sym.Symbol('x')
y = sym.Symbol('y')

#Module cari x
def getXval(fTmp, xTmp):
    return sym.solveset(fTmp, xTmp)

#Module cari y
def getYval(fTmp, yTmp):
    return sym.solveset(fTmp, yTmp)

#Module cari x dan y
def getXYval(f1Tmp, f2Tmp, xTmp, yTmp):
    return sym.solve([f1Tmp, f2Tmp], [xTmp, yTmp])

#Module cari Determinan
def getDeterminan(xx, yy, xy):
    #Rumus D = fxx * fyy - fxy**2
    return ((xx * yy) - (xy * xy))

#Module cari Jenis Titik
def showJenisTitik(determinan, xx):
    if(determinan > 0):
        if(xx < 0):
            return "Titik Maksimum Lokal."
        else:
            return "Titik Minimum Lokal."
    elif(determinan < 0):
        return "Titik Pelana."
    else:
        return "Tidak dapat ditarik kesimpulan."

#Input
f = input("Masukkan Fungsinya : ")

print("\nSTEP 1 : CARI TURUNANNYA")

#Turunan Fx
print("\nTurunan terhadap Fx : ")
fx = sym.diff(f, x)
print(fx)

#Turunan Fy
print("\nTurunan terhadap Fy : ")
fy = sym.diff(f, y)
print(fy)

#Turunan Fxx
print("\nTurunan terhadap Fxx : ")
fxx = sym.diff(fx, x)
print(fxx)

#Turunan Fxy
print("\nTurunan terhadap Fxy : ")
fxy = sym.diff(fx, y)
print(fxy)

#Turunan Fyx
print("\nTurunan terhadap Fyx : ")
fyx = sym.diff(fy, x)
print(fyx)

#Turunan Fyy
print("\nTurunan terhadap Fyy : ")
fyy = sym.diff(fy, y)
print(fyy)

print("\nSTEP 2 : CARI TITIK KRITIS")

#GetXnY / Titik Kritis
print("\nTitik Kritis yang Didapat adalah : ")
pointArray = getXYval(fx, fy, x, y)
print(pointArray)

print("\nSTEP 3 : CARI NILAI Fxx, Fyy, Fxy, dan Determinan\n")

#GetJenisTitik
arrxx = [] * 10
arryy = [] * 10
arrxy = [] * 10
determinan = [] * 10

for i in range(len(pointArray)):
    #Reset tiap for
    argxx = fxx
    argyy = fyy
    argxy = fxy
    
    #Untuk Fxx
    argxx = argxx.subs(x, pointArray[i][0])
    arrxx.insert(i, (argxx.subs(y, pointArray[i][1])))
    
    #Untuk Fyy
    argyy = argyy.subs(x, pointArray[i][0])
    arryy.insert(i, (argyy.subs(y, pointArray[i][1])))
    
    #Untuk Fxy
    argxy = argxy.subs(x, pointArray[i][0])
    arrxy.insert(i, (argxy.subs(y, pointArray[i][1])))

    #Determinan
    determinan.insert(i, (getDeterminan(arrxx[i], arryy[i], arrxy[i])))
    
    #Tampilan
    print("Untuk titik " + str(pointArray[i]) + " :\n\tFxx = " + str(arrxx[i]) + "\n\tFyy = " + str(arryy[i]) + "\n\tFxy = " + str(arrxy[i]) + "\n\tDeterminan = " + str(determinan[i]))

print("\nSTEP 4 : CARI JENIS NILAI TITIK\n")
for i in range(len(pointArray)):
    print(str(i+1) + ". Untuk titik " + str(pointArray[i]) + " berjenis : " + showJenisTitik(arrxx[i], determinan[i]))
