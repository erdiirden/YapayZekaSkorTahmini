import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import math
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

pencere=tk.Tk()
#KODLAR


# Pencere boyutunu yüzde olarak ayarlama fonksiyonu
def set_pencere_boyutu(yuzde_genislik, yuzde_yukseklik):
    ekran_genislik = pencere.winfo_screenwidth()
    ekran_yukseklik = pencere.winfo_screenheight()
    genislik = int(ekran_genislik * (yuzde_genislik / 100))
    yukseklik = int(ekran_yukseklik * (yuzde_yukseklik / 100))
    pencere.geometry(f"{genislik}x{yukseklik}")
    
# Ekranın tam ortasında açılmasını sağlama fonksiyonu
def ortada_ac():
    pencere.update_idletasks()
    ekran_genislik = pencere.winfo_screenwidth()
    ekran_yukseklik = pencere.winfo_screenheight()
    pencere_genislik = pencere.winfo_width()
    pencere_yukseklik = pencere.winfo_height()
    x = int((ekran_genislik - pencere_genislik) / 2)
    y = int((ekran_yukseklik - pencere_yukseklik) / 2)
    pencere.geometry(f"+{x}+{y}")
    
# Görselleri boyutlandırma fonksiyonu
def boyutlandir_gorsel(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def button_click():
    
    selected_team1 = combobox1.get()
    altTakim1.config(text=selected_team1)
    takim1_adi=combobox1.get()

    selected_team2 = combobox2.get()
    altTakim2.config(text=selected_team2)
    takim2_adi=combobox2.get()

    # Resim URL'sini değiştirme
    if selected_team1 == "ADANADEMIR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ADANADEMIR.png"
    elif selected_team1 == "ALANYASPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ALANYASPOR.png"
    elif selected_team1 == "ANKARAGUCU":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ANKARAGUCU.png"
    elif selected_team1 == "ANTALYASPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ANTALYASPOR.png"
    elif selected_team1 == "BASAKSEHIR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/BASAKSEHIR.png"
    elif selected_team1 == "BESIKTAS":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/BESIKTAS.png"
    elif selected_team1 == "FENERBAHCE":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/FENERBAHCE.png"
    elif selected_team1 == "GALATASARAY":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/GALATASARAY.png"
    elif selected_team1 == "GAZIANTEPFK":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/GAZIANTEPFK.png"
    elif selected_team1 == "GIRESUNSPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/GIRESUNSPOR.png"
    elif selected_team1 == "HATAYSPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/HATAYSPOR.png"
    elif selected_team1 == "ISTANBULSPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ISTANBULSPOR.png"
    elif selected_team1 == "KARAGUMRUK":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KARAGUMRUK.png"
    elif selected_team1 == "KASIMPASA":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KASIMPASA.png"
    elif selected_team1 == "KAYSERISPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KAYSERISPOR.png"
    elif selected_team1 == "KONYASPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KONYASPOR.png"
    elif selected_team1 == "SIVASSPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/SIVASSPOR.png"
    elif selected_team1 == "TRABZONSPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/TRABZONSPOR.png"
    elif selected_team1 == "UMRANIYESPOR":
        image_url1  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/UMRANIYESPOR.png"
    else:
        image_url1 = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/denemelogo.png"  # Varsayılan olarak boş bir URL kullanabilirsiniz
    
    # Resim URL'sini değiştirme
    if selected_team2 == "ADANADEMIR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ADANADEMIR.png"
    elif selected_team2 == "ALANYASPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ALANYASPOR.png"
    elif selected_team2 == "ANKARAGUCU":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ANKARAGUCU.png"
    elif selected_team2 == "ANTALYASPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ANTALYASPOR.png"
    elif selected_team2 == "BASAKSEHIR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/BASAKSEHIR.png"
    elif selected_team2 == "BESIKTAS":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/BESIKTAS.png"
    elif selected_team2 == "FENERBAHCE":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/FENERBAHCE.png"
    elif selected_team2 == "GALATASARAY":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/GALATASARAY.png"
    elif selected_team2 == "GAZIANTEPFK":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/GAZIANTEPFK.png"
    elif selected_team2 == "GIRESUNSPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/GIRESUNSPOR.png"
    elif selected_team2 == "HATAYSPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/HATAYSPOR.png"
    elif selected_team2 == "ISTANBULSPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/ISTANBULSPOR.png"
    elif selected_team2 == "KARAGUMRUK":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KARAGUMRUK.png"
    elif selected_team2 == "KASIMPASA":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KASIMPASA.png"
    elif selected_team2 == "KAYSERISPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KAYSERISPOR.png"
    elif selected_team2 == "KONYASPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/KONYASPOR.png"
    elif selected_team2 == "SIVASSPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/SIVASSPOR.png"
    elif selected_team2 == "TRABZONSPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/TRABZONSPOR.png"
    elif selected_team2 == "UMRANIYESPOR":
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/UMRANIYESPOR.png"
    else:
        image_url2  = "C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/denemelogo.png"  # Varsayılan olarak boş bir URL kullanabilirsiniz
    
    # Görselleri değiştirme
    if image_url1:
        new_image1 = boyutlandir_gorsel(image_url1, 180, 180)
    else:
        new_image1 = boyutlandir_gorsel("C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/denemelogo.png", 180, 180)
    resimKutusu1.config(image=new_image1)
    resimKutusu1.image = new_image1

    if image_url2:
        new_image2 = boyutlandir_gorsel(image_url2, 180, 180)
    else:
        new_image2 = boyutlandir_gorsel("C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/denemelogo.png", 180, 180)
    resimKutusu2.config(image=new_image2)
    resimKutusu2.image = new_image2
    
    
    
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Veri setini yükle
    istatistik = pd.read_csv('C:/Users/erdi/Desktop/skorTahminYapayZeka/verisetleri/STSL_istatistikler.csv')
    maclar = pd.read_csv('C:/Users/erdi/Desktop/skorTahminYapayZeka/verisetleri/STSL_maclar.csv')

    # Tahmin yapılacak maçın takım adlarını belirle
    # takim1_adi = "BESIKTAS"
    # takim2_adi = "GALATASARAY"

    # Tahmin yapılacak maçın özelliklerini belirle İSTATİSTİK
    takim1 = istatistik[istatistik['TakimAdi'] == takim1_adi]
    takim1_ozellikler = takim1[['MacSayisi', 'AtGol', 'YeGol', 'Galibiyet', 'Beraberlik', 'Maglubiyet']]
    takim2 = istatistik[istatistik['TakimAdi'] == takim2_adi]
    takim2_ozellikler = takim2[['MacSayisi', 'AtGol', 'YeGol', 'Galibiyet', 'Beraberlik', 'Maglubiyet']]
    tahmin_ozellikler1 = takim1_ozellikler
    tahmin_ozellikler2 = takim2_ozellikler

    # Tahmin yapılacak maçın eski maçlarla karşılaştırılması MACLAR
    takim1 = maclar[(maclar['ev'] == takim1_adi) & (maclar['dep'] == takim2_adi)]
    takim1_maclar = takim1[['evGol','evGol']]
    takim2 = maclar[(maclar['ev'] == takim1_adi) & (maclar['dep'] == takim2_adi)]
    takim2_maclar = takim2[['depGol','depGol']]
    tahmin_maclar1 = takim1_maclar
    tahmin_maclar2 = takim2_maclar

    # Özellikler ve hedef değişkeni ayır İSTATİSTİK
    features = istatistik.drop(['Puan', 'TakimAdi'], axis=1)
    target = istatistik['Puan']

    # Özellikler ve hedef değişkeni ayır MACLAR
    features2  = maclar.drop(['macNo', 'ev', 'dep'], axis=1)
    target2 = maclar['macNo']

    # Eğitim ve test veri setlerini bölelim İSTATİSTİK
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

    # Eğitim ve test veri setlerini bölelim MACLAR
    X_train2, X_test2, y_train2, y_test2 = train_test_split(features2, target2, test_size=0.2, random_state=0)

    # Çoklu lineer regresyon modelini oluştur İSTATİSTİK
    model = LinearRegression()

    # Çoklu lineer regresyon modelini oluştur MACLAR
    model2 = LinearRegression()

    # Modeli eğit İSTATİSTİK
    model.fit(X_train, y_train)

    # Modeli eğit MACLAR
    model2.fit(X_train2, y_train2)

    # Tahmin yap İSTATİSTİK
    tahmin_skor1istatistik = model.predict(tahmin_ozellikler1)
    tahmin_skor2istatistik = model.predict(tahmin_ozellikler2)

    # Tahmin yap MACLAR
    tahmin_skor1maclar = model2.predict(tahmin_maclar1)
    tahmin_skor2maclar = model2.predict(tahmin_maclar2)

    # Tahminleri tek rakama indirme İSTATİSTİK
    skor1 = int(str(tahmin_skor1istatistik[0])[0])
    skor2 = int(str(tahmin_skor2istatistik[0])[0])

    # Tahminleri tek rakama indirme MACLAR
    skor11 = int(str(tahmin_skor1maclar[0])[0])
    skor22 = int(str(tahmin_skor2maclar[0])[0])
    # Simulasyon İçin takımlara göre katsayılar
    takim_katsayilari = {
    "BESIKTAS": 1.6,
    "FENERBAHCE": 1.6,
    "GALATASARAY": 1.6,
    "TRABZONSPOR": 1.4,
    "BASAKSEHIR": 1.4,
    "SIVASSPOR": 1.1,
    "KAYSERISPOR": 0.9,
    "KONYASPOR": 0.8,
    "ANTALYASPOR": 0.7,
    "KASIMPASA": 0.6,
    "ANKARAGUCU": 0.8,
    "ALANYASPOR": 0.8,
    "GAZIANTEPFK": 0.7,
    "KARAGUMRUK": 0.9,
    "HATAYSPOR": 0.6,
    "ADANADEMIR": 1.2,
    "ISTANBULSPOR": 0.6,
    "GIRESUNSPOR": 0.6,
    "UMRANIYESPOR": 0.5
    }
    katsayi1 = takim_katsayilari.get(takim1_adi, 1.2)  # Takımın katsayısını sözlükten alın, varsayılan değer 1.0
    katsayi2 = takim_katsayilari.get(takim2_adi, 0.8)  # Takımın katsayısını sözlükten alın, varsayılan değer 1.0

    
    # Simulasyon Skor
    simulasyon1 = ((tahmin_skor1istatistik*1.1) + (tahmin_skor1maclar*1.1*katsayi1) ) / 3
    simulasyon2 = ((tahmin_skor2istatistik*0.8) + (tahmin_skor2maclar*0.8*katsayi2) ) / 4

    # Tahminleri tek rakama indirme Simulasyon
    simuskor1 = int(str(simulasyon1[0])[0])
    simuskor2 = int(str(simulasyon2[0])[0])
    
    #FARKLI YONTEM
    avg1 = sum(simulasyon1)/len(simulasyon1)  # Örnek sayı
    sol_basamak_sayisi1 = math.floor(math.log10(avg1)) + 1
    if sol_basamak_sayisi1 >3:
        sayi_str = str(avg1)  # Sayıyı string olarak dönüştür
        ikinci_basamak = int(sayi_str[1])  # Soldan ikinci basamağı al
        if ikinci_basamak >= 5:  # İkinci basamak 5'ten büyük veya eşitse
            sayi_str = str(int(sayi_str[0]) + 1) + sayi_str[1:]  # İlk basamağı 1 arttır
        ilk_basamak = int(sayi_str[0])  # İlk basamağı al
    else:
        ilk_basamak=0
    
    avg2 = sum(simulasyon2)/len(simulasyon2)  # Örnek sayı
    sol_basamak_sayisi2 = math.floor(math.log10(avg2)) + 1
    if sol_basamak_sayisi2 >3:
        sayi_str2 = str(avg2)  # Sayıyı string olarak dönüştür
        ikinci_basamak2 = int(sayi_str2[1])  # Soldan ikinci basamağı al
        if ikinci_basamak2 >= 5:  # İkinci basamak 5'ten büyük veya eşitse
            sayi_str2 = str(int(sayi_str2[0]) + 1) + sayi_str2[1:]  # İlk basamağı 1 arttır
        ilk_basamak2 = int(sayi_str2[0])  # İlk basamağı al
    else:
        ilk_basamak2=0
        

    #İSTATİSTİK
    print("İstatistiğe Göre Skor:","\n", takim1_adi," ", skor1," - ", skor2," ",takim2_adi)
    print("Geçmiş Maçlara Göre Skor:","\n", takim1_adi," ", skor11," - ", skor22," ",takim2_adi)
    print("Simulasyon Skoru:","\n", takim1_adi," ", simuskor1," - ", simuskor2," ",takim2_adi)
    print("Simulasyon Skoru:","\n", takim1_adi," ", simulasyon1," - ", simulasyon2," ",takim2_adi)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    skorYaz.config(text=str(int(ilk_basamak)) + " - " + str(int(ilk_basamak2)))
    print(ilk_basamak," - ",ilk_basamak2)
    


# Pencere boyutunu yüzdeyle ayarlamak için çağırma (örnek: genişlik: 50%, yükseklik: 75%)
set_pencere_boyutu(50, 75)
# Pencereyi ortada açmak için çağırma
ortada_ac()

applogo=PhotoImage(file='C:/Users/erdi/Desktop/skorTahminYapayZeka/applogo32.png')
pencere.iconphoto(False,applogo)
pencere.iconbitmap("C:/Users/erdi/Desktop/skorTahminYapayZeka/applogo.ico")

pencere.title("Yapay Zeka İle Skor Simulasyonu")
textTakim1 = tk.Label(text="Takım Seçiniz", font="Verdana 14 bold")
textTakim1.grid(row=0, column=0, padx=(80), pady=(60, 0), sticky='w')
textTakim2 = tk.Label(text="Takım Seçiniz", font="Verdana 14 bold")
textTakim2.grid(row=0, column=1, padx=(356, 80), pady=(60, 0), sticky='e')

combobox1 = ttk.Combobox(pencere, values=["ADANADEMIR", "ALANYASPOR","ANKARAGUCU", "ANTALYASPOR", "BASAKSEHIR", "BESIKTAS", "FENERBAHCE", "GALATASARAY", "GAZIANTEPFK", "GIRESUNSPOR", "HATAYSPOR", "ISTANBULSPOR", "KARAGUMRUK", "KASIMPASA", "KAYSERISPOR", "KONYASPOR", "SIVASSPOR", "TRABZONSPOR", "UMRANIYESPOR"])
combobox1.grid(row=1, column=0, padx=(80), pady=(30, 0), sticky='w')
combobox2 = ttk.Combobox(pencere, values=["ADANADEMIR", "ALANYASPOR","ANKARAGUCU", "ANTALYASPOR", "BASAKSEHIR", "BESIKTAS", "FENERBAHCE", "GALATASARAY", "GAZIANTEPFK", "GIRESUNSPOR", "HATAYSPOR", "ISTANBULSPOR", "KARAGUMRUK", "KASIMPASA", "KAYSERISPOR", "KONYASPOR", "SIVASSPOR", "TRABZONSPOR", "UMRANIYESPOR"])
combobox2.grid(row=1, column=1, padx=(80), pady=(30, 0), sticky='e')

resim1 = boyutlandir_gorsel("C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/denemelogo.png", 180, 180)
resimKutusu1 = tk.Label(image=resim1)
resimKutusu1.grid(row=2, column=0, padx=(80), pady=(80, 0), sticky='w')

resim2 = boyutlandir_gorsel("C:/Users/erdi/Desktop/skorTahminYapayZeka/Logolar/denemelogo.png", 180, 180)
resimKutusu2 = tk.Label(image=resim2)
resimKutusu2.grid(row=2, column=1, padx=(80), pady=(80, 0), sticky='e')

buton = tk.Button(text="Simulasyonu Çalıştır", font="Verdana 14 bold", width=14, height=4, wraplength=180, command=button_click)
buton.grid(row=2, column=0, columnspan=2, pady=(120, 0))

altTakim1 = tk.Label(text="NULL", font="Verdana 14 bold")
altTakim1.grid(row=3, column=0, padx=(80), pady=(80, 0), sticky='w')
skorYaz = tk.Label(text="-", font="Verdana 14 bold")
skorYaz.grid(row=3, column=0, columnspan=2, pady=(80, 0))
altTakim2 = tk.Label(text="NULL", font="Verdana 14 bold")
altTakim2.grid(row=3, column=1, padx=(356, 80), pady=(80, 0), sticky='e')

#KODLAR
pencere.mainloop()