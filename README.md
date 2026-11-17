# Quantum Key Lab

A dependency-free Python simulation of BB84 quantum key distribution. Alice prepares one of four single-qubit states using the Z or X basis. Bob independently chooses a measurement basis. A matching basis recovers Alice's bit in the ideal channel. Measuring in the other basis yields a uniformly random bit.

| Basis | Bit 0 | Bit 1 |
| --- | --- | --- |
| Z | \|0⟩ | \|1⟩ |
| X | \|+⟩ | \|−⟩ |

Alice and Bob keep matching-basis rounds and disclose a random sample to estimate the quantum bit error rate (QBER). The optional noise parameter models independent flips of the measured bits.

```bash
python3 bb84.py --seed 42
python3 bb84.py --seed 42 --noise 0.10
```

Expect zero sampled errors in the ideal run and roughly 10% in the noisy run. Finite samples vary. This educational model uses ideal measurement probabilities and omits authenticated classical communication, error correction, and privacy amplification. It never exports key material.
