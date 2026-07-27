# Quantum Computing Notation & Pronunciation Guide

---

## Dirac Notation (Bra-Ket Notation)

This is the standard way to write quantum states, invented by physicist Paul Dirac.

| Symbol | How to say it | Meaning |
|--------|--------------|---------|
| `\|0⟩` | "ket zero" or "ket nought" | Quantum state representing classical 0 |
| `\|1⟩` | "ket one" | Quantum state representing classical 1 |
| `\|ψ⟩` | "ket psi" | A general quantum state (psi is a Greek letter) |
| `\|φ⟩` | "ket phi" | Another general quantum state (phi is a Greek letter) |
| `\|+⟩` | "ket plus" | The superposition state (\|0⟩+\|1⟩)/√2 |
| `\|−⟩` | "ket minus" | The superposition state (\|0⟩−\|1⟩)/√2 |
| `\|ψ⟩⟨ψ\|` | "ket psi bra psi" | Outer product / projection operator |
| `⟨ψ\|ψ⟩` | "bra psi ket psi" | Inner product (gives a number) |

### What is a Ket?
- A ket `\|ψ⟩` is a **column vector** representing a quantum state
- The matching "bra" `⟨ψ\|` is the **row vector** (conjugate transpose)
- Together they form "bracket" = inner product

### Writing Kets
- In LaTeX: `\|0\rangle` renders as \|0⟩
- In text/PennyLane code: just use the state variable name, e.g. `qubit0`
- In conversation: "ket zero", "ket one", "ket psi"

---

## Greek Letters Used in Quantum Computing

| Letter | Capital | Lowercase | How to say | Common use |
|--------|---------|-----------|-----------|------------|
| Alpha | Α | α | "AL-fuh" | Rotation angle |
| Beta | Β | β | "BAY-tuh" | Rotation angle |
| Gamma | Γ | γ | "GAM-uh" | Phase angle |
| Delta | Δ | δ | "DEL-tuh" | Change / difference |
| Epsilon | Ε | ε | "EP-suh-lon" | Small error tolerance |
| Eta | Η | η | "AY-tuh" | Efficiency |
| Theta | Θ | θ | "THAY-tuh" | Rotation angle on Bloch sphere |
| Lambda | Λ | λ | "LAM-duh" | Eigenvalue, phase angle |
| Mu | Μ | μ | "MYOO" | Chemical potential |
| Omega | Ω | ω | "oh-MAY-guh" | Angular frequency, Ohm |
| Phi | Φ | φ | "FYE" or "FEE" | Phase angle, Euler angle |
| Pi | Π | π | "PIE" | 3.14159... (half-rotation) |
| Psi | Ψ | ψ | "PSY" (like "psyche") | Quantum state |
| Rho | Ρ | ρ | "ROH" | Density matrix |
| Sigma | Σ | σ | "SIG-muh" | Pauli gates (σx, σy, σz) |
| Tau | Τ | τ | "TOW" | Time constant |
| Omega | Ω | ω | "oh-MAY-guh" | Angular frequency |

---

## Pauli Gates (also called σ gates)

| Gate | Math Name | How to say | Matrix |
|------|-----------|-----------|--------|
| X | σ_x (sigma-x) | "sigma X" or "Pauli X" | [[0,1],[1,0]] — bit flip (NOT gate) |
| Y | σ_y (sigma-y) | "sigma Y" or "Pauli Y" | [[0,-i],[i,0]] — bit + phase flip |
| Z | σ_z (sigma-z) | "sigma Z" or "Pauli Z" | [[1,0],[0,-1]] — phase flip |

---

## Common Quantum Terms & Pronunciation

