'''
Made by Mizogg Look for Bitcoin Compressed and Uncompressed 3 bc1 Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting Bitcoin_randomCPU_Divison.py Version 1 scan randomly  in Range Divsion with CPU Speed Improvments

https://mizogg.co.uk

'''
import secp256k1 as ice
import time, multiprocessing, random
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
from time import sleep

def hunt(start, stop, add, rangediv, display, cores='all'):

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
            p = Process(target=main, args=(counter, start, stop, add, display, rangediv))
            workers.append(p)
            p.start()
    
        for worker in workers:
            worker.join()
    
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully. Thank you and Happy Hunting')

def main(counter, start, stop, add, display, rangediv):
    count = 0
    st = time.time()
    sleep(0.00001)
    while True:
        try: 
            data = []
            with counter.get_lock():
                counter.value += 1
            speed = round(counter.value/(time.time() - st))
            cpuspeed = speed*rangediv
            def data_wallet():
                for i in range(0,rangediv):
                    percent = div * i
                    first = start+percent
                    last = start+first
                    ran= random.randrange(first,last)
                    seed = str(ran)
                    HEX = "%064x" % ran
                    wifc = ice.btc_pvk_to_wif(HEX)
                    wifu = ice.btc_pvk_to_wif(HEX, False)
                    caddr = ice.privatekey_to_address(0, True, int(seed)) #Compressed
                    uaddr = ice.privatekey_to_address(0, False, int(seed))  #Uncompressed
                    p2sh = ice.privatekey_to_address(1, True, int(seed)) #p2sh
                    bech32 = ice.privatekey_to_address(2, True, int(seed))  #bech32
                    data.append({
                        'seed': seed,
                        'HEX': HEX,
                        'wifc': wifc,
                        'wifu': wifu,
                        'caddr': caddr,
                        'uaddr': uaddr,
                        'p2sh': p2sh,
                        'bech32': bech32,
                        'percent': f"Hex scan Percent {i}%",
                    })
                
            data = []
            count += 1
            remainingtotal=stop-start
            div= round(remainingtotal / rangediv)
            finish = div + start
            data_wallet()
            for data_w in data:
                caddr = data_w['caddr']
                uaddr = data_w['uaddr']
                p2sh = data_w['p2sh']
                bech32 = data_w['bech32']
                if caddr in add or uaddr in add or p2sh in add or bech32 in add:
                    print('\nMatch Found IN : ', data_w['percent'])
                    print('\nPrivatekey (dec): ', data_w['seed'], '\nPrivatekey (hex): ', data_w['HEX'], '\nPrivatekey Uncompressed: ', data_w['wifu'], '\nPrivatekey compressed: ', data_w['wifc'], '\nPublic Address 1 Uncompressed: ', data_w['uaddr'], '\nPublic Address 1 compressed: ', data_w['caddr'], '\nPublic Address 3 P2SH: ', data_w['p2sh'], '\nPublic Address bc1 BECH32: ', data_w['bech32'])
                    with open("winner.txt", "a") as f:
                        f.write(f"""\nMatch Found IN  {data_w['percent']}
                        Privatekey (dec):  {data_w['seed']}
                        Privatekey (hex): {data_w['HEX']}
                        Privatekey Uncompressed:  {data_w['wifu']}
                        Privatekey Compressed:  {data_w['wifc']}
                        Public Address 1 Uncompressed:  {data_w['uaddr']}
                        Public Address 1 Compressed:  {data_w['caddr']}
                        Public Address 3 P2SH:  {data_w['p2sh']}
                        Public Address bc1 BECH32:  {data_w['bech32']}
                        =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====""")
                        
                else:
                    if display == 1:

                            print('Scan: ', count , ' : Keys/s : ', str(cpuspeed), end='\r')
                    elif display == 2:
                        for bad_wallet in data:
                            #print('\nPrivatekey (dec): ', bad_wallet['seed'], '\nPrivatekey (hex): ', bad_wallet['HEX'], '\nPrivatekey Uncompressed: ', bad_wallet['wifu'], '\nPrivatekey compressed: ', bad_wallet['wifc'], '\nPublic Address 1 Uncompressed: ', bad_wallet['uaddr'], '\nPublic Address 1 compressed: ', bad_wallet['caddr'], '\nPublic Address 3 P2SH: ', bad_wallet['p2sh'], '\nPublic Address bc1 BECH32: ', bad_wallet['bech32'])
                            print(bad_wallet['percent'], '\nPrivatekey (hex): ', bad_wallet['HEX'], end='\r')
                    else:
                        print("WRONG NUMBER!!! MUST CHOSE 1 or 2")
                        break
                
                        
        except(KeyboardInterrupt, SystemExit):
            exit('\nCTRL-C detected. Exiting gracefully.  Thank you and Happy Hunting')
            

if __name__ == '__main__':
    print('[+] Starting.Bitcoin_randomCPU_Divison.py Please Wait.....Bitcoin Address List Loading.....')
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
    rangediv=int(input("Division of Range 1% t0 ???% ->  "))
    display =int(input("Choose method Display Method: 1 - Less Details:(Quicker); 2 - More Details:(Slower)  "))
    print("Starting search... Please Wait min range: " + str(start))
    print("Max range: " + str(stop))
    print("==========================================================")
    print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
    hunt(start, stop, add, rangediv, display, cores = howmany)