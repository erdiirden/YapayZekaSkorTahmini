import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Veri setini yükle
data = pd.read_csv('C:/Users/erdi/Desktop/son20yil/son20sene.csv')
print(data)

# Tahmin yapılacak maçın takım adlarını belirle
takim1_adi = 1
takim2_adi = 2


# Tahmin yapılacak maçın özelliklerini belirle
takim1 = data[data['Takim_adi'] == takim1_adi]
#takim1_toplamMac = takim1['Oynadigi_mac_sayisi']
#takim1_attigiGol = takim1['Attigi_gol_sayisi']
#takim1_yedigiGol = takim1['Yedigi_gol_sayisi']
#takim1_galibiyet = takim1['Galibiyet_sayisi']
#takim1_beraberlik = takim1['Beraberlik_sayisi']
#takim1_maglubiyet = takim1['Maglubiyet_sayisi']
takim1_ozellikler = takim1[['Oynadigi_mac_sayisi', 'Attigi_gol_sayisi', 'Yedigi_gol_sayisi', 'Galibiyet_sayisi', 'Beraberlik_sayisi', 'Maglubiyet_sayisi']]


takim2 = data[data['Takim_adi'] == takim2_adi]
#takim2_toplamMac = takim2['Oynadigi_mac_sayisi']
#takim2_attigiGol = takim2['Attigi_gol_sayisi']
#takim2_yedigiGol = takim2['Yedigi_gol_sayisi']
#takim2_galibiyet = takim2['Galibiyet_sayisi']
#takim2_beraberlik = takim2['Beraberlik_sayisi']
#takim2_maglubiyet = takim2['Maglubiyet_sayisi']
takim2_ozellikler = takim2[['Oynadigi_mac_sayisi', 'Attigi_gol_sayisi', 'Yedigi_gol_sayisi', 'Galibiyet_sayisi', 'Beraberlik_sayisi', 'Maglubiyet_sayisi']]


tahmin_ozellikler = takim1_ozellikler.values.tolist()[0] + takim2_ozellikler.values.tolist()[0]
tahmin_ozellikler = np.array([tahmin_ozellikler])

# İki takımın özelliklerini birleştir
#takim1 = data[data['Takim_adi'] == takim1_adi]
#takim1_ozellikler = takim1[['Takim_adi','Oynadigi_mac_sayisi', 'Attigi_gol_sayisi', 'Yedigi_gol_sayisi', 'Galibiyet_sayisi', 'Beraberlik_sayisi', 'Maglubiyet_sayisi']]

#takim2 = data[data['Takim_adi'] == takim2_adi]
#takim2_ozellikler = takim2[['Takim_adi','Oynadigi_mac_sayisi', 'Attigi_gol_sayisi', 'Yedigi_gol_sayisi', 'Galibiyet_sayisi', 'Beraberlik_sayisi', 'Maglubiyet_sayisi']]
#tahmin_ozellikler = list(takim1_ozellikler) + list(takim2_ozellikler)
#tahmin_ozellikler = takim1_ozellikler + takim2_ozellikler


print(tahmin_ozellikler)



# Özellikler ve hedef değişkeni ayır
#features = data[['Takim_adi','Oynadigi_mac_sayisi', 'Attigi_gol_sayisi', 'Yedigi_gol_sayisi', 'Galibiyet_sayisi', 'Beraberlik_sayisi', 'Maglubiyet_sayisi']]
#target = data['Takim_adi']
#features = data.drop('Takim_adi', axis=1)
features = data.drop('Puan', axis=1)
target = data['Puan']


# Eğitim ve test veri setlerini bölelim
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

# Çoklu lineer regresyon modelini oluştur
model = LinearRegression()

# Modeli eğit
model.fit(X_train, y_train)

# Tahmin yap
tahmin_skor = model.predict(tahmin_ozellikler)



print("Tahmin edilen skor:", tahmin_skor)

