# =========================================================
# IMPLEMENTASI ALGORITMA RSA FROM SCRATCH
# =========================================================
# Nama  : Muhammad Reyhan Sheva RizQulah
# NIM   : 25051204261
# Kelas : 2024 TIH
#
# DESKRIPSI:
# Program ini merupakan implementasi algoritma RSA tanpa
# menggunakan library kriptografi instan.
#
# SEJARAH SINGKAT RSA:
# RSA dikembangkan pada tahun 1977 oleh Ron Rivest,
# Adi Shamir, dan Leonard Adleman.
# Nama RSA sendiri berasal dari inisial nama belakang mereka.
# Algoritma ini merupakan algoritma kriptografi kunci publik
# pertama yang banyak digunakan untuk keamanan data digital.
# Keamanannya bergantung pada sulitnya memfaktorkan bilangan
# besar menjadi dua bilangan prima.
# =========================================================

# Fungsi mencari GCD Greatest Common Divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Extended Euclidean Algorithm
def extended_euclidean(e, phi):
    if e == 0:
        return phi, 0, 1
    else:
        gcd_value, x1, y1 = extended_euclidean(phi % e, e)
        x = y1 - (phi // e) * x1
        y = x1
        return gcd_value, x, y


# Fungsi mencari invers modulo
def mod_inverse(e, phi):
    gcd_value, x, y = extended_euclidean(e, phi)
    if gcd_value != 1:
        return None
    else:
        return x % phi


# PEMBANGKITAN KUNCI (KEY GENERATION)
def generate_keys():
    print("========== PROSES PEMBANGKITAN KUNCI ==========")

    # Pilih dua bilangan prima
    p = 17
    q = 11

    print("Bilangan prima p =", p)
    print("Bilangan prima q =", q)

    # Hitung n
    n = p * q
    print("n = p × q =", n)

    # Hitung totient Euler
    phi = (p - 1) * (q - 1)
    print("phi(n) =", phi)

    # Pilih e yang relatif prima terhadap phi
    e = 3
    while gcd(e, phi) != 1:
        e += 1

    print("Public exponent (e) =", e)

    # Hitung d sebagai invers modulo
    d = mod_inverse(e, phi)
    print("Private exponent (d) =", d)

    print("Public Key  =", (e, n))
    print("Private Key =", (d, n))

    return (e, n), (d, n)


# ENKRIPSI
def encrypt(public_key, plaintext):
    e, n = public_key
    print("\n========== PROSES ENKRIPSI ==========")

    cipher = []

    for char in plaintext:
        m = ord(char)  # Konversi ke ASCII
        c = pow(m, e, n)  # Rumus RSA
        print(f"Karakter: {char}")
        print(f"ASCII   : {m}")
        print(f"Cipher  : {c}")
        print("----------------------------------")
        cipher.append(c)

    return cipher


# DEKRIPSI
def decrypt(private_key, ciphertext):
    d, n = private_key
    print("\n========== PROSES DEKRIPSI ==========")

    plaintext = ""

    for c in ciphertext:
        m = pow(c, d, n)
        char = chr(m)
        print(f"Cipher  : {c}")
        print(f"ASCII   : {m}")
        print(f"Karakter: {char}")
        print("----------------------------------")
        plaintext += char

    return plaintext

# PROGRAM UTAMA
def main():
    public_key, private_key = generate_keys()

    print("\nMasukkan pesan yang ingin dienkripsi:")
    message = input("> ")
    
    print("\nPlaintext:", message)

    encrypted_message = encrypt(public_key, message)
    print("Ciphertext:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Hasil Dekripsi:", decrypted_message)


if __name__ == "__main__":
    main()