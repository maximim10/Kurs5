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
C_ijkl[1-1][1-1][2-1][3-1] = C_IJ[1-1,4-1]/2
C_ijkl[1-1][1-1][1-1][3-1] = C_IJ[1-1,5-1]/2
C_ijkl[1-1][1-1][1-1][2-1] = C_IJ[1-1,6-1]/2

C_ijkl[2-1][2-1][1-1][1-1] = C_IJ[2-1,1-1]
C_ijkl[2-1][2-1][2-1][2-1] = C_IJ[2-1,2-1]
C_ijkl[2-1][2-1][3-1][3-1] = C_IJ[2-1,3-1]
C_ijkl[2-1][2-1][2-1][3-1] = C_IJ[2-1,4-1]/2
C_ijkl[2-1][2-1][1-1][3-1] = C_IJ[2-1,5-1]/2
C_ijkl[2-1][2-1][1-1][2-1] = C_IJ[2-1,6-1]/2

C_ijkl[3-1][3-1][1-1][1-1] = C_IJ[3-1,1-1]
C_ijkl[3-1][3-1][2-1][2-1] = C_IJ[3-1,2-1]
C_ijkl[3-1][3-1][3-1][3-1] = C_IJ[3-1,3-1]
C_ijkl[3-1][3-1][2-1][3-1] = C_IJ[3-1,4-1]/2
C_ijkl[3-1][3-1][1-1][3-1] = C_IJ[3-1,5-1]/2
C_ijkl[3-1][3-1][1-1][2-1] = C_IJ[3-1,6-1]/2

C_ijkl[2-1][3-1][1-1][1-1] = C_IJ[4-1,1-1]
C_ijkl[2-1][3-1][2-1][2-1] = C_IJ[4-1,2-1]
C_ijkl[2-1][3-1][3-1][3-1] = C_IJ[4-1,3-1]
C_ijkl[2-1][3-1][2-1][3-1] = C_IJ[4-1,4-1]/2
C_ijkl[2-1][3-1][1-1][3-1] = C_IJ[4-1,5-1]/2
C_ijkl[2-1][3-1][1-1][2-1] = C_IJ[4-1,6-1]/2

C_ijkl[3-1][1-1][1-1][1-1] = C_IJ[5-1,1-1]
C_ijkl[3-1][1-1][2-1][2-1] = C_IJ[5-1,2-1]
C_ijkl[3-1][1-1][3-1][3-1] = C_IJ[5-1,3-1]
C_ijkl[3-1][1-1][2-1][3-1] = C_IJ[5-1,4-1]/2
C_ijkl[3-1][1-1][1-1][3-1] = C_IJ[5-1,5-1]/2
C_ijkl[3-1][1-1][1-1][2-1] = C_IJ[5-1,6-1]/2

C_ijkl[1-1][2-1][1-1][1-1] = C_IJ[6-1,1-1]
C_ijkl[1-1][2-1][2-1][2-1] = C_IJ[6-1,2-1]
C_ijkl[1-1][2-1][3-1][3-1] = C_IJ[6-1,3-1]
C_ijkl[1-1][2-1][2-1][3-1] = C_IJ[6-1,4-1]/2
C_ijkl[1-1][2-1][1-1][3-1] = C_IJ[6-1,5-1]/2
C_ijkl[1-1][2-1][1-1][2-1] = C_IJ[6-1,6-1]/2

##print(C_ijkl)
for three_times in range(3):
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

print(f"{C_ijkl = }")

N_kpq0 = [[[None, None, None] for j in range(3)] for i in range(3)]
for p in range(3):
    for q0 in range(3):
        A = sympy.Matrix([[C_ijkl[0][2][0][2], C_ijkl[0][2][1][2], C_ijkl[0][2][2][2]],
                          [C_ijkl[1][2][0][2], C_ijkl[1][2][1][2], C_ijkl[1][2][2][2]],
                          [C_ijkl[2][2][0][2], C_ijkl[2][2][1][2], C_ijkl[2][2][2][2]]])
        B = sympy.Matrix([[-C_ijkl[0][2][p][q0]],
                          [-C_ijkl[1][2][p][q0]],
                          [-C_ijkl[2][2][p][q0]]])
##        print(f"{A = },\n {B = }")
        N_kpq0[0][p][q0] = (A**-1*(-B))[0]
        N_kpq0[1][p][q0] = (A**-1*(-B))[1]
        N_kpq0[2][p][q0] = (A**-1*(-B))[2]
##        print(f"{N_kpq0[0][p][q0] = }, {N_kpq0[1][p][q0] = }, {N_kpq0[2][p][q0] = }\n\n")
##print(f"{N_kpq0 = }")

for k in range(3):
    print(f"{N_kpq0[k] = }")

