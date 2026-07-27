import pennylane as qml
import numpy as np

def qft(n, qubits):
    #For each qubit
    for i in range(n):
        #Apply Hadamard to the qubit
        qml.Hadamard(wires=qubits[i])
        #Apply CR_j gates where j is the control and i is the target
        for j in range(i+1, n):
            #Define and apply CR_j gate
            qml.ControlledPhaseShift(np.pi * 2 / 2**j, wires=[qubits[j], qubits[i]])

    #Swap gates
    for i in range(n//2):
        qml.SWAP(wires=[qubits[i], qubits[n-i-1]])
