'''
Made by Mizogg Look for HASH160 Compressed and Uncompressed Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting HASH160_sequence.py Version 3 Range division by 1%-1000000% and scan sequentially 

https://mizogg.co.uk

'''

import secp256k1 as ice
import time, multiprocessing
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
from time import sleep

print('[+] Starting.........Please Wait.....HASH160 List Loading.....')

filename ='puzzleHASH160.txt' #RIPEMD160
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    h160 = file.read().split()
h160 = set(h160)


print('Total HASH160 Addresses Loaded and Checking : ',str (line_count))
start=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
stop=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
mag=int(input("Magnitude Jump Stride -> "))
rangediv=int(input("Division of Range 1% t0 ???% ->  "))
print("Starting search... Please Wait min range: " + str(start))
print("Max range: " + str(stop))
print("==========================================================")
print('Total HASH160 Addresses Loaded and Checking : ',str (line_count))

HEXSTART = "%064x" % start
HEXSTOP = "%064x" % stop
 
remainingtotal=stop-start
div = round(remainingtotal / rangediv)
finish = div + start
count = 0
total = 0

def data_wallet():
    for i in range(0,rangediv):
        percent = div * i
        ran= start+percent
        HEX = "%064x" % ran        
        hash160 = ice.privatekey_to_h160(0, True, ran).hex()
        hash160u = ice.privatekey_to_h160(0, False, ran).hex()
        data.append({
            'seed': str(ran),
            'HEX': HEX,
            'hash160': hash160,
            'hash160u': hash160u,
            'percent': f"Hex scan Percent {i}%",
        })
    
count = 0
total = 0
data = []

while start < finish:
    try:
        data = []
        remainingtotal-=mag
        finish-=mag
        start+=mag
        count += 1
        total += rangediv*2
        data_wallet()
        for data_w in data:
            hash160 = data_w['hash160']
            hash160u = data_w['hash160u']
            if hash160 in h160 or hash160u in h160:
                print('\nMatch Found IN : ', data_w['percent'])
                print('\nPrivatekey (dec): ', data_w['seed'], '\nPrivatekey (hex): ', data_w['HEX'], '\nHASH160 Uncompressed: ', data_w['hash160u'], '\nHASH160 compressed: ', data_w['hash160'])
                with open("winner.txt", "a") as f:
                    f.write(f"""\nMatch Found IN  {data_w['percent']}
                    Privatekey (dec):  {data_w['seed']}
                    Privatekey (hex): {data_w['HEX']}
                    HASH160 Uncompressed:  {data_w['hash160u']}
                    HASH160 Compressed:  {data_w['hash160']}
                    =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====""")
        else:
            for bad_wallet in data:
                #print('Scan: ', count , ' :Remaining: ', str(finish), ' :Total: ', str(total), end='\r')
                #print(bad_wallet['percent'], '\nPrivatekey (dec): ', bad_wallet['seed'], '\nPrivatekey (hex): ', bad_wallet['HEX'], '\nHASH160 Uncompressed: ', bad_wallet['hash160u'], '\nHASH160 compressed: ', bad_wallet['hash160'])
                print(bad_wallet['percent'], '\nPrivatekey (hex): ', bad_wallet['HEX'], end='\r')
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully.  Thank you and Happy Hunting')
