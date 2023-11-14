import pandas as pd


pd.options.display.max_rows = None
pd.options.display.width = None

df = pd.read_csv('./penguins_size.csv')
#  print(df.info())         # VERI SETINDEKI VERILERIN TURLERINI KAC ADET VERI SATIRININ DOLU OLDUGUNU GOSTERIR.
# print(df.shape)       # KAC TANE DEGER VE KOLONUMUZ OLDUGUNU GOSTERIR.
#print(df.describe())    #SAYISAL OLAN DEGERLERI VERIR.     BUNLARIN STANDART SAPMA MINIMUM MAKSIMUM GIBI SAYISAL VERILERINI VERIR
#print(df.describe(include='all'))       #BU DA BUTUN DEGERLERI GETIRIR.
# print(df.corr(numeric_only= True))  #KORELASYON DEGERLERINI GOSTERIR. BURADA SADECE NUMERIK DEGERLERI OLAN SUTUNLARIN KORELASYON DEGERLERINI ALMAK ICIN NUMERIC_ONLY METDOUNU KULANDIK.
                                        # TABI ARALARINDA STRING OLAN KOLONLAR DA OLABILIR ONLARI DA TO_STRING METODUIYLA STRINGE CEVIRMEMIZ GEREKIYOR

import seaborn as sns                 #SEABORN KUTUPHANESI MAPLOTLIB KUTUPHANESI UZERINE INSA EDILMIS BIR GRAFIK GORSELLESTIRME KUTUPHANESIDIR ORADA BUNU IMPORT EDIYORUZ
import matplotlib.pyplot as plt   #MATPLOTLIB KUTUPHNESI ISE PYTHONDA EN POPULER GRAFIK KUTUPHANESIDIR BURADA DA MATPLOTLIB JKUTUPHANESINI IMPORT DIYOUZ
#
#
# sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Reds')  #BURADA SEABORNDA IMPORT ETTIGIMIZ SNS YI HEATMAP KOMUTU KULLANARAK GORSELLESTIRMEYE BASLIYORUZ
                                                                    #ARDINDAN ISE DF.CORR METODUYLA (USTTE DE KORELASYONA YARADIGINI SOYLEMISTIK) KORELASYONU CAGIRIYORUZ NUMERIC ONLY OLARAK
                                                                    #SONRA ANNOT TRUE KOMUTUYLA GORSEL GRAFIGIMIZIN USTUNE SAYISAL DEGERLERI BASTIRIYORUZ.
                                                                    #ARDINDAN CMAP KOMUTUYLA GRAFIGIMIZE SAYISAL VERILERIN BUYUKLUGUNU OLCMEK ICIN RENK PALETI EKLIYORUZ.
# plt.show()     #PLT SHOW METHODU ISE MAPLOTLIB KUTPHANESINDEN CEKTIGIMIZ BIR KOMUT BU KOMUT ISE SHOW KOMUTU ILE BIRLESIP BIZE ISTEDIGIMIZ GORSEL GRAFIGI BASTIRIYOR. PRINT OLARAK DUSUN.

#print(df.isna().sum())  #VERI SETIMIZDEKI EKSIK DEGERLERI GOSTERITYOR. SUM OLMADAN TRUE FALSE OLARAK GOSTERIYOR SUM EKELDIGMIZDE HANGI KOLONDA KAC EKSIK VAR BUNU SAYISAL OLARAK GOSTERIYIOR.
#print(df.isna().sum() / df.count() *100)         #BURADA ISE EKSIK DEGERLERIN TOPLAM DEGERLERE YUZDE ORANINI GORUYORUZ. YANI DF.COUNTA BOLUYORUZ / ISAREYTIELE 100 ILE CARPIYORUZ 100DE GORMEK ICIN

#nan_percentage = (df.isna().sum() / df.count() *100)        #YUZDELERI BIR DEGISKENE ATIYORUZ
#nan_count = df.isna().sum()         #TOPLAMI DEGISKENE ATIYORUZ

#print(nan_count)

