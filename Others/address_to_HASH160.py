import secp256k1 as ice

fname = 'btc.txt'
with open(fname) as textfile, open("base_h160_1_bc1.txt", 'w+') as f_1, open("base_h160_3.txt", 'w+') as f_2:
        count = 0
        skip = 0
        for line in textfile.readlines()[1:]:
            addr = (line.rstrip('\n'))
            if addr.startswith('1'):
                address = addr.split('\t')[0]
                f_1.write(ice.address_to_h160(address) + '\n')
                count +=1
            if addr.startswith('3'):
                address = addr.split('\t')[0]
                f_2.write(ice.address_to_h160(address) + '\n')
                count +=1
            if addr.startswith('bc1') and len(addr.split('\t')[0])< 50 :
                address = addr.split('\t')[0]
                f_1.write(ice.bech32_address_decode(address,coin_type=0) + '\n')
                count +=1
        else:
            skip += 1
        print ('Total write address>',count, '-skiped address>',skip)