N_kpq0q1 = [[[[None, None, None] for k in range(3)] for j in range(3)] for i in range(3)]
for p in range(3):
    for q0 in range(3):
        for q1 in range(3):
            A = sympy.Matrix([[C_ijkl[0][2][0][2], C_ijkl[0][2][1][2], C_ijkl[0][2][2][2]],
                              [C_ijkl[1][2][0][2], C_ijkl[1][2][1][2], C_ijkl[1][2][2][2]],
                              [C_ijkl[2][2][0][2], C_ijkl[2][2][1][2], C_ijkl[2][2][2][2]]])
            B = sympy.Matrix([[C_ijkl[0][q1][p][q0]],
                              [C_ijkl[1][q1][p][q0]],
                              [C_ijkl[2][q1][p][q0]]])
            C = sympy.Matrix([[C_ijkl[0][q1][0][2], C_ijkl[0][q1][1][2], C_ijkl[0][q1][2][2]],
                              [C_ijkl[1][q1][0][2], C_ijkl[1][q1][1][2], C_ijkl[1][q1][2][2]],
                              [C_ijkl[2][q1][0][2], C_ijkl[2][q1][1][2], C_ijkl[2][q1][2][2]]])
            D = sympy.Matrix([[C_ijkl[0][2][0][q1], C_ijkl[0][2][1][q1], C_ijkl[0][2][2][q1]],
                              [C_ijkl[1][2][0][q1], C_ijkl[1][2][1][q1], C_ijkl[1][2][2][q1]],
                              [C_ijkl[2][2][0][q1], C_ijkl[2][2][1][q1], C_ijkl[2][2][2][q1]]])
            E = sympy.Matrix([[N_kpq0[0][p][q0]],
                              [N_kpq0[1][p][q0]],
                              [N_kpq0[2][p][q0]]])
            N_kpq0q1[0][p][q0][q1] = (A**-1*(B-(C+D)*E))[0]
            N_kpq0q1[1][p][q0][q1] = (A**-1*(B-(C+D)*E))[1]
            N_kpq0q1[2][p][q0][q1] = (A**-1*(B-(C+D)*E))[2]
for k in range(3):
    print(f"{N_kpq0q1[k] = }")
C1_kpq0q1 = [[[[None, None, None] for k in range(3)] for j in range(3)] for i in range(3)]
for p in range(3):
    for q0 in range(3):
        for q1 in range(3):
            A = sympy.Matrix([[C_ijkl[0][2][0][2], C_ijkl[0][2][1][2], C_ijkl[0][2][2][2]],
                              [C_ijkl[1][2][0][2], C_ijkl[1][2][1][2], C_ijkl[1][2][2][2]],
                              [C_ijkl[2][2][0][2], C_ijkl[2][2][1][2], C_ijkl[2][2][2][2]]])
            B = sympy.Matrix([[C_ijkl[0][2][0][q1], C_ijkl[0][2][1][q1], C_ijkl[0][2][2][q1]],
                              [C_ijkl[1][2][0][q1], C_ijkl[1][2][1][q1], C_ijkl[1][2][2][q1]],
                              [C_ijkl[2][2][0][q1], C_ijkl[2][2][1][q1], C_ijkl[2][2][2][q1]]])
            C = sympy.Matrix([[N_kpq0[0][p][q0]],
                              [N_kpq0[1][p][q0]],
                              [N_kpq0[2][p][q0]]])
            D = sympy.Matrix([[N_kpq0q1[0][p][q0][q1]],
                              [N_kpq0q1[1][p][q0][q1]],
                              [N_kpq0q1[2][p][q0][q1]]])
            C1_kpq0q1[0][p][q0][q1] = -(A**-1*B*C/12+D/8)[0]
            C1_kpq0q1[1][p][q0][q1] = -(A**-1*B*C/12+D/8)[1]
            C1_kpq0q1[2][p][q0][q1] = -(A**-1*B*C/12+D/8)[2]
for k in range(3):
    print(f"{C1_kpq0q1[k] = }")


N_kpq0q1q2 = [[[[[None, None, None] for l in range(3)] for k in range(3)] for j in range(3)] for i in range(3)]
for p in range(3):
    for q0 in range(3):
        for q1 in range(3):
            for q2 in range(3):
                A = sympy.Matrix([[C_ijkl[0][2][0][2], C_ijkl[0][2][1][2], C_ijkl[0][2][2][2]],
                                  [C_ijkl[1][2][0][2], C_ijkl[1][2][1][2], C_ijkl[1][2][2][2]],
                                  [C_ijkl[2][2][0][2], C_ijkl[2][2][1][2], C_ijkl[2][2][2][2]]])
                B = sympy.Matrix([[C_ijkl[0][q2][0][q1], C_ijkl[0][q2][1][q1], C_ijkl[0][q2][2][q1]],
                                  [C_ijkl[1][q2][0][q1], C_ijkl[1][q2][1][q1], C_ijkl[1][q2][2][q1]],
                                  [C_ijkl[2][q2][0][q1], C_ijkl[2][q2][1][q1], C_ijkl[2][q2][2][q1]]])
                C = sympy.Matrix([[N_kpq0[0][p][q0]],
                                  [N_kpq0[1][p][q0]],
                                  [N_kpq0[2][p][q0]]])



















        