#nan_table = pd.concat([nan_count, nan_percentage], axis=1)  #BURADA ISE NAN_COUNT VE NAN_PERCENTAGE TABLOSAL VERILERINI BIRLESTIRIP YENI BIR TABLO OLUSTURUYORUZ. AXIS 1 ILE YATAY YAPIYORUZ.
#nan_table.columns = ['Count', 'Percentage']     #BURADA ISE KOLON ISIMLERINI DEGISTIRIYORUZ.
# print(nan_table) #BURADA YENI TABLOMUZUN CIKTIINI GORUYORUZ.


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\EKSIK VERILERI TAMAMLAMA/////////////////////////////////////////////////////
from sklearn.impute import SimpleImputer        #BURADA SKLEARN KUTUPHANESINDEN SIMPLEIMPUTER IMPORT EDIYORUZ CUNKU EKSIK VERILERI TAMAMLAMA KOMUTU BU

imputer = SimpleImputer(strategy='most_frequent')   #EN COK TEKRAR EDEN VERILERI SIMPLEIMPUTER KOMUTU ARACILIGIYLA IMPUTER DEGISKENINE ATIYORUZ
df.iloc[:, :] = imputer.fit_transform(df)       #BURADA ISE VERILERIN EN BASINDAN EN SONUNA KADAR FIT_TRANSFORM ILE DF VERI SETINDE EKLEMELER YAPIYORUZ IMPUTERI IMPORT EDIYORUZ.
#print(df.isna().sum())      #BURADA KONTROL EDIYORUZ EKSIK VERI KALDI MI DIYE.


from sklearn.preprocessing import LabelEncoder      #KOLONLARA KARAKTER YERINE INT SAYI ATAMASI SAYPMAMIZA YARIYOR. METIN VERILERI SAYISAL VERILERE CEVIRIYOR.

le = LabelEncoder()         #BURDA ATAMASINI YAZPIYORUZ
df['gender'] = le.fit_transform(df['sex'])      #VERI SETIMIZDEKI SEX KOLONUNU LE.FIT_TRANSFORM ILE DF GENDER DEGISKENINE SAYISAL VERILER ATANARAK ATIYORUZ.
                                                #GENDER DOIYE YENI BIR KOLON OLUSTURUYORUZ.
#print(df.head())
#print(df['sex'].value_counts())         #SEX KOLONUNDAKI DEGISKENLERIN NE KADAR TEKRARLANDIGINI GOSTERIYOR.
#print(df['gender'].value_counts())      #BURADA DA SEX KOLONUNDA 1 TANE . ISRETI OLDUGUNDAN . YA 0 DEGER ATAMASI YAPIP FEMALE VE MALE DEGERLERINE 1 VE 2 DEGERLERINI VERMIS BURADAN GORUYOERUZ. KAC TANE DEGER ATAMASI YPTINI

df = df.drop(labels=['sex'], axis=1)        #SEX KOLONUNU DROPLUYORUZ VERI SETIMIZDEN!!!!!!!!!!!
#print(df.head())

#print(df['species'].value_counts())     #SPECIES KOLONUNUN VERILERINIIN KAC KERE TEKRARLANDIGI
#print(df['species'].value_counts().reset_index())       #SPECIES KOLONUNDAKI VERILERIN INDEXLERINI RESETLIYORUZ VE 0 1 2 DEGERLERI VERILIYUOR(KAC TANE VARSA) INDEXTEKI DEGERLERI KOLON OLARAK GETIRIYORUZ
                                                        #SEABORNLA OLUSTURGUMUZ KUTUPHANEYI DAHA KOLAY HALE GETIRMEK ICIN YAPIYORUZ YAN BARPLOT OLUSTURUYORUZ

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ VERI GORSELLESTIRME 2. KISIMMMM /////////////////////////////////

