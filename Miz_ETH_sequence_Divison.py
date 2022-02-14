'''
Made by Mizogg Look for ETH Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting Miz_ETH_sequence_Divison.py Version 2 Range division by 1%-1000000% and scan sequentially 

https://mizogg.co.uk

'''
import secp256k1 as ice
from alive_progress import alive_bar

print('[+] Starting.........Please Wait.....ETH List Loading.....')

filename ='eth.txt'
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
    eth_list = [line.split()[0].lower() for line in open(filename,'r')]
    for i in compute():
            bar()
            
eth_list = set(eth_list)

print('Total ETH Addresses Loaded and Checking : ',str (line_count))
start=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
stop=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
mag=int(input("Magnitude Jump Stride -> "))
rangediv=int(input("Division of Range 1% t0 ???% ->  "))
display =int(input("Choose method Display Method: 1 - BAR:(New Under Testing); 2 - Less Details:(Quicker); 3 - More Details:(Slower)  "))
print("Starting search... Please Wait min range: " + str(start))
print("Max range: " + str(stop))
print("===========Miz_ETH.py Version 2 Range division by 1%-1000000000000% and scan sequentially=============")
print('Total ETH Addresses Loaded and Checking : ',str (line_count))
 
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
        ETHadd = ice.privatekey_to_ETH_address(ran)

        data.append({
            'seed': str(ran),
            'HEX': HEX,
            'ETHadd': ETHadd,
            'percent': f"Hex scan Percent {i}%",
        })
    

data = []
        
while start < finish:
    try:
        data = []
        finish-=mag
        start+=mag
        count += 1
        total += rangediv
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
                with alive_bar(finishscan, title='Processing') as bar:
                    bar(start)
            elif display == 2:
                print('Scan: ', count , ' :Remaining: ', str(finish), ' :Total: ', str(total), end='\r')
            elif display == 3:
                for bad_wallet in data:
                    #print(bad_wallet['percent'], '\nPrivatekey (dec): ', bad_wallet['seed'], '\nPrivatekey (hex): ', bad_wallet['HEX'], '\nEth Address: ', bad_wallet['ETHadd'])
                    print(bad_wallet['percent'], '\nPrivatekey (hex): ', bad_wallet['HEX'], end='\r')
            else:
                print("WRONG NUMBER!!! MUST CHOSE 1, 2 or 3")
                break
            
                    
    except(KeyboardInterrupt, SystemExit):
        exit('\nCTRL-C detected. Exiting gracefully.  Thank you and Happy Hunting')
