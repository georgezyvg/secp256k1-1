import random, time
import secp256k1 as ice
from time import sleep
import time, multiprocessing, random
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count

n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

def hunt(start, stop, add, cores='all'):

    try:
        available_cores = cpu_count()
    
        if cores == 'all':
            cores = available_cores
        elif 0 < int(cores) <= available_cores:
            cores = int(cores)
        else:
            cores = 1
    
        counter = Value('L')
        match = Event()
        queue = Queue()
    
        workers = []
        for r in range(cores):
            p = Process(target=main, args=(counter, start, stop, add))
            workers.append(p)
            p.start()
    
        for worker in workers:
            worker.join()
    
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully. Thank you and Happy Hunting')

def main(counter, start, stop, add):
    count=0
    iteration = 0
    start_time = time.time()
    while True:
        count += 8
        iteration += 1
        ran=random.randrange(start,stop)
        k1 = int(ran)
        HEXk1 = "%064x" % k1
        k2 = (k1*(n-1))%n
        HEXk2 = "%064x" % k2
        wifck1 = ice.btc_pvk_to_wif(HEXk1)
        wifuk1 = ice.btc_pvk_to_wif(HEXk1, False)
        caddrk1 = ice.privatekey_to_address(0, True, k1) #Compressed
        uaddrk1 = ice.privatekey_to_address(0, False, k1)  #Uncompressed
        P2SHk1 = ice.privatekey_to_address(1, True, k1) #p2sh
        BECH32k1 = ice.privatekey_to_address(2, True, k1)  #bech32
        
        wifck2 = ice.btc_pvk_to_wif(HEXk2)
        wifuk2 = ice.btc_pvk_to_wif(HEXk2, False)
        caddrk2 = ice.privatekey_to_address(0, True, k2) #Compressed
        uaddrk2 = ice.privatekey_to_address(0, False, k2)  #Uncompressed
        P2SHk2 = ice.privatekey_to_address(1, True, k2) #p2sh
        BECH32k2 = ice.privatekey_to_address(2, True, k2)  #bech32    
        if caddrk1 in add or uaddrk1 in add or P2SHk1 in add or BECH32k1 in add :
            print('\nMatch Found')
            print('\nPrivatekey (dec): ', k1,'\nPrivatekey (hex): ', HEXk1, '\nPrivatekey Uncompressed: ', wifuk1, '\nPrivatekey compressed: ', wifck1, '\nPublic Address 1 Uncompressed: ', uaddrk1, '\nPublic Address 1 Compressed: ', caddrk1, '\nPublic Address 3 P2SH: ', P2SHk1, '\nPublic Address bc1 BECH32: ', BECH32k1)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(k1))
            f.write('\nPrivatekey (hex): ' + HEXk1)
            f.write('\nPrivatekey Uncompressed: ' + wifuk1)
            f.write('\nPrivatekey compressed: ' + wifck1)
            f.write('\nPublic Address 1 Compressed: ' + caddrk1)
            f.write('\nPublic Address 1 Uncompressed: ' + uaddrk1)
            f.write('\nPublic Address 3 P2SH: ' + P2SHk1)
            f.write('\nPublic Address bc1 BECH32: ' + BECH32k1)
        if caddrk2 in add or uaddrk2 in add or P2SHk2 in add or BECH32k2 in add :
            print('\nMatch Found')
            print('\nPrivatekey (dec): ', k2,'\nPrivatekey (hex): ', HEXk2, '\nPrivatekey Uncompressed: ', wifuk2, '\nPrivatekey compressed: ', wifck2, '\nPublic Address 1 Uncompressed: ', uaddrk2, '\nPublic Address 1 Compressed: ', caddrk2, '\nPublic Address 3 P2SH: ', P2SHk2, '\nPublic Address bc1 BECH32: ', BECH32k2)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + str(k2))
            f.write('\nPrivatekey (hex): ' + HEXk2)
            f.write('\nPrivatekey Uncompressed: ' + wifuk2)
            f.write('\nPrivatekey compressed: ' + wifck2)
            f.write('\nPublic Address 1 Compressed: ' + caddrk2)
            f.write('\nPublic Address 1 Uncompressed: ' + uaddrk2)
            f.write('\nPublic Address 3 P2SH: ' + P2SHk2)
            f.write('\nPublic Address bc1 BECH32: ' + BECH32k2)
        else:
            if iteration % 10000 == 0:
                elapsed = time.time() - start_time
                addper= round(iteration / elapsed)*8
                print(f'It/CPU={iteration} checked={count} Address/Sec={addper} Keys/Sec={iteration / elapsed:.1f}')
                #print('\nPrivatekey (dec): ', k1, '\nPrivatekey (hex): ', HEXk1)
                #print('\nPrivatekey (dec): ', k2, '\nPrivatekey (hex): ', HEXk2)
                #print('\nPrivatekey (dec): ', k1,'\nPrivatekey (hex): ', HEXk1, '\nPrivatekey Uncompressed: ', wifuk1, '\nPrivatekey compressed: ', wifck1, '\nPublic Address 1 Uncompressed: ', uaddrk1, '\nPublic Address 1 Compressed: ', caddrk1, '\nPublic Address 3 P2SH: ', P2SHk1, '\nPublic Address bc1 BECH32: ', BECH32k1)        
                #print('\nPrivatekey (dec): ', k2,'\nPrivatekey (hex): ', HEXk2, '\nPrivatekey Uncompressed: ', wifuk2, '\nPrivatekey compressed: ', wifck2, '\nPublic Address 1 Uncompressed: ', uaddrk2, '\nPublic Address 1 Compressed: ', caddrk2, '\nPublic Address 3 P2SH: ', P2SHk2, '\nPublic Address bc1 BECH32: ', BECH32k2)        

if __name__ == '__main__':
    print('[+] Starting.........Please Wait.....Bitcoin Address List Loading.....')
    filename ='btc.txt'
    with open(filename) as f:
        line_count = 0
        for line in f:
            line != "\n"
            line_count += 1
    with open(filename) as file:
        add = file.read().split()
    add = set(add)
    print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
    howmany=int(input("Number of Cores CPU -> "))   
    start = int(input("start range Min 1-57896044618658097711785492504343953926418782139537452191302581570759080747168 ->  "))
    stop = int(input("start range MAX 57896044618658097711785492504343953926418782139537452191302581570759080747169 ->  "))
    print("Starting search... Please Wait min range: " + str(start))
    print("Max range: " + str(stop))
    print("==========================================================")
    print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
    hunt(start, stop, add, cores = howmany)