import hashlib, random, codecs, time, sys
from hashlib import sha256
import secp256k1 as ice
from time import sleep
from rich.console import Console
console = Console()
console.clear()

animation = ["❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  0%","☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  5%","☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 10%","☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 15%","☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 20%","☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 25%","☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 30%","☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 35%","☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 40%","☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 45%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 50%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 55%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️ 60%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️ 65%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️ 70%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️ 75%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️ 80%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️ 85%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️ 90%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️ 95%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️100%"]

for i in range(len(animation)):
    time.sleep(0.05)
    sys.stdout.write("\r" + "Merry Christmas:" + animation[i % len(animation)])
    sys.stdout.flush()
console.print("\n[yellow]💰-----------------💰 HUNT4BITCOIN RANGE DIVISION 100% 💰----------------------💰[/yellow]")
console.print("[yellow]   🤖🤖🤖       Made by Mizogg      🤖🤖🤖[/yellow]")
console.print("[yellow]    🤩 With iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  🤩 [/yellow]")
console.print("[yellow]💰-------💰 Divide the Chosen Range by 100% and Scan Sequentially 💰-----------💰[/yellow]")
console.print("[purple]         ⏳Starting search... Please Wait ⏳[/purple]")

print('Bitcoin Addresses Loading Please Wait: ')

filename ='puzzle.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read(1024*1024).split()
add = set(add)

print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
start = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
stop = 2**y
mag=int(input("Magnitude Jump Stride -> "))
print("Starting search... Please Wait min range: " + str(start))
print("Max range: " + str(stop))
print("==========================================================")
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))


base58_alphabet = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def b58encode_int(x, default_one=True):
    if not x and default_one:
        return base58_alphabet[0:1]
    base = len(base58_alphabet)
    string = b''
    while x:
        x, remainder = divmod(x, base)
        string = base58_alphabet[remainder:remainder+1] + string
    return string

def b58encode(x):
    old_len = len(x)
    x = x.lstrip(b'\0')
    new_len = len(x)
    acc = int.from_bytes(x, byteorder='big')
    result = b58encode_int(acc, default_one=False)
    return base58_alphabet[0:1] * (old_len - new_len) + result

def b58encode_check(x):
    digest = sha256(sha256(x).digest()).digest()
    return b58encode(x + digest[:4])
    
HEXSTART = "%064x" % start
HEXSTOP = "%064x" % stop
 
remainingtotal=stop-start
div= round(remainingtotal / 100)
finish = div + start
count = 0
total = 0

