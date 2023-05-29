import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Veri setini yükle
data = pd.read_csv('C:/Users/erdi/Desktop/skorTahminYapayZeka/verisetleri/STSL_istatistikler.csv')
print(data)

# Tahmin yapılacak maçın takım adlarını belirle
takim1_adi = "BESIKTAS"
takim2_adi = "TRABZONSPOR"

# Tahmin yapılacak maçın özelliklerini belirle
takim1 = data[data['TakimAdi'] == takim1_adi]
takim1_ozellikler = takim1[['MacSayisi', 'AtGol', 'YeGol', 'Galibiyet', 'Beraberlik', 'Maglubiyet']]

takim2 = data[data['TakimAdi'] == takim2_adi]
takim2_ozellikler = takim2[['MacSayisi', 'AtGol', 'YeGol', 'Galibiyet', 'Beraberlik', 'Maglubiyet']]

tahmin_ozellikler1 = takim1_ozellikler
tahmin_ozellikler2 = takim2_ozellikler

#tahmin_ozellikler = pd.concat([takim1_ozellikler, takim2_ozellikler], axis=1).values


# Özellikler ve hedef değişkeni ayır
features = data.drop(['Puan', 'TakimAdi'], axis=1)
target = data['Puan']

# Eğitim ve test veri setlerini bölelim
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# Çoklu lineer regresyon modelini oluştur
model = LinearRegression()

# Modeli eğit
model.fit(X_train, y_train)


# Tahmin yap
tahmin_skor1 = model.predict(tahmin_ozellikler1)
tahmin_skor2 = model.predict(tahmin_ozellikler2)

# Tahminleri tek rakama indirme
skor1 = int(str(tahmin_skor1[0])[0])
skor2 = int(str(tahmin_skor2[0])[0])

print("Tahmin edilen skor:","\n", takim1_adi," ", skor1," - ", skor2," ",takim2_adi)
