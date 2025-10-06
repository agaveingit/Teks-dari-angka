    floating_point_len: int = len(str(i))
    hasil_baca: list[str] = ["koma"]
    for idx in range(floating_point_len - 2):
        angka_desimal: str = str(i)
        baca_desimal = angka_desimal[idx + 2]
        hasil = SATUAN[int(baca_desimal)]
        hasil_baca.append(hasil)
    hasil_baca = " ".join(hasil_baca)
    return f"panjang {floating_point_len}, {hasil_baca}"
