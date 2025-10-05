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
    
class Desimal:
    def __init__(self):
        self.BELAKANG_KOMA: list[tuple[int, str]] = [
            (0.1, "satu"),
            (0.01, "nol nol satu"),
        ]
    def _baca_desimal(self, angka: float) -> str:
        depan_koma: int = int(angka)
        setelah_koma: float = angka - depan_koma
        raise NotImplementedError("Ntar dulu")

def main():
    k = Konverter()
    print("Masukkan angka untuk dikonversi (atau 'keluar' untuk berhenti):")
    while True:
        try:
            masukan = input("> ")
            if masukan.lower() == 'keluar':
                break
            angka = int(masukan)
            hasil = k.konversi(angka)
            print(f"Hasil: {hasil}")
        except ValueError:
            print("Error: Input tidak valid. Harap masukkan angka bulat.")
        except TypeError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()