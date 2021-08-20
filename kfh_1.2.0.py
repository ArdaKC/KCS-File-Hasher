import hashlib
print("KCS File Hasher 1.2.0-^")
print("Which language? / Hangi dil? \n 1-Türkçe\n 2-English")
dil = int(input("Select language / Dil seçin:"))
if dil == 1:
 hoh = input("Konum girin:")
 dh = open(hoh, "rb")
 hooh = dh.read()
 print(" 1-SHA1 \n 2-SHA256 \n 3-SHA384 \n 4-SHA512 \n 5-MD5 \n 6-SHA224 \n 7-RIPEmd160")
 ahoh = input("Hash seçin:")
 if ahoh == "1":
   sha1 = hashlib.sha1(hooh).hexdigest()
   print("Dosyanin SHA1 Hash değeri = " + sha1)
 elif ahoh == "2":
   sha2 = hashlib.sha256(hooh).hexdigest()
   print("Dosyanin SHA256 Hash değeri = " + sha2)
 elif ahoh == "3":
   sha3 = hashlib.sha384(hooh).hexdigest()
   print("Dosyanin SHA384 Hash değeri = " + sha3)
 elif ahoh == "4":
   sha5 = hashlib.sha512(hooh).hexdigest()
   print("Dosyanin SHA512 Hash değeri = " + sha5)
 elif ahoh == "5":
   md5 = hashlib.md5(hooh).hexdigest()
   print("Dosyanin MD5 Hash değeri = " + md5)
 elif ahoh == "6":
   sha224 = hashlib.sha224(hooh).hexdigest()
   print("Dosyanin SHA224 Hash değeri = " + sha224)
 elif ahoh == "7":
    ripemd160 = hashlib.new("ripemd160")
    ripemd160.update(hooh)
    print("Dosyanin RIPEmd160 Hash değeri = " + ripemd160.hexdigest())
 else:
   sha2 = hashlib.sha256(hooh).hexdigest()
   print("Dosyanin SHA256 Hash değeri = " + sha2)

elif dil == 2:
 hoh = input("Specify the location:")
 dh = open(hoh, "rb")
 hooh = dh.read()
 print(" 1-SHA1 \n 2-SHA256 \n 3-SHA384 \n 4-SHA512 \n 5-MD5 \n 6-SHA224 \n 7-RIPEmd160")
 ahoh = input("Select Hash:")
 if ahoh == "1":
   sha1 = hashlib.sha1(hooh).hexdigest()
   print("File SHA1 Hash value = " + sha1)
 elif ahoh == "2":
   sha2 = hashlib.sha256(hooh).hexdigest()
   print("File SHA256 Hash value = " + sha2)
 elif ahoh == "3":
   sha3 = hashlib.sha384(hooh).hexdigest()
   print("File SHA384 Hash value = " + sha3)
 elif ahoh == "4":
   sha5 = hashlib.sha512(hooh).hexdigest()
   print("File SHA512 Hash value = " + sha5)
 elif ahoh == "5":
   md5 = hashlib.md5(hooh).hexdigest()
   print("File MD5 Hash value = " + md5)
 elif ahoh == "6":
   sha224 = hashlib.sha224(hooh).hexdigest()
   print("File SHA224 Hash value = " + sha224)
 elif ahoh == "7":
    ripemd160 = hashlib.new("ripemd160")
    ripemd160.update(hooh)
    print("File RIPEmd160 Hash value = " + ripemd160.hexdigest())
 else:
   sha2 = hashlib.sha256(hooh).hexdigest()
   print("File SHA256 Hash value = " + sha2)