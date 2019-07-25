tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

print("\n"*15)
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)
kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]
x_durumu = []
o_durumu = []

sıra = 2
counter=0
while True:
    if sıra % 2 == 0:
        sign = "X".center(3)
    else:
        sign = "O".center(3)
    print()
    print("İŞARET: {}\n".format(sign))
    
    x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
    y = input("soldan sağa [1, 2, 3]: ".ljust(30))
    if x!= "1" and x!="2" and x!="3":
        print("Lutfen giris degerlerinizi kontrol ediniz.")
        continue
    if y!= "1" and y!="2" and y!="3":
        print("Lutfen giris degerlerinizi kontrol ediniz.")
        continue
    
    x = int(x)-1
    y = int(y)-1
    print("\n"*15)
    
    if tahta[x][y] == "___":
       tahta[x][y] = sign
       if sign == "X".center(3):
            x_durumu += [[x, y]]
       elif sign == "O".center(3):
            o_durumu += [[x, y]]
       sıra += 1
    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")
        continue
if sira%2==1:
    if konum==[]:
        print("draw")
    elif tahta[0][0]==" O " and tahta[0][1]==" O " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])
    elif tahta[1][0]==" O " and tahta[1][1]==" O " and tahta[1][2]=="---":
                tahta[1][2]=" O "
                bilgisayar_durum+=[[1,2]]
                konum.remove([1,2])
    elif tahta[2][0]==" O " and tahta[2][1]==" O " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
    elif tahta[0][0]==" O " and tahta[1][0]==" O " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])
    elif tahta[0][1]==" O " and tahta[1][1]==" O " and tahta[2][1]=="---":
                tahta[2][1]=" O "
                bilgisayar_durum+=[[2,1]]
                konum.remove([2,1])
    elif tahta[0][2]==" O " and tahta[1][2]==" O " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
     elif tahta[0][0]==" O " and tahta[1][1]==" O " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
     elif tahta[2][0]==" O " and tahta[1][1]==" O " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])               
    elif tahta[0][0]==" X " and tahta[0][1]==" X " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])
    elif tahta[1][0]==" X " and tahta[1][1]==" X " and tahta[1][2]=="---":
                tahta[1][2]=" O "
                bilgisayar_durum+=[[1,2]]
                konum.remove([1,2])
    elif tahta[2][0]==" X " and tahta[2][1]==" X " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
    elif tahta[0][0]==" X " and tahta[1][0]==" X " and tahta[2][0]=="---":
                tahta[2][0]=" O "
                bilgisayar_durum+=[[2,0]]
                konum.remove([2,0])
     elif tahta[0][1]==" X " and tahta[1][1]==" X " and tahta[2][1]=="---":
                tahta[2][1]=" O "
                bilgisayar_durum+=[[2,1]]
                konum.remove([2,1])
    elif tahta[0][2]==" X " and tahta[1][2]==" X " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
    elif tahta[0][0]==" X " and tahta[1][1]==" X " and tahta[2][2]=="---":
                tahta[2][2]=" O "
                bilgisayar_durum+=[[2,2]]
                konum.remove([2,2])
    elif tahta[2][0]==" X " and tahta[1][1]==" X " and tahta[0][2]=="---":
                tahta[0][2]=" O "
                bilgisayar_durum+=[[0,2]]
                konum.remove([0,2])               
    else:
        secim=random.choice(konum)
        if tahta[secim[0]][secim[1]]=="---":
                tahta[secim[0]][secim[1]]=isaret
                bilgisayar_durum+=[[secim[0],secim[1]]]
                konum.remove(secim)
        else:
            continue



        
    sira+=1
    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)


    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        
    if len(o) == len(i):
        print("O KAZANDI!")
        quit()
    if len(x) == len(i):
        print("X KAZANDI!")
        quit()



