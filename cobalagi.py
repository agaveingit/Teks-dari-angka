from decimal import Decimal

PRESISI: list[Decimal] = [
            Decimal('0.1'),
            Decimal('0.01'),
            Decimal('0.001'),
            Decimal('0.0001'),
            Decimal('0.00001')
        ]

def pisah_presisi(i: float) -> tuple[int, Decimal]:
    # Wajib konversi float ke string dulu sebelum ke Decimal
    angka_decimal = Decimal(str(i))
    utuh = int(angka_decimal)
    pecahan = angka_decimal - Decimal(utuh)
    return utuh, pecahan

def cari_presisi(i: Decimal): # Input 'i' sebaiknya diubah jadi tipe Decimal
    # 1. Pakai indeks dan nilai dari enumerate
    for indeks, presisi_val in enumerate(PRESISI):
        # 2. Bandingkan 'i' dengan nilai presisi (presisi_val)
        if i >= presisi_val:
            # Lu bisa kembalikan indeks atau nilai
            return f"Berhasil di indeks {indeks} dengan presisi {presisi_val}"
    
    # Tambahkan pengembalian default jika tidak ada yang cocok
    return "Tidak ada presisi yang cocok."

# Contoh eksekusi lu:
y_decimal, z_decimal = pisah_presisi(2.33)
print(f"Hasil pisah_presisi: {y_decimal}, {z_decimal}") # Hasil: 2, 0.33

w = cari_presisi(z_decimal)
print(f"Hasil cari_presisi: {w}") # Hasil: Berhasil di indeks 0 dengan presisi 0.1