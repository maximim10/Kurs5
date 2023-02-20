import sympy

E11 = 430
E22 = 6.9
v12 = 0.3
v23 = 0.49
G12 = 2.65
G23 = 2.32
v21 = v12/E11*E22
v32 = v23
J_IJ = sympy.Matrix([[1/E11, -v21/E22, -v21/E22, 0, 0, 0],
                     [-v12/E11, 1/E22, -v32/E22, 0, 0, 0],
                     [-v12/E11, -v23/E22, 1/E22, 0, 0, 0],
                     [0, 0, 0, 1/G12, 0 ,0],
                     [0, 0, 0, 0, 1/G23, 0],
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
for three_times in range(1):
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
                        if not (el == None) and not abs(el-first_num)<1e-7:
                            print(f"EXIT; ijkl = {i} {j} {k} {l}     ", eq_mass)
                            exit()
                    for el_num in range(len(eq_mass)):
                        C_ijkl[i][j][k][l] = first_num
                        C_ijkl[j][i][k][l] = first_num
                        C_ijkl[i][j][l][k] = first_num
                        C_ijkl[k][l][i][j] = first_num
    ##                if C_ijkl[i][j][k][l]
print(C_ijkl)
