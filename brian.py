check_list= []

def check(original, edited):
   if (original == edited):
      check_list.append("Palindrom")
   else:
      check_list.append("Bukan Palindrom")

def reversed(word):
   ori = word
   rev = word[::-1]
   check(ori, rev)

n = int(input("Jumlah huruf yang ingin diperiksa: "))
for i in range(n):
   kata = input("Tuliskan sebuah kata: ")
   reversed(kata)

print("")
print(*check_list, sep='\n')