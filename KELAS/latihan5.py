for i in range(1,9):
    for j in range(1,9):
        print(i,"x",j,"=",i*j)
    print("========================================")
print("Program Selesai")
import numpy as np 
A = np.array([[1, 2, 3],
                [4, 5, 6]])
B = np.array([[7, 8, 9],
                [10, 11, 12]])
# Penjumlahan Matriks
C = A + B
print("Hasil Penjumlahan Matriks A dan B:")
print(C)
# Pengurangan Matriks
D = A - B
print("Hasil Pengurangan Matriks A dan B:")
print(D)
# Perkalian Matriks
E = A @ B.T  # Menggunakan transpose B untuk perkalian yang sesuai
print("Hasil Perkalian Matriks A dan B:")
print(E)
# Transpose Matriks
F = A.T
print("Transpose Matriks A:")
print(F)
# Determinan Matriks
G = np.array([[1, 2],
              [3, 4]])
det_G = np.linalg.det(G)
print("Determinan Matriks G:")

print(det_G)
# Invers Matriks
inv_G = np.linalg.inv(G)
print("Invers Matriks G:")
print(inv_G)

# Eigenvalues dan Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(G)
print("Eigenvalues Matriks G:")
print(eigenvalues)
print("Eigenvectors Matriks G:")
print(eigenvectors)

# Rank Matriks

rank_G = np.linalg.matrix_rank(G)


