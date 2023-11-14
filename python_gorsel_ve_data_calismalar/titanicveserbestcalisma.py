# ///////////////////////PANDAS KUTUPHANESI OZELLIKLERI////////////////////////



# \\\\\\\\\\\\\\\\\\\\\            DERS 1       ///////////////////


# import pandas as pd
#
#
# data = pd.read_csv("titanic.csv")
#
# pd.options.display.max_rows = None
# pd.options.display.width = None


# print(data.head())   #datanin ilk 5 ini getirir icine deger yazarsan yazdigin kadar getirir
# print(data.iloc[1])     #belirli bir datayi bastirir

# print(data[data['Sex'] == 'female'])  # kadin olanlari yazdirir


# print(data['Sex'])     # sadece belirledigin sutundaki verileri getirir

#print(data['Sex'].replace('female', 'F'))      #istedigin sutun altindaki degeri degistirme ama bu tek seferlik degistiriyor


#data['Sex'] = data['Sex'].replace(['female', 'male'], ['F', 'M'])   #  burada ise ustteki tek seferlikken bu kodla tam zamanli degistirme yapiyoruz F degerini female degerine atiyoruz.
# birden fazla ayni anda degistirme yapmak icin [] kullaniyorusz.
#print(data['Sex'])


# print(data.rename(columns={'Pclass': 'PassengerClass', 'Sex': 'Gender'}))  #Tek seferlik degistiriyor. column isimlerini degistiriyor

# print(data.rename(columns={'Pclass': 'PassengerClass', 'Sex': 'Gender'}, inplace=True))
# print(data)  #Burada ise ustteki tek seferlikken burada tam zamanli atama yapip column isimlerine artik yeni atama yapiyoruz.

# print(data['Age'].min())   # yazmaya gerek yok anliyosun zaten yasin min degeri ve max degeri
# print(data['Age'].max())
#print(data['Age'].sum())  # buda yas degerlerinin to0plami
#print(data['Age'].count()) #kac tane yas degeri oldugunu gosterir

# print(data['Sex'].unique())    #belli bir column altindaki degerleri bastirir mesela burada cinsiyet altinda male and female bastiriyoruz. baska neyin arasinda gececek esekle adamin arasinda mi gececek.

# print(data['Sex'].value_counts())    #   HANGI DEGERDEN KAC TANE OLDUGUNU GOSTERIYOR..!!!!! COK KULLANISLI MESELA CLASSIFICATION DEGERLENDIRMESI YAPARKEN ORNEGIN IRIS DATA SETINDE KAC CESIT CICEK VAR ONU GOREBILIRSIN

# print(data.isnull())   #eksik degerleri true olarak gosterir.
#
# print(data.isnull().sum())      #eksik degerlerin hangi columnda kac tane oldugunu gosterir.

# print(data.isnull().sum().sum())  #eksik degelerin toplamini gosterir




# \\\\\\\\\\\\\\\\\\\\\\\\\\\   DERS 2   /////////////////////////


#import pandas as pd

#pd.options.display.max_rows = None
#pd.options.display.width = None

#df = pd.read_csv('titanic.csv')

# print(df.head(10))

# print(df.drop(labels=['Embarked'], axis=1))   #   Embarked sutununu kaldirma islemi yapiliyor. ONEMLI OLAN AXIS = 1 YAPMAMIZ YOKSA SUTUN YARINE SATIR SILER. AXIS = 1 OLUNCA SUTUN ANLAMINA GELIYOR.
                                                # BU KOD TEK SEFERLIK SILIYOR.


# df.drop(labels=['Embarked'], axis=1, inplace=True)        #BURADA ISE USTTEKI KODUN TEK SEFERLIK DEGIL TAM ZAMANLI SILME ISLMINI YAPIYORUZ./.
# print(df.head(10))
#
# df = df.drop(labels=['Embarked'], axis=1)        # BU SEKILDE DE YAPABILIRDIK BURDA DA DF = ISLEMI ILE ESITLIYORUZ VE YINE TAM ZAMANLI DEGISIKLIK YAPIYORUZ..////\\\\.
# print(df.head(10))


#print(df.drop(df[df['Sex'] != 'male'].index))           #sadece secili verileri getirme. indexle beraber..



#print(df.drop_duplicates())             #Tekrar eden verileri dropluyor...

# print(df.drop_duplicates(subset=['Sex']))       #Sadece 1 kadin ve 1 erkek birakti bu islem sectigin kolonun tekrar eden verilerini dropluyor ve sadece 1 tane male ve 1 tane female kaliyor. 1. siradakini tutar

# print(df.drop_duplicates(subset=['Sex'], keep='last'))            #Tekrar edenlerin en sondaki verileri tutar. keep komutu hangi yerdeki verileri tuatagini girdigin yer.



