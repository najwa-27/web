while True:
    print("==========NEO ICE CREAM==========")
    pembeli = input("Nama Pembeli : ")
    TanggalPembelian = input("Tanggal Pembelian : ")

    totalicecream = 0
    totaltopping = 0

    def icecream():
        global totalicecream
        global porsi
        global icecream
        print("\n==========MENU ICE CREAM==========")
        print("1. Ice cream Vanila - Rp. 8000,00")
        print("2. Ice cream Coklat - Rp. 8000,00")
        print("3. Ice cream Strawberry - Rp. 8000,00")
        nomor = int(input("Masukkan pilihan 1/2/3 : "))
        porsi = int(input("Berapa porsi : "))

        if nomor == 1:
            totalicecream = porsi * 8000
            print(porsi,'Ice Cream Vanila - Rp.',totalicecream)
            icecream=("Ice Cream Vanila")
        elif nomor == 2:
            totalicecream = porsi * 8000
            print (porsi, 'Ice Cream Coklat - Rp. ',totalicecream)
            icecream=("Ice Cream Coklat")
        elif nomor == 3:
            totalicecream = porsi * 8000
            print (porsi, 'Ice Cream Strawberry - Rp. ',totalicecream)
            icecream=("Ice Cream Strawberry")

    def topping() :
        global totaltopping
        global porsi
        global topping
        print ("1. Saus Coklat - Rp. 2.000,00")
        print ("2. Saus Caramel - Rp. 2.000,00")
        print ("3. Chocolate Chips - Rp. 2.000,00")
        print ("4. Kacang - Rp. 2.000,00")
        print ("5. Sereal - Rp. 3.000,00")
        print ("6. Oreo - Rp. 3.000,00")
        print ("7. Marsmallow - Rp. 3.000,00") 
        print ("8. Buah buahan - Rp. 5.000,00")
        nomor = int(input("Masukkan pilihan 1/2/3/4/5/6/7/8 : "))
        porsi = int(input("Berapa topping : "))

        if nomor == 1:
            totaltopping = porsi * 2000
            print(porsi,'Saus Coklat - Rp.',totaltopping)
            topping=("Saus Coklat")
        elif nomor == 2:
            totaltopping = porsi * 2000
            print (porsi, 'Saus Caramel - Rp. ',totaltopping)
            topping=("Saus Caramel")
        elif nomor == 3:
            totaltopping = porsi * 2000
            print (porsi, 'Chocolate Chips - Rp. ',totaltopping)
            topping=("Chocolate Chips")
        elif nomor == 4:
            totaltopping = porsi * 2000
            print (porsi,'Kacang - Rp. ',totaltopping)
            topping=("Kacang")
        elif nomor == 5:
            totaltopping = porsi * 3000
            print (porsi,'Sereal - Rp. ',totaltopping)
            topping=("Sereal")
        elif nomor == 6:
            totaltopping = porsi * 3000
            print (porsi,'Oreo - Rp. ',totaltopping)
            topping=("Oreo")
        elif nomor == 7:
            totaltopping = porsi * 3000
            print (porsi, 'Marsmallow - Rp. ',totaltopping)
            topping=("Marhmallow")
        elif nomor == 8:
            totaltopping = porsi * 5000
            print (porsi, 'Buah buahan - Rp. ',totaltopping)
            topping=("Buah buahan")
        

    icecream() 
    topping()
    total = totalicecream + totaltopping

    def pajak (total) :
        pajak = float(total*0.10)
        totalsemua = total + pajak
        totalsemua = round(float(total + pajak))
        return totalsemua

    totalsemua = pajak(total)

    print("Total yang harus di bayar : ", total)
    print("Total dengan pajak : ", totalsemua)
    uang = int(input("Uang Tunai Pembeli : Rp. "))
    kembalian = int(uang - totalsemua)
    print("Kembalian :", kembalian)

    print("\n==========S T R U K B E L I==========")
    print("Nama\t\t:", pembeli)
    print("Beli\t\t:", porsi, icecream, "(Rp.", totalicecream, ")")
    print("Beli\t\t:", porsi, topping, "(Rp.", totaltopping, ")")
    print("Tagihan\t\t: Rp.", totalsemua)
    print("Dibayar\t\t: Rp.", uang)
    print("Kembalian\t: Rp.", kembalian)
