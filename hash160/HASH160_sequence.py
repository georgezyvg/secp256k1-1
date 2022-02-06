'''
Made by Mizogg Look for HASH160 Compressed and Uncompressed Using iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  fastest Python Libary

Good Luck and Happy Hunting HASH160_sequence.py Version 1 Range division by 100% and scan sequentially 

https://mizogg.co.uk

'''

import secp256k1 as ice
import time, multiprocessing
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
from time import sleep

print('[+] Starting.........Please Wait.....HASH160 List Loading.....')

filename ='puzzleHASH160.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    h160 = file.read().split()
h160 = set(h160)

def main(counter):
    print('Total HASH160 Addresses Loaded and Checking : ',str (line_count))
    start=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
    stop=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
    mag=int(input("Magnitude Jump Stride -> "))
    print("Starting search... Please Wait min range: " + str(start))
    print("Max range: " + str(stop))
    print("==========================================================")
    print('Total HASH160 Addresses Loaded and Checking : ',str (line_count))

    HEXSTART = "%064x" % start
    HEXSTOP = "%064x" % stop
     
    remainingtotal=stop-start
    div= round(remainingtotal / 100)
    finish = div + start
    count = 0
    total = 0
    st = time.time()
    sleep(0.00001)
    while start<stop:
        with counter.get_lock():
            counter.value += 1
        try:
            speed = round(counter.value/(time.time() - st)*100)
            remainingtotal-=mag
            finish-=mag
            start+=mag
            total += 200
            count += 1
            ran= start
            HEX = "%064x" % ran        
            hash160 = ice.privatekey_to_h160(0, True, ran).hex()
            hash160u = ice.privatekey_to_h160(0, False, ran).hex()


            percent2 = div * 2
            ran2= start+percent2
            HEX2 = "%064x" % ran2
            hash1602 = ice.privatekey_to_h160(0, True, ran2).hex()
            hash160u2 = ice.privatekey_to_h160(0, False, ran2).hex()
            
            percent3 = div * 3
            ran3= start+percent3
            HEX3 = "%064x" % ran3
            hash1603 = ice.privatekey_to_h160(0, True, ran3).hex()
            hash160u3 = ice.privatekey_to_h160(0, False, ran3).hex()
            
            percent4 = div * 4
            ran4= start+percent4
            HEX4 = "%064x" % ran4
            hash1604 = ice.privatekey_to_h160(0, True, ran4).hex()
            hash160u4 = ice.privatekey_to_h160(0, False, ran4).hex()
            
            percent5 = div * 5
            ran5= start+percent5
            HEX5 = "%064x" % ran5
            hash1605 = ice.privatekey_to_h160(0, True, ran5).hex()
            hash160u5 = ice.privatekey_to_h160(0, False, ran5).hex()
            
            percent6 = div * 6
            ran6= start+percent6
            HEX6 = "%064x" % ran6
            hash1606 = ice.privatekey_to_h160(0, True, ran6).hex()
            hash160u6 = ice.privatekey_to_h160(0, False, ran6).hex()
            
            percent7 = div * 7
            ran7= start+percent7
            HEX7 = "%064x" % ran7
            hash1607 = ice.privatekey_to_h160(0, True, ran7).hex()
            hash160u7 = ice.privatekey_to_h160(0, False, ran7).hex()
            
            percent8 = div * 8
            ran8= start+percent8
            HEX8 = "%064x" % ran8
            hash1608 = ice.privatekey_to_h160(0, True, ran8).hex()
            hash160u8 = ice.privatekey_to_h160(0, False, ran8).hex()
            
            percent9 = div * 9
            ran9= start+percent9
            HEX9 = "%064x" % ran9
            hash1609 = ice.privatekey_to_h160(0, True, ran9).hex()
            hash160u9 = ice.privatekey_to_h160(0, False, ran9).hex()
            
            percent10 = div * 10
            ran10= start+percent10
            HEX10 = "%064x" % ran10
            hash16010 = ice.privatekey_to_h160(0, True, ran10).hex()
            hash160u10 = ice.privatekey_to_h160(0, False, ran10).hex()
            
            percent11 = div * 11
            ran11= start+percent11
            HEX11 = "%064x" % ran11
            hash16011 = ice.privatekey_to_h160(0, True, ran11).hex()
            hash160u11 = ice.privatekey_to_h160(0, False, ran11).hex()
            
            percent12 = div * 12
            ran12= start+percent12
            HEX12 = "%064x" % ran12
            hash16012 = ice.privatekey_to_h160(0, True, ran12).hex()
            hash160u12 = ice.privatekey_to_h160(0, False, ran12).hex()
            
            percent13 = div * 13
            ran13= start+percent13
            HEX13 = "%064x" % ran13
            hash16013 = ice.privatekey_to_h160(0, True, ran13).hex()
            hash160u13 = ice.privatekey_to_h160(0, False, ran13).hex()
            
            percent14 = div * 14
            ran14= start+percent14
            HEX14 = "%064x" % ran14
            hash16014 = ice.privatekey_to_h160(0, True, ran14).hex()
            hash160u14 = ice.privatekey_to_h160(0, False, ran14).hex()
            
            percent15 = div * 15
            ran15= start+percent15
            HEX15 = "%064x" % ran15
            hash16015 = ice.privatekey_to_h160(0, True, ran15).hex()
            hash160u15 = ice.privatekey_to_h160(0, False, ran15).hex()
            
            percent16 = div * 16
            ran16= start+percent16
            HEX16 = "%064x" % ran16
            hash16016 = ice.privatekey_to_h160(0, True, ran16).hex()
            hash160u16 = ice.privatekey_to_h160(0, False, ran16).hex()
            
            percent17 = div * 17
            ran17= start+percent17
            HEX17 = "%064x" % ran17
            hash16017 = ice.privatekey_to_h160(0, True, ran17).hex()
            hash160u17 = ice.privatekey_to_h160(0, False, ran17).hex()
            
            percent18 = div * 18
            ran18= start+percent18
            HEX18 = "%064x" % ran18
            hash16018 = ice.privatekey_to_h160(0, True, ran18).hex()
            hash160u18 = ice.privatekey_to_h160(0, False, ran18).hex()
            
            percent19 = div * 19
            ran19= start+percent19
            HEX19 = "%064x" % ran19
            hash16019 = ice.privatekey_to_h160(0, True, ran19).hex()
            hash160u19 = ice.privatekey_to_h160(0, False, ran19).hex()
            
            percent20 = div * 20
            ran20= start+percent20
            HEX20 = "%064x" % ran20
            hash16020 = ice.privatekey_to_h160(0, True, ran20).hex()
            hash160u20 = ice.privatekey_to_h160(0, False, ran20).hex()
            
            percent21 = div * 21
            ran21= start+percent21
            HEX21 = "%064x" % ran21
            hash16021 = ice.privatekey_to_h160(0, True, ran21).hex()
            hash160u21 = ice.privatekey_to_h160(0, False, ran21).hex()
            
            percent22 = div * 22
            ran22= start+percent22
            HEX22 = "%064x" % ran22
            hash16022 = ice.privatekey_to_h160(0, True, ran22).hex()
            hash160u22 = ice.privatekey_to_h160(0, False, ran22).hex()
            
            percent23 = div * 23
            ran23= start+percent23
            HEX23 = "%064x" % ran23
            hash16023 = ice.privatekey_to_h160(0, True, ran23).hex()
            hash160u23 = ice.privatekey_to_h160(0, False, ran23).hex()
            
            percent24 = div * 24
            ran24= start+percent24
            HEX24 = "%064x" % ran24
            hash16024 = ice.privatekey_to_h160(0, True, ran24).hex()
            hash160u24 = ice.privatekey_to_h160(0, False, ran24).hex()
            
            percent25 = div * 25
            ran25= start+percent25
            HEX25 = "%064x" % ran25
            hash16025 = ice.privatekey_to_h160(0, True, ran25).hex()
            hash160u25 = ice.privatekey_to_h160(0, False, ran25).hex()
            
            percent26 = div * 26
            ran26= start+percent26
            HEX26 = "%064x" % ran26
            hash16026 = ice.privatekey_to_h160(0, True, ran26).hex()
            hash160u26 = ice.privatekey_to_h160(0, False, ran26).hex()
            
            percent27 = div * 27
            ran27= start+percent27
            HEX27 = "%064x" % ran27
            hash16027 = ice.privatekey_to_h160(0, True, ran27).hex()
            hash160u27 = ice.privatekey_to_h160(0, False, ran27).hex()
            
            percent28 = div * 28
            ran28= start+percent28
            HEX28 = "%064x" % ran28
            hash16028 = ice.privatekey_to_h160(0, True, ran28).hex()
            hash160u28 = ice.privatekey_to_h160(0, False, ran28).hex()
            
            percent29 = div * 29
            ran29= start+percent29
            HEX29 = "%064x" % ran29
            hash16029 = ice.privatekey_to_h160(0, True, ran29).hex()
            hash160u29 = ice.privatekey_to_h160(0, False, ran29).hex()
            
            percent30 = div * 30
            ran30= start+percent30
            HEX30 = "%064x" % ran30
            hash16030 = ice.privatekey_to_h160(0, True, ran30).hex()
            hash160u30 = ice.privatekey_to_h160(0, False, ran30).hex()
            
            percent31 = div * 31
            ran31= start+percent31
            HEX31 = "%064x" % ran31
            hash16031 = ice.privatekey_to_h160(0, True, ran31).hex()
            hash160u31 = ice.privatekey_to_h160(0, False, ran31).hex()
            
            percent32 = div * 32
            ran32= start+percent32
            HEX32 = "%064x" % ran32
            hash16032 = ice.privatekey_to_h160(0, True, ran32).hex()
            hash160u32 = ice.privatekey_to_h160(0, False, ran32).hex()
            
            percent33 = div * 33
            ran33= start+percent33
            HEX33 = "%064x" % ran33
            hash16033 = ice.privatekey_to_h160(0, True, ran33).hex()
            hash160u33 = ice.privatekey_to_h160(0, False, ran33).hex()
            
            percent34 = div * 34
            ran34= start+percent34
            HEX34 = "%064x" % ran34
            hash16034 = ice.privatekey_to_h160(0, True, ran34).hex()
            hash160u34 = ice.privatekey_to_h160(0, False, ran34).hex()
            
            percent35 = div * 35
            ran35= start+percent35
            HEX35 = "%064x" % ran35
            hash16035 = ice.privatekey_to_h160(0, True, ran35).hex()
            hash160u35 = ice.privatekey_to_h160(0, False, ran35).hex()
            
            percent36 = div * 36
            ran36= start+percent36
            HEX36 = "%064x" % ran36
            hash16036 = ice.privatekey_to_h160(0, True, ran36).hex()
            hash160u36 = ice.privatekey_to_h160(0, False, ran36).hex()
            
            percent37 = div * 37
            ran37= start+percent37
            HEX37 = "%064x" % ran37
            hash16037 = ice.privatekey_to_h160(0, True, ran37).hex()
            hash160u37 = ice.privatekey_to_h160(0, False, ran37).hex()
            
            percent38 = div * 38
            ran38= start+percent38
            HEX38 = "%064x" % ran38
            hash16038 = ice.privatekey_to_h160(0, True, ran38).hex()
            hash160u38 = ice.privatekey_to_h160(0, False, ran38).hex()
            
            percent39 = div * 39
            ran39= start+percent39
            HEX39 = "%064x" % ran39
            hash16039 = ice.privatekey_to_h160(0, True, ran39).hex()
            hash160u39 = ice.privatekey_to_h160(0, False, ran39).hex()
            
            percent40 = div * 40
            ran40= start+percent40
            HEX40 = "%064x" % ran40
            hash16040 = ice.privatekey_to_h160(0, True, ran40).hex()
            hash160u40 = ice.privatekey_to_h160(0, False, ran40).hex()
            
            percent41 = div * 41
            ran41= start+percent41
            HEX41 = "%064x" % ran41
            hash16041 = ice.privatekey_to_h160(0, True, ran41).hex()
            hash160u41 = ice.privatekey_to_h160(0, False, ran41).hex()
            
            percent42 = div * 42
            ran42= start+percent42
            HEX42 = "%064x" % ran42
            hash16042 = ice.privatekey_to_h160(0, True, ran42).hex()
            hash160u42 = ice.privatekey_to_h160(0, False, ran42).hex()
            
            percent43 = div * 43
            ran43= start+percent43
            HEX43 = "%064x" % ran43
            hash16043 = ice.privatekey_to_h160(0, True, ran43).hex()
            hash160u43 = ice.privatekey_to_h160(0, False, ran43).hex()
            
            percent44 = div * 44
            ran44= start+percent44
            HEX44 = "%064x" % ran44
            hash16044 = ice.privatekey_to_h160(0, True, ran44).hex()
            hash160u44 = ice.privatekey_to_h160(0, False, ran44).hex()
            
            percent45 = div * 45
            ran45= start+percent45
            HEX45 = "%064x" % ran45
            hash16045 = ice.privatekey_to_h160(0, True, ran45).hex()
            hash160u45 = ice.privatekey_to_h160(0, False, ran45).hex()
            
            percent46 = div * 46
            ran46= start+percent46
            HEX46 = "%064x" % ran46
            hash16046 = ice.privatekey_to_h160(0, True, ran46).hex()
            hash160u46 = ice.privatekey_to_h160(0, False, ran46).hex()
            
            percent47 = div * 47
            ran47= start+percent47
            HEX47 = "%064x" % ran47
            hash16047 = ice.privatekey_to_h160(0, True, ran47).hex()
            hash160u47 = ice.privatekey_to_h160(0, False, ran47).hex()
            
            percent48 = div * 48
            ran48= start+percent48
            HEX48 = "%064x" % ran48
            hash16048 = ice.privatekey_to_h160(0, True, ran48).hex()
            hash160u48 = ice.privatekey_to_h160(0, False, ran48).hex()
            
            percent49 = div * 49
            ran49= start+percent49
            HEX49 = "%064x" % ran49
            hash16049 = ice.privatekey_to_h160(0, True, ran49).hex()
            hash160u49 = ice.privatekey_to_h160(0, False, ran49).hex()
            
            percent50 = div * 50
            ran50= start+percent50
            HEX50 = "%064x" % ran50
            hash16050 = ice.privatekey_to_h160(0, True, ran50).hex()
            hash160u50 = ice.privatekey_to_h160(0, False, ran50).hex()
            
            percent51 = div * 51
            ran51= start+percent51
            HEX51 = "%064x" % ran51
            hash16051 = ice.privatekey_to_h160(0, True, ran51).hex()
            hash160u51 = ice.privatekey_to_h160(0, False, ran51).hex()
            
            percent52 = div * 52
            ran52= start+percent52
            HEX52 = "%064x" % ran52
            hash16052 = ice.privatekey_to_h160(0, True, ran52).hex()
            hash160u52 = ice.privatekey_to_h160(0, False, ran52).hex()
            
            percent53 = div * 53
            ran53= start+percent53
            HEX53 = "%064x" % ran53
            hash16053 = ice.privatekey_to_h160(0, True, ran53).hex()
            hash160u53 = ice.privatekey_to_h160(0, False, ran53).hex()
            
            percent54 = div * 54
            ran54= start+percent54
            HEX54 = "%064x" % ran54
            hash16054 = ice.privatekey_to_h160(0, True, ran54).hex()
            hash160u54 = ice.privatekey_to_h160(0, False, ran54).hex()
            
            percent55 = div * 55
            ran55= start+percent55
            HEX55 = "%064x" % ran55
            hash16055 = ice.privatekey_to_h160(0, True, ran55).hex()
            hash160u55 = ice.privatekey_to_h160(0, False, ran55).hex()
            
            percent56 = div * 56
            ran56= start+percent56
            HEX56 = "%064x" % ran56
            hash16056 = ice.privatekey_to_h160(0, True, ran56).hex()
            hash160u56 = ice.privatekey_to_h160(0, False, ran56).hex()
            
            percent57 = div * 57
            ran57= start+percent57
            HEX57 = "%064x" % ran57
            hash16057 = ice.privatekey_to_h160(0, True, ran57).hex()
            hash160u57 = ice.privatekey_to_h160(0, False, ran57).hex()
            
            percent58 = div * 58
            ran58= start+percent58
            HEX58 = "%064x" % ran58
            hash16058 = ice.privatekey_to_h160(0, True, ran58).hex()
            hash160u58 = ice.privatekey_to_h160(0, False, ran58).hex()
            
            percent59 = div * 59
            ran59= start+percent59
            HEX59 = "%064x" % ran59
            hash16059 = ice.privatekey_to_h160(0, True, ran59).hex()
            hash160u59 = ice.privatekey_to_h160(0, False, ran59).hex()
            
            percent60 = div * 60
            ran60= start+percent60
            HEX60 = "%064x" % ran60
            hash16060 = ice.privatekey_to_h160(0, True, ran60).hex()
            hash160u60 = ice.privatekey_to_h160(0, False, ran60).hex()
            
            percent61 = div * 61
            ran61= start+percent61
            HEX61 = "%064x" % ran61
            hash16061 = ice.privatekey_to_h160(0, True, ran61).hex()
            hash160u61 = ice.privatekey_to_h160(0, False, ran61).hex()
            
            percent62 = div * 62
            ran62= start+percent62
            HEX62 = "%064x" % ran62
            hash16062 = ice.privatekey_to_h160(0, True, ran62).hex()
            hash160u62 = ice.privatekey_to_h160(0, False, ran62).hex()
            
            percent63 = div * 63
            ran63= start+percent63
            HEX63 = "%064x" % ran63
            hash16063 = ice.privatekey_to_h160(0, True, ran63).hex()
            hash160u63 = ice.privatekey_to_h160(0, False, ran63).hex()
            
            percent64 = div * 64
            ran64= start+percent64
            HEX64 = "%064x" % ran64
            hash16064 = ice.privatekey_to_h160(0, True, ran64).hex()
            hash160u64 = ice.privatekey_to_h160(0, False, ran64).hex()
            
            percent65 = div * 65
            ran65= start+percent65
            HEX65 = "%064x" % ran65
            hash16065 = ice.privatekey_to_h160(0, True, ran65).hex()
            hash160u65 = ice.privatekey_to_h160(0, False, ran65).hex()
            
            percent66 = div * 66
            ran66= start+percent66
            HEX66 = "%064x" % ran66
            hash16066 = ice.privatekey_to_h160(0, True, ran66).hex()
            hash160u66 = ice.privatekey_to_h160(0, False, ran66).hex()
            
            percent67 = div * 67
            ran67= start+percent67
            HEX67 = "%064x" % ran67
            hash16067 = ice.privatekey_to_h160(0, True, ran67).hex()
            hash160u67 = ice.privatekey_to_h160(0, False, ran67).hex()
            
            percent68 = div * 68
            ran68= start+percent68
            HEX68 = "%064x" % ran68
            hash16068 = ice.privatekey_to_h160(0, True, ran68).hex()
            hash160u68 = ice.privatekey_to_h160(0, False, ran68).hex()
            
            percent69 = div * 69
            ran69= start+percent69
            HEX69 = "%064x" % ran69
            hash16069 = ice.privatekey_to_h160(0, True, ran69).hex()
            hash160u69 = ice.privatekey_to_h160(0, False, ran69).hex()
            
            percent70 = div * 70
            ran70= start+percent70
            HEX70 = "%064x" % ran70
            hash16070 = ice.privatekey_to_h160(0, True, ran70).hex()
            hash160u70 = ice.privatekey_to_h160(0, False, ran70).hex()
            
            percent71 = div * 71
            ran71= start+percent71
            HEX71 = "%064x" % ran71
            hash16071 = ice.privatekey_to_h160(0, True, ran71).hex()
            hash160u71 = ice.privatekey_to_h160(0, False, ran71).hex()
            
            percent72 = div * 72
            ran72= start+percent72
            HEX72 = "%064x" % ran72
            hash16072 = ice.privatekey_to_h160(0, True, ran72).hex()
            hash160u72 = ice.privatekey_to_h160(0, False, ran72).hex()
            
            percent73 = div * 73
            ran73= start+percent73
            HEX73 = "%064x" % ran73
            hash16073 = ice.privatekey_to_h160(0, True, ran73).hex()
            hash160u73 = ice.privatekey_to_h160(0, False, ran73).hex()
            
            percent74 = div * 74
            ran74= start+percent74
            HEX74 = "%064x" % ran74
            hash16074 = ice.privatekey_to_h160(0, True, ran74).hex()
            hash160u74 = ice.privatekey_to_h160(0, False, ran74).hex()
            
            percent75 = div * 75
            ran75= start+percent75
            HEX75 = "%064x" % ran75
            hash16075 = ice.privatekey_to_h160(0, True, ran75).hex()
            hash160u75 = ice.privatekey_to_h160(0, False, ran75).hex()
            
            percent76 = div * 76
            ran76= start+percent76
            HEX76 = "%064x" % ran76
            hash16076 = ice.privatekey_to_h160(0, True, ran76).hex()
            hash160u76 = ice.privatekey_to_h160(0, False, ran76).hex()
            
            percent77 = div * 77
            ran77= start+percent77
            HEX77 = "%064x" % ran77
            hash16077 = ice.privatekey_to_h160(0, True, ran77).hex()
            hash160u77 = ice.privatekey_to_h160(0, False, ran77).hex()
            
            percent78 = div * 78
            ran78= start+percent78
            HEX78 = "%064x" % ran78
            hash16078 = ice.privatekey_to_h160(0, True, ran78).hex()
            hash160u78 = ice.privatekey_to_h160(0, False, ran78).hex()
            
            percent79 = div * 79
            ran79= start+percent79
            HEX79 = "%064x" % ran79
            hash16079 = ice.privatekey_to_h160(0, True, ran79).hex()
            hash160u79 = ice.privatekey_to_h160(0, False, ran79).hex()
            
            percent80 = div * 80
            ran80= start+percent80
            HEX80 = "%064x" % ran80
            hash16080 = ice.privatekey_to_h160(0, True, ran80).hex()
            hash160u80 = ice.privatekey_to_h160(0, False, ran80).hex()
            
            percent81 = div * 81
            ran81= start+percent81
            HEX81 = "%064x" % ran81
            hash16081 = ice.privatekey_to_h160(0, True, ran81).hex()
            hash160u81 = ice.privatekey_to_h160(0, False, ran81).hex()
            
            percent82 = div * 82
            ran82= start+percent82
            HEX82 = "%064x" % ran82
            hash16082 = ice.privatekey_to_h160(0, True, ran82).hex()
            hash160u82 = ice.privatekey_to_h160(0, False, ran82).hex()
            
            percent83 = div * 83
            ran83= start+percent83
            HEX83 = "%064x" % ran83
            hash16083 = ice.privatekey_to_h160(0, True, ran83).hex()
            hash160u83 = ice.privatekey_to_h160(0, False, ran83).hex()
            
            percent84 = div * 84
            ran84= start+percent84
            HEX84 = "%064x" % ran84
            hash16084 = ice.privatekey_to_h160(0, True, ran84).hex()
            hash160u84 = ice.privatekey_to_h160(0, False, ran84).hex()
            
            percent85 = div * 85
            ran85= start+percent85
            HEX85 = "%064x" % ran85
            hash16085 = ice.privatekey_to_h160(0, True, ran85).hex()
            hash160u85 = ice.privatekey_to_h160(0, False, ran85).hex()
            
            percent86 = div * 86
            ran86= start+percent86
            HEX86 = "%064x" % ran86
            hash16086 = ice.privatekey_to_h160(0, True, ran86).hex()
            hash160u86 = ice.privatekey_to_h160(0, False, ran86).hex()
            
            percent87 = div * 87
            ran87= start+percent87
            HEX87 = "%064x" % ran87
            hash16087 = ice.privatekey_to_h160(0, True, ran87).hex()
            hash160u87 = ice.privatekey_to_h160(0, False, ran87).hex()
            
            percent88 = div * 88
            ran88= start+percent88
            HEX88 = "%064x" % ran88
            hash16088 = ice.privatekey_to_h160(0, True, ran88).hex()
            hash160u88 = ice.privatekey_to_h160(0, False, ran88).hex()
            
            percent89 = div * 89
            ran89= start+percent89
            HEX89 = "%064x" % ran89
            hash16089 = ice.privatekey_to_h160(0, True, ran89).hex()
            hash160u89 = ice.privatekey_to_h160(0, False, ran89).hex()
            
            percent90 = div * 90
            ran90= start+percent90
            HEX90 = "%064x" % ran90
            hash16090 = ice.privatekey_to_h160(0, True, ran90).hex()
            hash160u90 = ice.privatekey_to_h160(0, False, ran90).hex()
            
            percent91 = div * 91
            ran91= start+percent91
            HEX91 = "%064x" % ran91
            hash16091 = ice.privatekey_to_h160(0, True, ran91).hex()
            hash160u91 = ice.privatekey_to_h160(0, False, ran91).hex()
            
            percent92 = div * 92
            ran92= start+percent92
            HEX92 = "%064x" % ran92
            hash16092 = ice.privatekey_to_h160(0, True, ran92).hex()
            hash160u92 = ice.privatekey_to_h160(0, False, ran92).hex()
            
            percent93 = div * 93
            ran93= start+percent93
            HEX93 = "%064x" % ran93
            hash16093 = ice.privatekey_to_h160(0, True, ran93).hex()
            hash160u93 = ice.privatekey_to_h160(0, False, ran93).hex()
            
            percent94 = div * 94
            ran94= start+percent94
            HEX94 = "%064x" % ran94
            hash16094 = ice.privatekey_to_h160(0, True, ran94).hex()
            hash160u94 = ice.privatekey_to_h160(0, False, ran94).hex()
            
            percent95 = div * 95
            ran95= start+percent95
            HEX95 = "%064x" % ran95
            hash16095 = ice.privatekey_to_h160(0, True, ran95).hex()
            hash160u95 = ice.privatekey_to_h160(0, False, ran95).hex()
            
            percent96 = div * 96
            ran96= start+percent96
            HEX96 = "%064x" % ran96
            hash16096 = ice.privatekey_to_h160(0, True, ran96).hex()
            hash160u96 = ice.privatekey_to_h160(0, False, ran96).hex()
            
            percent97 = div * 97
            ran97= start+percent97
            HEX97 = "%064x" % ran97
            hash16097 = ice.privatekey_to_h160(0, True, ran97).hex()
            hash160u97 = ice.privatekey_to_h160(0, False, ran97).hex()
            
            percent98 = div * 98
            ran98= start+percent98
            HEX98 = "%064x" % ran98
            hash16098 = ice.privatekey_to_h160(0, True, ran98).hex()
            hash160u98 = ice.privatekey_to_h160(0, False, ran98).hex()
            
            percent99 = div * 99
            ran99= start+percent99
            HEX99 = "%064x" % ran99
            hash16099 = ice.privatekey_to_h160(0, True, ran99).hex()
            hash160u99 = ice.privatekey_to_h160(0, False, ran99).hex()
            
            if hash160 in h160 or hash160u in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash160, '\nHASH160 Uncompressed : ', hash160u, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran))
                f.write('\nPrivatekey (hex): ' + HEX)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash160)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u)
                f.close()
                
            if hash1602 in h160 or hash160u2 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1602, '\nHASH160 Uncompressed : ', hash160u2, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX2)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran2))
                f.write('\nPrivatekey (hex): ' + HEX2)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1602)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u2)
                f.close()

            if hash1603 in h160 or hash160u3 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1603, '\nHASH160 Uncompressed : ', hash160u3, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX3)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran3))
                f.write('\nPrivatekey (hex): ' + HEX3)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1603)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u3)
                f.close()

            if hash1604 in h160 or hash160u4 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1604, '\nHASH160 Uncompressed : ', hash160u4, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX4)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran4))
                f.write('\nPrivatekey (hex): ' + HEX4)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1604)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u4)
                f.close()

            if hash1605 in h160 or hash160u5 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1605, '\nHASH160 Uncompressed : ', hash160u5, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX5)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran5))
                f.write('\nPrivatekey (hex): ' + HEX5)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1605)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u5)
                f.close()

            if hash1606 in h160 or hash160u6 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1606, '\nHASH160 Uncompressed : ', hash160u6, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX6)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran6))
                f.write('\nPrivatekey (hex): ' + HEX6)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1606)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u6)
                f.close()

            if hash1607 in h160 or hash160u7 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1607, '\nHASH160 Uncompressed : ', hash160u7, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX7)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran7))
                f.write('\nPrivatekey (hex): ' + HEX7)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1607)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u7)
                f.close()

            if hash1608 in h160 or hash160u8 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1608, '\nHASH160 Uncompressed : ', hash160u8, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX8)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran8))
                f.write('\nPrivatekey (hex): ' + HEX8)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1608)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u8)
                f.close()

            if hash1609 in h160 or hash160u9 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash1609, '\nHASH160 Uncompressed : ', hash160u9, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX9)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran9))
                f.write('\nPrivatekey (hex): ' + HEX9)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash1609)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u9)
                f.close()

            if hash16010 in h160 or hash160u10 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16010, '\nHASH160 Uncompressed : ', hash160u10, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX10)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran10))
                f.write('\nPrivatekey (hex): ' + HEX10)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16010)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u10)
                f.close()

            if hash16011 in h160 or hash160u11 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16011, '\nHASH160 Uncompressed : ', hash160u11, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX11)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran11))
                f.write('\nPrivatekey (hex): ' + HEX11)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16011)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u11)
                f.close()

            if hash16012 in h160 or hash160u12 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16012, '\nHASH160 Uncompressed : ', hash160u12, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX12)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran12))
                f.write('\nPrivatekey (hex): ' + HEX12)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16012)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u12)
                f.close()

            if hash16013 in h160 or hash160u13 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16013, '\nHASH160 Uncompressed : ', hash160u13, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX13)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran13))
                f.write('\nPrivatekey (hex): ' + HEX13)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16013)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u13)
                f.close()

            if hash16014 in h160 or hash160u14 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16014, '\nHASH160 Uncompressed : ', hash160u14, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX14)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran14))
                f.write('\nPrivatekey (hex): ' + HEX14)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16014)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u14)
                f.close()

            if hash16015 in h160 or hash160u15 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16015, '\nHASH160 Uncompressed : ', hash160u15, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX15)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran15))
                f.write('\nPrivatekey (hex): ' + HEX15)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16015)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u15)
                f.close()

            if hash16016 in h160 or hash160u16 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16016, '\nHASH160 Uncompressed : ', hash160u16, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX16)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran16))
                f.write('\nPrivatekey (hex): ' + HEX16)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16016)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u16)
                f.close()

            if hash16017 in h160 or hash160u17 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16017, '\nHASH160 Uncompressed : ', hash160u17, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX17)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran17))
                f.write('\nPrivatekey (hex): ' + HEX17)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16017)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u17)
                f.close()

            if hash16018 in h160 or hash160u18 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16018, '\nHASH160 Uncompressed : ', hash160u18, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX18)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran18))
                f.write('\nPrivatekey (hex): ' + HEX18)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16018)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u18)
                f.close()

            if hash16019 in h160 or hash160u19 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16019, '\nHASH160 Uncompressed : ', hash160u19, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX19)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran19))
                f.write('\nPrivatekey (hex): ' + HEX19)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16019)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u19)
                f.close()

            if hash16020 in h160 or hash160u20 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16020, '\nHASH160 Uncompressed : ', hash160u20, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX20)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran20))
                f.write('\nPrivatekey (hex): ' + HEX20)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16020)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u20)
                f.close()

            if hash16021 in h160 or hash160u21 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16021, '\nHASH160 Uncompressed : ', hash160u21, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX21)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran21))
                f.write('\nPrivatekey (hex): ' + HEX21)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16021)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u21)
                f.close()

            if hash16022 in h160 or hash160u22 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16022, '\nHASH160 Uncompressed : ', hash160u22, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX22)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran22))
                f.write('\nPrivatekey (hex): ' + HEX22)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16022)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u22)
                f.close()

            if hash16023 in h160 or hash160u23 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16023, '\nHASH160 Uncompressed : ', hash160u23, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX23)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran23))
                f.write('\nPrivatekey (hex): ' + HEX23)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16023)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u23)
                f.close()

            if hash16024 in h160 or hash160u24 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16024, '\nHASH160 Uncompressed : ', hash160u24, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX24)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran24))
                f.write('\nPrivatekey (hex): ' + HEX24)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16024)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u24)
                f.close()

            if hash16025 in h160 or hash160u25 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16025, '\nHASH160 Uncompressed : ', hash160u25, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX25)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran25))
                f.write('\nPrivatekey (hex): ' + HEX25)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16025)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u25)
                f.close()

            if hash16026 in h160 or hash160u26 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16026, '\nHASH160 Uncompressed : ', hash160u26, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX26)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran26))
                f.write('\nPrivatekey (hex): ' + HEX26)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16026)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u26)
                f.close()

            if hash16027 in h160 or hash160u27 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16027, '\nHASH160 Uncompressed : ', hash160u27, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX27)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran27))
                f.write('\nPrivatekey (hex): ' + HEX27)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16027)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u27)
                f.close()

            if hash16028 in h160 or hash160u28 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16028, '\nHASH160 Uncompressed : ', hash160u28, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX28)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran28))
                f.write('\nPrivatekey (hex): ' + HEX28)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16028)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u28)
                f.close()

            if hash16029 in h160 or hash160u29 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16029, '\nHASH160 Uncompressed : ', hash160u29, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX29)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran29))
                f.write('\nPrivatekey (hex): ' + HEX29)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16029)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u29)
                f.close()

            if hash16030 in h160 or hash160u30 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16030, '\nHASH160 Uncompressed : ', hash160u30, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX30)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran30))
                f.write('\nPrivatekey (hex): ' + HEX30)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16030)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u30)
                f.close()

            if hash16031 in h160 or hash160u31 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16031, '\nHASH160 Uncompressed : ', hash160u31, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX31)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran31))
                f.write('\nPrivatekey (hex): ' + HEX31)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16031)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u31)
                f.close()

            if hash16032 in h160 or hash160u32 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16032, '\nHASH160 Uncompressed : ', hash160u32, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX32)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran32))
                f.write('\nPrivatekey (hex): ' + HEX32)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16032)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u32)
                f.close()

            if hash16033 in h160 or hash160u33 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16033, '\nHASH160 Uncompressed : ', hash160u33, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX33)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran33))
                f.write('\nPrivatekey (hex): ' + HEX33)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16033)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u33)
                f.close()

            if hash16034 in h160 or hash160u34 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16034, '\nHASH160 Uncompressed : ', hash160u34, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX34)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran34))
                f.write('\nPrivatekey (hex): ' + HEX34)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16034)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u34)
                f.close()

            if hash16035 in h160 or hash160u35 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16035, '\nHASH160 Uncompressed : ', hash160u35, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX35)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran35))
                f.write('\nPrivatekey (hex): ' + HEX35)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16035)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u35)
                f.close()

            if hash16036 in h160 or hash160u36 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16036, '\nHASH160 Uncompressed : ', hash160u36, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX36)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran36))
                f.write('\nPrivatekey (hex): ' + HEX36)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16036)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u36)
                f.close()

            if hash16037 in h160 or hash160u37 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16037, '\nHASH160 Uncompressed : ', hash160u37, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX37)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran37))
                f.write('\nPrivatekey (hex): ' + HEX37)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16037)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u37)
                f.close()

            if hash16038 in h160 or hash160u38 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16038, '\nHASH160 Uncompressed : ', hash160u38, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX38)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran38))
                f.write('\nPrivatekey (hex): ' + HEX38)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16038)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u38)
                f.close()

            if hash16039 in h160 or hash160u39 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16039, '\nHASH160 Uncompressed : ', hash160u39, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX39)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran39))
                f.write('\nPrivatekey (hex): ' + HEX39)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16039)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u39)
                f.close()

            if hash16040 in h160 or hash160u40 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16040, '\nHASH160 Uncompressed : ', hash160u40, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX40)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran40))
                f.write('\nPrivatekey (hex): ' + HEX40)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16040)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u40)
                f.close()

            if hash16041 in h160 or hash160u41 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16041, '\nHASH160 Uncompressed : ', hash160u41, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX41)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran41))
                f.write('\nPrivatekey (hex): ' + HEX41)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16041)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u41)
                f.close()

            if hash16042 in h160 or hash160u42 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16042, '\nHASH160 Uncompressed : ', hash160u42, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX42)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran42))
                f.write('\nPrivatekey (hex): ' + HEX42)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16042)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u42)
                f.close()

            if hash16043 in h160 or hash160u43 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16043, '\nHASH160 Uncompressed : ', hash160u43, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX43)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran43))
                f.write('\nPrivatekey (hex): ' + HEX43)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16043)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u43)
                f.close()

            if hash16044 in h160 or hash160u44 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16044, '\nHASH160 Uncompressed : ', hash160u44, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX44)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran44))
                f.write('\nPrivatekey (hex): ' + HEX44)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16044)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u44)
                f.close()

            if hash16045 in h160 or hash160u45 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16045, '\nHASH160 Uncompressed : ', hash160u45, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX45)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran45))
                f.write('\nPrivatekey (hex): ' + HEX45)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16045)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u45)
                f.close()

            if hash16046 in h160 or hash160u46 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16046, '\nHASH160 Uncompressed : ', hash160u46, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX46)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran46))
                f.write('\nPrivatekey (hex): ' + HEX46)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16046)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u46)
                f.close()

            if hash16047 in h160 or hash160u47 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16047, '\nHASH160 Uncompressed : ', hash160u47, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX47)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran47))
                f.write('\nPrivatekey (hex): ' + HEX47)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16047)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u47)
                f.close()

            if hash16048 in h160 or hash160u48 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16048, '\nHASH160 Uncompressed : ', hash160u48, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX48)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran48))
                f.write('\nPrivatekey (hex): ' + HEX48)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16048)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u48)
                f.close()

            if hash16049 in h160 or hash160u49 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16049, '\nHASH160 Uncompressed : ', hash160u49, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX49)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran49))
                f.write('\nPrivatekey (hex): ' + HEX49)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16049)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u49)
                f.close()

            if hash16050 in h160 or hash160u50 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16050, '\nHASH160 Uncompressed : ', hash160u50, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX50)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran50))
                f.write('\nPrivatekey (hex): ' + HEX50)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16050)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u50)
                f.close()

            if hash16051 in h160 or hash160u51 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16051, '\nHASH160 Uncompressed : ', hash160u51, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX51)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran51))
                f.write('\nPrivatekey (hex): ' + HEX51)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16051)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u51)
                f.close()

            if hash16052 in h160 or hash160u52 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16052, '\nHASH160 Uncompressed : ', hash160u52, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX52)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran52))
                f.write('\nPrivatekey (hex): ' + HEX52)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16052)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u52)
                f.close()

            if hash16053 in h160 or hash160u53 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16053, '\nHASH160 Uncompressed : ', hash160u53, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX53)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran53))
                f.write('\nPrivatekey (hex): ' + HEX53)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16053)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u53)
                f.close()

            if hash16054 in h160 or hash160u54 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16054, '\nHASH160 Uncompressed : ', hash160u54, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX54)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran54))
                f.write('\nPrivatekey (hex): ' + HEX54)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16054)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u54)
                f.close()

            if hash16055 in h160 or hash160u55 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16055, '\nHASH160 Uncompressed : ', hash160u55, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX55)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran55))
                f.write('\nPrivatekey (hex): ' + HEX55)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16055)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u55)
                f.close()

            if hash16056 in h160 or hash160u56 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16056, '\nHASH160 Uncompressed : ', hash160u56, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX56)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran56))
                f.write('\nPrivatekey (hex): ' + HEX56)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16056)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u56)
                f.close()

            if hash16057 in h160 or hash160u57 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16057, '\nHASH160 Uncompressed : ', hash160u57, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX57)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran57))
                f.write('\nPrivatekey (hex): ' + HEX57)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16057)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u57)
                f.close()

            if hash16058 in h160 or hash160u58 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16058, '\nHASH160 Uncompressed : ', hash160u58, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX58)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran58))
                f.write('\nPrivatekey (hex): ' + HEX58)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16058)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u58)
                f.close()

            if hash16059 in h160 or hash160u59 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16059, '\nHASH160 Uncompressed : ', hash160u59, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX59)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran59))
                f.write('\nPrivatekey (hex): ' + HEX59)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16059)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u59)
                f.close()

            if hash16060 in h160 or hash160u60 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16060, '\nHASH160 Uncompressed : ', hash160u60, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX60)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran60))
                f.write('\nPrivatekey (hex): ' + HEX60)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16060)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u60)
                f.close()

            if hash16061 in h160 or hash160u61 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16061, '\nHASH160 Uncompressed : ', hash160u61, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX61)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran61))
                f.write('\nPrivatekey (hex): ' + HEX61)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16061)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u61)
                f.close()

            if hash16062 in h160 or hash160u62 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16062, '\nHASH160 Uncompressed : ', hash160u62, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX62)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran62))
                f.write('\nPrivatekey (hex): ' + HEX62)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16062)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u62)
                f.close()

            if hash16063 in h160 or hash160u63 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16063, '\nHASH160 Uncompressed : ', hash160u63, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX63)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran63))
                f.write('\nPrivatekey (hex): ' + HEX63)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16063)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u63)
                f.close()

            if hash16064 in h160 or hash160u64 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16064, '\nHASH160 Uncompressed : ', hash160u64, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX64)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran64))
                f.write('\nPrivatekey (hex): ' + HEX64)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16064)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u64)
                f.close()

            if hash16065 in h160 or hash160u65 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16065, '\nHASH160 Uncompressed : ', hash160u65, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX65)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran65))
                f.write('\nPrivatekey (hex): ' + HEX65)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16065)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u65)
                f.close()

            if hash16066 in h160 or hash160u66 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16066, '\nHASH160 Uncompressed : ', hash160u66, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX66)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran66))
                f.write('\nPrivatekey (hex): ' + HEX66)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16066)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u66)
                f.close()

            if hash16067 in h160 or hash160u67 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16067, '\nHASH160 Uncompressed : ', hash160u67, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX67)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran67))
                f.write('\nPrivatekey (hex): ' + HEX67)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16067)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u67)
                f.close()

            if hash16068 in h160 or hash160u68 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16068, '\nHASH160 Uncompressed : ', hash160u68, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX68)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran68))
                f.write('\nPrivatekey (hex): ' + HEX68)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16068)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u68)
                f.close()

            if hash16069 in h160 or hash160u69 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16069, '\nHASH160 Uncompressed : ', hash160u69, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX69)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran69))
                f.write('\nPrivatekey (hex): ' + HEX69)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16069)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u69)
                f.close()

            if hash16070 in h160 or hash160u70 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16070, '\nHASH160 Uncompressed : ', hash160u70, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX70)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran70))
                f.write('\nPrivatekey (hex): ' + HEX70)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16070)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u70)
                f.close()

            if hash16071 in h160 or hash160u71 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16071, '\nHASH160 Uncompressed : ', hash160u71, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX71)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran71))
                f.write('\nPrivatekey (hex): ' + HEX71)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16071)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u71)
                f.close()

            if hash16072 in h160 or hash160u72 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16072, '\nHASH160 Uncompressed : ', hash160u72, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX72)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran72))
                f.write('\nPrivatekey (hex): ' + HEX72)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16072)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u72)
                f.close()

            if hash16073 in h160 or hash160u73 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16073, '\nHASH160 Uncompressed : ', hash160u73, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX73)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran73))
                f.write('\nPrivatekey (hex): ' + HEX73)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16073)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u73)
                f.close()

            if hash16074 in h160 or hash160u74 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16074, '\nHASH160 Uncompressed : ', hash160u74, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX74)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran74))
                f.write('\nPrivatekey (hex): ' + HEX74)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16074)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u74)
                f.close()

            if hash16075 in h160 or hash160u75 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16075, '\nHASH160 Uncompressed : ', hash160u75, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX75)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran75))
                f.write('\nPrivatekey (hex): ' + HEX75)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16075)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u75)
                f.close()

            if hash16076 in h160 or hash160u76 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16076, '\nHASH160 Uncompressed : ', hash160u76, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX76)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran76))
                f.write('\nPrivatekey (hex): ' + HEX76)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16076)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u76)
                f.close()

            if hash16077 in h160 or hash160u77 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16077, '\nHASH160 Uncompressed : ', hash160u77, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX77)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran77))
                f.write('\nPrivatekey (hex): ' + HEX77)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16077)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u77)
                f.close()

            if hash16078 in h160 or hash160u78 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16078, '\nHASH160 Uncompressed : ', hash160u78, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX78)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran78))
                f.write('\nPrivatekey (hex): ' + HEX78)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16078)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u78)
                f.close()

            if hash16079 in h160 or hash160u79 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16079, '\nHASH160 Uncompressed : ', hash160u79, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX79)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran79))
                f.write('\nPrivatekey (hex): ' + HEX79)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16079)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u79)
                f.close()

            if hash16080 in h160 or hash160u80 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16080, '\nHASH160 Uncompressed : ', hash160u80, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX80)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran80))
                f.write('\nPrivatekey (hex): ' + HEX80)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16080)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u80)
                f.close()

            if hash16081 in h160 or hash160u81 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16081, '\nHASH160 Uncompressed : ', hash160u81, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX81)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran81))
                f.write('\nPrivatekey (hex): ' + HEX81)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16081)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u81)
                f.close()

            if hash16082 in h160 or hash160u82 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16082, '\nHASH160 Uncompressed : ', hash160u82, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX82)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran82))
                f.write('\nPrivatekey (hex): ' + HEX82)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16082)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u82)
                f.close()

            if hash16083 in h160 or hash160u83 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16083, '\nHASH160 Uncompressed : ', hash160u83, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX83)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran83))
                f.write('\nPrivatekey (hex): ' + HEX83)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16083)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u83)
                f.close()

            if hash16084 in h160 or hash160u84 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16084, '\nHASH160 Uncompressed : ', hash160u84, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX84)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran84))
                f.write('\nPrivatekey (hex): ' + HEX84)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16084)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u84)
                f.close()

            if hash16085 in h160 or hash160u85 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16085, '\nHASH160 Uncompressed : ', hash160u85, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX85)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran85))
                f.write('\nPrivatekey (hex): ' + HEX85)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16085)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u85)
                f.close()

            if hash16086 in h160 or hash160u86 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16086, '\nHASH160 Uncompressed : ', hash160u86, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX86)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran86))
                f.write('\nPrivatekey (hex): ' + HEX86)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16086)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u86)
                f.close()

            if hash16087 in h160 or hash160u87 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16087, '\nHASH160 Uncompressed : ', hash160u87, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX87)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran87))
                f.write('\nPrivatekey (hex): ' + HEX87)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16087)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u87)
                f.close()

            if hash16088 in h160 or hash160u88 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16088, '\nHASH160 Uncompressed : ', hash160u88, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX88)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran88))
                f.write('\nPrivatekey (hex): ' + HEX88)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16088)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u88)
                f.close()

            if hash16089 in h160 or hash160u89 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16089, '\nHASH160 Uncompressed : ', hash160u89, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX89)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran89))
                f.write('\nPrivatekey (hex): ' + HEX89)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16089)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u89)
                f.close()

            if hash16090 in h160 or hash160u90 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16090, '\nHASH160 Uncompressed : ', hash160u90, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX90)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran90))
                f.write('\nPrivatekey (hex): ' + HEX90)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16090)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u90)
                f.close()

            if hash16091 in h160 or hash160u91 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16091, '\nHASH160 Uncompressed : ', hash160u91, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX91)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran91))
                f.write('\nPrivatekey (hex): ' + HEX91)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16091)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u91)
                f.close()

            if hash16092 in h160 or hash160u92 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16092, '\nHASH160 Uncompressed : ', hash160u92, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX92)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran92))
                f.write('\nPrivatekey (hex): ' + HEX92)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16092)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u92)
                f.close()

            if hash16093 in h160 or hash160u93 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16093, '\nHASH160 Uncompressed : ', hash160u93, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX93)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran93))
                f.write('\nPrivatekey (hex): ' + HEX93)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16093)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u93)
                f.close()

            if hash16094 in h160 or hash160u94 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16094, '\nHASH160 Uncompressed : ', hash160u94, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX94)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran94))
                f.write('\nPrivatekey (hex): ' + HEX94)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16094)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u94)
                f.close()

            if hash16095 in h160 or hash160u95 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16095, '\nHASH160 Uncompressed : ', hash160u95, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX95)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran95))
                f.write('\nPrivatekey (hex): ' + HEX95)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16095)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u95)
                f.close()

            if hash16096 in h160 or hash160u96 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16096, '\nHASH160 Uncompressed : ', hash160u96, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX96)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran96))
                f.write('\nPrivatekey (hex): ' + HEX96)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16096)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u96)
                f.close()

            if hash16097 in h160 or hash160u97 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16097, '\nHASH160 Uncompressed : ', hash160u97, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX97)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran97))
                f.write('\nPrivatekey (hex): ' + HEX97)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16097)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u97)
                f.close()

            if hash16098 in h160 or hash160u98 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16098, '\nHASH160 Uncompressed : ', hash160u98, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX98)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran98))
                f.write('\nPrivatekey (hex): ' + HEX98)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16098)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u98)
                f.close()

            if hash16099 in h160 or hash160u99 in h160:
                print('\nMatch Found ', '\nHASH160 compressed : ', hash16099, '\nHASH160 Uncompressed : ', hash160u99, '\nPrivatekey (dec): ', ran, '\nPrivatekey (hex): ', HEX99)
                f=open("winner.txt","a")
                f.write('\nPrivatekey (dec): ' + str(ran99))
                f.write('\nPrivatekey (hex): ' + HEX99)
                f.write('\nMatching HASH160 Compressed Found   : ' + hash16099)
                f.write('\nMatching HASH160 Uncompressed Found : ' + hash160u99)
                f.close()        

            else:
                print('Scan: ', count , ' :Remaining: ', str(finish), ' :Total: ', str(total), ' : Keys/s : ', str(speed), end='\r')
                #print('\n :Start 0%: ', HEXSTART,'\n :HEX 1%:   ', HEX, '\n :HEX 5%:   ', HEX5, '\n :HEX 10%:  ', HEX10, '\n :HEX 15%:  ', HEX15, '\n :HEX 20%:  ', HEX20, '\n :HEX 25%:  ', HEX25, '\n :HEX 30%:  ', HEX30, '\n :HEX 35%:  ', HEX35, '\n :HEX 40%:  ', HEX40, '\n :HEX 45%:  ', HEX45, '\n :HEX 50%:  ', HEX50, '\n :HEX 55%:  ', HEX55, '\n :HEX 60%:  ', HEX60, '\n :HEX 65%:  ', HEX65, '\n :HEX 70%:  ', HEX70, '\n :HEX 75%:  ', HEX75, '\n :HEX 80%:  ', HEX80, '\n :HEX 85%:  ', HEX85, '\n :HEX 90%:  ', HEX90, '\n :HEX 95%:  ', HEX95, '\n :Stop100%: ', HEXSTOP)
                #print('\n :Start 0%: ', HEXSTART,'\n :HEX 1%:   ', HEX, '\n :HEX 2%:   ', HEX2, '\n :HEX 3%:   ', HEX3, '\n :HEX 4%:   ', HEX4, '\n :HEX 5%:   ', HEX5, '\n :HEX 6%:   ', HEX6, '\n :HEX 7%:   ', HEX7, '\n :HEX 8%:   ', HEX8, '\n :HEX 9%:   ', HEX9, '\n :HEX 10%:  ', HEX10, '\n :HEX 11%:  ', HEX11, '\n :HEX 12%:  ', HEX12, '\n :HEX 13%:  ', HEX13, '\n :HEX 14%:  ', HEX14, '\n :HEX 15%:  ', HEX15, '\n :HEX 16%:  ', HEX16, '\n :HEX 17%:  ', HEX17, '\n :HEX 18%:  ', HEX18, '\n :HEX 19%:  ', HEX19, '\n :HEX 20%:  ', HEX20, '\n :HEX 21%:  ', HEX21, '\n :HEX 22%:  ', HEX22, '\n :HEX 23%:  ', HEX23, '\n :HEX 24%:  ', HEX24, '\n :HEX 25%:  ', HEX25, '\n :HEX 26%:  ', HEX26, '\n :HEX 27%:  ', HEX27, '\n :HEX 28%:  ', HEX28, '\n :HEX 29%:  ', HEX29, '\n :HEX 30%:  ', HEX30, '\n :HEX 31%:  ', HEX31, '\n :HEX 32%:  ', HEX32, '\n :HEX 33%:  ', HEX33, '\n :HEX 34%:  ', HEX34, '\n :HEX 35%:  ', HEX35, '\n :HEX 36%:  ', HEX36, '\n :HEX 37%:  ', HEX37, '\n :HEX 38%:  ', HEX38, '\n :HEX 39%:  ', HEX39, '\n :HEX 40%:  ', HEX40, '\n :HEX 41%:  ', HEX41, '\n :HEX 42%:  ', HEX42, '\n :HEX 43%:  ', HEX43, '\n :HEX 44%:  ', HEX44, '\n :HEX 45%:  ', HEX45, '\n :HEX 46%:  ', HEX46, '\n :HEX 47%:  ', HEX47, '\n :HEX 48%:  ', HEX49, '\n :HEX 49%:  ', HEX49, '\n :HEX 50%:  ', HEX50, '\n :HEX 51%:  ', HEX51, '\n :HEX 52%:  ', HEX52, '\n :HEX 53%:  ', HEX53, '\n :HEX 54%:  ', HEX54, '\n :HEX 55%:  ', HEX55, '\n :HEX 56%:  ', HEX56, '\n :HEX 57%:  ', HEX57, '\n :HEX 58%:  ', HEX58, '\n :HEX 59%:  ', HEX59, '\n :HEX 60%:  ', HEX60, '\n :HEX 61%:  ', HEX61, '\n :HEX 62%:  ', HEX62, '\n :HEX 63%:  ', HEX63, '\n :HEX 64%:  ', HEX64, '\n :HEX 65%:  ', HEX65, '\n :HEX 66%:  ', HEX66, '\n :HEX 67%:  ', HEX67, '\n :HEX 68%:  ', HEX68, '\n :HEX 69%:  ', HEX69, '\n :HEX 70%:  ', HEX70, '\n :HEX 71%:  ', HEX71, '\n :HEX 72%:  ', HEX72, '\n :HEX 73%:  ', HEX73, '\n :HEX 74%:  ', HEX74, '\n :HEX 75%:  ', HEX75, '\n :HEX 76%:  ', HEX76, '\n :HEX 77%:  ', HEX77, '\n :HEX 78%:  ', HEX78, '\n :HEX 79%:  ', HEX79, '\n :HEX 80%:  ', HEX80, '\n :HEX 81%:  ', HEX81, '\n :HEX 82%:  ', HEX82, '\n :HEX 83%:  ', HEX83, '\n :HEX 84%:  ', HEX84, '\n :HEX 85%:  ', HEX85, '\n :HEX 86%:  ', HEX86, '\n :HEX 87%:  ', HEX87, '\n :HEX 88%:  ', HEX88, '\n :HEX 89%:  ', HEX89, '\n :HEX 90%:  ', HEX90, '\n :HEX 91%:  ', HEX91, '\n :HEX 92%:  ', HEX92, '\n :HEX 93%:  ', HEX93, '\n :HEX 94%:  ', HEX94, '\n :HEX 95%:  ', HEX95, '\n :HEX 96%:  ', HEX96, '\n :HEX 97%:  ', HEX97, '\n :HEX 98%:  ', HEX98, '\n :HEX 99%:  ', HEX99, '\n :Stop100%: ', HEXSTOP)

        except(KeyboardInterrupt, SystemExit):
            exit('\nCTRL-C detected. Exiting gracefully.  Thank you and Happy Hunting')

if __name__ == '__main__':
    counter = Value('L')
    main(counter)