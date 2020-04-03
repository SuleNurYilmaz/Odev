# Histogram ve histograma bağlı frekans eksik. Dosya okumada değişiklik yapılacak.
import random
#DOSYA OKUMA
def dosyaOkuma(i:int):
    text = open("{}.txt".format(i), "r")
    string = text.read()
    text.close()
    liste = string.split(" ")
    for j in liste:
        if "\n" in j:
            liste2 = j.split("\n")
            index = liste.index(j)
            liste.remove(j)
            a = 0
            for i in range(0, len(liste2)):
                if liste2[i] == "":
                    continue
                else:
                    liste.insert(index + a, liste2[i])
                    a += 1
    return liste
###################################################
def dic_birles():
    all_dict=dict()
    for i in range(1,6):
        all_dict.update(dict_olustur(i))
    return all_dict

####################################################
#İKİLİ-ÜÇLÜ-DÖRTLÜ-BEŞLİ LİSTELER
def listeIkili(liste:list):
    list2 = list()
    for i in range(0, len(liste) - 1):
        list2.append(liste[i] + " " + liste[i + 1])
    return list2
def listeUclu(liste:list):
    list3=list()
    for i in range(0,len(liste)-2):
        list3.append(liste[i]+" "+liste[i+1]+" "+liste[i+2])
    return list3
def listeDortlu(liste:list):
    list4=list()
    for i in range(0,len(liste)-3):
        list4.append(liste[i]+" "+liste[i+1]+" "+liste[i+2]+" "+liste[i+3])
    return list4
def listeBesli(liste:list):
    list5 = list()
    for i in range(0, len(liste) - 4):
        list5.append(liste[i] + " " + liste[i + 1] + " " + liste[i + 2] + " " + liste[i + 3]+" "+liste[i+4])
    return list5
#Liste
######################################################################################
def dict_olustur(sayi:int):
    if sayi == 1:
        dic = dict()
        main_dict=dict()
        for i in range(1,11):
            liste=dosyaOkuma(i)
            for i in range(0, len(liste)-1):
                if liste[i] not in dic:
                    dic1 = {liste[i]: {liste[i+1]: 1}}
                    dic.update(dic1)
                else:
                    if liste[i + 1] in dic[liste[i]]:
                        dic[liste[i]][liste[i + 1]] += 1
                    else:
                        di = {liste[i + 1]: 1}
                        dic[liste[i]].update(di)
            main_dict.update(dic)
        return main_dict
    if sayi==2:
        dic = dict()
        main_dict=dict()
        for i in range(1,11):
            liste=dosyaOkuma(i)
            lis=listeIkili(liste)
            for i in range(0, len(liste) - 2):
                if lis[i] not in dic:
                    dic1 = {lis[i]: {liste[i + 2]: 1}}
                    dic.update(dic1)
                else:
                    if liste[i + 2] in dic[lis[i]]:
                        dic[lis[i]][liste[i + 2]] += 1
                    else:
                        di = {liste[i + 2]: 1}
                        dic[lis[i]].update(di)
            main_dict.update(dic)
        return main_dict
    if sayi == 3:
        dic = dict()
        main_dict=dict()
        for i in range(1,11):
            liste=dosyaOkuma(i)
            lis = listeUclu(liste)
            for i in range(0, len(liste) - 3):
                if lis[i] not in dic:
                    dic1 = {lis[i]: {liste[i + 3]: 1}}
                    dic.update(dic1)
                else:
                    if liste[i + 2] in dic[lis[i]]:
                        dic[lis[i]][liste[i + 3]] += 1
                    else:
                        di = {liste[i + 3]: 1}
                        dic[lis[i]].update(di)
            main_dict.update(dic)
        return main_dict
    if sayi == 4:
        dic = dict()
        main_dict=dict()
        for i in range(1,11):
            liste=dosyaOkuma(i)
            lis = listeDortlu(liste)
            for i in range(0, len(liste) - 4):
                if lis[i] not in dic:
                    dic1 = {lis[i]: {liste[i + 4]: 1}}
                    dic.update(dic1)
                else:
                    if liste[i + 4] in dic[lis[i]]:
                        dic[lis[i]][liste[i + 4]] += 1
                    else:
                        di = {liste[i + 4]: 1}
                        dic[lis[i]].update(di)
            main_dict.update(dic)
        return main_dict
    if sayi == 5:
        dic = dict()
        main_dict=dict()
        for i in range(1,11):
            liste=dosyaOkuma(i)
            lis = listeBesli(liste)
            for i in range(0, len(liste) - 5):
                if lis[i] not in dic:
                    dic1 = {lis[i]: {liste[i + 5]: 1}}
                    dic.update(dic1)
                else:
                    if liste[i + 5] in dic[lis[i]]:
                        dic[lis[i]][liste[i + 5]] += 1
                    else:
                        di = {liste[i + 5]: 1}
                        dic[lis[i]].update(di)
            main_dict.update(dic)
        return main_dict
