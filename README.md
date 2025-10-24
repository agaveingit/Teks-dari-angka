# Angka Jadi Teks 🔢

Proyek ini menyediakan sebuah skrip Python sederhana untuk mengonversi angka (integer) menjadi ejaan yang sesuai dalam Bahasa Indonesia. Skrip ini mampu menangani angka dari nol hingga triliunan, termasuk bilangan negatif dan angka desimal.

## ✨ Fitur Utama

- **Konversi Angka ke Teks**: Mengubah angka bulat menjadi ejaan yang sesuai dalam Bahasa Indonesia.
- **Dukungan Angka Besar**: Mampu menangani angka hingga 999,999,999,999,999 (di bawah kuadriliun).
- **Penanganan Angka Negatif**: Mengawali hasil dengan "minus" untuk angka negatif.
- **Kasus Khusus Bahasa Indonesia**: Menangani secara benar kasus seperti "seratus", "seribu", "sebelas", dan puluhan/ratusan.
- **Antarmuka Interaktif**: Dilengkapi dengan _command-line interface_ (CLI) sederhana untuk penggunaan langsung.
- **Efisien**: Menggunakan algoritma rekursif dengan kompleksitas waktu **O(log n)**, sehingga sangat cepat bahkan untuk angka yang sangat besar.

## ⚙️ Instalasi

Cara termudah untuk menginstal adalah melalui `pip`:

```bash
pip install angkajaditeks
```

Anda juga dapat mengkloning repositori ini untuk pengembangan:

```bash
git clone https://github.com/username/angkajaditeks.git
cd angkajaditeks
```

## 🚀 Cara Penggunaan

Ada dua cara untuk menggunakan kode ini:

### 1. Melalui Command Line (Interaktif)

Jalankan file `main.py` untuk memulai mode interaktif. Masukkan angka yang ingin Anda konversi, dan tekan Enter. Ketik `keluar` untuk menghentikan program.

```bash
python main.py
```

**Contoh Sesi:**

```
Masukkan angka untuk dikonversi (atau 'keluar' untuk berhenti):
> 1247639
Hasil: satu juta dua ratus empat puluh tujuh ribu enam ratus tiga puluh sembilan
> -101
Hasil: minus seratus satu
> keluar
```

### 2. Sebagai Modul di Proyek Lain

Anda juga bisa mengimpor kelas `Konverter` ke dalam skrip Python Anda yang lain.

```python
from main import Konverter

# Buat instance dari Konverter
k = Konverter()

# Gunakan metode konversi()
print(k.konversi(2024))
# Output: dua ribu dua puluh empat

print(k.konversi(150000))
# Output: seratus lima puluh ribu
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Jika Anda memiliki ide untuk penyederhanaan, penambahan fitur (misalnya, angka desimal), atau perbaikan, silakan buat _pull request_ atau buka _issue_.
