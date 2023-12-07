import numpy

def garis():
	print("+"*50)

#Fungsi untuk memasukkan nilai input dari user menggunakan loop ke dalam array 2 dimensi
def inputNilai(a, b, c, d):
	for i in range(b):
		for j in range(c):
			if j < c-1:
				print("{} : ".format(d[j]), end="")
			else:
				print("Hasil {} : ".format(i+1), end="")
			a[i][j] = float(input())
			if j == c-1:
				garis()
				
#Fungsi yang digunakan untuk mencetak nilai input dari user di dalam array 
def outputSPL(a, b, c, d):
	for i in range(b):
		cek = False
		for j in range(c):
			if j < c-1:
				if a[i][j] != 0:
					if cek == True:
						if a[i][j] > 0:
							print(" +", end="")
						else:
							print(" ", end="")
					print(" {}{}".format(a[i][j], d[j]), end="")
					cek = True
			else:
				if cek == True:
					print(" =", a[i][j])

def outputMatriks(a, b, c):
	for i in range(b):
		print(" [", end="")
		for j in range(c):
			if j == c-1:
				print(" |", end="")
			print(" {0:6.2f}".format(a[i][j]), end="")
		print(" ]")

#Fungsi Sort digunakan untuk menukarkan baris 
#Fungsi ini bekerja dengan cara membandingkan nilai di baris yang berbeda
def sort(a, b, c, i, z):
	for j in range(i+1, b):
		if a[j][z] != 0:
			for k in range(c):
				a[i][k],a[j][k] = a[j][k],a[i][k]
			garis()
			print("R{} =><= R{}".format(i+1, j+1))
			outputMatriks(a, b, c)
			
			break

def gauss(a, b, c, i = 0, z = 0):
	if i < b:
		if z < c-1:
			if a[i][z] == 0:
				sort(a, b, c, i, z)
			if a[i][z] != 0:
				if a[i][z] != 1:
					temp = a[i][z]
					for j in range(z,c):
						a[i][j] /= temp
			
					garis()
					print("R{} / {}".format(i+1, temp))
					outputMatriks(a, b, c)
					
			
				for j in range(i+1,b):
					if a[j][z] != 0:
					
						temp = a[j][z] / a[i][z]
						for k in range(z,c):
							a[j][k] = a[j][k] - (temp * a[i][k])
              
						garis()
						print("R{}".format(j+1),end="")
						if temp > 0:
							print(" - ",end="")
						else:
							print(" + ",end="")
							temp *= -1
						print("{}R{}".format(temp, i+1))
						outputMatriks(a, b, c)
						
				
				i += 1
				gauss(a, b, c, i, z)
			else:
				z += 1
				gauss(a, b, c, i, z)

def jordan(a, b, c, d):
	
	unik = False
	for i in range(b):
		cekIsi = True
		cekHasil = False
		for j in range(c):
			if j < c-1:
				if a[i][j] == 0 and cekIsi == True: 
					cekIsi = True
				else:
					cekIsi = False
			else:
				if a[i][j] == 0:
					cekHasil = True
				else:
					cekHasil = False
		
		if cekIsi == True and cekHasil == False:
			garis()
			print("="+"Tidak Ada Solusi".center(48)+"=")
			break
		
		elif cekIsi == True and cekHasil == True:
			solusi = "Banyak Solusi"
			break
	
	else:
		solusi = "Solusi Unik"
		unik = True

	if unik == True or (cekIsi == True and cekHasil == True):
		
		for i in range(b-1, -1, -1):
			for j in range(c-1):
			
				if a[i][j] != 0:
					for k in range(i-1, -1, -1):
						
						if a[k][j] != 0:
							temp = a[k][j] / a[i][j]
							for l in range(j, c):
								a[k][l] -= (temp * a[i][l])
						
							garis()
							print("R{}".format(k+1),end="")
							if temp > 0:
								print(" - ",end="")
							else:
								print(" + ",end="")
								temp *= -1
							print("{}R{}".format(temp, i+1))
							outputMatriks(a, b, c)
							
					break
		garis()
		print("="+solusi.center(48)+"=")
		garis()
	
		for i in range(b):
			cek = False
			for j in range(c):
				if a[i][j] != 0 and j < c-1:
					if cek == True:
						print(" +", end="")
					print(" {}{}".format(a[i][j], d[j]), end="")
					cek = True
			if cek == True:
				print(" = {0:6.2f}".format(a[i][j]))
	garis()

def infoMenu():
	garis()
	print("|"+"Tubes Matriks dan Ruang Vektor".center(48)+"|")
	print("|"+(48*"-").center(48)+"|")
	print("|"+"Anggota Kelompok".center(48)+"|")
	print("|"+"Nama :Robby Bangsawan ".ljust(48)+"|")
	print("|"+"NIM  :120140190 ".ljust(48)+"|")
	print("|"+"Nama :Irwan Ferdi Kuswendi  ".ljust(48)+"|")
	print("|"+"NIM  :121140008 ".ljust(48)+"|")
	print("|"+"Nama :Farhan Kurniawan".ljust(48)+"|")
	print("|"+"NIM  :121140021 ".ljust(48)+"|") 
	print("|"+"Nama :Hafiza Eka Ramadhini".ljust(48)+"|")
	print("|"+"NIM  :121140048".ljust(48)+"|")
	print("|"+"Nama :Tiara Putri Elisa".ljust(48)+"|")
	print("|"+"NIM  :121140049".ljust(48)+"|")
	print("|"+(48*"-").center(48)+"|")


pilihan = "0"
while pilihan != "2":
	
	infoMenu()
	print("|"+"1. Menyelesaikan SPL atau Matriks".ljust(48)+"|")
	
	print("|"+"2. Berhenti".ljust(48)+"|")
	garis()

	pilihan = input("Masukkan Pilihan : ")
	garis()
	
	if pilihan == "1":
			baris = int(input("Baris : "))
			kolom = int(input("Kolom : "))
			garis()
			kolom += 1
			namaVariabel = ["x{}".format(i+1) for i in range(kolom-1)]
			matriks = numpy.zeros((baris, kolom))
			inputNilai(matriks, baris, kolom, namaVariabel)

			print("="+"Sistem Persamaan Variabel".center(48)+"=")
			garis()
			outputSPL(matriks, baris, kolom, namaVariabel)
			garis()
			print("="+"Matriks Augmented".center(48)+"=")
			garis()
			outputMatriks(matriks, baris, kolom)
			
			gauss(matriks, baris, kolom)
			jordan(matriks, baris, kolom, namaVariabel)
			
			
		
	elif pilihan != "2":
		print("="+"- Masukan Tidak Sesuai -".center(48)+"=")


print("=== Program Terhenti ===")