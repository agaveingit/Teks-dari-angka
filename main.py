from decimal import Decimal


class Konverter:
    """
    Mengonversi angka menjadi teks ejaannya dalam Bahasa Indonesia.
    """
    def __init__(self) -> None:
        self.SATUAN: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
        self.BELASAN: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", 
                                    "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
        self.ANGKA_LEVEL_TINGGI: list[tuple[int, str]] = [
            (1_000_000_000_000, "triliun"),
            (1_000_000_000, "miliar"),
            (1_000_000, "juta"),
            (1_000, "ribu"),
        ]

    def _puluhan(self, angka: int) -> str:
        # Mengubah angka di bawah 100 menjadi teks.
        if 0 <= angka < 10:
            return f"{self.SATUAN[angka]}"
        if 10 <= angka < 20:
            return f"{self.BELASAN[angka - 10]}"
        puluh: int = angka // 10
        sisa: int = angka % 10 
        if sisa == 0:
            return f"{self.SATUAN[puluh]} puluh"
        return f"{self.SATUAN[puluh]} puluh {self.SATUAN[sisa]}"

    def _ratusan(self, angka: int) -> str:
        # Mengubah angka di bawah 1000 menjadi teks.
        if angka < 100:
            return self._puluhan(angka)

        ratus: int = angka // 100
        sisa: int = angka % 100 

        awalan: str = "seratus" if ratus == 1 else f"{self.SATUAN[ratus]} ratus"

        if sisa == 0:
            return awalan
        return f"{awalan} {self._puluhan(sisa)}"

    def konversi(self, angka: int) -> str:
        # Operasi utama dilakukan di sini
        if not isinstance(angka, int):
            raise TypeError("Input harus berupa integer.")

        if angka < 0:
            return f"minus {self.konversi(-angka)}"
        
        if angka == 0:
            return "nol"
        
        if angka < 1000:
            return self._ratusan(angka)

        # Kode dilakukan dengan mencari nilai yang setara dengan
        # input yang diberikan. Dimulai dari level tertinggi
        # menuju level yang lebih rendah.
        for nilai, nama in self.ANGKA_LEVEL_TINGGI:
            if angka >= nilai:
                depan: int = angka // nilai
                sisa: int = angka % nilai

                awalan: str
                if nilai == 1_000 and depan == 1:
                    awalan = "seribu"
                else:
                    awalan = f"{self.konversi(depan)} {nama}"

                if sisa == 0:
                    return awalan  
                return f"{awalan} {self.konversi(sisa)}"

        # fallback 
        return ""


class BacaDesimal:

    def _pisah_presisi(self, angka: float) -> tuple[int, Decimal]:
        angka_decimal = Decimal(str(angka))
        utuh = int(angka_decimal)
        pecahan = angka_decimal - Decimal(utuh)
        return utuh, pecahan

    def _cari_presisi(self, angka: Decimal) -> str: 
        SATUAN: list[str] = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 
                                'enam', 'tujuh', 'delapan', 'sembilan']
        floating_point_len: int = len(str(angka))
        hasil_baca: list[str] = ["koma"]

        for idx in range(floating_point_len - 2):
            angka_desimal: str = str(angka)
            baca_desimal: int = int(angka_desimal[idx + 2])
            hasil: str= SATUAN[baca_desimal]
            hasil_baca.append(hasil)
        hasil_baca = " ".join(hasil_baca)
        return f"{hasil_baca}"
    
    def baca(self, angka: Decimal) -> str:
        k = Konverter()
        depan_koma, belakang_koma = self._pisah_presisi(angka)
        angka_int = int(depan_koma)
        hasil: str = k.konversi(angka_int)

        if not belakang_koma == 0: 
            w = self._cari_presisi(belakang_koma)
            return f"Hasil: {hasil} {w}"

        return f"Hasil: {hasil}"


def main():
    des = BacaDesimal()
    print("Masukkan angka untuk dikonversi (atau 'keluar' untuk berhenti):")
    while True:
        try:
            masukan = input("> ")
            if masukan.lower() == 'keluar':
                break
            desimal: Decimal = Decimal(masukan)
            hasil = des.baca(desimal)
            print(f"Hasil: {hasil}")
        except ValueError:
            print("Error: Input tidak valid. Harap masukkan angka bulat.")
        except TypeError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()