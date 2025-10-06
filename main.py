from decimal import Decimal, InvalidOperation


class Konverter:
    """
    Mengonversi angka menjadi teks ejaannya dalam Bahasa Indonesia.
    """
    SATUAN: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    BELASAN: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
                        "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
    ANGKA_LEVEL_TINGGI: list[tuple[int, str]] = [
        (1_000_000_000_000, "triliun"),
        (1_000_000_000, "miliar"),
        (1_000_000, "juta"),
        (1_000, "ribu"),
    ]

    def _puluhan(self, angka: int) -> str:
        """Mengubah angka di bawah 100 menjadi teks."""
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
        """Mengubah angka di bawah 1000 menjadi teks."""
        if angka < 100:
            return self._puluhan(angka)

        ratus: int = angka // 100
        sisa: int = angka % 100

        if ratus == 1:
            awalan = "seratus"
        else:
            awalan = f"{self.SATUAN[ratus]} ratus"

        if sisa == 0:
            return awalan
        return f"{awalan} {self._puluhan(sisa)}"

    def konversi(self, angka: int) -> str:
        """Mengonversi angka integer menjadi teks."""
        if not isinstance(angka, int):
            raise TypeError("Input harus berupa integer.")

        if angka < 0:
            return f"minus {self.konversi(-angka)}"
        
        if angka == 0:
            return "nol"
        
        if angka < 1000:
            return self._ratusan(angka)

        for nilai, nama in self.ANGKA_LEVEL_TINGGI:
            if angka >= nilai:
                depan: int = angka // nilai
                sisa: int = angka % nilai

                teks_depan = self.konversi(depan)
                if teks_depan == "satu" and nama in ["ribu"]: 
                    awalan = f"se{nama}"
                else:
                    awalan = f"{teks_depan} {nama}"

                if sisa == 0:
                    return awalan  
                return f"{awalan} {self.konversi(sisa)}"

        return "" 

    def _pisah_desimal(self, angka: Decimal) -> tuple[int, Decimal]:
        """Memisahkan bagian utuh dan pecahan dari Decimal."""
        utuh = int(angka)
        pecahan = angka - Decimal(utuh)
        return utuh, pecahan

    def _baca_pecahan(self, pecahan: Decimal) -> str:
        """Mengonversi bagian pecahan (setelah koma) menjadi teks."""
        digit_pecahan = str(pecahan).split('.')[1]
        
        satuan_dengan_nol = ['nol'] + self.SATUAN[1:]
        hasil_baca = [satuan_dengan_nol[int(digit)] for digit in digit_pecahan]
        
        return "koma " + " ".join(hasil_baca)

    def konversi_desimal(self, angka: Decimal) -> str:
        """Mengonversi angka Decimal (bisa utuh atau pecahan) menjadi teks."""
        bagian_utuh, bagian_pecahan = self._pisah_desimal(angka)
        hasil_utuh = self.konversi(bagian_utuh)

        if bagian_pecahan != 0:
            hasil_pecahan = self._baca_pecahan(bagian_pecahan)
            return f"{hasil_utuh} {hasil_pecahan}"
        return hasil_utuh


def main():
    konverter = Konverter()
    print("Masukkan angka untuk dikonversi (atau 'keluar' untuk berhenti):")
    while True:
        try:
            masukan = input("> ").replace(',', '.')
            if masukan.lower() == 'keluar':
                break
            angka_desimal = Decimal(masukan)
            hasil = konverter.konversi_desimal(angka_desimal)
            print(f"Hasil: {hasil}")
            
        except InvalidOperation:
            print("Error: Input tidak valid. Harap masukkan angka yang benar.")
        except TypeError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()