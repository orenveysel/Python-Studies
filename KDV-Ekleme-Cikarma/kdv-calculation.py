print("1- Fiyata kdv ekleme \n2- Fiyat/kdv ayırma \n3- Çıkış (veya çarpıya tıklayın) \n")

while True:
    try:
        answer = int(input("\nYapmak istediginiz islemi seciniz(1-3): "))
        if answer == 1:
            fiyat1 = float(input("\nFiyatı giriniz: "))
            kdv1 = (fiyat1 * 18) / 100
            total1 = kdv1 + fiyat1
            print(f"\nFiyat: {fiyat1:.2f}")
            print(f"Kdv: {kdv1:.2f}")
            print(f"Kdv dahil fiyat: {total1:.2f}\n")
        elif answer == 2:
            fiyat2 = float(input("\nFiyatı giriniz: "))
            kdv2 = (fiyat2 / 118) * 100
            total2 = fiyat2 - kdv2
            print(f"\nKdv dahil fiyat: {fiyat2:.2f}")
            print(f"Fiyat: {kdv2:.2f}")
            print(f"Kdv: {total2:.2f}\n")
        elif answer == 3:
            break
        else:
            print("\nHatalı veri girişi. Tekrar deneyin...")
            continue
    except ValueError:
        print("\nHatalı veri girişi. Tekrar deneyin...")
        continue
