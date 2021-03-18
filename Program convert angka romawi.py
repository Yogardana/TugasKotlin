angka = int(input("Masukan angka 1-10: "))
variabel_i = "I"
variabel_v = "V"
variabel_x = "X"
lebih5 = angka % 5

if (0 < angka < 4):
  print(variabel_i * angka)

elif (angka == 4):
  print(variabel_i + variabel_v)

elif 4 < angka < 9:
  print(variabel_v + variabel_i * lebih5)

elif angka == 9:
  print(variabel_i + variabel_x)

elif angka == 10:
  print(variabel_x)
