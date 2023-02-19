import sympy

E11 = 430
E22 = 6.9
E33 = E22
v12 = 0.3
v13 = v12
v23 = 0.49
G12 = 2.65
G13 = G12
G23 = 2.32
J_IJ = sympy.Matrix([[1/E11, -v12/E11, -v13/E11, 0, 0, 0],
                     [-v12/E22, 1/E22, -v23/E22, 0, 0, 0],
                     [-v13/E33, -v23/E33, 1/E33, 0, 0, 0],
                     [0, 0, 0, 1/G23, 0 ,0],
                     [0, 0, 0, 0, 1/G13, 0],
                     [0, 0, 0, 0, 0, 1/G12]])
C_IJ = J_IJ**-1
print(C_IJ)
C_ijkl = [[[[None, None, None] for k in range(3)] for j in range(3)] for i in range(3)]
print(C_ijkl[0][0][0][0])
C_ijkl[1-1][1-1][1-1][1-1] = C_IJ[1-1,1-1]
C_ijkl[1-1][1-1][2-1][2-1] = C_IJ[1-1,2-1]
C_ijkl[1-1][1-1][3-1][3-1] = C_IJ[1-1,3-1]
C_ijkl[1-1][1-1][2-1][3-1] = C_IJ[1-1,4-1]
C_ijkl[1-1][1-1][1-1][3-1] = C_IJ[1-1,5-1]
C_ijkl[1-1][1-1][1-1][2-1] = C_IJ[1-1,6-1]

C_ijkl[2-1][2-1][1-1][1-1] = C_IJ[2-1,1-1]
C_ijkl[2-1][2-1][2-1][2-1] = C_IJ[2-1,2-1]
C_ijkl[2-1][2-1][3-1][3-1] = C_IJ[2-1,3-1]
C_ijkl[2-1][2-1][2-1][3-1] = C_IJ[2-1,4-1]
C_ijkl[2-1][2-1][1-1][3-1] = C_IJ[2-1,5-1]
C_ijkl[2-1][2-1][1-1][2-1] = C_IJ[2-1,6-1]

C_ijkl[3-1][3-1][1-1][1-1] = C_IJ[3-1,1-1]
C_ijkl[3-1][3-1][2-1][2-1] = C_IJ[3-1,2-1]
C_ijkl[3-1][3-1][3-1][3-1] = C_IJ[3-1,3-1]
C_ijkl[3-1][3-1][2-1][3-1] = C_IJ[3-1,4-1]
C_ijkl[3-1][3-1][1-1][3-1] = C_IJ[3-1,5-1]
C_ijkl[3-1][3-1][1-1][2-1] = C_IJ[3-1,6-1]

C_ijkl[2-1][3-1][1-1][1-1] = C_IJ[4-1,1-1]
C_ijkl[2-1][3-1][2-1][2-1] = C_IJ[4-1,2-1]
C_ijkl[2-1][3-1][3-1][3-1] = C_IJ[4-1,3-1]
C_ijkl[2-1][3-1][2-1][3-1] = C_IJ[4-1,4-1]
C_ijkl[2-1][3-1][1-1][3-1] = C_IJ[4-1,5-1]
C_ijkl[2-1][3-1][1-1][2-1] = C_IJ[4-1,6-1]

C_ijkl[3-1][1-1][1-1][1-1] = C_IJ[5-1,1-1]
C_ijkl[3-1][1-1][2-1][2-1] = C_IJ[5-1,2-1]
C_ijkl[3-1][1-1][3-1][3-1] = C_IJ[5-1,3-1]
C_ijkl[3-1][1-1][2-1][3-1] = C_IJ[5-1,4-1]
C_ijkl[3-1][1-1][1-1][3-1] = C_IJ[5-1,5-1]
C_ijkl[3-1][1-1][1-1][2-1] = C_IJ[5-1,6-1]

C_ijkl[1-1][2-1][1-1][1-1] = C_IJ[6-1,1-1]
C_ijkl[1-1][2-1][2-1][2-1] = C_IJ[6-1,2-1]
C_ijkl[1-1][2-1][3-1][3-1] = C_IJ[6-1,3-1]
C_ijkl[1-1][2-1][2-1][3-1] = C_IJ[6-1,4-1]
C_ijkl[1-1][2-1][1-1][3-1] = C_IJ[6-1,5-1]
C_ijkl[1-1][2-1][1-1][2-1] = C_IJ[6-1,6-1]

print(C_ijkl)
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                first_num = None
                eq_mass = [C_ijkl[i][j][k][l], C_ijkl[j][i][k][l], C_ijkl[i][j][l][k], C_ijkl[k][l][i][j]]
                for el in eq_mass:
                    if first_num == None:
                        first_num = el
                for el in eq_mass:
                    if not (el == None) and not (el == first_num):
                        print(f"EXIT; ijkl = {i} {j} {k} {l}     ", eq_mass)
                        exit()
##                if C_ijkl[i][j][k][l]
print(C_ijkl)
