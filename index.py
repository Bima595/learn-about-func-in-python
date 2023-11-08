# x = 37  # Ganti nilai x dengan input yang ingin Anda periksa

# if x < 1:
#     print("Nilai yang Anda masukkan", x, "bukan bilangan valid. Nilai inputan harus >= 1.")
# else:
#     for i in range(1, x + 1):
#         if i % 2 == 0:
#             print("Nilai", i, "adalah bilangan genap.")
#         else:
#             print("Nilai", i, "adalah bilangan ganjil.")



def dua (numbers):
    new = []
    for n in numbers:
        new.append(n*2)
    return (new)

number = [1,2,3,4,5]
print (dua(number))