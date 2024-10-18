"""
2vbb calculations debug code.

Ex_energy = E_inter + average(Ei, Ef)

'k' is intermediate state:
op_l = < f | opl | k >
op_r = < k | opr | i >

sum = op_l * op_r/Ex_energy
"""

def cntr_2vbb(opl, opr, ex_energy):
    return round((opl * opr)/ex_energy, 6)

opl1 = -0.278995
opr1 = -0.039877
ex_energy1 = 2.874282

cntr1 = cntr_2vbb(opl1, opr1, ex_energy1)

print(cntr1)

opl2 = 0.058098
opr2 = 0.044247
ex_energy2 = 4.428780

cntr2 = cntr_2vbb(opl2, opr2, ex_energy2)

print(cntr2)

print(cntr1 + cntr2)