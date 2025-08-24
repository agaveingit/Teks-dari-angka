def num2word(angka):
    satuan: list = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']

    angka = int(angka)
    if angka == 0:
        return 0
    
    def belas_puluh(i):
        digit1 = int(i / 10)
        digit2 = int(i % 10)
        if digit1 == 1 and digit2 == 1:
            print("sebelas")
            return 0
        elif digit1 == 1:
            print(f"{satuan[digit2]} belas")
            return 0
        elif digit1 == 0:
            print(f"{satuan[digit2]}")
        else:
            print(f"{satuan[digit1]} puluh {satuan[digit2]}")
            return 0

    def ratus(i):
        digit1 = int(i / 100)
        digit2 = int((i - (digit1 * 100)) / 10)
        digit3 = int(i - (digit1 * 100) - (digit2 * 10))
        if digit1 == 1:
            if digit2 == 1 and digit3 == 1:
                print("seratus sebelas")
            else:
                print("seratus")
            return 0
        elif digit2 == 1:
            print(f"{satuan[digit1]} ratus {satuan[digit3]} belas")
            return 0
        elif digit2 == 0:
            print(f"{satuan[digit1]} ratus {satuan[digit3]}")
            return 0
        else:
            print(f"{satuan[digit1]} ratus {satuan[digit2]} puluh {satuan[digit3]}")

    if angka < 100:
        belas_puluh(angka)
    elif angka < 1000:
        ratus(angka)
    else:
        print("Error!: Maksimal input adalah 999")

def main():
    try:
        nomer = input("Masukin angka: ")
        num2word(nomer)
    except:
        ValueError
        print("Error! Harus masukan angka")
        main()

if __name__ == "__main__":
    main()
