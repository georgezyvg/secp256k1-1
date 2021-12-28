import hashlib, random
from hashlib import sha256
import secp256k1 as ice
import multiprocessing
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
import random, codecs, time, sys, atexit
from time import sleep
from rich.console import Console
console = Console()
console.clear()

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

my_colours = [W, R, G, O, B, P]

icons= ['⏳', 'ℹ️', '✅', '⛔️', '🔁', '🔑', '💸', '😔', '🌍', '✍️', '🚌', '👇', '📋', '📣', '🤩','😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '👋', '🤚', '🖐', '✋', '🖖', '👌', '🤌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '🖕', '👇', '☝️', '👍', '👎', '✊', '👊', '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏', '✍️', '💅', '🤳', '💪', '🦾', '🦵', '🦿', '🦶', '👣', '👂', '🦻', '👃', '🫀', '🫁', '🧠', '🦷', '🦴', '👀', '👁', '👅', '👄', '💋', '🩸', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🪱', '🐛', '🦋', '🐌', '🐞', '🐜', '🪰', '🪲', '🪳', '🦟', '🦗', '🕷', '🕸', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🦣', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', '🦘', '🦬', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐈‍⬛', '🪶', '🐓', '🦃', '🦤', '🦚', '🦜', '🦢', '🦩', '🕊', '🐇', '🦝', '🦨', '🦡', '🦫', '🦦', '🦥', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🪵', '🌱', '🌿', '☘️', '🍀', '🎍', '🪴', '🎋', '🍃', '🍂', '🍁', '🍄', '🐚', '🪨', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '🪐', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🌫', '⏰', '💰', '🎅🏻', '🎄', '🎁', '🎶']

animation = ["❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  0%","☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  5%","☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 10%","☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 15%","☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 20%","☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 25%","☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 30%","☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 35%","☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 40%","☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 45%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 50%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 55%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️ 60%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️ 65%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️ 70%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️ 75%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️ 80%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️ 85%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️ 90%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️ 95%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️100%"]

for i in range(len(animation)):
    time.sleep(0.10)
    sys.stdout.write("\r" + "Merry Christmas:" + animation[i % len(animation)])
    sys.stdout.flush()
console.print("\n[yellow]💰-----------------💰 HUNT4BITCOIN with Python 💰----------------------💰[/yellow]")
console.print("[yellow]   🤖🤖🤖 Made by Mizogg  with help from Михаил Х.XopMC  https://github.com/XopMC 🤖🤖🤖[/yellow]")
console.print("[yellow]    🤩 With iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  🤩 [/yellow]")
console.print("[yellow]💰-----------------💰 HUNT4BITCOIN with Python 💰----------------------💰[/yellow]")
console.print("[purple]         ⏳Starting search... Please Wait ⏳[/purple]")
print('Bitcoin Addresses Loading Please Wait: ')
filename ='puzzle.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
console.print("[purple]⏳Starting search... Please Wait ⏳[/purple]")
console.print("==========================================================")


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

def main(counter):
    count = 0
    total = 0
    st = time.time()
    sleep(0.00001)
    while True:
        with counter.get_lock():
            counter.value += 1
        count += 1
        total += 4
        ran=random.randrange(a,b)
        seed = str(ran)
        HEX = "%064x" % ran
        private_key_hex_px = '80' + HEX
        x = sha256(bytes.fromhex(private_key_hex_px)).hexdigest()
        x = sha256(bytes.fromhex(x)).hexdigest()
        checksum = x[:8]
        private_key_hex_px_cs = private_key_hex_px + checksum
        private_key_WIF = b58encode(bytes.fromhex(private_key_hex_px_cs)).decode("utf-8")
        private_key_hex_compressed_px = '80' + HEX + '01'
        x = sha256(bytes.fromhex(private_key_hex_compressed_px)).hexdigest()
        x = sha256(bytes.fromhex(x)).hexdigest()
        checksumc = x[:8]
        private_key_hex_compressed_px_cs = private_key_hex_compressed_px + checksumc
        private_key_WIF_compressed = b58encode(bytes.fromhex(private_key_hex_compressed_px_cs)).decode("utf-8")
        caddr = ice.privatekey_to_address(0, True, int(seed)) #Compressed
        uaddr = ice.privatekey_to_address(0, False, int(seed))  #Uncompressed
        P2SH = ice.privatekey_to_address(1, True, int(seed)) #p2sh
        BECH32 = ice.privatekey_to_address(2, True, int(seed))  #bech32
        speed = round(counter.value/(time.time() - st))

        if caddr in add or uaddr in add or P2SH in add or BECH32 in add :
            print('\nMatch Found')
            print('\nPrivatekey (dec): ', seed,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', private_key_WIF, '\nPrivatekey compressed: ', private_key_WIF_compressed, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 P2SH: ', P2SH, '\nPublic Address bc1 BECH32: ', BECH32)
            
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + seed)
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPrivatekey Uncompressed: ' + private_key_WIF)
            f.write('\nPrivatekey compressed: ' + private_key_WIF_compressed)
            f.write('\nPublic Address 1 Compressed: ' + caddr)
            f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
            f.write('\nPublic Address 3 P2SH: ' + P2SH)
            f.write('\nPublic Address bc1 BECH32: ' + BECH32)
            f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
            f.close()
            for i in range(len(animation)):
                time.sleep(0.10)
                sys.stdout.write("\r" + "Merry Christmas:" + animation[i % len(animation)])
                sys.stdout.flush()
        else:
            print('Scan Number : ', str(count), ' : Total Checked : ', str(total), ' : Keys/s : ', str(speed), end='\r')

if __name__ == '__main__':
    counter = Value('L')
    sleep(0.05)
    main(counter)
