prompt123= '''
    ************************ Rane Division Tools ***************************
    *                       Divide Range in bits or bytes                  *
    *                       Option.1  Divide Range in bits  =1             *
    *                       Option.2  Divide Range in bytes =2             *
    ************************ Rane Division Tools ***************************
Type You Choice Here Enter 1-2 :
'''
promptstart=int(input(prompt123))
if promptstart == 1:
    x=int(input("start range bits Min 1-255 ->  "))
    y=int(input("stop range bits Max 256 -> "))
    start=2**x
    stop=2**y
    
elif promptstart == 2:    
    start=int(input("start range Min bytes 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
    stop=int(input("stop range Max bytes 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))

rangediv=int(input("Division of Range 1% t0 ???% ->  "))
display =int(input("Choose method Display Method: 1 - HEX:; 2 - DEC  "))

remainingtotal=stop-start
div = round(remainingtotal / rangediv)
   
divsion = []

def divsion_wallet():
    for i in range(0,rangediv):
        percent = div * i
        ran= start+percent
        seed = str(ran)
        HEX = "%064x" % ran
        divsion.append({
            'seed': seed,
            'HEX': HEX,
            'percent': f"{i}%",
        })
        
if display == 1:
    divsion = []
    divsion_wallet()
    for data_w in divsion:
        HEX = data_w['HEX']
        print('Percent', data_w['percent'], ' : Privatekey (hex): ', data_w['HEX'])
        with open("hex.txt", "a") as f:
            f.write(f"""\nPercent{data_w['percent']} Privatekey (hex): {data_w['HEX']}""")
            f.close
elif display == 2:
    divsion = []
    divsion_wallet()
    for data_w in divsion:
        seed = data_w['seed']
        print('Percent', data_w['percent'], ' : Privatekey (dec): ', data_w['seed'])
        with open("dec.txt", "a") as f:
            f.write(f"""\nPercent{data_w['percent']} Privatekey (dec): {data_w['seed']}""")
            f.close
else:
    print("WRONG NUMBER!!! MUST CHOSE 1 - 2 ")