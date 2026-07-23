import pennylane as qp
import numpy as np

# U is a 2-qubit unitary with eigenvector |11>
array = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, -0.4762382+0.87931631j]])

def CU(control_wire, target_wires, power):
    """Controlled-U^power: control_wire is control, target_wires are target qubits."""
    powered = np.linalg.matrix_power(array, power)
    qp.ctrl(qp.QubitUnitary(powered, wires=target_wires), control=control_wire)

def Ux(x, N):

    k = 1
    while N > 2**k:
        k = k + 1

    u = np.zeros([2**k, 2**k], dtype=int)

    for i in range(N):
        u[x*i%N][i] = 1
    for i in range(N, 2**k):
        u[i][i] = 1

    def CUx_op(control_wire, target_wires, power):
        """Controlled-XU^power: control_wire is control, target_wires are target qubits."""
        powered = np.linalg.matrix_power(u, power)
        qp.ctrl(qp.QubitUnitary(powered, wires=target_wires), control=control_wire)

    return CUx_op
