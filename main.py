def teks_dari_angka(angka):
    satuan: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    belasan: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]

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

    if angka < 100:
        return puluhan(angka)
    elif angka < 1000:
        return ratusan(angka)
    else:
        return "Error!: Maksimal input adalah 999"

def main():
    try:
        nomer = input("Masukin angka: ")
        teks_dari_angka(nomer)
    except:
        ValueError
        print("Error! Harus masukan angka")
        main()

if __name__ == "__main__":
    main()
