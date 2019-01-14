import random as rand

#oyunbitimi Puan sayımı
#ihaleli batak , ihalesiz koz maca sayılı ,  eşli batak
#bot yazılcak

tur = ["maça", "kupa","sinek","karo"]
deste = ["AS","2" ,"3" , "4" , "5" ,"6" ,"7" , "8", "9", "10","VALE","KIZ" , "PAPAZ"];

destePuan = [30,2,3,4,5,6,7,8,9,10,15,20,25]

kagitPuanlar = [["AS",30],["2",2],
    ["3",3],
    ["4",4],
    ["5",5],
    ["6",6],
    ["7",7],
    ["8",8],
    ["9",9],
    ["10",10],
    ["VALE",15] ,
    ["KIZ",20] ,
    ["PAPAZ",25]]



def desteYarat():
    rastgeleDeste = [];
    for i in range(0,13):
        for x in range(0,4):
            rastgeleDeste.append(tur[x] + " " + deste[i])
    return(rastgeleDeste)

def kagitDagit(oyunDeste):
    rand.shuffle(oyunDeste)
    oyuncuEl = []
    for o in range(0,4):
        oyuncuKagit = []
        for k in range(0,13):
            oyuncuKagit.append(oyunDeste[0])
            oyunDeste.remove(oyunDeste[0])
        oyuncuEl.insert(o,oyuncuKagit)
    return(oyuncuEl)


def botOyna(yer,oyuncuDeste):
    print(1)
    
def eldeBuyukAra(gelenKagitPuan, tur , elDeste):
    global deste
    global destePuan
    kontrol = False
    for i in range(0,len(elDeste)):
        kontrolKagit = elDeste[i].split(' ')
        kagitSira = deste.index(str(kontrolKagit[1]))
        if(kontrolKagit[0] == tur and destePuan[kagitSira] > gelenKagitPuan):
            kontrol = True
            break
    return(kontrol)

def eldeTurAra(tur,deste):
    kontrol = False
    for i in range(0,len(deste)):
        kontrolKagit = deste[i].split(' ')
        if(kontrolKagit[0] == tur):
            kontrol = True
            break
    return(kontrol)

def yerEnBuyugu(yer,arananTur):
    arananYerBuyuk = []
    for i in range(0,len(yer)):
        if(yer[i][0] == arananTur):
            arananYerBuyuk.append(yer[i])
    
    arananYerBuyuk.sort(key=lambda x: x[3])
    return(arananYerBuyuk[-1][3])

def yerEnBuyuguArr(yer,arananTur):
    arananYerBuyuk = []
    for i in range(0,len(yer)):
        if(yer[i][0] == arananTur):
            arananYerBuyuk.append(yer[i])
    
    arananYerBuyuk.sort(key=lambda x: x[3])
    return(arananYerBuyuk[-1])

def yerBaslangicKagit(yer):
    return(yer[0][0]);

def kozCakildimi(yer,koz):
    kontrol = False
    for i in range(0,len(yer)):
        if(yer[i][0] == koz):
            kontrol = True
            break
        else:
            continue
    return(kontrol)

def yerKimeKaldi(yer,yerilk):
    global koz
    cakilma = kozCakildimi(yer,koz)
    if(cakilma == True):
        print("ÇAKILMA VAR",koz)
        enbuyukKagit = yerEnBuyuguArr(yer,koz)
        buyukOynayan = enbuyukKagit[2]
    else:
        enbuyukKagit = yerEnBuyuguArr(yer,yerilk)
        buyukOynayan = enbuyukKagit[2]
    return([enbuyukKagit,buyukOynayan])

destem = desteYarat()

