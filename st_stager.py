
import base64,zlib


guid = ""
psk  = ""
urls = ""
b64  = ""



def stager(b64):
    compressed   =  base64.b64decode(b64)
    decompressed = zlib.decompress(compressed,-15)
    return decompressed


#open("stage2.exe","wb").write(stager(b64))
	
    
