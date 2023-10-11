def input_meter():
    print("konversi meter")
    print(" 1. meter ke milimeter")
    print(" 2. meter ke centimeter")
    print(" 3. meter ke inci")
    print(" 4. meter ke kaki")
    print(" 5. meter ke yard")
    print("=" * 25)
    konversi_meter()

def konversi_meter():
    operasi = input("pilih operasi (1/2/3/4/5): ")
    meter = eval(input("masukkan jumlah meter : "))
    print("=" * 25)

    if operasi == "1":
        hasil = meter * 1000
        print(f"hasil konversi dari meter ke milimeter = {hasil:.1f}")
        return hasil

    elif operasi == "2":
        hasil = meter * 100
        print(f"hasil konversi dari meter ke centimeter = = {hasil:.1f}")
        return hasil

    elif operasi == "3":
        hasil = meter * 39.3701
        print(f"hasil konversi dari meter ke inci = {hasil:.1f}")
        return hasil

    elif operasi == "4":
        hasil = meter * 3.28084
        print(f"hasil konversi dari meter ke kaki = {hasil:.1f}")
        return hasil
    
    elif operasi == "5":
        hasil = meter * 1.09361
        print(f"hasil konversi dari meter ke yard = {hasil:.1f}")
        return hasil

    else:
        print("operasi tidak valid")
        return False

input_meter()