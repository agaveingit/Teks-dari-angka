from decimal import Decimal

PRESISI: list[Decimal] = [
            Decimal('0.1'),
            Decimal('0.01'),
            Decimal('0.001'),
            Decimal('0.0001'),
            Decimal('0.00001')
        ]

def pisah_presisi(i: float) -> tuple[int, Decimal]:
    angka_decimal = Decimal(str(i))
    utuh = int(angka_decimal)
    pecahan = angka_decimal - Decimal(utuh)
    return utuh, pecahan

def cari_presisi(i: Decimal): 
    SATUAN: list[str] = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    for indeks, presisi_val in enumerate(PRESISI):
        if i >= presisi_val:
            floating_point_len: int = len(str(i))
            baca: list[str] = ["koma"]
            for idx in range(floating_point_len - 2):
                belakang_koma: str = str(i)
                int_bk = belakang_koma[idx + 2]
                hasil = SATUAN[int(int_bk)]
                baca.append(hasil)
            return f"For loop 1. Index: {indeks}, presisi: {presisi_val}, panjang {floating_point_len}, {baca}"
    
    return "Tidak ada presisi yang cocok."

y_decimal, z_decimal = pisah_presisi(2.879)
print(f"Hasil pisah_presisi: {y_decimal}, {z_decimal}") 

w = cari_presisi(z_decimal)
print(f"Hasil cari_presisi: {w}") 