#print(df.groupby(by=['Sex']).mean())            #Cinsiyete gore survived olanlarin ortalamasi

#print(df.groupby(by=['Sex']).count())           #cinsiyete gore verilerin toplamlari

#print(df.groupby(by=['Sex', 'Survived']).count())           #hayatta kalanlarin cinsiyetlere gore gosterimi

# print(df.groupby(by=['Sex', 'Survived']).mean())              #hayatta kalanlarin cinsiyet ayrimina gore yas ortalamari




# \\\\\\\\\\\\\\\\\\\\\\\\\\\   DERS 3   /////////////////////////

import pandas as pd

pd.options.display.max_rows = None
pd.options.display.width = None

df = pd.read_csv('titanic.csv')

#for name in df["Name"]:                # for döngüsüyle isim sütünüunu özelliklerini yazdırma işlemi.
#    print(name)


#def uppercase(x):               # Burada bir fonksiyon üretiyoruz ve ürettiğimiz fonksiyonları pandasın apply komutu ile kullanabiliyoruz.
#    return x.upper()
#print(df["Name"].apply(uppercase))                  #burada apply komutu ile ürettiğimiz fonksiyonu uyguluyoruz. buradaki fonksiyonumuz isimleri büyük harfle yazmaya yazıyor.


# data_a = {'id': ['1', '2', '3'],
#           'isim': ['Tayyib', 'Kaan', 'Alp'],
#           'soyisim': ['isen', 'tki', 'coko']}                   #Verilerimizi oluşturuyoruz sözlük biçiminde yazdık
#
# data_b = {'id': ['4', '5', '6'],
#           'isim': ['Aysen', 'Gunes', 'Lisa'],
#           'soyisim': ['kely', 'london', 'vorte']}           #Aynı sekilde 2. verilerimizi de olusturduk
#
# df_a = pd.DataFrame(data_a)             #burada sozluklerimizi pandas formatındaki verilere çeviriyoruz
# df_b = pd.DataFrame(data_b)
#
# df_ab = pd.concat([df_a, df_b])                      #CONCAT FORMATI BIZIM 2 TANE AYRI VERI SETIMIZI BIRLESITMRMIZE YARIYOR. CONCAT ONEMLI BURADA 2SININ TOPLAMINI DF_AB DEGISKENINE ATADIK.
# print(df_ab)                                        # sonuna axis=1 dersek ise yan yana ekler alt alta degıl



# employee_data = {'employee_id': ['1', '2', '3','4'],
#           'name': ['Tayyib', 'Kaan', 'Alp', 'Caglayan']}                   #Verilerimizi oluşturuyoruz sözlük biçiminde yazdık
#
#
# sales_data = {'employee_id': ['3', '4', '5','6'],
#           'sales': ['123', '456', '678', '9009']}                   #Verilerimizi oluşturuyoruz sözlük biçiminde yazdık
#
#
# employee = pd.DataFrame(employee_data)      #EVET GORDUGUMUZ GIBI BURADAKI DATALARIN SUTUNLARI USTTEKILER GIBI AYNI DEGIL BURADA FARKLI SUTUNLARA DA SAHIP VERILERIMIZ VAR
# sale = pd.DataFrame(sales_data)        #MERGE KOMUTU ILE FARKLI SUTUNLARI OLAN VERILERIMIZI DE BIRLESTIRIYORUZ FAKAT DUZ BIRLESTIRME YAPARSAK AYNI ORAN VERILERI BULUP ONLARI YAZDIRACAK
                                        #YANI BURADAKI ORTAK OLAN DEGERLER ID DEGERLERI. ID DEGERLERI 3 VE 4 OLANLAR ORTAK OLDUGU ICIN SADECE ORTAKLARI YAZDIRDI.
#print(pd.merge(employee, sale, on='employee_id'))          #on etiketi ile hangi veriye gore yazdi cikaracagini da ekstra ekleyebiliyoruz. onu yazmazsak da ortak olani ekliyor. ama oradan esneklik yapiyoruz.

#print(pd.merge(employee, sale, on='employee_id', how='outer'))      #BURADA HOW METODUNU KULLANARAK OUTER KOMUTUYLA BUTUN VERILERI YAZDIRIP ORTAK OLANLAR YAZILIR DEGER KARSILIGI OLMAYANLAR NAN GECER.

#print(pd.merge(employee, sale, on='employee_id', how='left'))    #BURADADA SOLDAKI VERILERIN HEPSINI GETIR SAGDA DA ONLARLA ESLESENLERI GETIRIR


#print(pd.merge(employee, sale, on='employee_id', how='right'))      #SOYLEMEME GEREK YOK SAG YANI 2. GIRILEN VERI SETINE GORE HAREKET EDER USTTEKI DE ILK GIRILEN VERI SETINE GORE














