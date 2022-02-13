'''
Made by Mizogg Look for Bitcoin Compressed and Uncompressed 3 bc1 Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting Bitcoin_randomCPU.py Version 1 scan randomly  in Range with CPU Speed Improvments

https://mizogg.co.uk

'''
import secp256k1 as ice
import time, multiprocessing, random
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
from time import sleep

def hunt(start, stop, h160, cores='all'):

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
    count = 0
    st = time.time()
    sleep(0.00001)
    while True:
        with counter.get_lock():
            counter.value += 1
        speed = round(counter.value/(time.time() - st))
        count += 1
        ran=random.randrange(start,stop)
        seed = str(ran)
        HEX = "%064x" % ran   
        wifc = ice.btc_pvk_to_wif(HEX)
        wifu = ice.btc_pvk_to_wif(HEX, False)
        caddr = ice.privatekey_to_address(0, True, int(seed)) #Compressed
        uaddr = ice.privatekey_to_address(0, False, int(seed))  #Uncompressed
        P2SH = ice.privatekey_to_address(1, True, int(seed)) #p2sh
        BECH32 = ice.privatekey_to_address(2, True, int(seed))  #bech32

        if caddr in add or uaddr in add or P2SH in add or BECH32 in add :
            print('\nMatch Found')
            print('\nPrivatekey (dec): ', seed,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wifu, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 P2SH: ', P2SH, '\nPublic Address bc1 BECH32: ', BECH32)
            f=open("winner.txt","a")
            f.write('\nPrivatekey (dec): ' + seed)
            f.write('\nPrivatekey (hex): ' + HEX)
            f.write('\nPrivatekey Uncompressed: ' + wifu)
            f.write('\nPrivatekey compressed: ' + wifc)
            f.write('\nPublic Address 1 Compressed: ' + caddr)
            f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
            f.write('\nPublic Address 3 P2SH: ' + P2SH)
            f.write('\nPublic Address bc1 BECH32: ' + BECH32)
        else:
            print(HEX, ' : Keys/s : ', str(speed), end='\r')
            

if __name__ == '__main__':
    print('[+] Starting.........Please Wait.....Bitcoin Address List Loading.....')
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
    howmany=int(input("Number of Cores CPU -> "))   
    start=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
    stop=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
    print("Starting search... Please Wait min range: " + str(start))
    print("Max range: " + str(stop))
    print("==========================================================")
    print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
    hunt(start, stop, add, cores = howmany)