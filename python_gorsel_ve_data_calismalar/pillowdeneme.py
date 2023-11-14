#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\IMAGE KUTUPHANESINDE HIZLI PROCCES ISLEMLERI TEMELLER. ///////////////////////////////

# import os
#
# from PIL import Image           #GORSEL MANIPULASYONU ICIN GEREKLI OLAN KUTPHANELERIMMIIZ IMPORT EDIOYURZ.
# import PIL
#
# img = Image.open('./thumb.jpeg')        #BURADA ISE DOSYAMIZIN ICINDEKI GORSELI KUTUPHANEMIZ YARDIMIYLA ACIYOTUZ VE DEGISKENE ATIYORUZ
# #img.show()             #GORSELI ACMAMIZA YARIYOR. PRINT GIBI
#
# #print(img.size)     #GORSELIN BOYUT OZELLIKLERINI GOSERTIROYR
# #print(img.mode)     #GORSELIN HANGI MODDA OLDUGNU GOSTERIYOR.
#
# #img.rotate(90).show()       #BURADA ISE GORSELIN FORMATINI KORUYARAK RESMI 90 DERECE DONDRYORUZ.
#                         #ONEMLI OOLAN SHOW METDOGUNU BURADA YAPMAK ISTEDIGIMIZ ISLEMI YAPTIKTAN SONRA EKLEYINCE CALISIYOR.
#
#                         # Resmi 90 derece döndür.
#                         #image = image.rotate(90)
#                                                     #AMAA ISTERSEK BOYLE ATAYIP DA BASTIRABILIRIZ.
#                         # Resmi ekrana yazdır.
#                         #image.show()
#
# #img.rotate(90, expand=1).show()     #BUARADA EXPAND 1 KOMUTU ISE RESMI KOMPLE 90 DERECE DONDURMEMIZE YARIYOR YANI RESMIN BOYUTLARINI DA DEGISTIRIYOR.
#
# #img.transpose(method=Image.FLIP_TOP_BOTTOM).show()      #RESMIN TRANSKOZUNU ALIYORUZ YANI TAM TERSINI GETIRIYORUZ AYNALAMA YONTEMI YAPIYOTUZ YANI.
#
# #img.resize((300, 300)).show()       #BURADA FOTOGRAFI ORANTI OLMADAN KUCULTUYOR. YENIDEN BOYUTLANDIRMAYA YARIYOR RESIZE.
#
# width, height = img.size       #BURADA IMAGE MIZIN WIDTH DEGERINI WIDTH DEGISKENINE ATIYORUZ. HEIGHT DEGERINI ISE HEIGHT DEGISKENINE ATAMASINI YEPIYORTUZ. ARTIK BU DEGISKENLERLE UZERINDE OYNMAY YAPICAZ.
#
# new_width = int(width/3) #YENI WIDTH DEGERINI ESKININ 1/3 ORANINA GEGIRIYORU
# new_height = int(height/3)      #AYNISINI HEIGHJ ICIN DE YUAPIYORUZ.
# #print(new_height, new_width)
# #small_image = img.resize((new_width, new_height))  #BOYLE YAPINCA RESMI 3 TE 1 ORANINDA KUCULTMUS OLUYORUZ ORANTILI OLARAK.11111  VE ATAMASINI YAPTIK. SIRNAKA ATADIK
#
# #small_image.save('./small_image.jpeg')
#
# #\\\\\\\\\\\\\\\\\SIMDI BURADA DA USTEKI YAPTIGMIZ KUCULTME ISLEMINI HAZIR KOMUTLA YAPICAZ BURDA DA MESELA BIR BOYUT VERDIK 300 E 300 BIR KENER MAX 300 OLACAK SEKILDE DIGER KENARI ORANTILI KLUCULTUYOR.////
#
# #MAX_SIZE = (300, 300)      #OLACAK EN BUYUK BOYUTUNU BURAYA GIRIYORUZ.
# #img2 = img.copy()       #BURADA IMG NIN BIR KOPYASINI IMG 2 YAPIYORUZ.!!!
# #img2.thumbnail(MAX_SIZE)    #BIR KENARI MAX 300 OLACAK SEKILDE KENDISI DIGER KENARIN BOYUTUNU MAX BOYUTA GORE AYARLIYOR..!!!!!
# #img2.show()
# #print(img2.size)       #GORUYORUZ BI KENARI MAX 300 OLACAK SEKILDE AYARLAMIS
#
#
#
# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ BURADA SIMDI BUTUN BIR DATA SETININ NASIL BOYUT KUCULTMESI YAPIALCAGINI OGRENIYORUZ ////////////////////////////////////////
#
# folder_path = './images'
# paths = os.listdir(folder_path)
#
# #print(*paths, sep='\n')     #BUNU BEN YAPIYORUM BOYLE YAPARAK CIOKTILARA YAN YANA DEGIL ALT ALTA GOPREBILIYORUZ.
#
# for path in paths:
#     if path.endswith('.jpeg'):
#         img = Image.open(os.path.join(folder_path, path))       #folder_path KLASORUN ISMI path DOSYANIN ISMI.  BRUADA KLASORE GIDIP ORDAN RESME GIDIYORUZ. ARTIK DOSYAYI OKUYABILIRIZ..
#         thumb = img.copy()      #YINE COPY YAPTIK CUNKU FOTONUN ORJINALINE DOKUNMAK ISTEMIYORUZ.!!!!!!!!
#         thumb.thumbnail((300, 300))                #SDIMDI FOYOU BICIMLENDIRIYORUZ.!!!!
#         thumb = thumb.transpose(Image.FLIP_LEFT_RIGHT)       #BURADA DA FOTOLARI TERS CEVIRIYORTUZ TRANSPOZUNU ALIYORUZ.!!!!!!!
#         thumb.save(f'./process_images/{path}')     #YENI DOSYAYA YENI FOTLARI AKRATIYORUZ. KAYDEDIYORUZ.
#
# #//////////////////////////////////     KENDIME NOT          ?!@#!@#!@#              YOLO V5 KULLANARAK OBJECT DETECKTED YAP            .!!@!!!!!!@##!@#!@#!@# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#
#










































