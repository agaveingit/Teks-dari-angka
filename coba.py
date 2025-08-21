satuan: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
belasan: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]

def angka_jadi_teks (angka):
    def puluhan(i):
        puluh: int = int(i / 10)
        sisa: int = i % 10
        match i:
            case _ if i < 10:
                return satuan[i]
            case _ if i < 20:
                return belasan[i - 10]
            case _ if i < 100:
                if (sisa) == 0:
                    return f"{satuan[puluh]} puluh" 
                else:
                    return f"{satuan[puluh]} puluh {satuan[sisa]}"
    def ratusan(i):
        ratus: int = int(i / 100)
        sisa: int = i % 100
        match i:
            case _ if i < 200:
                if (sisa) == 0:
                    return "seratus"
                else:
                    return f"seratus {puluhan(sisa)}"
            case _ if i < 1000:
                if (sisa) == 0:
                    return f"{satuan[ratus]} ratus"  
                else:
                    return f"{satuan[ratus]} ratus {puluhan(sisa)}"

    if angka == 0:
        return "Nol"
    elif angka < 100:
        return puluhan(angka)
    elif angka < 1000:
        return ratusan(angka)
    else:
        return "Eror! Harus masukaan angka 0-1000"

if __name__ == "__main__":
    e = int(input("angka: "))
    n = angka_jadi_teks(e)
    print(n)