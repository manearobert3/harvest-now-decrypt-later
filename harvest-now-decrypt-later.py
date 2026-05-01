import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("Generating standard RSA-2048 keys (This takes a moment)...")
key = RSA.generate(2048)
public_key = key.publickey()

actual_p = key.p
actual_q = key.q

def mock_shors_algorithm(n, p, q):
    """
    Simulates a Cryptographically Relevant Quantum Computer (CRQC).
    In reality, Shor's algorithm uses quantum superposition and period finding
    to factor 'n' in polynomial time. We just simulate the delay here.
    """
    print("\n[Quantum Computer] Initializing Shor's Algorithm...")
    print("[Quantum Computer] Running quantum circuits...")
    time.sleep(3)
    return p, q

def rebuild_private_key(p, q, e):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return RSA.construct((p * q, e, d, p, q))

print("YEAR 2024")
secret = b"TOP SECRET: TLS session key 0xDEADBEEF"
ciphertext = PKCS1_OAEP.new(public_key).encrypt(secret)

print(f"[Alice]    message   : {secret.decode()}")
print(f"[Alice]    ciphertext: {ciphertext.hex()[:48]}...")

print("\n[Network]  Adversary intercepts traffic.")
print("[Network]  Ciphertext routed to massive data storage facility.")
print("[Network]  Waiting for technology to advance...")
time.sleep(2) 

print("YEAR 2035")
t0 = time.time()

p, q = mock_shors_algorithm(public_key.n, actual_p, actual_q)
elapsed = time.time() - t0

recovered_key = rebuild_private_key(p, q, public_key.e)
plaintext = PKCS1_OAEP.new(recovered_key).decrypt(ciphertext)

print(f"[Attacker] Factored 2048-bit modulus in {elapsed:.4f}s using Simulated CRQC.")
print(f"[Attacker] Decrypted Payload : {plaintext.decode()}")
print(f"\n[{'OK' if plaintext == secret else 'FAIL'}] Original payload matches decrypted data!")