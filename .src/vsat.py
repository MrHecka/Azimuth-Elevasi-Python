import math
import os


# CLEAR CONSOLE TERLEBIH DAHULU!

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

###########

# INPUT DATA

print("KALKULATOR AZIMUTH & ELEVASI CREATED BY MRHECKA!")
lso = float(input("Masukkan long sat other: ").replace(',','.'))
lsb = float(input("Masukkan long sb: ").replace(',','.'))
lst = float(input("Masukkan lat sb: ").replace(',','.'))


############

# PERHITUNGAN AZIMUTH

az1 = math.tan(math.radians(lsb-lso)*-1)
az2 = math.sin(math.radians(lst))
az3 = az1/az2
hasilaz = math.degrees(math.atan(az3))

# PERHITUNGAN AZIMUTH


# _______________________


# PERHITUNGAN ELEVASI

el1 = lso-lsb
el2 = math.cos(math.radians(el1))
el3 = math.cos(math.radians(lst))
el4 = el3*el2-0.151
el5 = el4*-1
el6 = 1-(el3*el2)**2
el66 = math.sqrt(abs(el6))
el7 = el5/el66
el8 = el7*-1
hasilel = math.degrees(math.atan(el8))

# PERHITUNGAN ELEVASI



#####################

# JALANKAN (OUTPUT DATA)

print('')
print('HASIL : ')
print('')
print('Azimuth: ', hasilaz)
print('')
print('Elevasi: ', hasilel)
print('')

# CREATED BY MRHECKA


# CMD (OUTPUT DATA)

# os.system('')
# os.system('HASIL : ')
# os.system('')
# os.system('Azimuth: ', hasilaz)
# os.system('')
# os.system('Elevasi: ', hasilel)
# os.system('')

####################