#MainDict
##################################################################
def karsilastir(main_dict:dict,kelime:str):
    max=0
    lit = list()
    if kelime in main_dict:
        a = main_dict[kelime]
        for x in main_dict[kelime]:
            if max < a[x]:
                max = a[x]
                lit.clear()
                lit = [x]
            elif max == a[x]:
                lit.append(x)
        return lit[random.randint(0, len(lit) - 1)]
    else:
        return None
#str
def Oneri():#Her seferinde dict oluşturuyor ancak sadece verilen kelime sayısına ait dict
    b = open("input.txt", "r+")
    a = b.readlines()
    b.close()
    liste = []
    for i in a:
        if "\n" in i:
            i = i.replace("\n", "")
        liste.append(i)
    b = open("output.txt", "a")
    for i in liste:
        x=i.split(" ",5)
        if len(x)>5:
            b.writelines(i+"Hata: 5ten fazla kelime girmeyiniz")
        else:
            if len(x)==1:
                a=karsilastir(dict_olustur(len(x)),i)
                if a is None:
                    b.writelines(i + " - "+"Öneri yapılamadı."+"\n")
                else:
                    b.writelines(i+ " - " + a +"\n")
            elif len(x)==2:
                a=karsilastir(dict_olustur(len(x)),i)
                if a is None:
                    b.writelines(i + " - "+"Öneri yapılamadı."+"\n")
                else:
                    b.writelines(i+ " - " + a +"\n")
            elif len(x) == 3:
                a=karsilastir(dict_olustur(len(x)),i)

                if a is None:
                    b.writelines(i + " - "+"Öneri yapılamadı."+"\n")
                else:
                    b.writelines(i+ " - " + a +"\n")
            elif len(x) == 4:
                a=karsilastir(dict_olustur(len(x)),i)

                if a is None:
                    b.writelines(i + " - " + "Öneri yapılamadı."+"\n")
                else:
                    b.writelines(i+ " - " + a +"\n")
            else:
                a=karsilastir(dict_olustur(len(x)),i)
                if a is None:
                    b.writelines(i + " - "+"Öneri yapılamadı."+"\n")
                else:
                    b.writelines(i+ " - " + a +"\n")
    b.close()

def Oneri_2():#yeni output dosyası ve ana bir sözlük
    b = open("input.txt", "r+")
    a = b.readlines()
    b.close()
    liste = []
    dic= dic_birles()
    for i in a:
        if "\n" in i:
            i = i.replace("\n", "")
        liste.append(i)
    b = open("output.txt", "a")
    for i in liste:
        x=i.split(" ",5)
        if len(x)>5:
            b.writelines(i+"Hata: 5ten fazla kelime girmeyiniz")
        else:
            a=karsilastir(dic,i)
            if a is None:
                b.writelines(i + " - "+"Öneri yapılamadı."+"\n")
            else:
                b.writelines(i+ " - " + a +"\n")
    b.close()


def Oneri_3():
    b = open("input.txt", "r+")
    a = b.readlines()
    b.close()
    liste = []
    dic= dic_birles()
    for i in a:
        if "\n" in i:
            i = i.replace("\n", "")
        liste.append(i)
    b=open("input.txt","w") #Dosya temizlendi
    b.close()
    b = open("input.txt", "a")
    for i in liste:
        x=i.split(" ",5)
        if len(x)>5:
            b.writelines(i+"Hata: 5ten fazla kelime girmeyiniz")
        else:
            a=karsilastir(dic,i)
            if a is None:
                b.writelines(i + " - "+"Öneri yapılamadı."+"\n")
            else:
                b.writelines(i+ " - " + a +"\n")
    b.close()



