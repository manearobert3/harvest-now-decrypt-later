# Harvest Now, Decrypt Later (HNDL) Simulation

## Overview

This repository contains a Python Proof-of-Concept (PoC) demonstrating the "Harvest Now, Decrypt Later" (HNDL) attack model.

The HNDL attack is a long-term network security threat where adversaries passively intercept and store encrypted network traffic (such as TLS sessions) today, with the intention of decrypting it years later when a Cryptographically Relevant Quantum Computer (CRQC) becomes available.

This script simulates the entire lifecycle of the attack:

1. **The Harvest Phase (2024):** Generating an RSA-2048 key, encrypting a simulated TLS session key, and storing the ciphertext.
2. **The Decrypt Phase (2035):** Using a mock function to simulate Shor's algorithm successfully factoring the RSA modulus, rebuilding the private key, and recovering the original plaintext.

## Prerequisites

To run this simulation, you need Python 3 installed on your system, along with the `pycryptodome` library.

**Important:** Ensure you do not have the legacy `crypto` library installed, as it conflicts with `pycryptodome`.

## Installation

Install the required cryptography library via pip:

```bash
pip install pycryptodome
```