#species_count = df['species'].value_counts().reset_index(name='count')  #RESET INDEX BIR PANDAS DATAFREAMESININ INDEKSINI SSUTUNA DONUSTURURTURUR. NAME KISMI ISE DONUSTURDUGU SUTUNA ISIM VERMEYE YARAR
                                        #BURADA VERDIGIMIZ ISIMI ASSADGIDA KULLANABILIYORUZ CUNKU OYLE BIR SUTUN OLUSTURDUK USTTEKI TARAFTA

#sns.barplot(data=species_count, x='species', y='count')     #SANS.BARPLOT() İŞLEVİ, BİR PANDAS DATAFRAME'İNDEN BİR ÇUBUK GRAFİĞİ OLUŞTURUR.
                                                            #DATA PARAMETRE, ÇUBUK GRAFİĞİNİN OLUŞTURULACAĞI DATAFRAME'İ BELİRTİR.
                                                            #X PARAMETRE, ÇUBUKLARIN X EKSENİNDE GÖSTERİLECEĞİ SÜTUNUN ADINI BELİRTİR.
                                                                #Y PARAMETRE, ÇUBUKLARIN Y EKSENİNDE GÖSTERİLECEĞİ SÜTUNUN ADINI BELİRTİR.
#plt.show() #PRINT GIBI DUSUN GRAFIGI YAZDIRMAYA YARIYORUR.


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\BURADA TEK TEK GIRIP TURLERIN AGIRLIKLARININ GRAFIGINI CIKARTIYORUZ/////////////////////////////////////

# sns.kdeplot(df[df['species']=='Adelie']['body_mass_g'])     #SNS.KDEPLOT ILE BIR GRAFIK OLUSTURUYORUZ VE ICINE VERI SETIMIZDEKI GRAFIGINI GORMEK ISTEDIGIMIZ VERININ YOLUNU GIRIYORUZ.
# sns.kdeplot(df[df['species']=='Gentoo']['body_mass_g'])         #SNS.KDEPLOT ILE BIR GRAFIK OLUSTURUYORUZ VE ICINE VERI SETIMIZDEKI GRAFIGINI GORMEK ISTEDIGIMIZ VERININ YOLUNU GIRIYORUZ.
# sns.kdeplot(df[df['species']=='Chinstrap']['body_mass_g'])      #SNS.KDEPLOT ILE BIR GRAFIK OLUSTURUYORUZ VE ICINE VERI SETIMIZDEKI GRAFIGINI GORMEK ISTEDIGIMIZ VERININ YOLUNU GIRIYORUZ.
# plt.show()      #EKRANA GRAFIGI GETIRIYORUZ.

#BURADA BU ISLEMI FOR DONGUSU ILE KOD TEKRARI OLMADAN YAPICAZ.

# for spec in df['species'].unique():     #BURADA SPECIES ALTINDAKI DEGERLERIN LISTESINI UNIQ SEKILDE OLUSTURUYORUZ KI 1 KERE YAZSIN VE BURADA BU DEGERLERI BASTIRIYORUZ.
#     sns.kdeplot(df[df['species']==spec]['body_mass_g'], fill=True, label=spec)   #BRUADA ISE HEDEF KONUMUNU SPEC YAPTIK VE DEGERLERI GRAFIGE BASTIRDIK.
# plt.legend()        #AYNI ZAMANDA FILL KULLANARAK GRAFIGIN ICINI DOLDURDUK. LABEL ISE PEGUEN TURLERININ ISIMLERINI DONDURUP LEGENDE ATIYOR. LEGEND ISE SAG USTTEKI GORSELI BASTIRIYOR.
# plt.show()


