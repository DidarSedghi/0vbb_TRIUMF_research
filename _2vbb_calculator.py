"""
2vbb calculations debug code.

Ex_energy = E_inter + average(Ei, Ef)

'k' is intermediate state:
op_l = < f | opl | k >
op_r = < k | opr | i >

sum = op_l * op_r/Ex_energy
"""


op_l = -0.278995
op_r = -0.039877

Ex_energy = 2.874282
inter = -62.16550720

constant = 65.0397892

sum_ = (op_l * op_r)/Ex_energy

print(round(sum_, 6))

op_l2 = 0.058098
op_r2 = 0.044247

Ex_energy2 = 4.428780
inter2 = -60.61100966

new = constant + inter2
print(new)