oyuncuEller = kagitDagit(destem)
kopye = oyuncuEller[0] + oyuncuEller[1] +oyuncuEller[2] + oyuncuEller[3]
oyuncuToplama = {}
sira = 0;
yer = []
koz = "maça"
print("Merhaba Oyuncu")
oyuncu = 0
while(sira <= 52):
    if(oyuncu > 3):
        oyuncu = 0

    print('\n')
    print("##############################################")
    print('#yer önce : ', yer)
    oyuncuEller[oyuncu].sort()
    print("Merhaba Oyuncu " + str(oyuncu + 1) + " kartlarınız : " ,oyuncuEller[oyuncu] )
    kagit = int(input("Kagit seç :"))
    print("##############################################")
    
    atilanKagit = (oyuncuEller[oyuncu][kagit-1]).split(' ')
    atilanKagitSira = deste.index(atilanKagit[1])
    atilanKagitPuan = destePuan[atilanKagitSira]
    if(len(yer) > 0):
        kagitYerSira = deste.index(atilanKagit[1])
        kagitYerPuan = destePuan[kagitYerSira]
        atilan = [atilanKagit[0], atilanKagit[1],oyuncu,kagitYerPuan]
        yerilkKagitTuru = yerBaslangicKagit(yer);
        print('#yer önce : ', yer)
        print("Yere atılmaya çalışan : " , atilanKagit)

        if(yerilkKagitTuru == koz):
            print("--> YERE ATILAN İLK KAGIT KOZ")
            kozVarmi = eldeTurAra(koz,oyuncuEller[oyuncu])
            if(kozVarmi == True):##kozvarsa
                print("--> YERE ATILAN İLK KAGIT KOZ VE ELİNDE KOZVAR")
                buyukVarmi = eldeBuyukAra(yerEnBuyugu(yer , koz) , koz , oyuncuEller[oyuncu])#c
                if(buyukVarmi == True):
                    print("--> YERE ATILAN İLK KAGIT KOZ VE ELİNDE KOZ VE BÜYÜK VAR")
                    if(atilanKagit[0] != koz or atilanKagit[1] < yer[-1][1]):
                        print("HATAAAAAAAAAAAAAAAAA")
                        continue
                else:
                    if(atilanKagit[0] != koz):
                        print("HATAAAAAAAAAAAAAAAAA")
                        continue
        else:
            kozCakilmaDurumu = kozCakildimi(yer,koz)
            if(kozCakilmaDurumu == True):
                elindeYerKagidiVarmi = eldeTurAra(yerilkKagitTuru ,oyuncuEller[oyuncu])
                if(elindeYerKagidiVarmi == True):
                    if(atilanKagit[0] != yerilkKagitTuru):
                        print("--> ELİNDE YER KAGIDI VAR ATSANA DANGOZ baska kagıt CAKAMASSIN")
                        print("HATAAAAAAAAAAAAAAAAA")
                        continue
                else:
                    kozVarmi = eldeTurAra(koz,oyuncuEller[oyuncu])
                    if(kozVarmi == True):##kozvarsa
                        print("--> YERE çakılan  KAGIT KOZ VE ELİNDE KOZVAR")
                        buyukVarmi = eldeBuyukAra(yerEnBuyugu(yer , koz) , koz , oyuncuEller[oyuncu])#c
                        if(buyukVarmi == True):
                            print("--> YERE çakılan  KAGIT koz VE ELİNDE KOZ VE BÜYÜK VAR")
                            if(atilanKagit[0] != koz or atilanKagit[1] < yer[-1][1]):
                                print("HATAAAAAAAAAAAAAAAAA")
                                continue
                        
                        else:
                            if(atilanKagit[0] != koz):
                                print("HATAAAAAAAAAAAAAAAAA")
                                continue
            else:
                print("--> OYUN NORMAL KOZ CAKILMAMIS")
                elindeYerKagidiVarmi = eldeTurAra(yerilkKagitTuru ,oyuncuEller[oyuncu])
                if(elindeYerKagidiVarmi == True):
                    print("--> ELİNDE YER KAGIDI MEVCUT")
                    buyukVarmi = eldeBuyukAra(yerEnBuyugu(yer,yerilkKagitTuru) , yerilkKagitTuru , oyuncuEller[oyuncu]) ##b
                    if(buyukVarmi == True):
                        print("--> ELİNDE YER KAGIDInın buyugde MEVCUT")
                        if(atilanKagit[0] != yerilkKagitTuru or atilanKagitPuan < yerEnBuyugu(yer,yerilkKagitTuru)):
                            print("HATAAAAAAAAAAAAAAAAA")
                            continue
                    else:
                        print("--> ELİNDE YER KAGIDI buyugu yok ama MEVCUT")
                        if(atilanKagit[0] != yerilkKagitTuru):
                            print("HATAAAAAAAAAAAAAAAAA")
                            continue
                else:
                    kozVarmi = eldeTurAra(koz,oyuncuEller[oyuncu])
                    if(kozVarmi == True):
                        print("--> ELİNDE YER KAGIDI  yok ama koz var koz çak")
                        if(atilanKagit[0] != koz):
                            print("HATAAAAAAAAAAAAAAAAA")
                            continue
    oyuncuEller[oyuncu].pop(kagit-1)
    oyuncu = oyuncu + 1
    sira = sira + 1

    kagitYerSira = deste.index(atilanKagit[1])
    kagitYerPuan = destePuan[kagitYerSira]
    atilan = [atilanKagit[0], atilanKagit[1],oyuncu-1,kagitYerPuan]
    yer.append(atilan)

    print("##############################################")
    print('#YER : ', yer)
    print( '#OYANAYAk OYUNCU : ', oyuncu)
    print( '#oyun sırası : ', sira)
    print("##############################################")
    if(sira % 4 == 0):
        yerKagitBilgi = yerKimeKaldi(yer,yerilkKagitTuru)
        oyuncustr = 'oyuncu'+str(int(yerKagitBilgi[1]))
        oyuncuToplama[oyuncustr] = yer
        print("##############################################")
        print("Eli Alan Oyuncu " , str(yerKagitBilgi[1] + 1) , "Eli Alan Kağıt " , yerKagitBilgi[0][0], yerKagitBilgi[0][1])
        print("##############################################")
        yer = []
        oyuncu = yerKagitBilgi[1]
        print("BAŞLAYACAK OYUNCU",str(yerKagitBilgi[1] + 1) )
        
