
# IRIS VERI SETI CALISMASI

# from sklearn.datasets import load_iris
# iris_dataset = load_iris()
#
# from sklearn.model_selection import train_test_split
# x_ogren, x_test, y_ogren, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])
# print(x_ogren.shape)
# print(x_test.shape)
#
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors = 1)
#
# knn.fit(x_ogren, y_ogren)
#
# x_yeni = [[2.6, 3.2, 4.5, 2.4]]
# tahmin = knn.predict(x_yeni)
# print(tahmin)
#
# dogruluk = knn.predict(x_test)
# print(dogruluk)
#
# import numpy as np
# print(np.mean (dogruluk == y_test) * 100)






# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# dataset = pd.read_csv("Data.csv")
# print(dataset.values[0])
# print(dataset.ndim)
# print(dataset.size)
# print(dataset.shape)
# print(dataset.values.shape)
# print(dataset.dtypes)
# values = dataset.values
# print(values[0])
# print(values[0][0])
# print(values[0,0])
# print(values[0:2])
# print(values[:,1])
# print(dataset.iloc[2].values)


#   EKSIK VERILERI DOLDURMA

# x = dataset.iloc[:,:-1].values
#
# y = dataset.iloc[:,-1].values
#
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# imputer.fit(x[:,1:])
# x[:,1:] = imputer.transform(x[:,1:])
#
#
# # 2 DEN DAHA AZ SINIFLANDIRMALARDA LABELENCODER 2 DEN DAHA FAZLA SINIFLANDIRMALARDA ONEHOTENCODER KULLANILIR
#
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
#
# ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
# x = np.array(ct.fit_transform(x))
#
#
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y)
#
# from sklearn.model_selection import train_test_split
# x_ogren, x_test, y_ogren, y_test = train_test_split(x,y,test_size=0.2)
#
#
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# x_ogren[:,3:] = scaler.fit_transform(x_ogren[:,3:])
# x_test[:,3:] = scaler.transform(x_test[:,3:])
#
# print(x_ogren)
# print(x_test)




# BASIT LINEER REGRESYON UYGULAMASI

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# dataset = pd.read_csv("Salary_Data.csv")
# x = dataset.iloc[:, :-1].values  #ozellikler / bagimsiz degisken
# y = dataset.iloc[:,-1].values # bagimli degisken
#
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=1/3, random_state=0)
#
#
# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(x_train,y_train)  #ogrenme icin fit fonksiyonu kullaniliyor
#
#
# y_pred = regressor.predict(x_test) #predict fonksiyonu test icin kullaniliyor
#
#
# # OGRENME SONUCLARINI GORSELLESTIRILMESI..!!! MATLOPLIB KUTUPHANESI KULLANILIYOR
#
# plt.scatter(x_train, y_train, color='red')
# plt.plot(x_train, regressor.predict(x_train), color='blue')
# plt.title('Maas ve Deneyim (Ogrenme verisi)')
# plt.xlabel('Deneyim')
# plt.ylabel('Maas')
# # plt.show()
#
#
# # TEST SONUCLARININ GORSELLESTIRILMESI..!!!
#
# plt.scatter(x_test, y_test, color='red')
# plt.plot(x_train, regressor.predict(x_train), color='blue')
# #buradaki train komutlari degismez cunku unik yapilar oldug icin ogrenme verisindeki verileri ceker ve bunlar degismez. buna gore testleri yorumlar o yuzden degismez.!!
# plt.title('Maas ve Deneyim (Ogrenme verisi)')
# plt.xlabel('Deneyim')
# plt.ylabel('Maas')
# # plt.show()
#
#
#
#
# #Tahmin yapiyoruz
#
# # print(regressor.predict([[12]]))   # neden 2 tane parantez kullandik cunku:  2 boyutlu diiz oldugu icin. eger 1 parantezli kullansaydik tek boyutlu dizi olurdu hic kullanmasaydik ise skaler bir dizi olurdu
#
#
#
# # DOGRUNUN DENKLEMINI BULMAK
#
# print(regressor.coef_) #b1
# print(regressor.intercept_) #b0
#
# # y = b1 * x + b0
# # y = 9345.9 * x + 26816.19







