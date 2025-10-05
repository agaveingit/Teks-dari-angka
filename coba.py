from decimal import Decimal

class Desimal:
    def __init__(self):
        self.BELAKANG_KOMA: list[float]= [
            0.1, 
            0.01, 
            0.001, 
            0.0001, 
            0.00001]

    def _baca_desimal(self, angka: float) -> str:
        depan_koma: int = int(angka)
        setelah_koma: float = angka - depan_koma
        raise NotImplementedError("Ntar ya")

def pisah_desimal_decimal(angka: float) -> tuple[int, Decimal]:
    """Memisahkan angka desimal menggunakan modul Decimal untuk presisi tinggi."""
    d = Decimal(str(angka))  # Inisialisasi dari string untuk presisi
    utuh = int(d)
    pecahan = d - Decimal(utuh)
    return utuh, pecahan

y_decimal, z_decimal = pisah_desimal_decimal(25.4321)
print(f"Menggunakan Decimal:    {y_decimal}, {z_decimal}")