while start<finish:
    remainingtotal-=mag
    finish-=mag
    start+=mag
    div= round(remainingtotal / 100)
    count += 1
    total += 400
    ran= start
    seed = str(ran)
    HEX = "%064x" % ran
    private_key_hex_px = '80' + HEX
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr = ice.privatekey_to_address(0, True, int(seed)) #Compressed
    uaddr = ice.privatekey_to_address(0, False, int(seed))  #Uncompressed
    p2sh = ice.privatekey_to_address(1, True, int(seed)) #p2sh
    bech32 = ice.privatekey_to_address(2, True, int(seed))  #bech32

    percent2 = div * 2
    ran2= start+percent2
    HEX2 = "%064x" % ran2
    seed2 = str(ran2)
    private_key_hex_px = '80' + HEX2
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc2 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX2 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu2 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr2 = ice.privatekey_to_address(0, True, int(seed2)) #Compressed
    uaddr2 = ice.privatekey_to_address(0, False, int(seed2))  #Uncompressed
    p2sh2 = ice.privatekey_to_address(1, True, int(seed2)) #p2sh
    bech322 = ice.privatekey_to_address(2, True, int(seed2))  #bech32
    
    percent3 = div * 3
    ran3= start+percent3
    HEX3 = "%064x" % ran3
    seed3 = str(ran3)
    private_key_hex_px = '80' + HEX3
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc3 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX3 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu3 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr3 = ice.privatekey_to_address(0, True, int(seed3)) #Compressed
    uaddr3 = ice.privatekey_to_address(0, False, int(seed3))  #Uncompressed
    p2sh3 = ice.privatekey_to_address(1, True, int(seed3)) #p2sh
    bech323 = ice.privatekey_to_address(2, True, int(seed3))  #bech32
    
    percent4 = div * 4
    ran4= start+percent4
    HEX4 = "%064x" % ran4
    seed4 = str(ran4)
    private_key_hex_px = '80' + HEX4
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc4 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX4 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu4 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr4 = ice.privatekey_to_address(0, True, int(seed4)) #Compressed
    uaddr4 = ice.privatekey_to_address(0, False, int(seed4))  #Uncompressed
    p2sh4 = ice.privatekey_to_address(1, True, int(seed4)) #p2sh
    bech324 = ice.privatekey_to_address(2, True, int(seed4))  #bech32
    
    percent5 = div * 5
    ran5= start+percent5
    HEX5 = "%064x" % ran5
    seed5 = str(ran5)
    private_key_hex_px = '80' + HEX5
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc5 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX5 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu5 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr5 = ice.privatekey_to_address(0, True, int(seed5)) #Compressed
    uaddr5 = ice.privatekey_to_address(0, False, int(seed5))  #Uncompressed
    p2sh5 = ice.privatekey_to_address(1, True, int(seed5)) #p2sh
    bech325 = ice.privatekey_to_address(2, True, int(seed5))  #bech32
    
    percent6 = div * 6
    ran6= start+percent6
    HEX6 = "%064x" % ran6
    seed6 = str(ran6)
    private_key_hex_px = '80' + HEX6
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc6 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX6 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu6 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr6 = ice.privatekey_to_address(0, True, int(seed6)) #Compressed
    uaddr6 = ice.privatekey_to_address(0, False, int(seed6))  #Uncompressed
    p2sh6 = ice.privatekey_to_address(1, True, int(seed6)) #p2sh
    bech326 = ice.privatekey_to_address(2, True, int(seed6))  #bech32
    
    percent7 = div * 7
    ran7= start+percent7
    HEX7 = "%064x" % ran7
    seed7 = str(ran7)
    private_key_hex_px = '80' + HEX7
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc7 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX7 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu7 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr7 = ice.privatekey_to_address(0, True, int(seed7)) #Compressed
    uaddr7 = ice.privatekey_to_address(0, False, int(seed7))  #Uncompressed
    p2sh7 = ice.privatekey_to_address(1, True, int(seed7)) #p2sh
    bech327 = ice.privatekey_to_address(2, True, int(seed7))  #bech32
    
    percent8 = div * 8
    ran8= start+percent8
    HEX8 = "%064x" % ran8
    seed8 = str(ran8)
    private_key_hex_px = '80' + HEX8
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc8 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX8 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu8 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr8 = ice.privatekey_to_address(0, True, int(seed8)) #Compressed
    uaddr8 = ice.privatekey_to_address(0, False, int(seed8))  #Uncompressed
    p2sh8 = ice.privatekey_to_address(1, True, int(seed8)) #p2sh
    bech328 = ice.privatekey_to_address(2, True, int(seed8))  #bech32
    
    percent9 = div * 9
    ran9= start+percent9
    HEX9 = "%064x" % ran9
    seed9 = str(ran9)
    private_key_hex_px = '80' + HEX9
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc9 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX9 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu9 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr9 = ice.privatekey_to_address(0, True, int(seed9)) #Compressed
    uaddr9 = ice.privatekey_to_address(0, False, int(seed9))  #Uncompressed
    p2sh9 = ice.privatekey_to_address(1, True, int(seed9)) #p2sh
    bech329 = ice.privatekey_to_address(2, True, int(seed9))  #bech32
    
    percent10 = div * 10
    ran10= start+percent10
    HEX10 = "%064x" % ran10
    seed10 = str(ran10)
    private_key_hex_px = '80' + HEX10
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc10 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX10 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu10 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr10 = ice.privatekey_to_address(0, True, int(seed10)) #Compressed
    uaddr10 = ice.privatekey_to_address(0, False, int(seed10))  #Uncompressed
    p2sh10 = ice.privatekey_to_address(1, True, int(seed10)) #p2sh
    bech3210 = ice.privatekey_to_address(2, True, int(seed10))  #bech32
    
    percent11 = div * 11
    ran11= start+percent11
    HEX11 = "%064x" % ran11
    seed11 = str(ran11)
    private_key_hex_px = '80' + HEX11
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc11 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX11 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu11 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr11 = ice.privatekey_to_address(0, True, int(seed11)) #Compressed
    uaddr11 = ice.privatekey_to_address(0, False, int(seed11))  #Uncompressed
    p2sh11 = ice.privatekey_to_address(1, True, int(seed11)) #p2sh
    bech3211 = ice.privatekey_to_address(2, True, int(seed11))  #bech32
    
    percent12 = div * 12
    ran12= start+percent12
    HEX12 = "%064x" % ran12
    seed12 = str(ran12)
    private_key_hex_px = '80' + HEX12
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc12 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX12 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu12 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr12 = ice.privatekey_to_address(0, True, int(seed12)) #Compressed
    uaddr12 = ice.privatekey_to_address(0, False, int(seed12))  #Uncompressed
    p2sh12 = ice.privatekey_to_address(1, True, int(seed12)) #p2sh
    bech3212 = ice.privatekey_to_address(2, True, int(seed12))  #bech32
    
    percent13 = div * 13
    ran13= start+percent13
    HEX13 = "%064x" % ran13
    seed13 = str(ran13)
    private_key_hex_px = '80' + HEX13
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc13 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX13 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu13 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr13 = ice.privatekey_to_address(0, True, int(seed13)) #Compressed
    uaddr13 = ice.privatekey_to_address(0, False, int(seed13))  #Uncompressed
    p2sh13 = ice.privatekey_to_address(1, True, int(seed13)) #p2sh
    bech3213 = ice.privatekey_to_address(2, True, int(seed13))  #bech32
    
    percent14 = div * 14
    ran14= start+percent14
    HEX14 = "%064x" % ran14
    seed14 = str(ran14)
    private_key_hex_px = '80' + HEX14
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc14 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX14 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu14 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr14 = ice.privatekey_to_address(0, True, int(seed14)) #Compressed
    uaddr14 = ice.privatekey_to_address(0, False, int(seed14))  #Uncompressed
    p2sh14 = ice.privatekey_to_address(1, True, int(seed14)) #p2sh
    bech3214 = ice.privatekey_to_address(2, True, int(seed14))  #bech32
    
    percent15 = div * 15
    ran15= start+percent15
    HEX15 = "%064x" % ran15
    seed15 = str(ran15)
    private_key_hex_px = '80' + HEX15
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc15 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX15 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu15 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr15 = ice.privatekey_to_address(0, True, int(seed15)) #Compressed
    uaddr15 = ice.privatekey_to_address(0, False, int(seed15))  #Uncompressed
    p2sh15 = ice.privatekey_to_address(1, True, int(seed15)) #p2sh
    bech3215 = ice.privatekey_to_address(2, True, int(seed15))  #bech32
    
    percent16 = div * 16
    ran16= start+percent16
    HEX16 = "%064x" % ran16
    seed16 = str(ran16)
    private_key_hex_px = '80' + HEX16
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc16 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX16 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu16 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr16 = ice.privatekey_to_address(0, True, int(seed16)) #Compressed
    uaddr16 = ice.privatekey_to_address(0, False, int(seed16))  #Uncompressed
    p2sh16 = ice.privatekey_to_address(1, True, int(seed16)) #p2sh
    bech3216 = ice.privatekey_to_address(2, True, int(seed16))  #bech32
    
    percent17 = div * 17
    ran17= start+percent17
    HEX17 = "%064x" % ran17
    seed17 = str(ran17)
    private_key_hex_px = '80' + HEX17
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc17 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX17 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu17 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr17 = ice.privatekey_to_address(0, True, int(seed17)) #Compressed
    uaddr17 = ice.privatekey_to_address(0, False, int(seed17))  #Uncompressed
    p2sh17 = ice.privatekey_to_address(1, True, int(seed17)) #p2sh
    bech3217 = ice.privatekey_to_address(2, True, int(seed17))  #bech32
    
    percent18 = div * 18
    ran18= start+percent18
    HEX18 = "%064x" % ran18
    seed18 = str(ran18)
    private_key_hex_px = '80' + HEX18
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc18 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX18 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu18 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr18 = ice.privatekey_to_address(0, True, int(seed18)) #Compressed
    uaddr18 = ice.privatekey_to_address(0, False, int(seed18))  #Uncompressed
    p2sh18 = ice.privatekey_to_address(1, True, int(seed18)) #p2sh
    bech3218 = ice.privatekey_to_address(2, True, int(seed18))  #bech32
    
    percent19 = div * 19
    ran19= start+percent19
    HEX19 = "%064x" % ran19
    seed19 = str(ran19)
    private_key_hex_px = '80' + HEX19
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc19 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX19 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu19 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr19 = ice.privatekey_to_address(0, True, int(seed19)) #Compressed
    uaddr19 = ice.privatekey_to_address(0, False, int(seed19))  #Uncompressed
    p2sh19 = ice.privatekey_to_address(1, True, int(seed19)) #p2sh
    bech3219 = ice.privatekey_to_address(2, True, int(seed19))  #bech32
    
    percent20 = div * 20
    ran20= start+percent20
    HEX20 = "%064x" % ran20
    seed20 = str(ran20)
    private_key_hex_px = '80' + HEX20
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc20 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX20 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu20 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr20 = ice.privatekey_to_address(0, True, int(seed20)) #Compressed
    uaddr20 = ice.privatekey_to_address(0, False, int(seed20))  #Uncompressed
    p2sh20 = ice.privatekey_to_address(1, True, int(seed20)) #p2sh
    bech3220 = ice.privatekey_to_address(2, True, int(seed20))  #bech32
    
    percent21 = div * 21
    ran21= start+percent21
    HEX21 = "%064x" % ran21
    seed21 = str(ran21)
    private_key_hex_px = '80' + HEX21
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc21 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX21 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu21 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr21 = ice.privatekey_to_address(0, True, int(seed21)) #Compressed
    uaddr21 = ice.privatekey_to_address(0, False, int(seed21))  #Uncompressed
    p2sh21 = ice.privatekey_to_address(1, True, int(seed21)) #p2sh
    bech3221 = ice.privatekey_to_address(2, True, int(seed21))  #bech32
    
    percent22 = div * 22
    ran22= start+percent22
    HEX22 = "%064x" % ran22
    seed22 = str(ran22)
    private_key_hex_px = '80' + HEX22
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc22 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX22 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu22 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr22 = ice.privatekey_to_address(0, True, int(seed22)) #Compressed
    uaddr22 = ice.privatekey_to_address(0, False, int(seed22))  #Uncompressed
    p2sh22 = ice.privatekey_to_address(1, True, int(seed22)) #p2sh
    bech3222 = ice.privatekey_to_address(2, True, int(seed22))  #bech32
    
    percent23 = div * 23
    ran23= start+percent23
    HEX23 = "%064x" % ran23
    seed23 = str(ran23)
    private_key_hex_px = '80' + HEX23
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc23 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX23 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu23 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr23 = ice.privatekey_to_address(0, True, int(seed23)) #Compressed
    uaddr23 = ice.privatekey_to_address(0, False, int(seed23))  #Uncompressed
    p2sh23 = ice.privatekey_to_address(1, True, int(seed23)) #p2sh
    bech3223 = ice.privatekey_to_address(2, True, int(seed23))  #bech32
    
    percent24 = div * 24
    ran24= start+percent24
    HEX24 = "%064x" % ran24
    seed24 = str(ran24)
    private_key_hex_px = '80' + HEX24
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc24 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX24 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu24 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr24 = ice.privatekey_to_address(0, True, int(seed24)) #Compressed
    uaddr24 = ice.privatekey_to_address(0, False, int(seed24))  #Uncompressed
    p2sh24 = ice.privatekey_to_address(1, True, int(seed24)) #p2sh
    bech3224 = ice.privatekey_to_address(2, True, int(seed24))  #bech32
    
    percent25 = div * 25
    ran25= start+percent25
    HEX25 = "%064x" % ran25
    seed25 = str(ran25)
    private_key_hex_px = '80' + HEX25
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc25 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX25 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu25 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr25 = ice.privatekey_to_address(0, True, int(seed25)) #Compressed
    uaddr25 = ice.privatekey_to_address(0, False, int(seed25))  #Uncompressed
    p2sh25 = ice.privatekey_to_address(1, True, int(seed25)) #p2sh
    bech3225 = ice.privatekey_to_address(2, True, int(seed25))  #bech32
    
    percent26 = div * 26
    ran26= start+percent26
    HEX26 = "%064x" % ran26
    seed26 = str(ran26)
    private_key_hex_px = '80' + HEX26
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc26 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX26 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu26 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr26 = ice.privatekey_to_address(0, True, int(seed26)) #Compressed
    uaddr26 = ice.privatekey_to_address(0, False, int(seed26))  #Uncompressed
    p2sh26 = ice.privatekey_to_address(1, True, int(seed26)) #p2sh
    bech3226 = ice.privatekey_to_address(2, True, int(seed26))  #bech32
    
    percent27 = div * 27
    ran27= start+percent27
    HEX27 = "%064x" % ran27
    seed27 = str(ran27)
    private_key_hex_px = '80' + HEX27
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc27 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX27 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu27 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr27 = ice.privatekey_to_address(0, True, int(seed27)) #Compressed
    uaddr27 = ice.privatekey_to_address(0, False, int(seed27))  #Uncompressed
    p2sh27 = ice.privatekey_to_address(1, True, int(seed27)) #p2sh
    bech3227 = ice.privatekey_to_address(2, True, int(seed27))  #bech32
    
    percent28 = div * 28
    ran28= start+percent28
    HEX28 = "%064x" % ran28
    seed28 = str(ran28)
    private_key_hex_px = '80' + HEX28
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc28 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX28 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu28 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr28 = ice.privatekey_to_address(0, True, int(seed28)) #Compressed
    uaddr28 = ice.privatekey_to_address(0, False, int(seed28))  #Uncompressed
    p2sh28 = ice.privatekey_to_address(1, True, int(seed28)) #p2sh
    bech3228 = ice.privatekey_to_address(2, True, int(seed28))  #bech32
    
    percent29 = div * 29
    ran29= start+percent29
    HEX29 = "%064x" % ran29
    seed29 = str(ran29)
    private_key_hex_px = '80' + HEX29
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc29 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX29 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu29 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr29 = ice.privatekey_to_address(0, True, int(seed29)) #Compressed
    uaddr29 = ice.privatekey_to_address(0, False, int(seed29))  #Uncompressed
    p2sh29 = ice.privatekey_to_address(1, True, int(seed29)) #p2sh
    bech3229 = ice.privatekey_to_address(2, True, int(seed29))  #bech32
    
    percent30 = div * 30
    ran30= start+percent30
    HEX30 = "%064x" % ran30
    seed30 = str(ran30)
    private_key_hex_px = '80' + HEX30
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc30 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX30 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu30 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr30 = ice.privatekey_to_address(0, True, int(seed30)) #Compressed
    uaddr30 = ice.privatekey_to_address(0, False, int(seed30))  #Uncompressed
    p2sh30 = ice.privatekey_to_address(1, True, int(seed30)) #p2sh
    bech3230 = ice.privatekey_to_address(2, True, int(seed30))  #bech32
    
    percent31 = div * 31
    ran31= start+percent31
    HEX31 = "%064x" % ran31
    seed31 = str(ran31)
    private_key_hex_px = '80' + HEX31
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc31 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX31 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu31 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr31 = ice.privatekey_to_address(0, True, int(seed31)) #Compressed
    uaddr31 = ice.privatekey_to_address(0, False, int(seed31))  #Uncompressed
    p2sh31 = ice.privatekey_to_address(1, True, int(seed31)) #p2sh
    bech3231 = ice.privatekey_to_address(2, True, int(seed31))  #bech32
    
    percent32 = div * 32
    ran32= start+percent32
    HEX32 = "%064x" % ran32
    seed32 = str(ran32)
    private_key_hex_px = '80' + HEX32
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc32 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX32 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu32 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr32 = ice.privatekey_to_address(0, True, int(seed32)) #Compressed
    uaddr32 = ice.privatekey_to_address(0, False, int(seed32))  #Uncompressed
    p2sh32 = ice.privatekey_to_address(1, True, int(seed32)) #p2sh
    bech3232 = ice.privatekey_to_address(2, True, int(seed32))  #bech32
    
    percent33 = div * 33
    ran33= start+percent33
    HEX33 = "%064x" % ran33
    seed33 = str(ran33)
    private_key_hex_px = '80' + HEX33
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc33 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX33 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu33 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr33 = ice.privatekey_to_address(0, True, int(seed33)) #Compressed
    uaddr33 = ice.privatekey_to_address(0, False, int(seed33))  #Uncompressed
    p2sh33 = ice.privatekey_to_address(1, True, int(seed33)) #p2sh
    bech3233 = ice.privatekey_to_address(2, True, int(seed33))  #bech32
    
    percent34 = div * 34
    ran34= start+percent34
    HEX34 = "%064x" % ran34
    seed34 = str(ran34)
    private_key_hex_px = '80' + HEX34
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc34 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX34 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu34 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr34 = ice.privatekey_to_address(0, True, int(seed34)) #Compressed
    uaddr34 = ice.privatekey_to_address(0, False, int(seed34))  #Uncompressed
    p2sh34 = ice.privatekey_to_address(1, True, int(seed34)) #p2sh
    bech3234 = ice.privatekey_to_address(2, True, int(seed34))  #bech32
    
    percent35 = div * 35
    ran35= start+percent35
    HEX35 = "%064x" % ran35
    seed35 = str(ran35)
    private_key_hex_px = '80' + HEX35
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc35 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX35 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu35 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr35 = ice.privatekey_to_address(0, True, int(seed35)) #Compressed
    uaddr35 = ice.privatekey_to_address(0, False, int(seed35))  #Uncompressed
    p2sh35 = ice.privatekey_to_address(1, True, int(seed35)) #p2sh
    bech3235 = ice.privatekey_to_address(2, True, int(seed35))  #bech32
    
    percent36 = div * 36
    ran36= start+percent36
    HEX36 = "%064x" % ran36
    seed36 = str(ran36)
    private_key_hex_px = '80' + HEX36
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc36 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX36 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu36 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr36 = ice.privatekey_to_address(0, True, int(seed36)) #Compressed
    uaddr36 = ice.privatekey_to_address(0, False, int(seed36))  #Uncompressed
    p2sh36 = ice.privatekey_to_address(1, True, int(seed36)) #p2sh
    bech3236 = ice.privatekey_to_address(2, True, int(seed36))  #bech32
    
    percent37 = div * 37
    ran37= start+percent37
    HEX37 = "%064x" % ran37
    seed37 = str(ran37)
    private_key_hex_px = '80' + HEX37
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc37 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX37 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu37 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr37 = ice.privatekey_to_address(0, True, int(seed37)) #Compressed
    uaddr37 = ice.privatekey_to_address(0, False, int(seed37))  #Uncompressed
    p2sh37 = ice.privatekey_to_address(1, True, int(seed37)) #p2sh
    bech3237 = ice.privatekey_to_address(2, True, int(seed37))  #bech32
    
    percent38 = div * 38
    ran38= start+percent38
    HEX38 = "%064x" % ran38
    seed38 = str(ran38)
    private_key_hex_px = '80' + HEX38
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc38 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX38 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu38 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr38 = ice.privatekey_to_address(0, True, int(seed38)) #Compressed
    uaddr38 = ice.privatekey_to_address(0, False, int(seed38))  #Uncompressed
    p2sh38 = ice.privatekey_to_address(1, True, int(seed38)) #p2sh
    bech3238 = ice.privatekey_to_address(2, True, int(seed38))  #bech32
    
    percent39 = div * 39
    ran39= start+percent39
    HEX39 = "%064x" % ran39
    seed39 = str(ran39)
    private_key_hex_px = '80' + HEX39
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc39 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX39 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu39 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr39 = ice.privatekey_to_address(0, True, int(seed39)) #Compressed
    uaddr39 = ice.privatekey_to_address(0, False, int(seed39))  #Uncompressed
    p2sh39 = ice.privatekey_to_address(1, True, int(seed39)) #p2sh
    bech3239 = ice.privatekey_to_address(2, True, int(seed39))  #bech32
    
    percent40 = div * 40
    ran40= start+percent40
    HEX40 = "%064x" % ran40
    seed40 = str(ran40)
    private_key_hex_px = '80' + HEX40
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc40 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX40 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu40 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr40 = ice.privatekey_to_address(0, True, int(seed40)) #Compressed
    uaddr40 = ice.privatekey_to_address(0, False, int(seed40))  #Uncompressed
    p2sh40 = ice.privatekey_to_address(1, True, int(seed40)) #p2sh
    bech3240 = ice.privatekey_to_address(2, True, int(seed40))  #bech32
    
    percent41 = div * 41
    ran41= start+percent41
    HEX41 = "%064x" % ran41
    seed41 = str(ran41)
    private_key_hex_px = '80' + HEX41
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc41 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX41 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu41 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr41 = ice.privatekey_to_address(0, True, int(seed41)) #Compressed
    uaddr41 = ice.privatekey_to_address(0, False, int(seed41))  #Uncompressed
    p2sh41 = ice.privatekey_to_address(1, True, int(seed41)) #p2sh
    bech3241 = ice.privatekey_to_address(2, True, int(seed41))  #bech32
    
    percent42 = div * 42
    ran42= start+percent42
    HEX42 = "%064x" % ran42
    seed42 = str(ran42)
    private_key_hex_px = '80' + HEX42
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc42 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX42 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu42 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr42 = ice.privatekey_to_address(0, True, int(seed42)) #Compressed
    uaddr42 = ice.privatekey_to_address(0, False, int(seed42))  #Uncompressed
    p2sh42 = ice.privatekey_to_address(1, True, int(seed42)) #p2sh
    bech3242 = ice.privatekey_to_address(2, True, int(seed42))  #bech32
    
    percent43 = div * 43
    ran43= start+percent43
    HEX43 = "%064x" % ran43
    seed43 = str(ran43)
    private_key_hex_px = '80' + HEX43
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc43 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX43 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu43 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr43 = ice.privatekey_to_address(0, True, int(seed43)) #Compressed
    uaddr43 = ice.privatekey_to_address(0, False, int(seed43))  #Uncompressed
    p2sh43 = ice.privatekey_to_address(1, True, int(seed43)) #p2sh
    bech3243 = ice.privatekey_to_address(2, True, int(seed43))  #bech32
    
    percent44 = div * 44
    ran44= start+percent44
    HEX44 = "%064x" % ran44
    seed44 = str(ran44)
    private_key_hex_px = '80' + HEX44
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc44 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX44 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu44 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr44 = ice.privatekey_to_address(0, True, int(seed44)) #Compressed
    uaddr44 = ice.privatekey_to_address(0, False, int(seed44))  #Uncompressed
    p2sh44 = ice.privatekey_to_address(1, True, int(seed44)) #p2sh
    bech3244 = ice.privatekey_to_address(2, True, int(seed44))  #bech32
    
    percent45 = div * 45
    ran45= start+percent45
    HEX45 = "%064x" % ran45
    seed45 = str(ran45)
    private_key_hex_px = '80' + HEX45
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc45 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX45 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu45 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr45 = ice.privatekey_to_address(0, True, int(seed45)) #Compressed
    uaddr45 = ice.privatekey_to_address(0, False, int(seed45))  #Uncompressed
    p2sh45 = ice.privatekey_to_address(1, True, int(seed45)) #p2sh
    bech3245 = ice.privatekey_to_address(2, True, int(seed45))  #bech32
    
    percent46 = div * 46
    ran46= start+percent46
    HEX46 = "%064x" % ran46
    seed46 = str(ran46)
    private_key_hex_px = '80' + HEX46
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc46 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX46 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu46 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr46 = ice.privatekey_to_address(0, True, int(seed46)) #Compressed
    uaddr46 = ice.privatekey_to_address(0, False, int(seed46))  #Uncompressed
    p2sh46 = ice.privatekey_to_address(1, True, int(seed46)) #p2sh
    bech3246 = ice.privatekey_to_address(2, True, int(seed46))  #bech32
    
    percent47 = div * 47
    ran47= start+percent47
    HEX47 = "%064x" % ran47
    seed47 = str(ran47)
    private_key_hex_px = '80' + HEX47
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc47 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX47 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu47 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr47 = ice.privatekey_to_address(0, True, int(seed47)) #Compressed
    uaddr47 = ice.privatekey_to_address(0, False, int(seed47))  #Uncompressed
    p2sh47 = ice.privatekey_to_address(1, True, int(seed47)) #p2sh
    bech3247 = ice.privatekey_to_address(2, True, int(seed47))  #bech32
    
    percent48 = div * 48
    ran48= start+percent48
    HEX48 = "%064x" % ran48
    seed48 = str(ran48)
    private_key_hex_px = '80' + HEX48
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc48 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX48 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu48 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr48 = ice.privatekey_to_address(0, True, int(seed48)) #Compressed
    uaddr48 = ice.privatekey_to_address(0, False, int(seed48))  #Uncompressed
    p2sh48 = ice.privatekey_to_address(1, True, int(seed48)) #p2sh
    bech3248 = ice.privatekey_to_address(2, True, int(seed48))  #bech32
    
    percent49 = div * 49
    ran49= start+percent49
    HEX49 = "%064x" % ran49
    seed49 = str(ran49)
    private_key_hex_px = '80' + HEX49
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc49 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX49 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu49 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr49 = ice.privatekey_to_address(0, True, int(seed49)) #Compressed
    uaddr49 = ice.privatekey_to_address(0, False, int(seed49))  #Uncompressed
    p2sh49 = ice.privatekey_to_address(1, True, int(seed49)) #p2sh
    bech3249 = ice.privatekey_to_address(2, True, int(seed49))  #bech32
    
    percent50 = div * 50
    ran50= start+percent50
    HEX50 = "%064x" % ran50
    seed50 = str(ran50)
    private_key_hex_px = '80' + HEX50
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc50 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX50 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu50 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr50 = ice.privatekey_to_address(0, True, int(seed50)) #Compressed
    uaddr50 = ice.privatekey_to_address(0, False, int(seed50))  #Uncompressed
    p2sh50 = ice.privatekey_to_address(1, True, int(seed50)) #p2sh
    bech3250 = ice.privatekey_to_address(2, True, int(seed50))  #bech32
    
    percent51 = div * 51
    ran51= start+percent51
    HEX51 = "%064x" % ran51
    seed51 = str(ran51)
    private_key_hex_px = '80' + HEX51
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc51 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX51 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu51 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr51 = ice.privatekey_to_address(0, True, int(seed51)) #Compressed
    uaddr51 = ice.privatekey_to_address(0, False, int(seed51))  #Uncompressed
    p2sh51 = ice.privatekey_to_address(1, True, int(seed51)) #p2sh
    bech3251 = ice.privatekey_to_address(2, True, int(seed51))  #bech32
    
    percent52 = div * 52
    ran52= start+percent52
    HEX52 = "%064x" % ran52
    seed52 = str(ran52)
    private_key_hex_px = '80' + HEX52
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc52 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX52 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu52 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr52 = ice.privatekey_to_address(0, True, int(seed52)) #Compressed
    uaddr52 = ice.privatekey_to_address(0, False, int(seed52))  #Uncompressed
    p2sh52 = ice.privatekey_to_address(1, True, int(seed52)) #p2sh
    bech3252 = ice.privatekey_to_address(2, True, int(seed52))  #bech32
    
    percent53 = div * 53
    ran53= start+percent53
    HEX53 = "%064x" % ran53
    seed53 = str(ran53)
    private_key_hex_px = '80' + HEX53
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc53 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX53 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu53 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr53 = ice.privatekey_to_address(0, True, int(seed53)) #Compressed
    uaddr53 = ice.privatekey_to_address(0, False, int(seed53))  #Uncompressed
    p2sh53 = ice.privatekey_to_address(1, True, int(seed53)) #p2sh
    bech3253 = ice.privatekey_to_address(2, True, int(seed53))  #bech32
    
    percent54 = div * 54
    ran54= start+percent54
    HEX54 = "%064x" % ran54
    seed54 = str(ran54)
    private_key_hex_px = '80' + HEX54
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc54 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX54 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu54 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr54 = ice.privatekey_to_address(0, True, int(seed54)) #Compressed
    uaddr54 = ice.privatekey_to_address(0, False, int(seed54))  #Uncompressed
    p2sh54 = ice.privatekey_to_address(1, True, int(seed54)) #p2sh
    bech3254 = ice.privatekey_to_address(2, True, int(seed54))  #bech32
    
    percent55 = div * 55
    ran55= start+percent55
    HEX55 = "%064x" % ran55
    seed55 = str(ran55)
    private_key_hex_px = '80' + HEX55
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc55 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX55 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu55 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr55 = ice.privatekey_to_address(0, True, int(seed55)) #Compressed
    uaddr55 = ice.privatekey_to_address(0, False, int(seed55))  #Uncompressed
    p2sh55 = ice.privatekey_to_address(1, True, int(seed55)) #p2sh
    bech3255 = ice.privatekey_to_address(2, True, int(seed55))  #bech32
    
    percent56 = div * 56
    ran56= start+percent56
    HEX56 = "%064x" % ran56
    seed56 = str(ran56)
    private_key_hex_px = '80' + HEX56
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc56 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX56 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu56 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr56 = ice.privatekey_to_address(0, True, int(seed56)) #Compressed
    uaddr56 = ice.privatekey_to_address(0, False, int(seed56))  #Uncompressed
    p2sh56 = ice.privatekey_to_address(1, True, int(seed56)) #p2sh
    bech3256 = ice.privatekey_to_address(2, True, int(seed56))  #bech32
    
    percent57 = div * 57
    ran57= start+percent57
    HEX57 = "%064x" % ran57
    seed57 = str(ran57)
    private_key_hex_px = '80' + HEX57
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc57 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX57 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu57 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr57 = ice.privatekey_to_address(0, True, int(seed57)) #Compressed
    uaddr57 = ice.privatekey_to_address(0, False, int(seed57))  #Uncompressed
    p2sh57 = ice.privatekey_to_address(1, True, int(seed57)) #p2sh
    bech3257 = ice.privatekey_to_address(2, True, int(seed57))  #bech32
    
    percent58 = div * 58
    ran58= start+percent58
    HEX58 = "%064x" % ran58
    seed58 = str(ran58)
    private_key_hex_px = '80' + HEX58
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc58 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX58 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu58 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr58 = ice.privatekey_to_address(0, True, int(seed58)) #Compressed
    uaddr58 = ice.privatekey_to_address(0, False, int(seed58))  #Uncompressed
    p2sh58 = ice.privatekey_to_address(1, True, int(seed58)) #p2sh
    bech3258 = ice.privatekey_to_address(2, True, int(seed58))  #bech32
    
    percent59 = div * 59
    ran59= start+percent59
    HEX59 = "%064x" % ran59
    seed59 = str(ran59)
    private_key_hex_px = '80' + HEX59
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc59 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX59 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu59 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr59 = ice.privatekey_to_address(0, True, int(seed59)) #Compressed
    uaddr59 = ice.privatekey_to_address(0, False, int(seed59))  #Uncompressed
    p2sh59 = ice.privatekey_to_address(1, True, int(seed59)) #p2sh
    bech3259 = ice.privatekey_to_address(2, True, int(seed59))  #bech32
    
    percent60 = div * 60
    ran60= start+percent60
    HEX60 = "%064x" % ran60
    seed60 = str(ran60)
    private_key_hex_px = '80' + HEX60
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc60 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX60 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu60 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr60 = ice.privatekey_to_address(0, True, int(seed60)) #Compressed
    uaddr60 = ice.privatekey_to_address(0, False, int(seed60))  #Uncompressed
    p2sh60 = ice.privatekey_to_address(1, True, int(seed60)) #p2sh
    bech3260 = ice.privatekey_to_address(2, True, int(seed60))  #bech32
    
    percent61 = div * 61
    ran61= start+percent61
    HEX61 = "%064x" % ran61
    seed61 = str(ran61)
    private_key_hex_px = '80' + HEX61
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc61 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX61 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu61 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr61 = ice.privatekey_to_address(0, True, int(seed61)) #Compressed
    uaddr61 = ice.privatekey_to_address(0, False, int(seed61))  #Uncompressed
    p2sh61 = ice.privatekey_to_address(1, True, int(seed61)) #p2sh
    bech3261 = ice.privatekey_to_address(2, True, int(seed61))  #bech32
    
    percent62 = div * 62
    ran62= start+percent62
    HEX62 = "%064x" % ran62
    seed62 = str(ran62)
    private_key_hex_px = '80' + HEX62
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc62 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX62 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu62 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr62 = ice.privatekey_to_address(0, True, int(seed62)) #Compressed
    uaddr62 = ice.privatekey_to_address(0, False, int(seed62))  #Uncompressed
    p2sh62 = ice.privatekey_to_address(1, True, int(seed62)) #p2sh
    bech3262 = ice.privatekey_to_address(2, True, int(seed62))  #bech32
    
    percent63 = div * 63
    ran63= start+percent63
    HEX63 = "%064x" % ran63
    seed63 = str(ran63)
    private_key_hex_px = '80' + HEX63
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc63 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX63 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu63 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr63 = ice.privatekey_to_address(0, True, int(seed63)) #Compressed
    uaddr63 = ice.privatekey_to_address(0, False, int(seed63))  #Uncompressed
    p2sh63 = ice.privatekey_to_address(1, True, int(seed63)) #p2sh
    bech3263 = ice.privatekey_to_address(2, True, int(seed63))  #bech32
    
    percent64 = div * 64
    ran64= start+percent64
    HEX64 = "%064x" % ran64
    seed64 = str(ran64)
    private_key_hex_px = '80' + HEX64
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc64 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX64 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu64 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr64 = ice.privatekey_to_address(0, True, int(seed64)) #Compressed
    uaddr64 = ice.privatekey_to_address(0, False, int(seed64))  #Uncompressed
    p2sh64 = ice.privatekey_to_address(1, True, int(seed64)) #p2sh
    bech3264 = ice.privatekey_to_address(2, True, int(seed64))  #bech32
    
    percent65 = div * 65
    ran65= start+percent65
    HEX65 = "%064x" % ran65
    seed65 = str(ran65)
    private_key_hex_px = '80' + HEX65
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc65 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX65 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu65 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr65 = ice.privatekey_to_address(0, True, int(seed65)) #Compressed
    uaddr65 = ice.privatekey_to_address(0, False, int(seed65))  #Uncompressed
    p2sh65 = ice.privatekey_to_address(1, True, int(seed65)) #p2sh
    bech3265 = ice.privatekey_to_address(2, True, int(seed65))  #bech32
    
    percent66 = div * 66
    ran66= start+percent66
    HEX66 = "%064x" % ran66
    seed66 = str(ran66)
    private_key_hex_px = '80' + HEX66
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc66 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX66 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu66 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr66 = ice.privatekey_to_address(0, True, int(seed66)) #Compressed
    uaddr66 = ice.privatekey_to_address(0, False, int(seed66))  #Uncompressed
    p2sh66 = ice.privatekey_to_address(1, True, int(seed66)) #p2sh
    bech3266 = ice.privatekey_to_address(2, True, int(seed66))  #bech32
    
    percent67 = div * 67
    ran67= start+percent67
    HEX67 = "%064x" % ran67
    seed67 = str(ran67)
    private_key_hex_px = '80' + HEX67
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc67 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX67 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu67 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr67 = ice.privatekey_to_address(0, True, int(seed67)) #Compressed
    uaddr67 = ice.privatekey_to_address(0, False, int(seed67))  #Uncompressed
    p2sh67 = ice.privatekey_to_address(1, True, int(seed67)) #p2sh
    bech3267 = ice.privatekey_to_address(2, True, int(seed67))  #bech32
    
    percent68 = div * 68
    ran68= start+percent68
    HEX68 = "%064x" % ran68
    seed68 = str(ran68)
    private_key_hex_px = '80' + HEX68
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc68 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX68 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu68 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr68 = ice.privatekey_to_address(0, True, int(seed68)) #Compressed
    uaddr68 = ice.privatekey_to_address(0, False, int(seed68))  #Uncompressed
    p2sh68 = ice.privatekey_to_address(1, True, int(seed68)) #p2sh
    bech3268 = ice.privatekey_to_address(2, True, int(seed68))  #bech32
    
    percent69 = div * 69
    ran69= start+percent69
    HEX69 = "%064x" % ran69
    seed69 = str(ran69)
    private_key_hex_px = '80' + HEX69
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc69 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX69 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu69 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr69 = ice.privatekey_to_address(0, True, int(seed69)) #Compressed
    uaddr69 = ice.privatekey_to_address(0, False, int(seed69))  #Uncompressed
    p2sh69 = ice.privatekey_to_address(1, True, int(seed69)) #p2sh
    bech3269 = ice.privatekey_to_address(2, True, int(seed69))  #bech32
    
    percent70 = div * 70
    ran70= start+percent70
    HEX70 = "%064x" % ran70
    seed70 = str(ran70)
    private_key_hex_px = '80' + HEX70
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc70 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX70 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu70 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr70 = ice.privatekey_to_address(0, True, int(seed70)) #Compressed
    uaddr70 = ice.privatekey_to_address(0, False, int(seed70))  #Uncompressed
    p2sh70 = ice.privatekey_to_address(1, True, int(seed70)) #p2sh
    bech3270 = ice.privatekey_to_address(2, True, int(seed70))  #bech32
    
    percent71 = div * 71
    ran71= start+percent71
    HEX71 = "%064x" % ran71
    seed71 = str(ran71)
    private_key_hex_px = '80' + HEX71
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc71 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX71 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu71 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr71 = ice.privatekey_to_address(0, True, int(seed71)) #Compressed
    uaddr71 = ice.privatekey_to_address(0, False, int(seed71))  #Uncompressed
    p2sh71 = ice.privatekey_to_address(1, True, int(seed71)) #p2sh
    bech3271 = ice.privatekey_to_address(2, True, int(seed71))  #bech32
    
    percent72 = div * 72
    ran72= start+percent72
    HEX72 = "%064x" % ran72
    seed72 = str(ran72)
    private_key_hex_px = '80' + HEX72
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc72 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX72 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu72 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr72 = ice.privatekey_to_address(0, True, int(seed72)) #Compressed
    uaddr72 = ice.privatekey_to_address(0, False, int(seed72))  #Uncompressed
    p2sh72 = ice.privatekey_to_address(1, True, int(seed72)) #p2sh
    bech3272 = ice.privatekey_to_address(2, True, int(seed72))  #bech32
    
    percent73 = div * 73
    ran73= start+percent73
    HEX73 = "%064x" % ran73
    seed73 = str(ran73)
    private_key_hex_px = '80' + HEX73
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc73 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX73 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu73 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr73 = ice.privatekey_to_address(0, True, int(seed73)) #Compressed
    uaddr73 = ice.privatekey_to_address(0, False, int(seed73))  #Uncompressed
    p2sh73 = ice.privatekey_to_address(1, True, int(seed73)) #p2sh
    bech3273 = ice.privatekey_to_address(2, True, int(seed73))  #bech32
    
    percent74 = div * 74
    ran74= start+percent74
    HEX74 = "%064x" % ran74
    seed74 = str(ran74)
    private_key_hex_px = '80' + HEX74
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc74 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX74 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu74 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr74 = ice.privatekey_to_address(0, True, int(seed74)) #Compressed
    uaddr74 = ice.privatekey_to_address(0, False, int(seed74))  #Uncompressed
    p2sh74 = ice.privatekey_to_address(1, True, int(seed74)) #p2sh
    bech3274 = ice.privatekey_to_address(2, True, int(seed74))  #bech32
    
    percent75 = div * 75
    ran75= start+percent75
    HEX75 = "%064x" % ran75
    seed75 = str(ran75)
    private_key_hex_px = '80' + HEX75
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc75 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX75 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu75 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr75 = ice.privatekey_to_address(0, True, int(seed75)) #Compressed
    uaddr75 = ice.privatekey_to_address(0, False, int(seed75))  #Uncompressed
    p2sh75 = ice.privatekey_to_address(1, True, int(seed75)) #p2sh
    bech3275 = ice.privatekey_to_address(2, True, int(seed75))  #bech32
    
    percent76 = div * 76
    ran76= start+percent76
    HEX76 = "%064x" % ran76
    seed76 = str(ran76)
    private_key_hex_px = '80' + HEX76
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc76 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX76 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu76 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr76 = ice.privatekey_to_address(0, True, int(seed76)) #Compressed
    uaddr76 = ice.privatekey_to_address(0, False, int(seed76))  #Uncompressed
    p2sh76 = ice.privatekey_to_address(1, True, int(seed76)) #p2sh
    bech3276 = ice.privatekey_to_address(2, True, int(seed76))  #bech32
    
    percent77 = div * 77
    ran77= start+percent77
    HEX77 = "%064x" % ran77
    seed77 = str(ran77)
    private_key_hex_px = '80' + HEX77
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc77 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX77 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu77 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr77 = ice.privatekey_to_address(0, True, int(seed77)) #Compressed
    uaddr77 = ice.privatekey_to_address(0, False, int(seed77))  #Uncompressed
    p2sh77 = ice.privatekey_to_address(1, True, int(seed77)) #p2sh
    bech3277 = ice.privatekey_to_address(2, True, int(seed77))  #bech32
    
    percent78 = div * 78
    ran78= start+percent78
    HEX78 = "%064x" % ran78
    seed78 = str(ran78)
    private_key_hex_px = '80' + HEX78
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc78 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX78 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu78 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr78 = ice.privatekey_to_address(0, True, int(seed78)) #Compressed
    uaddr78 = ice.privatekey_to_address(0, False, int(seed78))  #Uncompressed
    p2sh78 = ice.privatekey_to_address(1, True, int(seed78)) #p2sh
    bech3278 = ice.privatekey_to_address(2, True, int(seed78))  #bech32
    
    percent79 = div * 79
    ran79= start+percent79
    HEX79 = "%064x" % ran79
    seed79 = str(ran79)
    private_key_hex_px = '80' + HEX79
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc79 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX79 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu79 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr79 = ice.privatekey_to_address(0, True, int(seed79)) #Compressed
    uaddr79 = ice.privatekey_to_address(0, False, int(seed79))  #Uncompressed
    p2sh79 = ice.privatekey_to_address(1, True, int(seed79)) #p2sh
    bech3279 = ice.privatekey_to_address(2, True, int(seed79))  #bech32
    
    percent80 = div * 80
    ran80= start+percent80
    HEX80 = "%064x" % ran80
    seed80 = str(ran80)
    private_key_hex_px = '80' + HEX80
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc80 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX80 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu80 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr80 = ice.privatekey_to_address(0, True, int(seed80)) #Compressed
    uaddr80 = ice.privatekey_to_address(0, False, int(seed80))  #Uncompressed
    p2sh80 = ice.privatekey_to_address(1, True, int(seed80)) #p2sh
    bech3280 = ice.privatekey_to_address(2, True, int(seed80))  #bech32
    
    percent81 = div * 81
    ran81= start+percent81
    HEX81 = "%064x" % ran81
    seed81 = str(ran81)
    private_key_hex_px = '80' + HEX81
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc81 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX81 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu81 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr81 = ice.privatekey_to_address(0, True, int(seed81)) #Compressed
    uaddr81 = ice.privatekey_to_address(0, False, int(seed81))  #Uncompressed
    p2sh81 = ice.privatekey_to_address(1, True, int(seed81)) #p2sh
    bech3281 = ice.privatekey_to_address(2, True, int(seed81))  #bech32
    
    percent82 = div * 82
    ran82= start+percent82
    HEX82 = "%064x" % ran82
    seed82 = str(ran82)
    private_key_hex_px = '80' + HEX82
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc82 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX82 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu82 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr82 = ice.privatekey_to_address(0, True, int(seed82)) #Compressed
    uaddr82 = ice.privatekey_to_address(0, False, int(seed82))  #Uncompressed
    p2sh82 = ice.privatekey_to_address(1, True, int(seed82)) #p2sh
    bech3282 = ice.privatekey_to_address(2, True, int(seed82))  #bech32
    
    percent83 = div * 83
    ran83= start+percent83
    HEX83 = "%064x" % ran83
    seed83 = str(ran83)
    private_key_hex_px = '80' + HEX83
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc83 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX83 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu83 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr83 = ice.privatekey_to_address(0, True, int(seed83)) #Compressed
    uaddr83 = ice.privatekey_to_address(0, False, int(seed83))  #Uncompressed
    p2sh83 = ice.privatekey_to_address(1, True, int(seed83)) #p2sh
    bech3283 = ice.privatekey_to_address(2, True, int(seed83))  #bech32
    
    percent84 = div * 84
    ran84= start+percent84
    HEX84 = "%064x" % ran84
    seed84 = str(ran84)
    private_key_hex_px = '80' + HEX84
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc84 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX84 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu84 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr84 = ice.privatekey_to_address(0, True, int(seed84)) #Compressed
    uaddr84 = ice.privatekey_to_address(0, False, int(seed84))  #Uncompressed
    p2sh84 = ice.privatekey_to_address(1, True, int(seed84)) #p2sh
    bech3284 = ice.privatekey_to_address(2, True, int(seed84))  #bech32
    
    percent85 = div * 85
    ran85= start+percent85
    HEX85 = "%064x" % ran85
    seed85 = str(ran85)
    private_key_hex_px = '80' + HEX85
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc85 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX85 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu85 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr85 = ice.privatekey_to_address(0, True, int(seed85)) #Compressed
    uaddr85 = ice.privatekey_to_address(0, False, int(seed85))  #Uncompressed
    p2sh85 = ice.privatekey_to_address(1, True, int(seed85)) #p2sh
    bech3285 = ice.privatekey_to_address(2, True, int(seed85))  #bech32
    
    percent86 = div * 86
    ran86= start+percent86
    HEX86 = "%064x" % ran86
    seed86 = str(ran86)
    private_key_hex_px = '80' + HEX86
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc86 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX86 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu86 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr86 = ice.privatekey_to_address(0, True, int(seed86)) #Compressed
    uaddr86 = ice.privatekey_to_address(0, False, int(seed86))  #Uncompressed
    p2sh86 = ice.privatekey_to_address(1, True, int(seed86)) #p2sh
    bech3286 = ice.privatekey_to_address(2, True, int(seed86))  #bech32
    
    percent87 = div * 87
    ran87= start+percent87
    HEX87 = "%064x" % ran87
    seed87 = str(ran87)
    private_key_hex_px = '80' + HEX87
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc87 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX87 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu87 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr87 = ice.privatekey_to_address(0, True, int(seed87)) #Compressed
    uaddr87 = ice.privatekey_to_address(0, False, int(seed87))  #Uncompressed
    p2sh87 = ice.privatekey_to_address(1, True, int(seed87)) #p2sh
    bech3287 = ice.privatekey_to_address(2, True, int(seed87))  #bech32
    
    percent88 = div * 88
    ran88= start+percent88
    HEX88 = "%064x" % ran88
    seed88 = str(ran88)
    private_key_hex_px = '80' + HEX88
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc88 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX88 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu88 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr88 = ice.privatekey_to_address(0, True, int(seed88)) #Compressed
    uaddr88 = ice.privatekey_to_address(0, False, int(seed88))  #Uncompressed
    p2sh88 = ice.privatekey_to_address(1, True, int(seed88)) #p2sh
    bech3288 = ice.privatekey_to_address(2, True, int(seed88))  #bech32
    
    percent89 = div * 89
    ran89= start+percent89
    HEX89 = "%064x" % ran89
    seed89 = str(ran89)
    private_key_hex_px = '80' + HEX89
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc89 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX89 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu89 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr89 = ice.privatekey_to_address(0, True, int(seed89)) #Compressed
    uaddr89 = ice.privatekey_to_address(0, False, int(seed89))  #Uncompressed
    p2sh89 = ice.privatekey_to_address(1, True, int(seed89)) #p2sh
    bech3289 = ice.privatekey_to_address(2, True, int(seed89))  #bech32
    
    percent90 = div * 90
    ran90= start+percent90
    HEX90 = "%064x" % ran90
    seed90 = str(ran90)
    private_key_hex_px = '80' + HEX90
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc90 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX90 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu90 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr90 = ice.privatekey_to_address(0, True, int(seed90)) #Compressed
    uaddr90 = ice.privatekey_to_address(0, False, int(seed90))  #Uncompressed
    p2sh90 = ice.privatekey_to_address(1, True, int(seed90)) #p2sh
    bech3290 = ice.privatekey_to_address(2, True, int(seed90))  #bech32
    
    percent91 = div * 91
    ran91= start+percent91
    HEX91 = "%064x" % ran91
    seed91 = str(ran91)
    private_key_hex_px = '80' + HEX91
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc91 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX91 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu91 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr91 = ice.privatekey_to_address(0, True, int(seed91)) #Compressed
    uaddr91 = ice.privatekey_to_address(0, False, int(seed91))  #Uncompressed
    p2sh91 = ice.privatekey_to_address(1, True, int(seed91)) #p2sh
    bech3291 = ice.privatekey_to_address(2, True, int(seed91))  #bech32
    
    percent92 = div * 92
    ran92= start+percent92
    HEX92 = "%064x" % ran92
    seed92 = str(ran92)
    private_key_hex_px = '80' + HEX92
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc92 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX92 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu92 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr92 = ice.privatekey_to_address(0, True, int(seed92)) #Compressed
    uaddr92 = ice.privatekey_to_address(0, False, int(seed92))  #Uncompressed
    p2sh92 = ice.privatekey_to_address(1, True, int(seed92)) #p2sh
    bech3292 = ice.privatekey_to_address(2, True, int(seed92))  #bech32
    
    percent93 = div * 93
    ran93= start+percent93
    HEX93 = "%064x" % ran93
    seed93 = str(ran93)
    private_key_hex_px = '80' + HEX93
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc93 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX93 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu93 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr93 = ice.privatekey_to_address(0, True, int(seed93)) #Compressed
    uaddr93 = ice.privatekey_to_address(0, False, int(seed93))  #Uncompressed
    p2sh93 = ice.privatekey_to_address(1, True, int(seed93)) #p2sh
    bech3293 = ice.privatekey_to_address(2, True, int(seed93))  #bech32
    
    percent94 = div * 94
    ran94= start+percent94
    HEX94 = "%064x" % ran94
    seed94 = str(ran94)
    private_key_hex_px = '80' + HEX94
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc94 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX94 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu94 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr94 = ice.privatekey_to_address(0, True, int(seed94)) #Compressed
    uaddr94 = ice.privatekey_to_address(0, False, int(seed94))  #Uncompressed
    p2sh94 = ice.privatekey_to_address(1, True, int(seed94)) #p2sh
    bech3294 = ice.privatekey_to_address(2, True, int(seed94))  #bech32
    
    percent95 = div * 95
    ran95= start+percent95
    HEX95 = "%064x" % ran95
    seed95 = str(ran95)
    private_key_hex_px = '80' + HEX95
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc95 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX95 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu95 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr95 = ice.privatekey_to_address(0, True, int(seed95)) #Compressed
    uaddr95 = ice.privatekey_to_address(0, False, int(seed95))  #Uncompressed
    p2sh95 = ice.privatekey_to_address(1, True, int(seed95)) #p2sh
    bech3295 = ice.privatekey_to_address(2, True, int(seed95))  #bech32
    
    percent96 = div * 96
    ran96= start+percent96
    HEX96 = "%064x" % ran96
    seed96 = str(ran96)
    private_key_hex_px = '80' + HEX96
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc96 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX96 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu96 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr96 = ice.privatekey_to_address(0, True, int(seed96)) #Compressed
    uaddr96 = ice.privatekey_to_address(0, False, int(seed96))  #Uncompressed
    p2sh96 = ice.privatekey_to_address(1, True, int(seed96)) #p2sh
    bech3296 = ice.privatekey_to_address(2, True, int(seed96))  #bech32
    
    percent97 = div * 97
    ran97= start+percent97
    HEX97 = "%064x" % ran97
    seed97 = str(ran97)
    private_key_hex_px = '80' + HEX97
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc97 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX97 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu97 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr97 = ice.privatekey_to_address(0, True, int(seed97)) #Compressed
    uaddr97 = ice.privatekey_to_address(0, False, int(seed97))  #Uncompressed
    p2sh97 = ice.privatekey_to_address(1, True, int(seed97)) #p2sh
    bech3297 = ice.privatekey_to_address(2, True, int(seed97))  #bech32
    
    percent98 = div * 98
    ran98= start+percent98
    HEX98 = "%064x" % ran98
    seed98 = str(ran98)
    private_key_hex_px = '80' + HEX98
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc98 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX98 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu98 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr98 = ice.privatekey_to_address(0, True, int(seed98)) #Compressed
    uaddr98 = ice.privatekey_to_address(0, False, int(seed98))  #Uncompressed
    p2sh98 = ice.privatekey_to_address(1, True, int(seed98)) #p2sh
    bech3298 = ice.privatekey_to_address(2, True, int(seed98))  #bech32
    
    percent99 = div * 99
    ran99= start+percent99
    HEX99 = "%064x" % ran99
    seed99 = str(ran99)
    private_key_hex_px = '80' + HEX99
    x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksum = x[:8]
    private_key_hex_px_cs = private_key_hex_px + checksum
    wifc99 = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
    private_key_hex_compressed_px = '80' + HEX99 + '01'
    x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
    x = sha256(bytes.fromhex(x)).hexdigest()
    checksumc = x[:8]
    private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
    wifu99 = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
    caddr99 = ice.privatekey_to_address(0, True, int(seed99)) #Compressed
    uaddr99 = ice.privatekey_to_address(0, False, int(seed99))  #Uncompressed
    p2sh99 = ice.privatekey_to_address(1, True, int(seed99)) #p2sh
    bech3299 = ice.privatekey_to_address(2, True, int(seed99))  #bech32
    
    if uaddr in add or caddr in add or p2sh in add or bech32 in add:
        print('\nMatch Found 1%')
        print('\nPrivatekey (dec): ', seed,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wifu, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 P2SH: ', p2sh, '\nPublic Address bc1 BECH32: ', bech32)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed)
        f.write('\nPrivatekey (hex): ' + HEX)
        f.write('\nPrivatekey Uncompressed: ' + wifu)
        f.write('\nPrivatekey compressed: ' + wifc)
        f.write('\nPublic Address 1 Compressed: ' + caddr)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
        f.write('\nPublic Address 3 P2SH: ' + p2sh)
        f.write('\nPublic Address bc1 BECH32: ' + bech32)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr2 in add or caddr2 in add or p2sh2 in add or bech322 in add:
        print('\nMatch Found 2%')
        print('\nPrivatekey (dec): ', seed2,'\nPrivatekey (hex): ', HEX2, '\nPrivatekey Uncompressed: ', wifu2, '\nPrivatekey compressed: ', wifc2, '\nPublic Address 1 Uncompressed: ', uaddr2, '\nPublic Address 1 Compressed: ', caddr2, '\nPublic Address 3 P2SH: ', p2sh2, '\nPublic Address bc1 BECH32: ', bech322)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed2)
        f.write('\nPrivatekey (hex): ' + HEX2)
        f.write('\nPrivatekey Uncompressed: ' + wifu2)
        f.write('\nPrivatekey compressed: ' + wifc2)
        f.write('\nPublic Address 1 Compressed: ' + caddr2)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr2)
        f.write('\nPublic Address 3 P2SH: ' + p2sh2)
        f.write('\nPublic Address bc1 BECH32: ' + bech322)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr3 in add or caddr3 in add or p2sh3 in add or bech323 in add:
        print('\nMatch Found 3%')
        print('\nPrivatekey (dec): ', seed3,'\nPrivatekey (hex): ', HEX3, '\nPrivatekey Uncompressed: ', wifu3, '\nPrivatekey compressed: ', wifc3, '\nPublic Address 1 Uncompressed: ', uaddr3, '\nPublic Address 1 Compressed: ', caddr3, '\nPublic Address 3 P2SH: ', p2sh3, '\nPublic Address bc1 BECH32: ', bech323)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed3)
        f.write('\nPrivatekey (hex): ' + HEX3)
        f.write('\nPrivatekey Uncompressed: ' + wifu3)
        f.write('\nPrivatekey compressed: ' + wifc3)
        f.write('\nPublic Address 1 Compressed: ' + caddr3)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr3)
        f.write('\nPublic Address 3 P2SH: ' + p2sh3)
        f.write('\nPublic Address bc1 BECH32: ' + bech323)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr4 in add or caddr4 in add or p2sh4 in add or bech324 in add:
        print('\nMatch Found 4% ')
        print('\nPrivatekey (dec): ', seed4,'\nPrivatekey (hex): ', HEX4, '\nPrivatekey Uncompressed: ', wifu4, '\nPrivatekey compressed: ', wifc4, '\nPublic Address 1 Uncompressed: ', uaddr4, '\nPublic Address 1 Compressed: ', caddr4, '\nPublic Address 3 P2SH: ', p2sh4, '\nPublic Address bc1 BECH32: ', bech324)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed4)
        f.write('\nPrivatekey (hex): ' + HEX4)
        f.write('\nPrivatekey Uncompressed: ' + wifu4)
        f.write('\nPrivatekey compressed: ' + wifc4)
        f.write('\nPublic Address 1 Compressed: ' + caddr4)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr4)
        f.write('\nPublic Address 3 P2SH: ' + p2sh4)
        f.write('\nPublic Address bc1 BECH32: ' + bech324)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr5 in add or caddr5 in add or p2sh5 in add or bech325 in add:
        print('\nMatch Found 5% ')
        print('\nPrivatekey (dec): ', seed5,'\nPrivatekey (hex): ', HEX5, '\nPrivatekey Uncompressed: ', wifu5, '\nPrivatekey compressed: ', wifc5, '\nPublic Address 1 Uncompressed: ', uaddr5, '\nPublic Address 1 Compressed: ', caddr5, '\nPublic Address 3 P2SH: ', p2sh5, '\nPublic Address bc1 BECH32: ', bech325)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed5)
        f.write('\nPrivatekey (hex): ' + HEX5)
        f.write('\nPrivatekey Uncompressed: ' + wifu5)
        f.write('\nPrivatekey compressed: ' + wifc5)
        f.write('\nPublic Address 1 Compressed: ' + caddr5)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr5)
        f.write('\nPublic Address 3 P2SH: ' + p2sh5)
        f.write('\nPublic Address bc1 BECH32: ' + bech325)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr6 in add or caddr6 in add or p2sh6 in add or bech326 in add:
        print('\nMatch Found 6% ')
        print('\nPrivatekey (dec): ', seed6,'\nPrivatekey (hex): ', HEX6, '\nPrivatekey Uncompressed: ', wifu6, '\nPrivatekey compressed: ', wifc6, '\nPublic Address 1 Uncompressed: ', uaddr6, '\nPublic Address 1 Compressed: ', caddr6, '\nPublic Address 3 P2SH: ', p2sh6, '\nPublic Address bc1 BECH32: ', bech326)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed6)
        f.write('\nPrivatekey (hex): ' + HEX6)
        f.write('\nPrivatekey Uncompressed: ' + wifu6)
        f.write('\nPrivatekey compressed: ' + wifc6)
        f.write('\nPublic Address 1 Compressed: ' + caddr6)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr6)
        f.write('\nPublic Address 3 P2SH: ' + p2sh6)
        f.write('\nPublic Address bc1 BECH32: ' + bech326)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr7 in add or caddr7 in add or p2sh7 in add or bech327 in add:
        print('\nMatch Found 7% ')
        print('\nPrivatekey (dec): ', seed7,'\nPrivatekey (hex): ', HEX7, '\nPrivatekey Uncompressed: ', wifu7, '\nPrivatekey compressed: ', wifc7, '\nPublic Address 1 Uncompressed: ', uaddr7, '\nPublic Address 1 Compressed: ', caddr7, '\nPublic Address 3 P2SH: ', p2sh7, '\nPublic Address bc1 BECH32: ', bech327)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed7)
        f.write('\nPrivatekey (hex): ' + HEX7)
        f.write('\nPrivatekey Uncompressed: ' + wifu7)
        f.write('\nPrivatekey compressed: ' + wifc7)
        f.write('\nPublic Address 1 Compressed: ' + caddr7)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr7)
        f.write('\nPublic Address 3 P2SH: ' + p2sh7)
        f.write('\nPublic Address bc1 BECH32: ' + bech327)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr8 in add or caddr8 in add or p2sh8 in add or bech328 in add:
        print('\nMatch Found 8% ')
        print('\nPrivatekey (dec): ', seed8,'\nPrivatekey (hex): ', HEX8, '\nPrivatekey Uncompressed: ', wifu8, '\nPrivatekey compressed: ', wifc8, '\nPublic Address 1 Uncompressed: ', uaddr8, '\nPublic Address 1 Compressed: ', caddr8, '\nPublic Address 3 P2SH: ', p2sh8, '\nPublic Address bc1 BECH32: ', bech328)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed8)
        f.write('\nPrivatekey (hex): ' + HEX8)
        f.write('\nPrivatekey Uncompressed: ' + wifu8)
        f.write('\nPrivatekey compressed: ' + wifc8)
        f.write('\nPublic Address 1 Compressed: ' + caddr8)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr8)
        f.write('\nPublic Address 3 P2SH: ' + p2sh8)
        f.write('\nPublic Address bc1 BECH32: ' + bech328)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr9 in add or caddr9 in add or p2sh9 in add or bech329 in add:
        print('\nMatch Found 9% ')
        print('\nPrivatekey (dec): ', seed9,'\nPrivatekey (hex): ', HEX9, '\nPrivatekey Uncompressed: ', wifu9, '\nPrivatekey compressed: ', wifc9, '\nPublic Address 1 Uncompressed: ', uaddr9, '\nPublic Address 1 Compressed: ', caddr9, '\nPublic Address 3 P2SH: ', p2sh9, '\nPublic Address bc1 BECH32: ', bech329)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed9)
        f.write('\nPrivatekey (hex): ' + HEX9)
        f.write('\nPrivatekey Uncompressed: ' + wifu9)
        f.write('\nPrivatekey compressed: ' + wifc9)
        f.write('\nPublic Address 1 Compressed: ' + caddr9)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr9)
        f.write('\nPublic Address 3 P2SH: ' + p2sh9)
        f.write('\nPublic Address bc1 BECH32: ' + bech329)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr10 in add or caddr10 in add or p2sh10 in add or bech3210 in add:
        print('\nMatch Found 10% ')
        print('\nPrivatekey (dec): ', seed10,'\nPrivatekey (hex): ', HEX10, '\nPrivatekey Uncompressed: ', wifu10, '\nPrivatekey compressed: ', wifc10, '\nPublic Address 1 Uncompressed: ', uaddr10, '\nPublic Address 1 Compressed: ', caddr10, '\nPublic Address 3 P2SH: ', p2sh10, '\nPublic Address bc1 BECH32: ', bech3210)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed10)
        f.write('\nPrivatekey (hex): ' + HEX10)
        f.write('\nPrivatekey Uncompressed: ' + wifu10)
        f.write('\nPrivatekey compressed: ' + wifc10)
        f.write('\nPublic Address 1 Compressed: ' + caddr10)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr10)
        f.write('\nPublic Address 3 P2SH: ' + p2sh10)
        f.write('\nPublic Address bc1 BECH32: ' + bech3210)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr11 in add or caddr11 in add or p2sh11 in add or bech3211 in add:
        print('\nMatch Found 11% ')
        print('\nPrivatekey (dec): ', seed11,'\nPrivatekey (hex): ', HEX11, '\nPrivatekey Uncompressed: ', wifu11, '\nPrivatekey compressed: ', wifc11, '\nPublic Address 1 Uncompressed: ', uaddr11, '\nPublic Address 1 Compressed: ', caddr11, '\nPublic Address 3 P2SH: ', p2sh11, '\nPublic Address bc1 BECH32: ', bech3211)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed11)
        f.write('\nPrivatekey (hex): ' + HEX11)
        f.write('\nPrivatekey Uncompressed: ' + wifu11)
        f.write('\nPrivatekey compressed: ' + wifc11)
        f.write('\nPublic Address 1 Compressed: ' + caddr11)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr11)
        f.write('\nPublic Address 3 P2SH: ' + p2sh11)
        f.write('\nPublic Address bc1 BECH32: ' + bech3211)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr12 in add or caddr12 in add or p2sh12 in add or bech3212 in add:
        print('\nMatch Found 12% ')
        print('\nPrivatekey (dec): ', seed12,'\nPrivatekey (hex): ', HEX12, '\nPrivatekey Uncompressed: ', wifu12, '\nPrivatekey compressed: ', wifc12, '\nPublic Address 1 Uncompressed: ', uaddr12, '\nPublic Address 1 Compressed: ', caddr12, '\nPublic Address 3 P2SH: ', p2sh12, '\nPublic Address bc1 BECH32: ', bech3212)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed12)
        f.write('\nPrivatekey (hex): ' + HEX12)
        f.write('\nPrivatekey Uncompressed: ' + wifu12)
        f.write('\nPrivatekey compressed: ' + wifc12)
        f.write('\nPublic Address 1 Compressed: ' + caddr12)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr12)
        f.write('\nPublic Address 3 P2SH: ' + p2sh12)
        f.write('\nPublic Address bc1 BECH32: ' + bech3212)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr13 in add or caddr13 in add or p2sh13 in add or bech3213 in add:
        print('\nMatch Found 13% ')
        print('\nPrivatekey (dec): ', seed13,'\nPrivatekey (hex): ', HEX13, '\nPrivatekey Uncompressed: ', wifu13, '\nPrivatekey compressed: ', wifc13, '\nPublic Address 1 Uncompressed: ', uaddr13, '\nPublic Address 1 Compressed: ', caddr13, '\nPublic Address 3 P2SH: ', p2sh13, '\nPublic Address bc1 BECH32: ', bech3213)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed13)
        f.write('\nPrivatekey (hex): ' + HEX13)
        f.write('\nPrivatekey Uncompressed: ' + wifu13)
        f.write('\nPrivatekey compressed: ' + wifc13)
        f.write('\nPublic Address 1 Compressed: ' + caddr13)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr13)
        f.write('\nPublic Address 3 P2SH: ' + p2sh13)
        f.write('\nPublic Address bc1 BECH32: ' + bech3213)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr14 in add or caddr14 in add or p2sh14 in add or bech3214 in add:
        print('\nMatch Found 14% ')
        print('\nPrivatekey (dec): ', seed14,'\nPrivatekey (hex): ', HEX14, '\nPrivatekey Uncompressed: ', wifu14, '\nPrivatekey compressed: ', wifc14, '\nPublic Address 1 Uncompressed: ', uaddr14, '\nPublic Address 1 Compressed: ', caddr14, '\nPublic Address 3 P2SH: ', p2sh14, '\nPublic Address bc1 BECH32: ', bech3214)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed14)
        f.write('\nPrivatekey (hex): ' + HEX14)
        f.write('\nPrivatekey Uncompressed: ' + wifu14)
        f.write('\nPrivatekey compressed: ' + wifc14)
        f.write('\nPublic Address 1 Compressed: ' + caddr14)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr14)
        f.write('\nPublic Address 3 P2SH: ' + p2sh14)
        f.write('\nPublic Address bc1 BECH32: ' + bech3214)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr15 in add or caddr15 in add or p2sh15 in add or bech3215 in add:
        print('\nMatch Found 15% ')
        print('\nPrivatekey (dec): ', seed15,'\nPrivatekey (hex): ', HEX15, '\nPrivatekey Uncompressed: ', wifu15, '\nPrivatekey compressed: ', wifc15, '\nPublic Address 1 Uncompressed: ', uaddr15, '\nPublic Address 1 Compressed: ', caddr15, '\nPublic Address 3 P2SH: ', p2sh15, '\nPublic Address bc1 BECH32: ', bech3215)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed15)
        f.write('\nPrivatekey (hex): ' + HEX15)
        f.write('\nPrivatekey Uncompressed: ' + wifu15)
        f.write('\nPrivatekey compressed: ' + wifc15)
        f.write('\nPublic Address 1 Compressed: ' + caddr15)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr15)
        f.write('\nPublic Address 3 P2SH: ' + p2sh15)
        f.write('\nPublic Address bc1 BECH32: ' + bech3215)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr16 in add or caddr16 in add or p2sh16 in add or bech3216 in add:
        print('\nMatch Found 16% ')
        print('\nPrivatekey (dec): ', seed16,'\nPrivatekey (hex): ', HEX16, '\nPrivatekey Uncompressed: ', wifu16, '\nPrivatekey compressed: ', wifc16, '\nPublic Address 1 Uncompressed: ', uaddr16, '\nPublic Address 1 Compressed: ', caddr16, '\nPublic Address 3 P2SH: ', p2sh16, '\nPublic Address bc1 BECH32: ', bech3216)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed16)
        f.write('\nPrivatekey (hex): ' + HEX16)
        f.write('\nPrivatekey Uncompressed: ' + wifu16)
        f.write('\nPrivatekey compressed: ' + wifc16)
        f.write('\nPublic Address 1 Compressed: ' + caddr16)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr16)
        f.write('\nPublic Address 3 P2SH: ' + p2sh16)
        f.write('\nPublic Address bc1 BECH32: ' + bech3216)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr17 in add or caddr17 in add or p2sh17 in add or bech3217 in add:
        print('\nMatch Found 17% ')
        print('\nPrivatekey (dec): ', seed17,'\nPrivatekey (hex): ', HEX17, '\nPrivatekey Uncompressed: ', wifu17, '\nPrivatekey compressed: ', wifc17, '\nPublic Address 1 Uncompressed: ', uaddr17, '\nPublic Address 1 Compressed: ', caddr17, '\nPublic Address 3 P2SH: ', p2sh17, '\nPublic Address bc1 BECH32: ', bech3217)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed17)
        f.write('\nPrivatekey (hex): ' + HEX17)
        f.write('\nPrivatekey Uncompressed: ' + wifu17)
        f.write('\nPrivatekey compressed: ' + wifc17)
        f.write('\nPublic Address 1 Compressed: ' + caddr17)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr17)
        f.write('\nPublic Address 3 P2SH: ' + p2sh17)
        f.write('\nPublic Address bc1 BECH32: ' + bech3217)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr18 in add or caddr18 in add or p2sh18 in add or bech3218 in add:
        print('\nMatch Found 18% ')
        print('\nPrivatekey (dec): ', seed18,'\nPrivatekey (hex): ', HEX18, '\nPrivatekey Uncompressed: ', wifu18, '\nPrivatekey compressed: ', wifc18, '\nPublic Address 1 Uncompressed: ', uaddr18, '\nPublic Address 1 Compressed: ', caddr18, '\nPublic Address 3 P2SH: ', p2sh18, '\nPublic Address bc1 BECH32: ', bech3218)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed18)
        f.write('\nPrivatekey (hex): ' + HEX18)
        f.write('\nPrivatekey Uncompressed: ' + wifu18)
        f.write('\nPrivatekey compressed: ' + wifc18)
        f.write('\nPublic Address 1 Compressed: ' + caddr18)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr18)
        f.write('\nPublic Address 3 P2SH: ' + p2sh18)
        f.write('\nPublic Address bc1 BECH32: ' + bech3218)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr19 in add or caddr19 in add or p2sh19 in add or bech3219 in add:
        print('\nMatch Found 19% ')
        print('\nPrivatekey (dec): ', seed19,'\nPrivatekey (hex): ', HEX19, '\nPrivatekey Uncompressed: ', wifu19, '\nPrivatekey compressed: ', wifc19, '\nPublic Address 1 Uncompressed: ', uaddr19, '\nPublic Address 1 Compressed: ', caddr19, '\nPublic Address 3 P2SH: ', p2sh19, '\nPublic Address bc1 BECH32: ', bech3219)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed19)
        f.write('\nPrivatekey (hex): ' + HEX19)
        f.write('\nPrivatekey Uncompressed: ' + wifu19)
        f.write('\nPrivatekey compressed: ' + wifc19)
        f.write('\nPublic Address 1 Compressed: ' + caddr19)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr19)
        f.write('\nPublic Address 3 P2SH: ' + p2sh19)
        f.write('\nPublic Address bc1 BECH32: ' + bech3219)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr20 in add or caddr20 in add or p2sh20 in add or bech3220 in add:
        print('\nMatch Found 20% ')
        print('\nPrivatekey (dec): ', seed20,'\nPrivatekey (hex): ', HEX20, '\nPrivatekey Uncompressed: ', wifu20, '\nPrivatekey compressed: ', wifc20, '\nPublic Address 1 Uncompressed: ', uaddr20, '\nPublic Address 1 Compressed: ', caddr20, '\nPublic Address 3 P2SH: ', p2sh20, '\nPublic Address bc1 BECH32: ', bech3220)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed20)
        f.write('\nPrivatekey (hex): ' + HEX20)
        f.write('\nPrivatekey Uncompressed: ' + wifu20)
        f.write('\nPrivatekey compressed: ' + wifc20)
        f.write('\nPublic Address 1 Compressed: ' + caddr20)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr20)
        f.write('\nPublic Address 3 P2SH: ' + p2sh20)
        f.write('\nPublic Address bc1 BECH32: ' + bech3220)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr21 in add or caddr21 in add or p2sh21 in add or bech3221 in add:
        print('\nMatch Found 21% ')
        print('\nPrivatekey (dec): ', seed21,'\nPrivatekey (hex): ', HEX21, '\nPrivatekey Uncompressed: ', wifu21, '\nPrivatekey compressed: ', wifc21, '\nPublic Address 1 Uncompressed: ', uaddr21, '\nPublic Address 1 Compressed: ', caddr21, '\nPublic Address 3 P2SH: ', p2sh21, '\nPublic Address bc1 BECH32: ', bech3221)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed21)
        f.write('\nPrivatekey (hex): ' + HEX21)
        f.write('\nPrivatekey Uncompressed: ' + wifu21)
        f.write('\nPrivatekey compressed: ' + wifc21)
        f.write('\nPublic Address 1 Compressed: ' + caddr21)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr21)
        f.write('\nPublic Address 3 P2SH: ' + p2sh21)
        f.write('\nPublic Address bc1 BECH32: ' + bech3221)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr22 in add or caddr22 in add or p2sh22 in add or bech3222 in add:
        print('\nMatch Found 22% ')
        print('\nPrivatekey (dec): ', seed22,'\nPrivatekey (hex): ', HEX22, '\nPrivatekey Uncompressed: ', wifu22, '\nPrivatekey compressed: ', wifc22, '\nPublic Address 1 Uncompressed: ', uaddr22, '\nPublic Address 1 Compressed: ', caddr22, '\nPublic Address 3 P2SH: ', p2sh22, '\nPublic Address bc1 BECH32: ', bech3222)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed22)
        f.write('\nPrivatekey (hex): ' + HEX22)
        f.write('\nPrivatekey Uncompressed: ' + wifu22)
        f.write('\nPrivatekey compressed: ' + wifc22)
        f.write('\nPublic Address 1 Compressed: ' + caddr22)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr22)
        f.write('\nPublic Address 3 P2SH: ' + p2sh22)
        f.write('\nPublic Address bc1 BECH32: ' + bech3222)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr23 in add or caddr23 in add or p2sh23 in add or bech3223 in add:
        print('\nMatch Found 23% ')
        print('\nPrivatekey (dec): ', seed23,'\nPrivatekey (hex): ', HEX23, '\nPrivatekey Uncompressed: ', wifu23, '\nPrivatekey compressed: ', wifc23, '\nPublic Address 1 Uncompressed: ', uaddr23, '\nPublic Address 1 Compressed: ', caddr23, '\nPublic Address 3 P2SH: ', p2sh23, '\nPublic Address bc1 BECH32: ', bech3223)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed23)
        f.write('\nPrivatekey (hex): ' + HEX23)
        f.write('\nPrivatekey Uncompressed: ' + wifu23)
        f.write('\nPrivatekey compressed: ' + wifc23)
        f.write('\nPublic Address 1 Compressed: ' + caddr23)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr23)
        f.write('\nPublic Address 3 P2SH: ' + p2sh23)
        f.write('\nPublic Address bc1 BECH32: ' + bech3223)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr24 in add or caddr24 in add or p2sh24 in add or bech3224 in add:
        print('\nMatch Found 24% ')
        print('\nPrivatekey (dec): ', seed24,'\nPrivatekey (hex): ', HEX24, '\nPrivatekey Uncompressed: ', wifu24, '\nPrivatekey compressed: ', wifc24, '\nPublic Address 1 Uncompressed: ', uaddr24, '\nPublic Address 1 Compressed: ', caddr24, '\nPublic Address 3 P2SH: ', p2sh24, '\nPublic Address bc1 BECH32: ', bech3224)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed24)
        f.write('\nPrivatekey (hex): ' + HEX24)
        f.write('\nPrivatekey Uncompressed: ' + wifu24)
        f.write('\nPrivatekey compressed: ' + wifc24)
        f.write('\nPublic Address 1 Compressed: ' + caddr24)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr24)
        f.write('\nPublic Address 3 P2SH: ' + p2sh24)
        f.write('\nPublic Address bc1 BECH32: ' + bech3224)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr25 in add or caddr25 in add or p2sh25 in add or bech3225 in add:
        print('\nMatch Found 25% ')
        print('\nPrivatekey (dec): ', seed25,'\nPrivatekey (hex): ', HEX25, '\nPrivatekey Uncompressed: ', wifu25, '\nPrivatekey compressed: ', wifc25, '\nPublic Address 1 Uncompressed: ', uaddr25, '\nPublic Address 1 Compressed: ', caddr25, '\nPublic Address 3 P2SH: ', p2sh25, '\nPublic Address bc1 BECH32: ', bech3225)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed25)
        f.write('\nPrivatekey (hex): ' + HEX25)
        f.write('\nPrivatekey Uncompressed: ' + wifu25)
        f.write('\nPrivatekey compressed: ' + wifc25)
        f.write('\nPublic Address 1 Compressed: ' + caddr25)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr25)
        f.write('\nPublic Address 3 P2SH: ' + p2sh25)
        f.write('\nPublic Address bc1 BECH32: ' + bech3225)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr26 in add or caddr26 in add or p2sh26 in add or bech3226 in add:
        print('\nMatch Found 26% ')
        print('\nPrivatekey (dec): ', seed26,'\nPrivatekey (hex): ', HEX26, '\nPrivatekey Uncompressed: ', wifu26, '\nPrivatekey compressed: ', wifc26, '\nPublic Address 1 Uncompressed: ', uaddr26, '\nPublic Address 1 Compressed: ', caddr26, '\nPublic Address 3 P2SH: ', p2sh26, '\nPublic Address bc1 BECH32: ', bech3226)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed26)
        f.write('\nPrivatekey (hex): ' + HEX26)
        f.write('\nPrivatekey Uncompressed: ' + wifu26)
        f.write('\nPrivatekey compressed: ' + wifc26)
        f.write('\nPublic Address 1 Compressed: ' + caddr26)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr26)
        f.write('\nPublic Address 3 P2SH: ' + p2sh26)
        f.write('\nPublic Address bc1 BECH32: ' + bech3226)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr27 in add or caddr27 in add or p2sh27 in add or bech3227 in add:
        print('\nMatch Found 27% ')
        print('\nPrivatekey (dec): ', seed27,'\nPrivatekey (hex): ', HEX27, '\nPrivatekey Uncompressed: ', wifu27, '\nPrivatekey compressed: ', wifc27, '\nPublic Address 1 Uncompressed: ', uaddr27, '\nPublic Address 1 Compressed: ', caddr27, '\nPublic Address 3 P2SH: ', p2sh27, '\nPublic Address bc1 BECH32: ', bech3227)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed27)
        f.write('\nPrivatekey (hex): ' + HEX27)
        f.write('\nPrivatekey Uncompressed: ' + wifu27)
        f.write('\nPrivatekey compressed: ' + wifc27)
        f.write('\nPublic Address 1 Compressed: ' + caddr27)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr27)
        f.write('\nPublic Address 3 P2SH: ' + p2sh27)
        f.write('\nPublic Address bc1 BECH32: ' + bech3227)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr28 in add or caddr28 in add or p2sh28 in add or bech3228 in add:
        print('\nMatch Found 28% ')
        print('\nPrivatekey (dec): ', seed28,'\nPrivatekey (hex): ', HEX28, '\nPrivatekey Uncompressed: ', wifu28, '\nPrivatekey compressed: ', wifc28, '\nPublic Address 1 Uncompressed: ', uaddr28, '\nPublic Address 1 Compressed: ', caddr28, '\nPublic Address 3 P2SH: ', p2sh28, '\nPublic Address bc1 BECH32: ', bech3228)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed28)
        f.write('\nPrivatekey (hex): ' + HEX28)
        f.write('\nPrivatekey Uncompressed: ' + wifu28)
        f.write('\nPrivatekey compressed: ' + wifc28)
        f.write('\nPublic Address 1 Compressed: ' + caddr28)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr28)
        f.write('\nPublic Address 3 P2SH: ' + p2sh28)
        f.write('\nPublic Address bc1 BECH32: ' + bech3228)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr29 in add or caddr29 in add or p2sh29 in add or bech3229 in add:
        print('\nMatch Found 29% ')
        print('\nPrivatekey (dec): ', seed29,'\nPrivatekey (hex): ', HEX29, '\nPrivatekey Uncompressed: ', wifu29, '\nPrivatekey compressed: ', wifc29, '\nPublic Address 1 Uncompressed: ', uaddr29, '\nPublic Address 1 Compressed: ', caddr29, '\nPublic Address 3 P2SH: ', p2sh29, '\nPublic Address bc1 BECH32: ', bech3229)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed29)
        f.write('\nPrivatekey (hex): ' + HEX29)
        f.write('\nPrivatekey Uncompressed: ' + wifu29)
        f.write('\nPrivatekey compressed: ' + wifc29)
        f.write('\nPublic Address 1 Compressed: ' + caddr29)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr29)
        f.write('\nPublic Address 3 P2SH: ' + p2sh29)
        f.write('\nPublic Address bc1 BECH32: ' + bech3229)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr30 in add or caddr30 in add or p2sh30 in add or bech3230 in add:
        print('\nMatch Found 30% ')
        print('\nPrivatekey (dec): ', seed30,'\nPrivatekey (hex): ', HEX30, '\nPrivatekey Uncompressed: ', wifu30, '\nPrivatekey compressed: ', wifc30, '\nPublic Address 1 Uncompressed: ', uaddr30, '\nPublic Address 1 Compressed: ', caddr30, '\nPublic Address 3 P2SH: ', p2sh30, '\nPublic Address bc1 BECH32: ', bech3230)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed30)
        f.write('\nPrivatekey (hex): ' + HEX30)
        f.write('\nPrivatekey Uncompressed: ' + wifu30)
        f.write('\nPrivatekey compressed: ' + wifc30)
        f.write('\nPublic Address 1 Compressed: ' + caddr30)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr30)
        f.write('\nPublic Address 3 P2SH: ' + p2sh30)
        f.write('\nPublic Address bc1 BECH32: ' + bech3230)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr31 in add or caddr31 in add or p2sh31 in add or bech3231 in add:
        print('\nMatch Found 31% ')
        print('\nPrivatekey (dec): ', seed31,'\nPrivatekey (hex): ', HEX31, '\nPrivatekey Uncompressed: ', wifu31, '\nPrivatekey compressed: ', wifc31, '\nPublic Address 1 Uncompressed: ', uaddr31, '\nPublic Address 1 Compressed: ', caddr31, '\nPublic Address 3 P2SH: ', p2sh31, '\nPublic Address bc1 BECH32: ', bech3231)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed31)
        f.write('\nPrivatekey (hex): ' + HEX31)
        f.write('\nPrivatekey Uncompressed: ' + wifu31)
        f.write('\nPrivatekey compressed: ' + wifc31)
        f.write('\nPublic Address 1 Compressed: ' + caddr31)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr31)
        f.write('\nPublic Address 3 P2SH: ' + p2sh31)
        f.write('\nPublic Address bc1 BECH32: ' + bech3231)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr32 in add or caddr32 in add or p2sh32 in add or bech3232 in add:
        print('\nMatch Found 32% ')
        print('\nPrivatekey (dec): ', seed32,'\nPrivatekey (hex): ', HEX32, '\nPrivatekey Uncompressed: ', wifu32, '\nPrivatekey compressed: ', wifc32, '\nPublic Address 1 Uncompressed: ', uaddr32, '\nPublic Address 1 Compressed: ', caddr32, '\nPublic Address 3 P2SH: ', p2sh32, '\nPublic Address bc1 BECH32: ', bech3232)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed32)
        f.write('\nPrivatekey (hex): ' + HEX32)
        f.write('\nPrivatekey Uncompressed: ' + wifu32)
        f.write('\nPrivatekey compressed: ' + wifc32)
        f.write('\nPublic Address 1 Compressed: ' + caddr32)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr32)
        f.write('\nPublic Address 3 P2SH: ' + p2sh32)
        f.write('\nPublic Address bc1 BECH32: ' + bech3232)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr33 in add or caddr33 in add or p2sh33 in add or bech3233 in add:
        print('\nMatch Found 33% ')
        print('\nPrivatekey (dec): ', seed33,'\nPrivatekey (hex): ', HEX33, '\nPrivatekey Uncompressed: ', wifu33, '\nPrivatekey compressed: ', wifc33, '\nPublic Address 1 Uncompressed: ', uaddr33, '\nPublic Address 1 Compressed: ', caddr33, '\nPublic Address 3 P2SH: ', p2sh33, '\nPublic Address bc1 BECH32: ', bech3233)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed33)
        f.write('\nPrivatekey (hex): ' + HEX33)
        f.write('\nPrivatekey Uncompressed: ' + wifu33)
        f.write('\nPrivatekey compressed: ' + wifc33)
        f.write('\nPublic Address 1 Compressed: ' + caddr33)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr33)
        f.write('\nPublic Address 3 P2SH: ' + p2sh33)
        f.write('\nPublic Address bc1 BECH32: ' + bech3233)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr34 in add or caddr34 in add or p2sh34 in add or bech3234 in add:
        print('\nMatch Found 34% ')
        print('\nPrivatekey (dec): ', seed34,'\nPrivatekey (hex): ', HEX34, '\nPrivatekey Uncompressed: ', wifu34, '\nPrivatekey compressed: ', wifc34, '\nPublic Address 1 Uncompressed: ', uaddr34, '\nPublic Address 1 Compressed: ', caddr34, '\nPublic Address 3 P2SH: ', p2sh34, '\nPublic Address bc1 BECH32: ', bech3234)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed34)
        f.write('\nPrivatekey (hex): ' + HEX34)
        f.write('\nPrivatekey Uncompressed: ' + wifu34)
        f.write('\nPrivatekey compressed: ' + wifc34)
        f.write('\nPublic Address 1 Compressed: ' + caddr34)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr34)
        f.write('\nPublic Address 3 P2SH: ' + p2sh34)
        f.write('\nPublic Address bc1 BECH32: ' + bech3234)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr35 in add or caddr35 in add or p2sh35 in add or bech3235 in add:
        print('\nMatch Found 35% ')
        print('\nPrivatekey (dec): ', seed35,'\nPrivatekey (hex): ', HEX35, '\nPrivatekey Uncompressed: ', wifu35, '\nPrivatekey compressed: ', wifc35, '\nPublic Address 1 Uncompressed: ', uaddr35, '\nPublic Address 1 Compressed: ', caddr35, '\nPublic Address 3 P2SH: ', p2sh35, '\nPublic Address bc1 BECH32: ', bech3235)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed35)
        f.write('\nPrivatekey (hex): ' + HEX35)
        f.write('\nPrivatekey Uncompressed: ' + wifu35)
        f.write('\nPrivatekey compressed: ' + wifc35)
        f.write('\nPublic Address 1 Compressed: ' + caddr35)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr35)
        f.write('\nPublic Address 3 P2SH: ' + p2sh35)
        f.write('\nPublic Address bc1 BECH32: ' + bech3235)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr36 in add or caddr36 in add or p2sh36 in add or bech3236 in add:
        print('\nMatch Found 36% ')
        print('\nPrivatekey (dec): ', seed36,'\nPrivatekey (hex): ', HEX36, '\nPrivatekey Uncompressed: ', wifu36, '\nPrivatekey compressed: ', wifc36, '\nPublic Address 1 Uncompressed: ', uaddr36, '\nPublic Address 1 Compressed: ', caddr36, '\nPublic Address 3 P2SH: ', p2sh36, '\nPublic Address bc1 BECH32: ', bech3236)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed36)
        f.write('\nPrivatekey (hex): ' + HEX36)
        f.write('\nPrivatekey Uncompressed: ' + wifu36)
        f.write('\nPrivatekey compressed: ' + wifc36)
        f.write('\nPublic Address 1 Compressed: ' + caddr36)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr36)
        f.write('\nPublic Address 3 P2SH: ' + p2sh36)
        f.write('\nPublic Address bc1 BECH32: ' + bech3236)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr37 in add or caddr37 in add or p2sh37 in add or bech3237 in add:
        print('\nMatch Found 37% ')
        print('\nPrivatekey (dec): ', seed37,'\nPrivatekey (hex): ', HEX37, '\nPrivatekey Uncompressed: ', wifu37, '\nPrivatekey compressed: ', wifc37, '\nPublic Address 1 Uncompressed: ', uaddr37, '\nPublic Address 1 Compressed: ', caddr37, '\nPublic Address 3 P2SH: ', p2sh37, '\nPublic Address bc1 BECH32: ', bech3237)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed37)
        f.write('\nPrivatekey (hex): ' + HEX37)
        f.write('\nPrivatekey Uncompressed: ' + wifu37)
        f.write('\nPrivatekey compressed: ' + wifc37)
        f.write('\nPublic Address 1 Compressed: ' + caddr37)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr37)
        f.write('\nPublic Address 3 P2SH: ' + p2sh37)
        f.write('\nPublic Address bc1 BECH32: ' + bech3237)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr38 in add or caddr38 in add or p2sh38 in add or bech3238 in add:
        print('\nMatch Found 38% ')
        print('\nPrivatekey (dec): ', seed38,'\nPrivatekey (hex): ', HEX38, '\nPrivatekey Uncompressed: ', wifu38, '\nPrivatekey compressed: ', wifc38, '\nPublic Address 1 Uncompressed: ', uaddr38, '\nPublic Address 1 Compressed: ', caddr38, '\nPublic Address 3 P2SH: ', p2sh38, '\nPublic Address bc1 BECH32: ', bech3238)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed38)
        f.write('\nPrivatekey (hex): ' + HEX38)
        f.write('\nPrivatekey Uncompressed: ' + wifu38)
        f.write('\nPrivatekey compressed: ' + wifc38)
        f.write('\nPublic Address 1 Compressed: ' + caddr38)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr38)
        f.write('\nPublic Address 3 P2SH: ' + p2sh38)
        f.write('\nPublic Address bc1 BECH32: ' + bech3238)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr39 in add or caddr39 in add or p2sh39 in add or bech3239 in add:
        print('\nMatch Found 39% ')
        print('\nPrivatekey (dec): ', seed39,'\nPrivatekey (hex): ', HEX39, '\nPrivatekey Uncompressed: ', wifu39, '\nPrivatekey compressed: ', wifc39, '\nPublic Address 1 Uncompressed: ', uaddr39, '\nPublic Address 1 Compressed: ', caddr39, '\nPublic Address 3 P2SH: ', p2sh39, '\nPublic Address bc1 BECH32: ', bech3239)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed39)
        f.write('\nPrivatekey (hex): ' + HEX39)
        f.write('\nPrivatekey Uncompressed: ' + wifu39)
        f.write('\nPrivatekey compressed: ' + wifc39)
        f.write('\nPublic Address 1 Compressed: ' + caddr39)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr39)
        f.write('\nPublic Address 3 P2SH: ' + p2sh39)
        f.write('\nPublic Address bc1 BECH32: ' + bech3239)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr40 in add or caddr40 in add or p2sh40 in add or bech3240 in add:
        print('\nMatch Found 40% ')
        print('\nPrivatekey (dec): ', seed40,'\nPrivatekey (hex): ', HEX40, '\nPrivatekey Uncompressed: ', wifu40, '\nPrivatekey compressed: ', wifc40, '\nPublic Address 1 Uncompressed: ', uaddr40, '\nPublic Address 1 Compressed: ', caddr40, '\nPublic Address 3 P2SH: ', p2sh40, '\nPublic Address bc1 BECH32: ', bech3240)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed40)
        f.write('\nPrivatekey (hex): ' + HEX40)
        f.write('\nPrivatekey Uncompressed: ' + wifu40)
        f.write('\nPrivatekey compressed: ' + wifc40)
        f.write('\nPublic Address 1 Compressed: ' + caddr40)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr40)
        f.write('\nPublic Address 3 P2SH: ' + p2sh40)
        f.write('\nPublic Address bc1 BECH32: ' + bech3240)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr41 in add or caddr41 in add or p2sh41 in add or bech3241 in add:
        print('\nMatch Found 41% ')
        print('\nPrivatekey (dec): ', seed41,'\nPrivatekey (hex): ', HEX41, '\nPrivatekey Uncompressed: ', wifu41, '\nPrivatekey compressed: ', wifc41, '\nPublic Address 1 Uncompressed: ', uaddr41, '\nPublic Address 1 Compressed: ', caddr41, '\nPublic Address 3 P2SH: ', p2sh41, '\nPublic Address bc1 BECH32: ', bech3241)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed41)
        f.write('\nPrivatekey (hex): ' + HEX41)
        f.write('\nPrivatekey Uncompressed: ' + wifu41)
        f.write('\nPrivatekey compressed: ' + wifc41)
        f.write('\nPublic Address 1 Compressed: ' + caddr41)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr41)
        f.write('\nPublic Address 3 P2SH: ' + p2sh41)
        f.write('\nPublic Address bc1 BECH32: ' + bech3241)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr42 in add or caddr42 in add or p2sh42 in add or bech3242 in add:
        print('\nMatch Found 42% ')
        print('\nPrivatekey (dec): ', seed42,'\nPrivatekey (hex): ', HEX42, '\nPrivatekey Uncompressed: ', wifu42, '\nPrivatekey compressed: ', wifc42, '\nPublic Address 1 Uncompressed: ', uaddr42, '\nPublic Address 1 Compressed: ', caddr42, '\nPublic Address 3 P2SH: ', p2sh42, '\nPublic Address bc1 BECH32: ', bech3242)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed42)
        f.write('\nPrivatekey (hex): ' + HEX42)
        f.write('\nPrivatekey Uncompressed: ' + wifu42)
        f.write('\nPrivatekey compressed: ' + wifc42)
        f.write('\nPublic Address 1 Compressed: ' + caddr42)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr42)
        f.write('\nPublic Address 3 P2SH: ' + p2sh42)
        f.write('\nPublic Address bc1 BECH32: ' + bech3242)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr43 in add or caddr43 in add or p2sh43 in add or bech3243 in add:
        print('\nMatch Found 43% ')
        print('\nPrivatekey (dec): ', seed43,'\nPrivatekey (hex): ', HEX43, '\nPrivatekey Uncompressed: ', wifu43, '\nPrivatekey compressed: ', wifc43, '\nPublic Address 1 Uncompressed: ', uaddr43, '\nPublic Address 1 Compressed: ', caddr43, '\nPublic Address 3 P2SH: ', p2sh43, '\nPublic Address bc1 BECH32: ', bech3243)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed43)
        f.write('\nPrivatekey (hex): ' + HEX43)
        f.write('\nPrivatekey Uncompressed: ' + wifu43)
        f.write('\nPrivatekey compressed: ' + wifc43)
        f.write('\nPublic Address 1 Compressed: ' + caddr43)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr43)
        f.write('\nPublic Address 3 P2SH: ' + p2sh43)
        f.write('\nPublic Address bc1 BECH32: ' + bech3243)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr44 in add or caddr44 in add or p2sh44 in add or bech3244 in add:
        print('\nMatch Found 44% ')
        print('\nPrivatekey (dec): ', seed44,'\nPrivatekey (hex): ', HEX44, '\nPrivatekey Uncompressed: ', wifu44, '\nPrivatekey compressed: ', wifc44, '\nPublic Address 1 Uncompressed: ', uaddr44, '\nPublic Address 1 Compressed: ', caddr44, '\nPublic Address 3 P2SH: ', p2sh44, '\nPublic Address bc1 BECH32: ', bech3244)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed44)
        f.write('\nPrivatekey (hex): ' + HEX44)
        f.write('\nPrivatekey Uncompressed: ' + wifu44)
        f.write('\nPrivatekey compressed: ' + wifc44)
        f.write('\nPublic Address 1 Compressed: ' + caddr44)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr44)
        f.write('\nPublic Address 3 P2SH: ' + p2sh44)
        f.write('\nPublic Address bc1 BECH32: ' + bech3244)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr45 in add or caddr45 in add or p2sh45 in add or bech3245 in add:
        print('\nMatch Found 45% ')
        print('\nPrivatekey (dec): ', seed45,'\nPrivatekey (hex): ', HEX45, '\nPrivatekey Uncompressed: ', wifu45, '\nPrivatekey compressed: ', wifc45, '\nPublic Address 1 Uncompressed: ', uaddr45, '\nPublic Address 1 Compressed: ', caddr45, '\nPublic Address 3 P2SH: ', p2sh45, '\nPublic Address bc1 BECH32: ', bech3245)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed45)
        f.write('\nPrivatekey (hex): ' + HEX45)
        f.write('\nPrivatekey Uncompressed: ' + wifu45)
        f.write('\nPrivatekey compressed: ' + wifc45)
        f.write('\nPublic Address 1 Compressed: ' + caddr45)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr45)
        f.write('\nPublic Address 3 P2SH: ' + p2sh45)
        f.write('\nPublic Address bc1 BECH32: ' + bech3245)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr46 in add or caddr46 in add or p2sh46 in add or bech3246 in add:
        print('\nMatch Found 46% ')
        print('\nPrivatekey (dec): ', seed46,'\nPrivatekey (hex): ', HEX46, '\nPrivatekey Uncompressed: ', wifu46, '\nPrivatekey compressed: ', wifc46, '\nPublic Address 1 Uncompressed: ', uaddr46, '\nPublic Address 1 Compressed: ', caddr46, '\nPublic Address 3 P2SH: ', p2sh46, '\nPublic Address bc1 BECH32: ', bech3246)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed46)
        f.write('\nPrivatekey (hex): ' + HEX46)
        f.write('\nPrivatekey Uncompressed: ' + wifu46)
        f.write('\nPrivatekey compressed: ' + wifc46)
        f.write('\nPublic Address 1 Compressed: ' + caddr46)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr46)
        f.write('\nPublic Address 3 P2SH: ' + p2sh46)
        f.write('\nPublic Address bc1 BECH32: ' + bech3246)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr47 in add or caddr47 in add or p2sh47 in add or bech3247 in add:
        print('\nMatch Found 47% ')
        print('\nPrivatekey (dec): ', seed47,'\nPrivatekey (hex): ', HEX47, '\nPrivatekey Uncompressed: ', wifu47, '\nPrivatekey compressed: ', wifc47, '\nPublic Address 1 Uncompressed: ', uaddr47, '\nPublic Address 1 Compressed: ', caddr47, '\nPublic Address 3 P2SH: ', p2sh47, '\nPublic Address bc1 BECH32: ', bech3247)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed47)
        f.write('\nPrivatekey (hex): ' + HEX47)
        f.write('\nPrivatekey Uncompressed: ' + wifu47)
        f.write('\nPrivatekey compressed: ' + wifc47)
        f.write('\nPublic Address 1 Compressed: ' + caddr47)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr47)
        f.write('\nPublic Address 3 P2SH: ' + p2sh47)
        f.write('\nPublic Address bc1 BECH32: ' + bech3247)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr48 in add or caddr48 in add or p2sh48 in add or bech3248 in add:
        print('\nMatch Found 48% ')
        print('\nPrivatekey (dec): ', seed48,'\nPrivatekey (hex): ', HEX48, '\nPrivatekey Uncompressed: ', wifu48, '\nPrivatekey compressed: ', wifc48, '\nPublic Address 1 Uncompressed: ', uaddr48, '\nPublic Address 1 Compressed: ', caddr48, '\nPublic Address 3 P2SH: ', p2sh48, '\nPublic Address bc1 BECH32: ', bech3248)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed48)
        f.write('\nPrivatekey (hex): ' + HEX48)
        f.write('\nPrivatekey Uncompressed: ' + wifu48)
        f.write('\nPrivatekey compressed: ' + wifc48)
        f.write('\nPublic Address 1 Compressed: ' + caddr48)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr48)
        f.write('\nPublic Address 3 P2SH: ' + p2sh48)
        f.write('\nPublic Address bc1 BECH32: ' + bech3248)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr49 in add or caddr49 in add or p2sh49 in add or bech3249 in add:
        print('\nMatch Found 49% ')
        print('\nPrivatekey (dec): ', seed49,'\nPrivatekey (hex): ', HEX49, '\nPrivatekey Uncompressed: ', wifu49, '\nPrivatekey compressed: ', wifc49, '\nPublic Address 1 Uncompressed: ', uaddr49, '\nPublic Address 1 Compressed: ', caddr49, '\nPublic Address 3 P2SH: ', p2sh49, '\nPublic Address bc1 BECH32: ', bech3249)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed49)
        f.write('\nPrivatekey (hex): ' + HEX49)
        f.write('\nPrivatekey Uncompressed: ' + wifu49)
        f.write('\nPrivatekey compressed: ' + wifc49)
        f.write('\nPublic Address 1 Compressed: ' + caddr49)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr49)
        f.write('\nPublic Address 3 P2SH: ' + p2sh49)
        f.write('\nPublic Address bc1 BECH32: ' + bech3249)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr50 in add or caddr50 in add or p2sh50 in add or bech3250 in add:
        print('\nMatch Found 50% ')
        print('\nPrivatekey (dec): ', seed50,'\nPrivatekey (hex): ', HEX50, '\nPrivatekey Uncompressed: ', wifu50, '\nPrivatekey compressed: ', wifc50, '\nPublic Address 1 Uncompressed: ', uaddr50, '\nPublic Address 1 Compressed: ', caddr50, '\nPublic Address 3 P2SH: ', p2sh50, '\nPublic Address bc1 BECH32: ', bech3250)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed50)
        f.write('\nPrivatekey (hex): ' + HEX50)
        f.write('\nPrivatekey Uncompressed: ' + wifu50)
        f.write('\nPrivatekey compressed: ' + wifc50)
        f.write('\nPublic Address 1 Compressed: ' + caddr50)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr50)
        f.write('\nPublic Address 3 P2SH: ' + p2sh50)
        f.write('\nPublic Address bc1 BECH32: ' + bech3250)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr51 in add or caddr51 in add or p2sh51 in add or bech3251 in add:
        print('\nMatch Found 51% ')
        print('\nPrivatekey (dec): ', seed51,'\nPrivatekey (hex): ', HEX51, '\nPrivatekey Uncompressed: ', wifu51, '\nPrivatekey compressed: ', wifc51, '\nPublic Address 1 Uncompressed: ', uaddr51, '\nPublic Address 1 Compressed: ', caddr51, '\nPublic Address 3 P2SH: ', p2sh51, '\nPublic Address bc1 BECH32: ', bech3251)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed51)
        f.write('\nPrivatekey (hex): ' + HEX51)
        f.write('\nPrivatekey Uncompressed: ' + wifu51)
        f.write('\nPrivatekey compressed: ' + wifc51)
        f.write('\nPublic Address 1 Compressed: ' + caddr51)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr51)
        f.write('\nPublic Address 3 P2SH: ' + p2sh51)
        f.write('\nPublic Address bc1 BECH32: ' + bech3251)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr52 in add or caddr52 in add or p2sh52 in add or bech3252 in add:
        print('\nMatch Found 52% ')
        print('\nPrivatekey (dec): ', seed52,'\nPrivatekey (hex): ', HEX52, '\nPrivatekey Uncompressed: ', wifu52, '\nPrivatekey compressed: ', wifc52, '\nPublic Address 1 Uncompressed: ', uaddr52, '\nPublic Address 1 Compressed: ', caddr52, '\nPublic Address 3 P2SH: ', p2sh52, '\nPublic Address bc1 BECH32: ', bech3252)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed52)
        f.write('\nPrivatekey (hex): ' + HEX52)
        f.write('\nPrivatekey Uncompressed: ' + wifu52)
        f.write('\nPrivatekey compressed: ' + wifc52)
        f.write('\nPublic Address 1 Compressed: ' + caddr52)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr52)
        f.write('\nPublic Address 3 P2SH: ' + p2sh52)
        f.write('\nPublic Address bc1 BECH32: ' + bech3252)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr53 in add or caddr53 in add or p2sh53 in add or bech3253 in add:
        print('\nMatch Found 53% ')
        print('\nPrivatekey (dec): ', seed53,'\nPrivatekey (hex): ', HEX53, '\nPrivatekey Uncompressed: ', wifu53, '\nPrivatekey compressed: ', wifc53, '\nPublic Address 1 Uncompressed: ', uaddr53, '\nPublic Address 1 Compressed: ', caddr53, '\nPublic Address 3 P2SH: ', p2sh53, '\nPublic Address bc1 BECH32: ', bech3253)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed53)
        f.write('\nPrivatekey (hex): ' + HEX53)
        f.write('\nPrivatekey Uncompressed: ' + wifu53)
        f.write('\nPrivatekey compressed: ' + wifc53)
        f.write('\nPublic Address 1 Compressed: ' + caddr53)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr53)
        f.write('\nPublic Address 3 P2SH: ' + p2sh53)
        f.write('\nPublic Address bc1 BECH32: ' + bech3253)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr54 in add or caddr54 in add or p2sh54 in add or bech3254 in add:
        print('\nMatch Found 54% ')
        print('\nPrivatekey (dec): ', seed54,'\nPrivatekey (hex): ', HEX54, '\nPrivatekey Uncompressed: ', wifu54, '\nPrivatekey compressed: ', wifc54, '\nPublic Address 1 Uncompressed: ', uaddr54, '\nPublic Address 1 Compressed: ', caddr54, '\nPublic Address 3 P2SH: ', p2sh54, '\nPublic Address bc1 BECH32: ', bech3254)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed54)
        f.write('\nPrivatekey (hex): ' + HEX54)
        f.write('\nPrivatekey Uncompressed: ' + wifu54)
        f.write('\nPrivatekey compressed: ' + wifc54)
        f.write('\nPublic Address 1 Compressed: ' + caddr54)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr54)
        f.write('\nPublic Address 3 P2SH: ' + p2sh54)
        f.write('\nPublic Address bc1 BECH32: ' + bech3254)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr55 in add or caddr55 in add or p2sh55 in add or bech3255 in add:
        print('\nMatch Found 55% ')
        print('\nPrivatekey (dec): ', seed55,'\nPrivatekey (hex): ', HEX55, '\nPrivatekey Uncompressed: ', wifu55, '\nPrivatekey compressed: ', wifc55, '\nPublic Address 1 Uncompressed: ', uaddr55, '\nPublic Address 1 Compressed: ', caddr55, '\nPublic Address 3 P2SH: ', p2sh55, '\nPublic Address bc1 BECH32: ', bech3255)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed55)
        f.write('\nPrivatekey (hex): ' + HEX55)
        f.write('\nPrivatekey Uncompressed: ' + wifu55)
        f.write('\nPrivatekey compressed: ' + wifc55)
        f.write('\nPublic Address 1 Compressed: ' + caddr55)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr55)
        f.write('\nPublic Address 3 P2SH: ' + p2sh55)
        f.write('\nPublic Address bc1 BECH32: ' + bech3255)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr56 in add or caddr56 in add or p2sh56 in add or bech3256 in add:
        print('\nMatch Found 56% ')
        print('\nPrivatekey (dec): ', seed56,'\nPrivatekey (hex): ', HEX56, '\nPrivatekey Uncompressed: ', wifu56, '\nPrivatekey compressed: ', wifc56, '\nPublic Address 1 Uncompressed: ', uaddr56, '\nPublic Address 1 Compressed: ', caddr56, '\nPublic Address 3 P2SH: ', p2sh56, '\nPublic Address bc1 BECH32: ', bech3256)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed56)
        f.write('\nPrivatekey (hex): ' + HEX56)
        f.write('\nPrivatekey Uncompressed: ' + wifu56)
        f.write('\nPrivatekey compressed: ' + wifc56)
        f.write('\nPublic Address 1 Compressed: ' + caddr56)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr56)
        f.write('\nPublic Address 3 P2SH: ' + p2sh56)
        f.write('\nPublic Address bc1 BECH32: ' + bech3256)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr57 in add or caddr57 in add or p2sh57 in add or bech3257 in add:
        print('\nMatch Found 57% ')
        print('\nPrivatekey (dec): ', seed57,'\nPrivatekey (hex): ', HEX57, '\nPrivatekey Uncompressed: ', wifu57, '\nPrivatekey compressed: ', wifc57, '\nPublic Address 1 Uncompressed: ', uaddr57, '\nPublic Address 1 Compressed: ', caddr57, '\nPublic Address 3 P2SH: ', p2sh57, '\nPublic Address bc1 BECH32: ', bech3257)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed57)
        f.write('\nPrivatekey (hex): ' + HEX57)
        f.write('\nPrivatekey Uncompressed: ' + wifu57)
        f.write('\nPrivatekey compressed: ' + wifc57)
        f.write('\nPublic Address 1 Compressed: ' + caddr57)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr57)
        f.write('\nPublic Address 3 P2SH: ' + p2sh57)
        f.write('\nPublic Address bc1 BECH32: ' + bech3257)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr58 in add or caddr58 in add or p2sh58 in add or bech3258 in add:
        print('\nMatch Found 58% ')
        print('\nPrivatekey (dec): ', seed58,'\nPrivatekey (hex): ', HEX58, '\nPrivatekey Uncompressed: ', wifu58, '\nPrivatekey compressed: ', wifc58, '\nPublic Address 1 Uncompressed: ', uaddr58, '\nPublic Address 1 Compressed: ', caddr58, '\nPublic Address 3 P2SH: ', p2sh58, '\nPublic Address bc1 BECH32: ', bech3258)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed58)
        f.write('\nPrivatekey (hex): ' + HEX58)
        f.write('\nPrivatekey Uncompressed: ' + wifu58)
        f.write('\nPrivatekey compressed: ' + wifc58)
        f.write('\nPublic Address 1 Compressed: ' + caddr58)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr58)
        f.write('\nPublic Address 3 P2SH: ' + p2sh58)
        f.write('\nPublic Address bc1 BECH32: ' + bech3258)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr59 in add or caddr59 in add or p2sh59 in add or bech3259 in add:
        print('\nMatch Found 59% ')
        print('\nPrivatekey (dec): ', seed59,'\nPrivatekey (hex): ', HEX59, '\nPrivatekey Uncompressed: ', wifu59, '\nPrivatekey compressed: ', wifc59, '\nPublic Address 1 Uncompressed: ', uaddr59, '\nPublic Address 1 Compressed: ', caddr59, '\nPublic Address 3 P2SH: ', p2sh59, '\nPublic Address bc1 BECH32: ', bech3259)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed59)
        f.write('\nPrivatekey (hex): ' + HEX59)
        f.write('\nPrivatekey Uncompressed: ' + wifu59)
        f.write('\nPrivatekey compressed: ' + wifc59)
        f.write('\nPublic Address 1 Compressed: ' + caddr59)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr59)
        f.write('\nPublic Address 3 P2SH: ' + p2sh59)
        f.write('\nPublic Address bc1 BECH32: ' + bech3259)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr60 in add or caddr60 in add or p2sh60 in add or bech3260 in add:
        print('\nMatch Found 60% ')
        print('\nPrivatekey (dec): ', seed60,'\nPrivatekey (hex): ', HEX60, '\nPrivatekey Uncompressed: ', wifu60, '\nPrivatekey compressed: ', wifc60, '\nPublic Address 1 Uncompressed: ', uaddr60, '\nPublic Address 1 Compressed: ', caddr60, '\nPublic Address 3 P2SH: ', p2sh60, '\nPublic Address bc1 BECH32: ', bech3260)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed60)
        f.write('\nPrivatekey (hex): ' + HEX60)
        f.write('\nPrivatekey Uncompressed: ' + wifu60)
        f.write('\nPrivatekey compressed: ' + wifc60)
        f.write('\nPublic Address 1 Compressed: ' + caddr60)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr60)
        f.write('\nPublic Address 3 P2SH: ' + p2sh60)
        f.write('\nPublic Address bc1 BECH32: ' + bech3260)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr61 in add or caddr61 in add or p2sh61 in add or bech3261 in add:
        print('\nMatch Found 61% ')
        print('\nPrivatekey (dec): ', seed61,'\nPrivatekey (hex): ', HEX61, '\nPrivatekey Uncompressed: ', wifu61, '\nPrivatekey compressed: ', wifc61, '\nPublic Address 1 Uncompressed: ', uaddr61, '\nPublic Address 1 Compressed: ', caddr61, '\nPublic Address 3 P2SH: ', p2sh61, '\nPublic Address bc1 BECH32: ', bech3261)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed61)
        f.write('\nPrivatekey (hex): ' + HEX61)
        f.write('\nPrivatekey Uncompressed: ' + wifu61)
        f.write('\nPrivatekey compressed: ' + wifc61)
        f.write('\nPublic Address 1 Compressed: ' + caddr61)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr61)
        f.write('\nPublic Address 3 P2SH: ' + p2sh61)
        f.write('\nPublic Address bc1 BECH32: ' + bech3261)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr62 in add or caddr62 in add or p2sh62 in add or bech3262 in add:
        print('\nMatch Found 62% ')
        print('\nPrivatekey (dec): ', seed62,'\nPrivatekey (hex): ', HEX62, '\nPrivatekey Uncompressed: ', wifu62, '\nPrivatekey compressed: ', wifc62, '\nPublic Address 1 Uncompressed: ', uaddr62, '\nPublic Address 1 Compressed: ', caddr62, '\nPublic Address 3 P2SH: ', p2sh62, '\nPublic Address bc1 BECH32: ', bech3262)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed62)
        f.write('\nPrivatekey (hex): ' + HEX62)
        f.write('\nPrivatekey Uncompressed: ' + wifu62)
        f.write('\nPrivatekey compressed: ' + wifc62)
        f.write('\nPublic Address 1 Compressed: ' + caddr62)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr62)
        f.write('\nPublic Address 3 P2SH: ' + p2sh62)
        f.write('\nPublic Address bc1 BECH32: ' + bech3262)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr63 in add or caddr63 in add or p2sh63 in add or bech3263 in add:
        print('\nMatch Found 63% ')
        print('\nPrivatekey (dec): ', seed63,'\nPrivatekey (hex): ', HEX63, '\nPrivatekey Uncompressed: ', wifu63, '\nPrivatekey compressed: ', wifc63, '\nPublic Address 1 Uncompressed: ', uaddr63, '\nPublic Address 1 Compressed: ', caddr63, '\nPublic Address 3 P2SH: ', p2sh63, '\nPublic Address bc1 BECH32: ', bech3263)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed63)
        f.write('\nPrivatekey (hex): ' + HEX63)
        f.write('\nPrivatekey Uncompressed: ' + wifu63)
        f.write('\nPrivatekey compressed: ' + wifc63)
        f.write('\nPublic Address 1 Compressed: ' + caddr63)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr63)
        f.write('\nPublic Address 3 P2SH: ' + p2sh63)
        f.write('\nPublic Address bc1 BECH32: ' + bech3263)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr64 in add or caddr64 in add or p2sh64 in add or bech3264 in add:
        print('\nMatch Found 64% ')
        print('\nPrivatekey (dec): ', seed64,'\nPrivatekey (hex): ', HEX64, '\nPrivatekey Uncompressed: ', wifu64, '\nPrivatekey compressed: ', wifc64, '\nPublic Address 1 Uncompressed: ', uaddr64, '\nPublic Address 1 Compressed: ', caddr64, '\nPublic Address 3 P2SH: ', p2sh64, '\nPublic Address bc1 BECH32: ', bech3264)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed64)
        f.write('\nPrivatekey (hex): ' + HEX64)
        f.write('\nPrivatekey Uncompressed: ' + wifu64)
        f.write('\nPrivatekey compressed: ' + wifc64)
        f.write('\nPublic Address 1 Compressed: ' + caddr64)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr64)
        f.write('\nPublic Address 3 P2SH: ' + p2sh64)
        f.write('\nPublic Address bc1 BECH32: ' + bech3264)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr65 in add or caddr65 in add or p2sh65 in add or bech3265 in add:
        print('\nMatch Found 65% ')
        print('\nPrivatekey (dec): ', seed65,'\nPrivatekey (hex): ', HEX65, '\nPrivatekey Uncompressed: ', wifu65, '\nPrivatekey compressed: ', wifc65, '\nPublic Address 1 Uncompressed: ', uaddr65, '\nPublic Address 1 Compressed: ', caddr65, '\nPublic Address 3 P2SH: ', p2sh65, '\nPublic Address bc1 BECH32: ', bech3265)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed65)
        f.write('\nPrivatekey (hex): ' + HEX65)
        f.write('\nPrivatekey Uncompressed: ' + wifu65)
        f.write('\nPrivatekey compressed: ' + wifc65)
        f.write('\nPublic Address 1 Compressed: ' + caddr65)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr65)
        f.write('\nPublic Address 3 P2SH: ' + p2sh65)
        f.write('\nPublic Address bc1 BECH32: ' + bech3265)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr66 in add or caddr66 in add or p2sh66 in add or bech3266 in add:
        print('\nMatch Found 66% ')
        print('\nPrivatekey (dec): ', seed66,'\nPrivatekey (hex): ', HEX66, '\nPrivatekey Uncompressed: ', wifu66, '\nPrivatekey compressed: ', wifc66, '\nPublic Address 1 Uncompressed: ', uaddr66, '\nPublic Address 1 Compressed: ', caddr66, '\nPublic Address 3 P2SH: ', p2sh66, '\nPublic Address bc1 BECH32: ', bech3266)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed66)
        f.write('\nPrivatekey (hex): ' + HEX66)
        f.write('\nPrivatekey Uncompressed: ' + wifu66)
        f.write('\nPrivatekey compressed: ' + wifc66)
        f.write('\nPublic Address 1 Compressed: ' + caddr66)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr66)
        f.write('\nPublic Address 3 P2SH: ' + p2sh66)
        f.write('\nPublic Address bc1 BECH32: ' + bech3266)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr67 in add or caddr67 in add or p2sh67 in add or bech3267 in add:
        print('\nMatch Found 67% ')
        print('\nPrivatekey (dec): ', seed67,'\nPrivatekey (hex): ', HEX67, '\nPrivatekey Uncompressed: ', wifu67, '\nPrivatekey compressed: ', wifc67, '\nPublic Address 1 Uncompressed: ', uaddr67, '\nPublic Address 1 Compressed: ', caddr67, '\nPublic Address 3 P2SH: ', p2sh67, '\nPublic Address bc1 BECH32: ', bech3267)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed67)
        f.write('\nPrivatekey (hex): ' + HEX67)
        f.write('\nPrivatekey Uncompressed: ' + wifu67)
        f.write('\nPrivatekey compressed: ' + wifc67)
        f.write('\nPublic Address 1 Compressed: ' + caddr67)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr67)
        f.write('\nPublic Address 3 P2SH: ' + p2sh67)
        f.write('\nPublic Address bc1 BECH32: ' + bech3267)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr68 in add or caddr68 in add or p2sh68 in add or bech3268 in add:
        print('\nMatch Found 68% ')
        print('\nPrivatekey (dec): ', seed68,'\nPrivatekey (hex): ', HEX68, '\nPrivatekey Uncompressed: ', wifu68, '\nPrivatekey compressed: ', wifc68, '\nPublic Address 1 Uncompressed: ', uaddr68, '\nPublic Address 1 Compressed: ', caddr68, '\nPublic Address 3 P2SH: ', p2sh68, '\nPublic Address bc1 BECH32: ', bech3268)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed68)
        f.write('\nPrivatekey (hex): ' + HEX68)
        f.write('\nPrivatekey Uncompressed: ' + wifu68)
        f.write('\nPrivatekey compressed: ' + wifc68)
        f.write('\nPublic Address 1 Compressed: ' + caddr68)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr68)
        f.write('\nPublic Address 3 P2SH: ' + p2sh68)
        f.write('\nPublic Address bc1 BECH32: ' + bech3268)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr69 in add or caddr69 in add or p2sh69 in add or bech3269 in add:
        print('\nMatch Found 69% ')
        print('\nPrivatekey (dec): ', seed69,'\nPrivatekey (hex): ', HEX69, '\nPrivatekey Uncompressed: ', wifu69, '\nPrivatekey compressed: ', wifc69, '\nPublic Address 1 Uncompressed: ', uaddr69, '\nPublic Address 1 Compressed: ', caddr69, '\nPublic Address 3 P2SH: ', p2sh69, '\nPublic Address bc1 BECH32: ', bech3269)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed69)
        f.write('\nPrivatekey (hex): ' + HEX69)
        f.write('\nPrivatekey Uncompressed: ' + wifu69)
        f.write('\nPrivatekey compressed: ' + wifc69)
        f.write('\nPublic Address 1 Compressed: ' + caddr69)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr69)
        f.write('\nPublic Address 3 P2SH: ' + p2sh69)
        f.write('\nPublic Address bc1 BECH32: ' + bech3269)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr70 in add or caddr70 in add or p2sh70 in add or bech3270 in add:
        print('\nMatch Found 70% ')
        print('\nPrivatekey (dec): ', seed70,'\nPrivatekey (hex): ', HEX70, '\nPrivatekey Uncompressed: ', wifu70, '\nPrivatekey compressed: ', wifc70, '\nPublic Address 1 Uncompressed: ', uaddr70, '\nPublic Address 1 Compressed: ', caddr70, '\nPublic Address 3 P2SH: ', p2sh70, '\nPublic Address bc1 BECH32: ', bech3270)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed70)
        f.write('\nPrivatekey (hex): ' + HEX70)
        f.write('\nPrivatekey Uncompressed: ' + wifu70)
        f.write('\nPrivatekey compressed: ' + wifc70)
        f.write('\nPublic Address 1 Compressed: ' + caddr70)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr70)
        f.write('\nPublic Address 3 P2SH: ' + p2sh70)
        f.write('\nPublic Address bc1 BECH32: ' + bech3270)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr71 in add or caddr71 in add or p2sh71 in add or bech3271 in add:
        print('\nMatch Found 71% ')
        print('\nPrivatekey (dec): ', seed71,'\nPrivatekey (hex): ', HEX71, '\nPrivatekey Uncompressed: ', wifu71, '\nPrivatekey compressed: ', wifc71, '\nPublic Address 1 Uncompressed: ', uaddr71, '\nPublic Address 1 Compressed: ', caddr71, '\nPublic Address 3 P2SH: ', p2sh71, '\nPublic Address bc1 BECH32: ', bech3271)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed71)
        f.write('\nPrivatekey (hex): ' + HEX71)
        f.write('\nPrivatekey Uncompressed: ' + wifu71)
        f.write('\nPrivatekey compressed: ' + wifc71)
        f.write('\nPublic Address 1 Compressed: ' + caddr71)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr71)
        f.write('\nPublic Address 3 P2SH: ' + p2sh71)
        f.write('\nPublic Address bc1 BECH32: ' + bech3271)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr72 in add or caddr72 in add or p2sh72 in add or bech3272 in add:
        print('\nMatch Found 72% ')
        print('\nPrivatekey (dec): ', seed72,'\nPrivatekey (hex): ', HEX72, '\nPrivatekey Uncompressed: ', wifu72, '\nPrivatekey compressed: ', wifc72, '\nPublic Address 1 Uncompressed: ', uaddr72, '\nPublic Address 1 Compressed: ', caddr72, '\nPublic Address 3 P2SH: ', p2sh72, '\nPublic Address bc1 BECH32: ', bech3272)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed72)
        f.write('\nPrivatekey (hex): ' + HEX72)
        f.write('\nPrivatekey Uncompressed: ' + wifu72)
        f.write('\nPrivatekey compressed: ' + wifc72)
        f.write('\nPublic Address 1 Compressed: ' + caddr72)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr72)
        f.write('\nPublic Address 3 P2SH: ' + p2sh72)
        f.write('\nPublic Address bc1 BECH32: ' + bech3272)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr73 in add or caddr73 in add or p2sh73 in add or bech3273 in add:
        print('\nMatch Found 73% ')
        print('\nPrivatekey (dec): ', seed73,'\nPrivatekey (hex): ', HEX73, '\nPrivatekey Uncompressed: ', wifu73, '\nPrivatekey compressed: ', wifc73, '\nPublic Address 1 Uncompressed: ', uaddr73, '\nPublic Address 1 Compressed: ', caddr73, '\nPublic Address 3 P2SH: ', p2sh73, '\nPublic Address bc1 BECH32: ', bech3273)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed73)
        f.write('\nPrivatekey (hex): ' + HEX73)
        f.write('\nPrivatekey Uncompressed: ' + wifu73)
        f.write('\nPrivatekey compressed: ' + wifc73)
        f.write('\nPublic Address 1 Compressed: ' + caddr73)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr73)
        f.write('\nPublic Address 3 P2SH: ' + p2sh73)
        f.write('\nPublic Address bc1 BECH32: ' + bech3273)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr74 in add or caddr74 in add or p2sh74 in add or bech3274 in add:
        print('\nMatch Found 74% ')
        print('\nPrivatekey (dec): ', seed74,'\nPrivatekey (hex): ', HEX74, '\nPrivatekey Uncompressed: ', wifu74, '\nPrivatekey compressed: ', wifc74, '\nPublic Address 1 Uncompressed: ', uaddr74, '\nPublic Address 1 Compressed: ', caddr74, '\nPublic Address 3 P2SH: ', p2sh74, '\nPublic Address bc1 BECH32: ', bech3274)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed74)
        f.write('\nPrivatekey (hex): ' + HEX74)
        f.write('\nPrivatekey Uncompressed: ' + wifu74)
        f.write('\nPrivatekey compressed: ' + wifc74)
        f.write('\nPublic Address 1 Compressed: ' + caddr74)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr74)
        f.write('\nPublic Address 3 P2SH: ' + p2sh74)
        f.write('\nPublic Address bc1 BECH32: ' + bech3274)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr75 in add or caddr75 in add or p2sh75 in add or bech3275 in add:
        print('\nMatch Found 75% ')
        print('\nPrivatekey (dec): ', seed75,'\nPrivatekey (hex): ', HEX75, '\nPrivatekey Uncompressed: ', wifu75, '\nPrivatekey compressed: ', wifc75, '\nPublic Address 1 Uncompressed: ', uaddr75, '\nPublic Address 1 Compressed: ', caddr75, '\nPublic Address 3 P2SH: ', p2sh75, '\nPublic Address bc1 BECH32: ', bech3275)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed75)
        f.write('\nPrivatekey (hex): ' + HEX75)
        f.write('\nPrivatekey Uncompressed: ' + wifu75)
        f.write('\nPrivatekey compressed: ' + wifc75)
        f.write('\nPublic Address 1 Compressed: ' + caddr75)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr75)
        f.write('\nPublic Address 3 P2SH: ' + p2sh75)
        f.write('\nPublic Address bc1 BECH32: ' + bech3275)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr76 in add or caddr76 in add or p2sh76 in add or bech3276 in add:
        print('\nMatch Found 76% ')
        print('\nPrivatekey (dec): ', seed76,'\nPrivatekey (hex): ', HEX76, '\nPrivatekey Uncompressed: ', wifu76, '\nPrivatekey compressed: ', wifc76, '\nPublic Address 1 Uncompressed: ', uaddr76, '\nPublic Address 1 Compressed: ', caddr76, '\nPublic Address 3 P2SH: ', p2sh76, '\nPublic Address bc1 BECH32: ', bech3276)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed76)
        f.write('\nPrivatekey (hex): ' + HEX76)
        f.write('\nPrivatekey Uncompressed: ' + wifu76)
        f.write('\nPrivatekey compressed: ' + wifc76)
        f.write('\nPublic Address 1 Compressed: ' + caddr76)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr76)
        f.write('\nPublic Address 3 P2SH: ' + p2sh76)
        f.write('\nPublic Address bc1 BECH32: ' + bech3276)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr77 in add or caddr77 in add or p2sh77 in add or bech3277 in add:
        print('\nMatch Found 77% ')
        print('\nPrivatekey (dec): ', seed77,'\nPrivatekey (hex): ', HEX77, '\nPrivatekey Uncompressed: ', wifu77, '\nPrivatekey compressed: ', wifc77, '\nPublic Address 1 Uncompressed: ', uaddr77, '\nPublic Address 1 Compressed: ', caddr77, '\nPublic Address 3 P2SH: ', p2sh77, '\nPublic Address bc1 BECH32: ', bech3277)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed77)
        f.write('\nPrivatekey (hex): ' + HEX77)
        f.write('\nPrivatekey Uncompressed: ' + wifu77)
        f.write('\nPrivatekey compressed: ' + wifc77)
        f.write('\nPublic Address 1 Compressed: ' + caddr77)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr77)
        f.write('\nPublic Address 3 P2SH: ' + p2sh77)
        f.write('\nPublic Address bc1 BECH32: ' + bech3277)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr78 in add or caddr78 in add or p2sh78 in add or bech3278 in add:
        print('\nMatch Found 78% ')
        print('\nPrivatekey (dec): ', seed78,'\nPrivatekey (hex): ', HEX78, '\nPrivatekey Uncompressed: ', wifu78, '\nPrivatekey compressed: ', wifc78, '\nPublic Address 1 Uncompressed: ', uaddr78, '\nPublic Address 1 Compressed: ', caddr78, '\nPublic Address 3 P2SH: ', p2sh78, '\nPublic Address bc1 BECH32: ', bech3278)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed78)
        f.write('\nPrivatekey (hex): ' + HEX78)
        f.write('\nPrivatekey Uncompressed: ' + wifu78)
        f.write('\nPrivatekey compressed: ' + wifc78)
        f.write('\nPublic Address 1 Compressed: ' + caddr78)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr78)
        f.write('\nPublic Address 3 P2SH: ' + p2sh78)
        f.write('\nPublic Address bc1 BECH32: ' + bech3278)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr79 in add or caddr79 in add or p2sh79 in add or bech3279 in add:
        print('\nMatch Found 79% ')
        print('\nPrivatekey (dec): ', seed79,'\nPrivatekey (hex): ', HEX79, '\nPrivatekey Uncompressed: ', wifu79, '\nPrivatekey compressed: ', wifc79, '\nPublic Address 1 Uncompressed: ', uaddr79, '\nPublic Address 1 Compressed: ', caddr79, '\nPublic Address 3 P2SH: ', p2sh79, '\nPublic Address bc1 BECH32: ', bech3279)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed79)
        f.write('\nPrivatekey (hex): ' + HEX79)
        f.write('\nPrivatekey Uncompressed: ' + wifu79)
        f.write('\nPrivatekey compressed: ' + wifc79)
        f.write('\nPublic Address 1 Compressed: ' + caddr79)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr79)
        f.write('\nPublic Address 3 P2SH: ' + p2sh79)
        f.write('\nPublic Address bc1 BECH32: ' + bech3279)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr80 in add or caddr80 in add or p2sh80 in add or bech3280 in add:
        print('\nMatch Found 80% ')
        print('\nPrivatekey (dec): ', seed80,'\nPrivatekey (hex): ', HEX80, '\nPrivatekey Uncompressed: ', wifu80, '\nPrivatekey compressed: ', wifc80, '\nPublic Address 1 Uncompressed: ', uaddr80, '\nPublic Address 1 Compressed: ', caddr80, '\nPublic Address 3 P2SH: ', p2sh80, '\nPublic Address bc1 BECH32: ', bech3280)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed80)
        f.write('\nPrivatekey (hex): ' + HEX80)
        f.write('\nPrivatekey Uncompressed: ' + wifu80)
        f.write('\nPrivatekey compressed: ' + wifc80)
        f.write('\nPublic Address 1 Compressed: ' + caddr80)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr80)
        f.write('\nPublic Address 3 P2SH: ' + p2sh80)
        f.write('\nPublic Address bc1 BECH32: ' + bech3280)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr81 in add or caddr81 in add or p2sh81 in add or bech3281 in add:
        print('\nMatch Found 81% ')
        print('\nPrivatekey (dec): ', seed81,'\nPrivatekey (hex): ', HEX81, '\nPrivatekey Uncompressed: ', wifu81, '\nPrivatekey compressed: ', wifc81, '\nPublic Address 1 Uncompressed: ', uaddr81, '\nPublic Address 1 Compressed: ', caddr81, '\nPublic Address 3 P2SH: ', p2sh81, '\nPublic Address bc1 BECH32: ', bech3281)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed81)
        f.write('\nPrivatekey (hex): ' + HEX81)
        f.write('\nPrivatekey Uncompressed: ' + wifu81)
        f.write('\nPrivatekey compressed: ' + wifc81)
        f.write('\nPublic Address 1 Compressed: ' + caddr81)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr81)
        f.write('\nPublic Address 3 P2SH: ' + p2sh81)
        f.write('\nPublic Address bc1 BECH32: ' + bech3281)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr82 in add or caddr82 in add or p2sh82 in add or bech3282 in add:
        print('\nMatch Found 82% ')
        print('\nPrivatekey (dec): ', seed82,'\nPrivatekey (hex): ', HEX82, '\nPrivatekey Uncompressed: ', wifu82, '\nPrivatekey compressed: ', wifc82, '\nPublic Address 1 Uncompressed: ', uaddr82, '\nPublic Address 1 Compressed: ', caddr82, '\nPublic Address 3 P2SH: ', p2sh82, '\nPublic Address bc1 BECH32: ', bech3282)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed82)
        f.write('\nPrivatekey (hex): ' + HEX82)
        f.write('\nPrivatekey Uncompressed: ' + wifu82)
        f.write('\nPrivatekey compressed: ' + wifc82)
        f.write('\nPublic Address 1 Compressed: ' + caddr82)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr82)
        f.write('\nPublic Address 3 P2SH: ' + p2sh82)
        f.write('\nPublic Address bc1 BECH32: ' + bech3282)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr83 in add or caddr83 in add or p2sh83 in add or bech3283 in add:
        print('\nMatch Found 83% ')
        print('\nPrivatekey (dec): ', seed83,'\nPrivatekey (hex): ', HEX83, '\nPrivatekey Uncompressed: ', wifu83, '\nPrivatekey compressed: ', wifc83, '\nPublic Address 1 Uncompressed: ', uaddr83, '\nPublic Address 1 Compressed: ', caddr83, '\nPublic Address 3 P2SH: ', p2sh83, '\nPublic Address bc1 BECH32: ', bech3283)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed83)
        f.write('\nPrivatekey (hex): ' + HEX83)
        f.write('\nPrivatekey Uncompressed: ' + wifu83)
        f.write('\nPrivatekey compressed: ' + wifc83)
        f.write('\nPublic Address 1 Compressed: ' + caddr83)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr83)
        f.write('\nPublic Address 3 P2SH: ' + p2sh83)
        f.write('\nPublic Address bc1 BECH32: ' + bech3283)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr84 in add or caddr84 in add or p2sh84 in add or bech3284 in add:
        print('\nMatch Found 84% ')
        print('\nPrivatekey (dec): ', seed84,'\nPrivatekey (hex): ', HEX84, '\nPrivatekey Uncompressed: ', wifu84, '\nPrivatekey compressed: ', wifc84, '\nPublic Address 1 Uncompressed: ', uaddr84, '\nPublic Address 1 Compressed: ', caddr84, '\nPublic Address 3 P2SH: ', p2sh84, '\nPublic Address bc1 BECH32: ', bech3284)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed84)
        f.write('\nPrivatekey (hex): ' + HEX84)
        f.write('\nPrivatekey Uncompressed: ' + wifu84)
        f.write('\nPrivatekey compressed: ' + wifc84)
        f.write('\nPublic Address 1 Compressed: ' + caddr84)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr84)
        f.write('\nPublic Address 3 P2SH: ' + p2sh84)
        f.write('\nPublic Address bc1 BECH32: ' + bech3284)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr85 in add or caddr85 in add or p2sh85 in add or bech3285 in add:
        print('\nMatch Found 85% ')
        print('\nPrivatekey (dec): ', seed85,'\nPrivatekey (hex): ', HEX85, '\nPrivatekey Uncompressed: ', wifu85, '\nPrivatekey compressed: ', wifc85, '\nPublic Address 1 Uncompressed: ', uaddr85, '\nPublic Address 1 Compressed: ', caddr85, '\nPublic Address 3 P2SH: ', p2sh85, '\nPublic Address bc1 BECH32: ', bech3285)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed85)
        f.write('\nPrivatekey (hex): ' + HEX85)
        f.write('\nPrivatekey Uncompressed: ' + wifu85)
        f.write('\nPrivatekey compressed: ' + wifc85)
        f.write('\nPublic Address 1 Compressed: ' + caddr85)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr85)
        f.write('\nPublic Address 3 P2SH: ' + p2sh85)
        f.write('\nPublic Address bc1 BECH32: ' + bech3285)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr86 in add or caddr86 in add or p2sh86 in add or bech3286 in add:
        print('\nMatch Found 86% ')
        print('\nPrivatekey (dec): ', seed86,'\nPrivatekey (hex): ', HEX86, '\nPrivatekey Uncompressed: ', wifu86, '\nPrivatekey compressed: ', wifc86, '\nPublic Address 1 Uncompressed: ', uaddr86, '\nPublic Address 1 Compressed: ', caddr86, '\nPublic Address 3 P2SH: ', p2sh86, '\nPublic Address bc1 BECH32: ', bech3286)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed86)
        f.write('\nPrivatekey (hex): ' + HEX86)
        f.write('\nPrivatekey Uncompressed: ' + wifu86)
        f.write('\nPrivatekey compressed: ' + wifc86)
        f.write('\nPublic Address 1 Compressed: ' + caddr86)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr86)
        f.write('\nPublic Address 3 P2SH: ' + p2sh86)
        f.write('\nPublic Address bc1 BECH32: ' + bech3286)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr87 in add or caddr87 in add or p2sh87 in add or bech3287 in add:
        print('\nMatch Found 87% ')
        print('\nPrivatekey (dec): ', seed87,'\nPrivatekey (hex): ', HEX87, '\nPrivatekey Uncompressed: ', wifu87, '\nPrivatekey compressed: ', wifc87, '\nPublic Address 1 Uncompressed: ', uaddr87, '\nPublic Address 1 Compressed: ', caddr87, '\nPublic Address 3 P2SH: ', p2sh87, '\nPublic Address bc1 BECH32: ', bech3287)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed87)
        f.write('\nPrivatekey (hex): ' + HEX87)
        f.write('\nPrivatekey Uncompressed: ' + wifu87)
        f.write('\nPrivatekey compressed: ' + wifc87)
        f.write('\nPublic Address 1 Compressed: ' + caddr87)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr87)
        f.write('\nPublic Address 3 P2SH: ' + p2sh87)
        f.write('\nPublic Address bc1 BECH32: ' + bech3287)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr88 in add or caddr88 in add or p2sh88 in add or bech3288 in add:
        print('\nMatch Found 88% ')
        print('\nPrivatekey (dec): ', seed88,'\nPrivatekey (hex): ', HEX88, '\nPrivatekey Uncompressed: ', wifu88, '\nPrivatekey compressed: ', wifc88, '\nPublic Address 1 Uncompressed: ', uaddr88, '\nPublic Address 1 Compressed: ', caddr88, '\nPublic Address 3 P2SH: ', p2sh88, '\nPublic Address bc1 BECH32: ', bech3288)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed88)
        f.write('\nPrivatekey (hex): ' + HEX88)
        f.write('\nPrivatekey Uncompressed: ' + wifu88)
        f.write('\nPrivatekey compressed: ' + wifc88)
        f.write('\nPublic Address 1 Compressed: ' + caddr88)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr88)
        f.write('\nPublic Address 3 P2SH: ' + p2sh88)
        f.write('\nPublic Address bc1 BECH32: ' + bech3288)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr89 in add or caddr89 in add or p2sh89 in add or bech3289 in add:
        print('\nMatch Found 89% ')
        print('\nPrivatekey (dec): ', seed89,'\nPrivatekey (hex): ', HEX89, '\nPrivatekey Uncompressed: ', wifu89, '\nPrivatekey compressed: ', wifc89, '\nPublic Address 1 Uncompressed: ', uaddr89, '\nPublic Address 1 Compressed: ', caddr89, '\nPublic Address 3 P2SH: ', p2sh89, '\nPublic Address bc1 BECH32: ', bech3289)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed89)
        f.write('\nPrivatekey (hex): ' + HEX89)
        f.write('\nPrivatekey Uncompressed: ' + wifu89)
        f.write('\nPrivatekey compressed: ' + wifc89)
        f.write('\nPublic Address 1 Compressed: ' + caddr89)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr89)
        f.write('\nPublic Address 3 P2SH: ' + p2sh89)
        f.write('\nPublic Address bc1 BECH32: ' + bech3289)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr90 in add or caddr90 in add or p2sh90 in add or bech3290 in add:
        print('\nMatch Found 90% ')
        print('\nPrivatekey (dec): ', seed90,'\nPrivatekey (hex): ', HEX90, '\nPrivatekey Uncompressed: ', wifu90, '\nPrivatekey compressed: ', wifc90, '\nPublic Address 1 Uncompressed: ', uaddr90, '\nPublic Address 1 Compressed: ', caddr90, '\nPublic Address 3 P2SH: ', p2sh90, '\nPublic Address bc1 BECH32: ', bech3290)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed90)
        f.write('\nPrivatekey (hex): ' + HEX90)
        f.write('\nPrivatekey Uncompressed: ' + wifu90)
        f.write('\nPrivatekey compressed: ' + wifc90)
        f.write('\nPublic Address 1 Compressed: ' + caddr90)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr90)
        f.write('\nPublic Address 3 P2SH: ' + p2sh90)
        f.write('\nPublic Address bc1 BECH32: ' + bech3290)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr91 in add or caddr91 in add or p2sh91 in add or bech3291 in add:
        print('\nMatch Found 91% ')
        print('\nPrivatekey (dec): ', seed91,'\nPrivatekey (hex): ', HEX91, '\nPrivatekey Uncompressed: ', wifu91, '\nPrivatekey compressed: ', wifc91, '\nPublic Address 1 Uncompressed: ', uaddr91, '\nPublic Address 1 Compressed: ', caddr91, '\nPublic Address 3 P2SH: ', p2sh91, '\nPublic Address bc1 BECH32: ', bech3291)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed91)
        f.write('\nPrivatekey (hex): ' + HEX91)
        f.write('\nPrivatekey Uncompressed: ' + wifu91)
        f.write('\nPrivatekey compressed: ' + wifc91)
        f.write('\nPublic Address 1 Compressed: ' + caddr91)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr91)
        f.write('\nPublic Address 3 P2SH: ' + p2sh91)
        f.write('\nPublic Address bc1 BECH32: ' + bech3291)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr92 in add or caddr92 in add or p2sh92 in add or bech3292 in add:
        print('\nMatch Found 92% ')
        print('\nPrivatekey (dec): ', seed92,'\nPrivatekey (hex): ', HEX92, '\nPrivatekey Uncompressed: ', wifu92, '\nPrivatekey compressed: ', wifc92, '\nPublic Address 1 Uncompressed: ', uaddr92, '\nPublic Address 1 Compressed: ', caddr92, '\nPublic Address 3 P2SH: ', p2sh92, '\nPublic Address bc1 BECH32: ', bech3292)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed92)
        f.write('\nPrivatekey (hex): ' + HEX92)
        f.write('\nPrivatekey Uncompressed: ' + wifu92)
        f.write('\nPrivatekey compressed: ' + wifc92)
        f.write('\nPublic Address 1 Compressed: ' + caddr92)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr92)
        f.write('\nPublic Address 3 P2SH: ' + p2sh92)
        f.write('\nPublic Address bc1 BECH32: ' + bech3292)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr93 in add or caddr93 in add or p2sh93 in add or bech3293 in add:
        print('\nMatch Found 93% ')
        print('\nPrivatekey (dec): ', seed93,'\nPrivatekey (hex): ', HEX93, '\nPrivatekey Uncompressed: ', wifu93, '\nPrivatekey compressed: ', wifc93, '\nPublic Address 1 Uncompressed: ', uaddr93, '\nPublic Address 1 Compressed: ', caddr93, '\nPublic Address 3 P2SH: ', p2sh93, '\nPublic Address bc1 BECH32: ', bech3293)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed93)
        f.write('\nPrivatekey (hex): ' + HEX93)
        f.write('\nPrivatekey Uncompressed: ' + wifu93)
        f.write('\nPrivatekey compressed: ' + wifc93)
        f.write('\nPublic Address 1 Compressed: ' + caddr93)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr93)
        f.write('\nPublic Address 3 P2SH: ' + p2sh93)
        f.write('\nPublic Address bc1 BECH32: ' + bech3293)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr94 in add or caddr94 in add or p2sh94 in add or bech3294 in add:
        print('\nMatch Found 94% ')
        print('\nPrivatekey (dec): ', seed94,'\nPrivatekey (hex): ', HEX94, '\nPrivatekey Uncompressed: ', wifu94, '\nPrivatekey compressed: ', wifc94, '\nPublic Address 1 Uncompressed: ', uaddr94, '\nPublic Address 1 Compressed: ', caddr94, '\nPublic Address 3 P2SH: ', p2sh94, '\nPublic Address bc1 BECH32: ', bech3294)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed94)
        f.write('\nPrivatekey (hex): ' + HEX94)
        f.write('\nPrivatekey Uncompressed: ' + wifu94)
        f.write('\nPrivatekey compressed: ' + wifc94)
        f.write('\nPublic Address 1 Compressed: ' + caddr94)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr94)
        f.write('\nPublic Address 3 P2SH: ' + p2sh94)
        f.write('\nPublic Address bc1 BECH32: ' + bech3294)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr95 in add or caddr95 in add or p2sh95 in add or bech3295 in add:
        print('\nMatch Found 95% ')
        print('\nPrivatekey (dec): ', seed95,'\nPrivatekey (hex): ', HEX95, '\nPrivatekey Uncompressed: ', wifu95, '\nPrivatekey compressed: ', wifc95, '\nPublic Address 1 Uncompressed: ', uaddr95, '\nPublic Address 1 Compressed: ', caddr95, '\nPublic Address 3 P2SH: ', p2sh95, '\nPublic Address bc1 BECH32: ', bech3295)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed95)
        f.write('\nPrivatekey (hex): ' + HEX95)
        f.write('\nPrivatekey Uncompressed: ' + wifu95)
        f.write('\nPrivatekey compressed: ' + wifc95)
        f.write('\nPublic Address 1 Compressed: ' + caddr95)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr95)
        f.write('\nPublic Address 3 P2SH: ' + p2sh95)
        f.write('\nPublic Address bc1 BECH32: ' + bech3295)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr96 in add or caddr96 in add or p2sh96 in add or bech3296 in add:
        print('\nMatch Found 96% ')
        print('\nPrivatekey (dec): ', seed96,'\nPrivatekey (hex): ', HEX96, '\nPrivatekey Uncompressed: ', wifu96, '\nPrivatekey compressed: ', wifc96, '\nPublic Address 1 Uncompressed: ', uaddr96, '\nPublic Address 1 Compressed: ', caddr96, '\nPublic Address 3 P2SH: ', p2sh96, '\nPublic Address bc1 BECH32: ', bech3296)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed96)
        f.write('\nPrivatekey (hex): ' + HEX96)
        f.write('\nPrivatekey Uncompressed: ' + wifu96)
        f.write('\nPrivatekey compressed: ' + wifc96)
        f.write('\nPublic Address 1 Compressed: ' + caddr96)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr96)
        f.write('\nPublic Address 3 P2SH: ' + p2sh96)
        f.write('\nPublic Address bc1 BECH32: ' + bech3296)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr97 in add or caddr97 in add or p2sh97 in add or bech3297 in add:
        print('\nMatch Found 97% ')
        print('\nPrivatekey (dec): ', seed97,'\nPrivatekey (hex): ', HEX97, '\nPrivatekey Uncompressed: ', wifu97, '\nPrivatekey compressed: ', wifc97, '\nPublic Address 1 Uncompressed: ', uaddr97, '\nPublic Address 1 Compressed: ', caddr97, '\nPublic Address 3 P2SH: ', p2sh97, '\nPublic Address bc1 BECH32: ', bech3297)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed97)
        f.write('\nPrivatekey (hex): ' + HEX97)
        f.write('\nPrivatekey Uncompressed: ' + wifu97)
        f.write('\nPrivatekey compressed: ' + wifc97)
        f.write('\nPublic Address 1 Compressed: ' + caddr97)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr97)
        f.write('\nPublic Address 3 P2SH: ' + p2sh97)
        f.write('\nPublic Address bc1 BECH32: ' + bech3297)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr98 in add or caddr98 in add or p2sh98 in add or bech3298 in add:
        print('\nMatch Found 98% ')
        print('\nPrivatekey (dec): ', seed98,'\nPrivatekey (hex): ', HEX98, '\nPrivatekey Uncompressed: ', wifu98, '\nPrivatekey compressed: ', wifc98, '\nPublic Address 1 Uncompressed: ', uaddr98, '\nPublic Address 1 Compressed: ', caddr98, '\nPublic Address 3 P2SH: ', p2sh98, '\nPublic Address bc1 BECH32: ', bech3298)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed98)
        f.write('\nPrivatekey (hex): ' + HEX98)
        f.write('\nPrivatekey Uncompressed: ' + wifu98)
        f.write('\nPrivatekey compressed: ' + wifc98)
        f.write('\nPublic Address 1 Compressed: ' + caddr98)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr98)
        f.write('\nPublic Address 3 P2SH: ' + p2sh98)
        f.write('\nPublic Address bc1 BECH32: ' + bech3298)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    if uaddr99 in add or caddr99 in add or p2sh99 in add or bech3299 in add:
        print('\nMatch Found 99% ')
        print('\nPrivatekey (dec): ', seed99,'\nPrivatekey (hex): ', HEX99, '\nPrivatekey Uncompressed: ', wifu99, '\nPrivatekey compressed: ', wifc99, '\nPublic Address 1 Uncompressed: ', uaddr99, '\nPublic Address 1 Compressed: ', caddr99, '\nPublic Address 3 P2SH: ', p2sh99, '\nPublic Address bc1 BECH32: ', bech3299)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed99)
        f.write('\nPrivatekey (hex): ' + HEX99)
        f.write('\nPrivatekey Uncompressed: ' + wifu99)
        f.write('\nPrivatekey compressed: ' + wifc99)
        f.write('\nPublic Address 1 Compressed: ' + caddr99)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr99)
        f.write('\nPublic Address 3 P2SH: ' + p2sh99)
        f.write('\nPublic Address bc1 BECH32: ' + bech3299)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
    

    else:
        print('Scan: ', count , ' :Remaining: ', str(finish), ' :Total: ', str(total), end='\r')
        #print('\n :Start 0%: ', HEXSTART,'\n :HEX 1%:   ', HEX, '\n :HEX 5%:   ', HEX5, '\n :HEX 10%:  ', HEX10, '\n :HEX 15%:  ', HEX15, '\n :HEX 20%:  ', HEX20, '\n :HEX 25%:  ', HEX25, '\n :HEX 30%:  ', HEX30, '\n :HEX 35%:  ', HEX35, '\n :HEX 40%:  ', HEX40, '\n :HEX 45%:  ', HEX45, '\n :HEX 50%:  ', HEX50, '\n :HEX 55%:  ', HEX55, '\n :HEX 60%:  ', HEX60, '\n :HEX 65%:  ', HEX65, '\n :HEX 70%:  ', HEX70, '\n :HEX 75%:  ', HEX75, '\n :HEX 80%:  ', HEX80, '\n :HEX 85%:  ', HEX85, '\n :HEX 90%:  ', HEX90, '\n :HEX 95%:  ', HEX95, '\n :Stop100%: ', HEXSTOP)