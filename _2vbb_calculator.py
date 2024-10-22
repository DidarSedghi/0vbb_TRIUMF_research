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

