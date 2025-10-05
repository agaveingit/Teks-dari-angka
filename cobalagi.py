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

def cari_presisi(i: Decimal) -> str: 
    SATUAN: list[str] = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    floating_point_len: int = len(str(i))
    hasil_baca: list[str] = ["koma"]
    for idx in range(floating_point_len - 2):
        angka_desimal: str = str(i)
        baca_desimal: int = int(angka_desimal[idx + 2])
        hasil: str= SATUAN[baca_desimal]
        hasil_baca.append(hasil)
    hasil_baca = " ".join(hasil_baca)
    return f"panjang {floating_point_len}, {hasil_baca}"

depan_koma, belakang_koma = pisah_presisi(2.879)

w = cari_presisi(belakang_koma)
print(f"Hasil cari_presisi: {w}") 