| Term | How to say | Meaning |
|------|-----------|---------|
| Qubit | "CUE-bit" | Quantum bit — the basic unit of quantum information |
| Superposition | "soo-per-puh-ZISH-un" | A qubit being in multiple states at once |
| Entanglement | "en-TANG-gul-ment" | Quantum connection between qubits |
| Amplitude | "AM-plih-tood" | The coefficient of a quantum state (can be complex) |
| Measurement | "mezh-er-ment" | Collapsing a quantum state to a classical outcome |
| Unitary | "yoo-NIH-tair-ee" | A matrix that preserves norms (reversible operation) |
| Hermitian | "HER-mih-tee-un" | Equal to its own conjugate transpose (observable) |
| Eigenvalue | "EYE-gun-vallyoo" | Value λ where A\|v⟩ = λ\|v⟩ |
| Eigenvector | "EYE-gun-veck-ter" | Vector \|v⟩ where A\|v⟩ = λ\|v⟩ |
| Hamiltonian | "ham-il-TOH-nee-un" | Operator describing total energy of a system |
| Hadamard | "HAD-uh-mard" | H gate — creates superposition |
| Toffoli | "toh-FOH-lee" | CCX gate — two-control NOT |
| Fredkin | "FRED-kin" | CSWAP gate — controlled swap |
| CNOT | "see-NOT" | Controlled-NOT gate |
| Bloch sphere | "BLOCK sfeer" | Geometric representation of a single qubit |
| Interference | "in-ter-FEER-ence" | Quantum waves reinforcing or canceling |
| Coherence | "koh-HER-ence" | Maintaining quantum superposition |
| Decoherence | "dee-koh-HER-ence" | Loss of quantum information to environment |
| Fidelity | "fih-DEL-ih-tee" | How close a state is to the target state |
| Tomography | "tuh-MOG-ruh-fee" | Reconstructing a quantum state from measurements |

---

## Mathematical Symbols in Quantum Computing

| Symbol | How to say | Meaning |
|--------|-----------|---------|
| ⟨ \| | "bra" | Left half of inner product (row vector) |
| \| ⟩ | "ket" | Right half of inner product (column vector) |
| ⊗ | "tensor" or "cross" | Tensor product (combining qubits): \|0⟩⊗\|1⟩ = \|01⟩ |
| ⊕ | "direct sum" or "XOR" | Modular addition |
| ≡ | "equivalent to" or "defined as" | Definition or identity |
| ∝ | "proportional to" | Scales by a constant factor |
| ⟩ | "ket" | Right side of bracket notation |
| † | "dagger" | Conjugate transpose: S† = "S dagger" |
| √ | "square root" | √2 = "root two" |
| i | "eye" | Imaginary unit: i² = −1 |
| ℂ | "complex numbers" | Set of complex numbers |
| ℝ | "real numbers" | Set of real numbers |
| ω | "omega" | ω = e^(2πi/N), primitive root of unity in DFT/QFT |

---

## PennyLane Code → Spoken form

| Code | Say it as |
|------|-----------|
| `qp.PauliX(wires=0)` | "Apply Pauli X to qubit zero" |
| `qp.Hadamard(wires=0)` | "Apply Hadamard to qubit zero" |
| `qp.CNOT(wires=[0,1])` | "CNOT with control zero, target one" |
| `qp.CZ(wires=[0,1])` | "Controlled-Z on qubits zero and one" |
| `qp.SWAP(wires=[0,1])` | "Swap qubits zero and one" |
| `qp.Toffoli(wires=[0,1,2])` | "Toffoli with controls zero and one, target two" |
| `qp.ControlledPhaseShift(λ, wires=[0,1])` | "Controlled phase shift of lambda on qubits zero and one" |
| `qp.ctrl(U, control=0)` | "Controlled U with control qubit zero" |
| `@qp.qnode(dev)` | "Q-node" or "quantum node" — a quantum circuit function |
| `return qp.counts()` | "Return counts" — measure all qubits |
| `return qp.state()` | "Return state" — get the full quantum state |
| `qp.matrix(circuit)()` | "Matrix of the circuit" — get the unitary matrix |

---

## Fraction & Power Pronunciation

| Expression | How to say |
|-----------|-----------|
| e^(2πiφ) | "e to the two-pi-i-phi" |
| 1/√2 | "one over root two" |
| 2^n | "two to the n" |
| n² | "n squared" |
| π/4 | "pi over four" or "pi by four" |
| e^(iπ/4) | "e to the i-pi-by-four" |
| √Z | "root Z" or "square root of Z" |
| T⁴ = Z | "T to the fourth equals Z" |
