"""Simulate ideal single-qubit BB84 measurements and optional channel noise."""
import argparse
import random

def measure(bit, preparation_basis, measurement_basis, rng):
    # In the ideal model, Z and X basis states have squared overlap 1/2.
    return bit if preparation_basis == measurement_basis else rng.randrange(2)

def simulate(shots, noise, rng):
    sifted = []
    for _ in range(shots):
        bit, alice_basis, bob_basis = (rng.randrange(2) for _ in range(3))
        received = measure(bit, alice_basis, bob_basis, rng)
        if rng.random() < noise:
            received ^= 1
        if alice_basis == bob_basis:
            sifted.append(bit != received)

    rng.shuffle(sifted)
    sample = sifted[:len(sifted) // 2]
    errors = sum(sample) / len(sample) if sample else None
    return len(sifted), len(sample), errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shots", type=int, default=4096)
    parser.add_argument("--noise", type=float, default=0)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    if args.shots < 1 or not 0 <= args.noise <= 1:
        parser.error("Use positive shots and noise in [0, 1].")
    sifted, sampled, qber = simulate(args.shots, args.noise, random.Random(args.seed))
    print(f"Transmitted: {args.shots} | Sifted: {sifted} | Sampled: {sampled}")
    if qber is None:
        print("Too few matching-basis measurements to estimate QBER.")
    else:
        print(f"Sample quantum bit error rate: {qber:.2%}")

if __name__ == "__main__":
    main()
