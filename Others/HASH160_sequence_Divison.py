'''
Made by Mizogg Look for HASH160 Compressed and Uncompressed Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting HASH160_sequence.py Version 4 Range division by 1%-1000000% and scan sequentially 

https://mizogg.co.uk

'''

import secp256k1 as ice
from alive_progress import alive_bar


print('[+] Starting.........Please Wait.....HASH160 List Loading.....')


filename ='puzzleHASH160.txt' #RIPEMD160  puzzleHASH160
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1

        
def compute():
    for i in range(line_count):
        ...
        yield

with alive_bar(line_count) as bar:
    with open(filename) as file:
        h160 = file.read().split()
        for i in compute():
            bar()
        

h160 = set(h160)

        
       
print('Total HASH160 Addresses Loaded and Checking : ',str (line_count))
start=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
stop=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
mag=int(input("Magnitude Jump Stride -> "))
rangediv=int(input("Division of Range 1% t0 ???% ->  "))
display =int(input("Choose method Display Method: 1 - BAR:(New Under Testing); 2 - Less Details:(Quicker); 3 - More Details:(Slower)  "))
print("Starting search... Please Wait min range: " + str(start))
print("Max range: " + str(stop))
print("===========HASH160_sequence.py Version 4 Range division by 1%-1000000% and scan sequentially=============")
print('Total HASH160 Addresses Loaded and Checking : ',str (line_count))

remainingtotal=stop-start
div = round(remainingtotal / rangediv)
finish = div + start
finishscan = round(stop / rangediv)
count = 0
total = 0

def computermain():
    for i in range(finishscan):
        ...
        yield
        
        
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
    

data = []

while start < finish:
    try:
        data = []
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
            if display == 1:
                with alive_bar(finishscan, title='Processing') as bar:
                    bar(start)
            elif display == 2:
                for bad_wallet in data:
                    print('Scan: ', count , ' :Remaining: ', str(finish), ' :Total: ', str(total), end='\r')
            elif display == 3:
                for bad_wallet in data:
                    #print(bad_wallet['percent'], '\nPrivatekey (dec): ', bad_wallet['seed'], '\nPrivatekey (hex): ', bad_wallet['HEX'], '\nHASH160 Uncompressed: ', bad_wallet['hash160u'], '\nHASH160 compressed: ', bad_wallet['hash160'])
                    print(bad_wallet['percent'], '\nPrivatekey (hex): ', bad_wallet['HEX'], end='\r')
            else:
                print("WRONG NUMBER!!! MUST CHOSE 1, 2 or 3")
                break
            
                    
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully.  Thank you and Happy Hunting')