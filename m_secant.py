def pangkat(e,y) :
    pkt = 1
    for i in range(y) :
        pkt = pkt * e
    return pkt

# Bagian ini Saja yang diubah
#######################################################################################
# ---------------------------Sesuaikan dengan Soal-------------------------------------
def soal(x) :
    # dengan Soal --> 3x^3 -x - 1 = 0
    jwb = (3 * pangkat(x,3)) - x - 1
    
    return jwb

# Untuk xi-1 / x0
x0 = -1
# Untuk xi / x1
x1 = 1
# Untuk Toleransi Error
error = 0.00843

# jika iterasi tidak diketahui, maka buat saja --> iterasi = 0
iterasi = 4


# ---------------------------Sesuaikan dengan Soal-------------------------------------
#######################################################################################

tempx = 0
tempy = 0
x2 = 0
j = 1

while True:
    y1 = soal(x1)
    y0 = soal(x0)
    
    x2 = x1 - ((y1 * (x1-x0)) / (y1 - y0))
    
    y2 = soal(x2)
    
    print("Iterasi ke -",j)
    print("X0    : ",x0)
    print("X1    : ",x1)
    print("X2    : ",x2)
    print("y0    : ",y0)
    print("y1    : ",y1)
    print("y2    : ",y2)
    print()
    
    if (iterasi == 0):
        if(y2 <= 0):
            pengganti_y2 = y2*-1
            if(pengganti_y2 < error):
                break
        elif(y2 > 0):
            if(y2 < error):
                break
    elif(iterasi <= j):
        break
    
    j = j+1
    
    tempy = y0
    y0 = y1
    y1 = y2
    
    tempx = x0
    x0 = x1
    x1 = x2
    

print("Hasil xi adalah :",x2)
print("Pada Iterasi ke-",j)

adul
