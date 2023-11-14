#\\\\\\\\\\\\\\\\\\\\\\\\ ELIMIZDEKI VERI SETINE GORE GECELERI VE KALANLARI AYIKLADIGIMIZ PROJE ///////////////////////


# with open("ornek_metin.txt", encoding="utf-8") as f:
#     with open("gecenler.txt", "w")as g:
#         with open("kalanlar.txt", "w") as k:
#             icerik = f.readlines()
#             m = 0
#             for satir in icerik:
#                 if m == 0:
#                     m +=1
#                     continue
#                 satir = satir.replace("\n", "")                   # replace metodu bir yaziyi digeriyle degistirmeye yariyor
#                 bosluk_sayisi = 0
#                 bosluk_indexleri = []
#                 index = 0
#                 for karakter in satir:
#                     if karakter == " ":
#                         bosluk_sayisi += 1
#                         bosluk_indexleri.append(index)
#                     index += 1
#                 ad_soyad = satir[:bosluk_indexleri[0]]
#                 soyad = ad_soyad.split("-")[-1]
#                 ad = ad_soyad[:ad_soyad.index(soyad) -1].replace("-", " ")
#                 notlar = satir.split(" ")[-1]
#                 notlar = notlar.split("/")
#                 birinci_vize = int(notlar[0])
#                 ikinci_vize = int(notlar[1])
#                 final = int(notlar[2])
#                 ortalama = birinci_vize * 0.3 + ikinci_vize * 0.3 + final * 0.4
#                 bolum = satir[bosluk_indexleri[0]+1:bosluk_indexleri[-1]]
#                 if ortalama >= 70 and final >= 70:
#                     g.write(ad)
#                     g.write(" " * (25 - len(ad)))
#                     g.write(soyad)
#                     g.write(" " * (25 - len(soyad)))
#                     g.write(bolum)
#                     g.write(" " * (25 - len(bolum)))
#                     g.write(str(round(ortalama,1)))
#                     g.write(" " * 21)
#                     g.write("Gecti")
#                     g.write("\n")
#
#                 else:
#                     k.write(ad)
#                     k.write(" " * (25 - len(ad)))
#                     k.write(soyad)
#                     k.write(" " * (25 - len(soyad)))
#                     k.write(bolum)
#                     k.write(" " * (25 - len(bolum)))
#                     k.write(str(round(ortalama, 1)))
#                     k.write(" " * 21)
#                     k.write("Kaldi")
#                     k.write("\n")
