# Bankamatik Uygulamasi

ad = 'Ali'
hesapNo = '12132132'
bakiye = 3000

SadikHesap = {
    'ad': 'Sadik Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('Paranizi alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanilsin mi (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranizi alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else:
            print('Uzgunuz, bakiye yetersiz.')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitinizde ise {hesap['ekHesap']} TL bulunmaktadir.")

paraCek(SadikHesap, 3000)

print('*****************')

paraCek(SadikHesap, 2000)




