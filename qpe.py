import pennylane as qml
import numpy as np
from operator_cu import Ux
from iqft import iqft

def qpe(t, control, target, x, N):
    
    #Apply Hadamard to control qubits
    for q in control:
        qml.Hadamard(wires=q)
    
    #Apply CU gates
    for i in range(t):
        #Obtain the power of x modulo N
        xi = pow(x, 2**i, N)
        #Get the controlled unitary for this power
        CUx_op = Ux(xi, N)
        #Apply CUi gate where t-i-1 is the control
        CUx_op([control[t-i-1]] + target)
        
    #Apply inverse QFT
    iqft(t, control)
