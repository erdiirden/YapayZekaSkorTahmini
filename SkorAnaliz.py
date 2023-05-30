import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Veri setini yükle
istatistik = pd.read_csv('C:/Users/erdi/Desktop/skorTahminYapayZeka/verisetleri/STSL_istatistikler.csv')
maclar = pd.read_csv('C:/Users/erdi/Desktop/skorTahminYapayZeka/verisetleri/STSL_maclar.csv')

# Tahmin yapılacak maçın takım adlarını belirle
takim1_adi = "BESIKTAS"
takim2_adi = "GALATASARAY"

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

# Simulasyon Skor
simulasyon1 = ((tahmin_skor1istatistik*1.1) + (tahmin_skor1maclar*5*1.2) ) / 6
simulasyon2 = ((tahmin_skor2istatistik*0.8) + (tahmin_skor2maclar*5*0.9) ) / 6

# Tahminleri tek rakama indirme Simulasyon
simuskor1 = int(str(simulasyon1[0])[0])
simuskor2 = int(str(simulasyon2[0])[0])

#İSTATİSTİK
print("İstatistiğe Göre Skor:","\n", takim1_adi," ", skor1," - ", skor2," ",takim2_adi)
print("Geçmiş Maçlara Göre Skor:","\n", takim1_adi," ", skor11," - ", skor22," ",takim2_adi)
print("Simulasyon Skoru:","\n", takim1_adi," ", simuskor1," - ", simuskor2," ",takim2_adi)
print("Simulasyon Skoru:","\n", takim1_adi," ", simulasyon1," - ", simulasyon2," ",takim2_adi)
