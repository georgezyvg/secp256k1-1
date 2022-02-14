'''
Made by Mizogg Look for ETH Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting Miz_ETH_Random_Divison_CPU.py Version 2 Range division by 1%-1000000% and scan randomly  in Range Divsion with CPU Speed Improvments 

https://mizogg.co.uk

'''
import random
import secp256k1 as ice
import time, multiprocessing, random
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
from time import sleep

def hunt(start, stop, eth_list, rangediv, display, cores='all'):

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
            p = Process(target=main, args=(counter, start, stop, eth_list, display, rangediv))
            workers.append(p)
            p.start()
    
        for worker in workers:
            worker.join()
    
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully. Thank you and Happy Hunting')

def main(counter, start, stop, eth_list, display, rangediv):
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
                    HEX = "%064x" % ran        
                    ETHadd = ice.privatekey_to_ETH_address(ran)

                    data.append({
                        'seed': str(ran),
                        'HEX': HEX,
                        'ETHadd': ETHadd,
                        'percent': f"Hex scan Percent {i}%",
                    })
            data = []
            count += 1
            remainingtotal=stop-start
            div= round(remainingtotal / rangediv)
            finish = div + start
            data_wallet()
            for data_w in data:
                ETHadd = data_w['ETHadd']
                if ETHadd in eth_list:
                    print('\nMatch Found IN : ', data_w['percent'])
                    print('\nPrivatekey (dec): ', data_w['seed'], '\nPrivatekey (hex): ', data_w['HEX'], '\nEth Address: ', data_w['ETHadd'])
                    with open("winner.txt", "a") as f:
                        f.write(f"""\nMatch Found IN  {data_w['percent']}
                        Privatekey (dec):  {data_w['seed']}
                        Privatekey (hex): {data_w['HEX']}
                        ETH Address:  {data_w['ETHadd']}
                        =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====""")
                else:
                    if display == 1:

                            print('Scan: ', count , ' : Keys/s : ', str(cpuspeed), end='\r')
                    elif display == 2:
                        for bad_wallet in data:
                            #print(bad_wallet['percent'], '\nPrivatekey (dec): ', bad_wallet['seed'], '\nPrivatekey (hex): ', bad_wallet['HEX'], '\nEth Address: ', bad_wallet['ETHadd'])
                            print(bad_wallet['percent'], '\nPrivatekey (hex): ', bad_wallet['HEX'], end='\r')
                    else:
                        print("WRONG NUMBER!!! MUST CHOSE 1 or 2")
                        break
                
                        
        except(KeyboardInterrupt, SystemExit):
            exit('\nCTRL-C detected. Exiting gracefully.  Thank you and Happy Hunting')
            
if __name__ == '__main__':
    print('[+] Starting.........Please Wait.....ETH List Loading.....')
    filename ='eth.txt'
    with open(filename) as f:
        line_count = 0
        for line in f:
            line != "\n"
            line_count += 1
        eth_list = [line.split()[0].lower() for line in open(filename,'r')]
    eth_list = set(eth_list)
    print('Total ETH Addresses Loaded and Checking : ',str (line_count))
    howmany=int(input("Number of Cores CPU -> "))   
    start=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
    stop=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
    rangediv=int(input("Division of Range 1% t0 ???% ->  "))
    display =int(input("Choose method Display Method: 1 - Less Details:(Quicker); 2 - More Details:(Slower)  "))
    print("Starting search... Please Wait min range: " + str(start))
    print("Max range: " + str(stop))
    print("==========================================================")
    print('Total ETH Addresses Loaded and Checking : ',str (line_count))
    hunt(start, stop, eth_list, rangediv, display, cores = howmany)
