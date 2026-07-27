import pennylane as qml
import numpy as np

def iqft(n, qubits):

    #Swap the qubits
    for i in range(n//2):
        qml.SWAP(wires=[qubits[i], qubits[n-i-1]])

    #For each qubit
    for i in range(n-1, -1, -1):
        #Apply CR_k gates where j is the control and i is the target
        k = n - i  #We start with k=n-i
        for j in range(n-1, i, -1):
            #Define and apply CR_k gate
            qml.ControlledPhaseShift(-np.pi * 2 / 2**k, wires=[qubits[j], qubits[i]])
            k = k - 1  #Decrement at each step

        #Apply Hadamard to the qubit
        qml.Hadamard(wires=qubits[i])
