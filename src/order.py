import numpy as np
import pennylane as qp

u5 = np.zeros([32, 32], dtype = int) 

for i in range(21):
    u5[5*i%21][i]=1
for i in range(21,32):
    u5[i][i]=1
    
def CU5(wires):
    """Controlled-U5: wires[0] is control, wires[1:] are target qubits."""
    qp.ctrl(qp.QubitUnitary(u5, wires=wires[1:]), control=wires[0])

u8 = np.zeros([16, 16], dtype = int) 

for i in range(15):
    u8[8*i%15][i]=1
for i in range(15,16):
    u8[i][i]=1
    
def CU8(wires):
    """Controlled-U8: wires[0] is control, wires[1:] are target qubits."""
    qp.ctrl(qp.QubitUnitary(u8, wires=wires[1:]), control=wires[0])
