# angka: int = int(input("Masukan angka:"))

def num2word(angka):
    satuan: list = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    # se: list = ['', 'sepuluh', 'seratus', 'seribu', 'sejuta']

    angka = int(angka)
    if angka == 0:
        return 0
    
    def satudigit(i):
        print(f"{satuan[i]}")
        return 0
    
    def duadigit(i):
        digit1 = int(i / 10)
        digit2 = int(i % 10)
        if digit1 == 1 and digit2 == 1:
            print("sebelas")
            return 0
        else:
            print(f"{satuan[digit1]} puluh {satuan[digit2]}")
            return 0

    def tigadigit(i):
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

    if angka < 10:
        satudigit(angka)
    elif len(str(angka)) == 2:
        duadigit(angka)
    elif len(str(angka)) == 3:
        tigadigit(angka)
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

# angka: int = int(input("Masukan angka:"))

# def num2word(angka):
#     satuan: list = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
#     # se: list = ['', 'sepuluh', 'seratus', 'seribu', 'sejuta']

#     angka = int(angka)
#     if angka == 0:
#         return 0
    
#     def satudigit(i):
#         print(f"{satuan[i]}")
#         return 0
    
#     def duadigit(i):
#         if i == 11:
#             print("sebelas")
#             return 0
#         elif i < 20:
#             digit1 = i - 10
#             print(f"{satuan[digit1]} belas")
#             return 0
#         elif i >= 20:
#             digit1 = int(i / 10)
#             digit2 = i % 10
#             print(f"{satuan[digit1]} puluh {satuan[digit2]}")
#             return 0
#         else:
#             pass

#     def tigadigit(i):
#         if i == 100:
#             print("seratus")
#             return 0
#         elif i == 111:
#             print("seratus sebelas")
#         elif i < 120:
#             digit = (i - 100)-10
#             print(f"seratus {satuan[digit]} belas")
#             return 0
#         elif i < 200:
#             digit2 = int((i-100) / 10)
#             digit3 = (i-100) % 10
#             print(f"seratus {satuan[digit2]} puluh {satuan[digit3]}")
#             return 0
#         else:
#             digit1 = int(i / 100)
#             digit2 = int((i - (digit1 * 100)) / 10)
#             digit3 = int(i - (digit1 * 100) - (digit2 * 10))
#             if digit2 == 1 and digit3 == 1:
#                 print(f"{satuan[digit1]} ratus sebelas")
#                 return 0
#             elif digit2 == 1:
#                 print(f"{satuan[digit1]} ratus {satuan[digit3]} belas")
#                 return 0
#             print(f"{satuan[digit1]} ratus {satuan[digit2]} puluh {satuan[digit3]}")
#             return 0

#     if angka < 10:
#         satudigit(angka)
#     elif len(str(angka)) == 2:
#         duadigit(angka)
#     elif len(str(angka)) == 3:
#         tigadigit(angka)
#     else:
#         print("Error!: Maksimal input adalah 999")

# nomer = input("Masukin angka: ")

# num2word(nomer)