#////////////////////////// USTTEKINI DAHA FAZLA VERIYE UYGULAMA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# for col in df.columns[2:-1]:  #SAYISAL DEGERLERI OLAN VERI BASLIKLARIMI YANI KOLONLARIMI BURADA SECIYORUM.
#     for spec in df['species'].unique():     #BURADA SPECIES ALTINDAKI DEGERLERIN LISTESINI UNIQ SEKILDE OLUSTURUYORUZ KI 1 KERE YAZSIN VE BURADA BU DEGERLERI BASTIRIYORUZ.
#         sns.kdeplot(df[df['species'] == spec][col], fill=True, label=spec)   #BRUADA ISE HEDEF KONUMUNU SPEC YAPTIK VE DEGERLERI GRAFIGE BASTIRDIK.
#         plt.legend()                    #BUTUN DEGERLERIN GRAFGIGE DOKULMUS VE DAGILIM YAPILMIS HALI
#     plt.show()      #BURADA PLT.SHOWU ICERI ALMAMIZIN SEBEBI ISE 1 GRAFIK TAMAMLANDIKTAN SONRA YAZDRIRILMASINI ISTEMEMIZ. DISARI YAZARSAK ANLASILMAZ BIR GRAFIK OLUSTURUYOR VE UST USTE YAZDIRIYOR.



#\\\\\\\\\\\\\\\\\\\\\\\\\\\ SIMDI YUKARIDA YAPTIKLARIMIZIN HEPSINI GEREKSIZ KILAN HAZIR OLAN BIR KOMUT GOSTERICEM. USTTEKIULER DE ONEMLI AMA BU HEPSINI HAZIR OLARAK BIZE SUNUYOR////////////

#sns.pairplot(df, hue='species', height=1, diag_kind='kde')     #sns.pairplot() işlevi, bir veri setindeki tüm değişkenler arasındaki ilişkileri görselleştirmek için kullanılır.
                                        # Bu işlev, her bir değişkenin diğer tüm değişkenlerle olan ilişkisini bir scatter plot olarak çizer.

#tight_layout=False                 #bu kod ise tight_layout parametresi, çizimin düzenini otomatik olarak ayarlayıp ayarlamayacağını kontrol eder.
                                    # Bu parametre, sns.pairplot() işlevine bir argüman olarak gönderilmemelidir.


                                            #diag_kind parametresi, diyagonal scatter plot'unun türünü kontrol eder.
                                            # Bu parametreye, "hist" değerini vererek, diyagonal scatter plot'unun bir histogram olarak çizilmesini sağlayabilirsiniz.
#plt.show()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MAKINE OGRENMESI ALANINA GECIS YAPIYORUZ ////////////////////////////////////////////////////////

#print(pd.get_dummies(df[['island']], dtype=int))  #////////////////////////////////////ONE HOT ENCODING YAPIYTORUZ BURADA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                                        #PANDASTA ONCEDEN DUMMIES DIRTEKT 0 VE 1 DEGERLERI DONDURURKE  SIMDI TRUE FALSE DEGERELRI DONDURUYOR.
                                        # BU DEGERLERI 0 VE 1 OLARAK BASTIRMAK ICIN DTYPE=INT KOMUTUNU YAZMAMIZ GEREKLI O ZAMAN 0 VE 1 DEGELERI DONDURULUYOR.
                                        #VERI DEGERI HANGI ADADANSA ONUN DEGERI 1 DIGERLERI 0 OLUYOR YANI VERI SETINDE HANGI VERI YAZIYORSA ONA 1 DIGER UNIQ VERILERE 0 VERIYOR.

#print(pd.get_dummies(df[['island']], dtype=int, drop_first=True))   #BURADA DROP_FIRST KOMUTU ILE ILK KOLONU DROPLUYORUZ, EGER IKISI DE 0 ISE SONUC ZATEN ILK KOLON OLACAKTIR
                                    #BU DA BIZE KODUN OKUNURLUGUNU VE KODUN BOYUTSALLIGINI AZALTIYOR

island = pd.get_dummies(df[['island']], dtype=int, drop_first=True)     #BU YENI ADA VERI SETIMIZI BIR DEGISENE ATIYORUZ. 0 VE 1 OLANLARI

df2 = pd.concat([df, island], axis=1).drop(['island'], axis=1)          #BU YENI VERI SETIMIZI DE ONCEKI ANA VERI SETIMIZE ENTEGRE EDIYORUZ VE IKISINI BIRLESTIRIP DF2 DIYE YENI BIR VERI SETINE ATAMASINI YAPITYORUZ

