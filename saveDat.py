import struct
data = open("mha_configuration-2023-04-04T140644.dat","rb").read()
le = int(len(data)/16)

left = [0 for i in range(le)]
right = [0 for i in range(le)]

for i in range(le):
    (left[i], right[i]) = struct.unpack_from("@dd",data,i*16)

f = open('2023-04-04T140644.txt','w')
for i in range(le):
    f.write(str(left[i]))
    f.write("    ")
    f.write(str(right[i]))
    f.write("\n")
    
f.close()
   
   