target, features = df2.species, df2.drop('species', axis=1)     #BURADA ISE VERILERIMIZI TARGET VE FEATURES(OZELLIKLERI) OLARAK AYIRIYORUZ. TARGET, FEATURES KOMUTU ILE ESITLIGIN SONRASINDA
                                            #DF.SPECIES DEDIGIMIZ DE DIREKTOLARAK KOLONU SECMIS OLUYORUZ. O TARGET OLUYOR. VE FEATURESTE DROP ISLEMI YAPIYORUZ TARGETI FEATURESTEN CIKARYIORUZ. AXIS 1 ILE!!!!
#print(features)

from sklearn.preprocessing import StandardScaler            #STANDAR SAPMA SUM I STANDART ORTALAMA SUM LARI ICIN GEREKLI KUTUPHANEYI IMPORT EDIYORUZ.
                                                            # ORTALAMASINI STANDART SAPMASINA SIGMA OLAN NORMAL DAGILIMA CEVIRMEK ICIN.
scaler = StandardScaler()       #STANDART SCALER ATIYORUZ!

scaler.fit(features.iloc[:, :4])        #BURADA Z SCORE(HER BIR KOLONUN KENDI ICINDEKI ORTALAMASI BUTUN DEGERLERDEN CIKARTILIP STANDART SAPMASINA BOLUNUYOR.)  HESAPLANIYOR
                                        # NEDEN FIT TRANSFORM ILE YAPMADIK CUNKU GELECEKTE BU SAYISAL KOLONLARIN (FEATURESLERIN) HANGI STANDART SCALING DE OLCEKLENDIGINI TEKRARDAN HATIRLAMAK ISTIYORSAK
                                        #YA DA BASKA BIR ZAMAMN KULLANCAKSAK ILERDE BIR DAHA FIT VE TRANSFORMU AYIRMAMIZ GEREKIYOR...!!!!!!
                                        #   EGER AYIRMAZSAK HER YENI VERI GELDIGINCE O YENI GELEN VERININ STANDART SAPMASI VE ORTALAMASINA GORE SCALING EDIYOR.!!!!!

features.iloc[:, :4] = scaler.transform(features.iloc[:, :4])       #TRANSFORM ETIGMIZ DEGERLERI TEKRARDAN DATA SETINNUSTUNE YAZIYTORUZ
                            #ILK 4 TANE SAYISAL KOLONLAR STANDART SEKILDE OLCEKLENMIS OLDU....!!! STNDART SCALING ISLEMI TAMAMLANDI

from sklearn.preprocessing import LabelEncoder               #TARGETLER LABEL ENCODING YAPILIYORR(YANI 0 1 2 SEKLINCE YAZILACAK)!!!! SUANDA STRING FORMATINDA DURUYORLAR

le = LabelEncoder()     #LABEL ENCODER OBJESI OLUSUTUROYURZ..
target_encoder = le.fit_transform(target)
#print(target_encoder)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ARTIK TRAIN VE TEST SPLIT YAPILACAK ML ICIN ///////////////////////////////////////////////////////

from sklearn.model_selection import train_test_split            #TRAIN VE TEST SETLERINI AYIRMAK ICIN GEREKLI KUTUPHANEYI IMPORT EDIYORUZ.
x_train, x_test, y_train, y_test = train_test_split(features, target_encoder, test_size=0.2, random_state=41)      #BURADA ISE ONCE VERI SETINDEKI SAYISAL OZELLIKLERI (x) SONRASINDA TARGETIMIZI ATIYORUZ (Y)
                                                #SONRAINDA TEST SIZE IMIZI YAZIYORUZ BURADA 0.2 YANI YUZDE 80 E YUZDE 20 OLARAK AYIRIYORUZ. RANDOM STATE I ISE 41 YA DA 42 RANDOM STATE TAM OLARAK NE BILMIYORUM.

#print(x_train.shape, x_test.shape) #SHAPE KOMUTU BURADA ICLERINDE KAC TANE ORNEK OLDUGNU YANI VERI SETI OLDUGNU SOYLUYOR.

from sklearn.tree import DecisionTreeClassifier #KARAR AGACI IMPORT EDIYORUZ BUNUNLA TRAIN EDICEZ.!!!!!!!!
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score  #MODELIMIIZIN PERFORMANSINI OLCMEK ICIN BU KUTUPHANEYI IMPORT EDIPORUZ.!!!!1 EKURISI VE CLASS REPORT DA EKLIYORUZ!!!!

tree = DecisionTreeClassifier() #AGAC ATIYTORUZ SUANDA BIR PARAMETRE GIRMEYE GEREK YOK ICINE

tree.fit(x_train, y_train)  #MODEL EGITIYORUZ FEATURE VE TARGETLARIN TRAIN OLARAK AYIRDIIMGIZ VERI SETLERIYLE.

predict = tree.predict(x_test) #X TEST DEGERLERIM GERCEK DEGERLERIME AKTARILSIN. Y TEST DEGERLERIM BENIM GERCEK DEGERLERIM. BURADA ONUN ICIN X TEST DEGERLERINI PREDICT EDIYORUZ.

confusion_matrix(y_test, predict)  #BURADADA X TEST DEGERLERI GERCEK DEGERLERIMLE NE KADAR BENZER DIYE BAKIYORUZ.

sns.heatmap(confusion_matrix(y_test, predict), annot=True, cbar=False)     #BURADA ISE BU VERILERIN DOGRULUGUNU GRAFIK OLARAK EKRANA BASTIRIYORUZ..
#plt.show()      #SHOT METODUYLA


#print(classification_report(y_test, predict))           #DOGRU TAHMIN ORANLARINI GORUYORUZ PRECISION, RECALL, F1 SCORE, SUPPORT DEGERLERINI BURADAN CLASSIFICATION REPORT SAYESINDE GOREBILIYORUZ.

#print(accuracy_score(y_test, predict) * 100)           #BU ACCURCY SCORE DOGRULUK ORANIMIZI GOSTERIYOR
                                                         #ACCURACY E BAKIYORUZ BURADAD DA. TEST ICIN SAYILAR ESIT OLDUGUNDAN HER BIRINDE 50 SER TANE OLDUGUNDAN DUZGUNNBIR DEGER CIKACAKTIR.
                                                            #SINIFLAR ARASINDAKI ORNEK SAYILARI BIRBIRINE YAKIN YANI

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ DESICION TREE EGITIMI BITTI BUNU YAPTIK SIMDI///////////////////////////////////

final_df = pd.concat([features, pd.Series(target_encoder, name='Target')], axis=1)    #EGITILMIS DATASETIMIZI SIMDI KAYDEDIYORUZ.!!!

final_df.to_csv('penguen_boyutu.csv', index=False, header=False, encoding='utf-8', sep=',')     #SIMDI BURADA DATAFREAMEMIZIN SON HALINI KAYDEDIYORUZ CSV SEKLINDE
                                                        #INDEX FALSE DEMEMIZIN SEBEBI GENELDE INDEXLERIN ISTENMEMESIDIR YOKSA DATASETIMIZDE EN BASTA GEREKSIZ BIR INDEX KALABALIGI OLUYOR.
                                                        #HEADET ISTENMIYORSA YANI BASLIKLAR HEADER FALSE KOMUTUNU GIRIYOTRUZ
                                                        #ENCODING ISE UTF-8 YAPIP HER BILGISAYARDA CALISMASINI SAGLIYORUZ. UYUMLU HALE GETIYIOROERUZ HATA VERMEMEISI ICIN
                                                        #SEP KOMUTU ISE VERILERIN NASIL AYRILACAGINI SECIYOR BAZI EXCEL DOSYALARI BUNU ; ILE AYRILMASINI DESTEKLEDIGINDEN ORAYA ISTERSEK ; YAZIYOTUZ YA DA ISTERSEK BOS BIRAKIP , ILE AYRILIYOR BEN ORARA GOSTERMELIK KOYDUM.






















