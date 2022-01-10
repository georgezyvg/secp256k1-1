import random, codecs, time, os, sys
import secp256k1 as ice
from time import sleep
from rich.console import Console
console = Console()
console.clear()

animation = ["❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  0%","☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  5%","☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 10%","☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 15%","☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 20%","☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 25%","☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 30%","☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 35%","☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 40%","☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 45%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 50%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 55%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️ 60%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️ 65%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️ 70%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️ 75%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️ 80%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️ 85%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️ 90%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️ 95%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️100%"]

for i in range(len(animation)):
    time.sleep(0.03)
    sys.stdout.write("\r" + "HAPPY HUNTING :" + animation[i % len(animation)])
    sys.stdout.flush()
console.print("\n[yellow]💰-----------------💰 HUNT4ETH RANGE DIVISION 100% VERSION MIZ_ETH 💰----------------------💰[/yellow]")
console.print("[yellow]   🤖🤖🤖       Made by Mizogg      🤖🤖🤖[/yellow]")
console.print("[yellow]    🤩 With iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  🤩 [/yellow]")
console.print("[yellow]💰-------💰 Divide the Chosen Range by 100% and Scan Sequentially 💰-----------💰[/yellow]")
console.print("[purple]         ⏳Starting search... Please Wait ⏳[/purple]")

print('ETH Addresses Loading Please Wait: ')

filename ='eth.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)

print('Total ETH Addresses Loaded and Checking : ',str (line_count))
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
start = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
stop = 2**y
mag=int(input("Magnitude Jump Stride -> "))
print("Starting search... Please Wait min range: " + str(start))
print("Max range: " + str(stop))
print("==========================================================")
print('Total ETH Addresses Loaded and Checking : ',str (line_count))

    
HEXSTART = "%064x" % start
HEXSTOP = "%064x" % stop
 
remainingtotal=stop-start
div= round(remainingtotal / 100)
finish = div + start
count = 0
total = 0

while start<finish:
    remainingtotal-=mag
    finish-=mag
    start+=mag
    div= round(remainingtotal / 100)
    count += 1
    total += 200
    ran= start
    seed = str(ran)
    HEX = "%064x" % ran
    addr = ice.privatekey_to_ETH_address(int(seed))

    percent2 = div * 2
    ran2= start+percent2
    HEX2 = "%064x" % ran2
    seed2 = str(ran2)
    addr2 = ice.privatekey_to_ETH_address(int(seed2))
    
    percent3 = div * 3
    ran3= start+percent3
    HEX3 = "%064x" % ran3
    seed3 = str(ran3)
    addr3 = ice.privatekey_to_ETH_address(int(seed3))
  
    percent4 = div * 4
    ran4= start+percent4
    HEX4 = "%064x" % ran4
    seed4 = str(ran4)
    addr4 = ice.privatekey_to_ETH_address(int(seed4))
   
    percent5 = div * 5
    ran5= start+percent5
    HEX5 = "%064x" % ran5
    seed5 = str(ran5)
    addr5 = ice.privatekey_to_ETH_address(int(seed5))
    
    percent6 = div * 6
    ran6= start+percent6
    HEX6 = "%064x" % ran6
    seed6 = str(ran6)
    addr6 = ice.privatekey_to_ETH_address(int(seed6))
    
    percent7 = div * 7
    ran7= start+percent7
    HEX7 = "%064x" % ran7
    seed7 = str(ran7)
    addr7 = ice.privatekey_to_ETH_address(int(seed7))
    
    percent8 = div * 8
    ran8= start+percent8
    HEX8 = "%064x" % ran8
    seed8 = str(ran8)
    addr8 = ice.privatekey_to_ETH_address(int(seed8))
    
    percent9 = div * 9
    ran9= start+percent9
    HEX9 = "%064x" % ran9
    seed9 = str(ran9)
    addr9 = ice.privatekey_to_ETH_address(int(seed9))
   
    percent10 = div * 10
    ran10= start+percent10
    HEX10 = "%064x" % ran10
    seed10 = str(ran10)
    addr10 = ice.privatekey_to_ETH_address(int(seed10))
    
    percent11 = div * 11
    ran11= start+percent11
    HEX11 = "%064x" % ran11
    seed11 = str(ran11)
    addr11 = ice.privatekey_to_ETH_address(int(seed11))
   
    percent12 = div * 12
    ran12= start+percent12
    HEX12 = "%064x" % ran12
    seed12 = str(ran12)
    addr12 = ice.privatekey_to_ETH_address(int(seed12))
   
    percent13 = div * 13
    ran13= start+percent13
    HEX13 = "%064x" % ran13
    seed13 = str(ran13)
    addr13 = ice.privatekey_to_ETH_address(int(seed13))
    
    percent14 = div * 14
    ran14= start+percent14
    HEX14 = "%064x" % ran14
    seed14 = str(ran14)
    addr14 = ice.privatekey_to_ETH_address(int(seed14))
    
    percent15 = div * 15
    ran15= start+percent15
    HEX15 = "%064x" % ran15
    seed15 = str(ran15)
    addr15 = ice.privatekey_to_ETH_address(int(seed15))
    
    percent16 = div * 16
    ran16= start+percent16
    HEX16 = "%064x" % ran16
    seed16 = str(ran16)
    addr16 = ice.privatekey_to_ETH_address(int(seed16))
    
    percent17 = div * 17
    ran17= start+percent17
    HEX17 = "%064x" % ran17
    seed17 = str(ran17)
    addr17 = ice.privatekey_to_ETH_address(int(seed17))
    
    percent18 = div * 18
    ran18= start+percent18
    HEX18 = "%064x" % ran18
    seed18 = str(ran18)
    addr18 = ice.privatekey_to_ETH_address(int(seed18))
     
    percent19 = div * 19
    ran19= start+percent19
    HEX19 = "%064x" % ran19
    seed19 = str(ran19)
    addr19 = ice.privatekey_to_ETH_address(int(seed19))
    
    percent20 = div * 20
    ran20= start+percent20
    HEX20 = "%064x" % ran20
    seed20 = str(ran20)
    addr20 = ice.privatekey_to_ETH_address(int(seed20))
   
    percent21 = div * 21
    ran21= start+percent21
    HEX21 = "%064x" % ran21
    seed21 = str(ran21)
    addr21 = ice.privatekey_to_ETH_address(int(seed21))
    
    percent22 = div * 22
    ran22= start+percent22
    HEX22 = "%064x" % ran22
    seed22 = str(ran22)
    addr22 = ice.privatekey_to_ETH_address(int(seed22))
    
    percent23 = div * 23
    ran23= start+percent23
    HEX23 = "%064x" % ran23
    seed23 = str(ran23)
    addr23 = ice.privatekey_to_ETH_address(int(seed23))
   
    percent24 = div * 24
    ran24= start+percent24
    HEX24 = "%064x" % ran24
    seed24 = str(ran24)
    addr24 = ice.privatekey_to_ETH_address(int(seed24))
   
    percent25 = div * 25
    ran25= start+percent25
    HEX25 = "%064x" % ran25
    seed25 = str(ran25)
    addr25 = ice.privatekey_to_ETH_address(int(seed25))
    
    percent26 = div * 26
    ran26= start+percent26
    HEX26 = "%064x" % ran26
    seed26 = str(ran26)
    addr26 = ice.privatekey_to_ETH_address(int(seed26))
 
    percent27 = div * 27
    ran27= start+percent27
    HEX27 = "%064x" % ran27
    seed27 = str(ran27)
    addr27 = ice.privatekey_to_ETH_address(int(seed27))
   
    percent28 = div * 28
    ran28= start+percent28
    HEX28 = "%064x" % ran28
    seed28 = str(ran28)
    addr28 = ice.privatekey_to_ETH_address(int(seed28))
    
    percent29 = div * 29
    ran29= start+percent29
    HEX29 = "%064x" % ran29
    seed29 = str(ran29)
    addr29 = ice.privatekey_to_ETH_address(int(seed29))
   
    percent30 = div * 30
    ran30= start+percent30
    HEX30 = "%064x" % ran30
    seed30 = str(ran30)
    addr30 = ice.privatekey_to_ETH_address(int(seed30))
    
    percent31 = div * 31
    ran31= start+percent31
    HEX31 = "%064x" % ran31
    seed31 = str(ran31)
    addr31 = ice.privatekey_to_ETH_address(int(seed31))
   
    percent32 = div * 32
    ran32= start+percent32
    HEX32 = "%064x" % ran32
    seed32 = str(ran32)
    addr32 = ice.privatekey_to_ETH_address(int(seed32))
   
    percent33 = div * 33
    ran33= start+percent33
    HEX33 = "%064x" % ran33
    seed33 = str(ran33)
    addr33 = ice.privatekey_to_ETH_address(int(seed33))
    
    percent34 = div * 34
    ran34= start+percent34
    HEX34 = "%064x" % ran34
    seed34 = str(ran34)
    addr34 = ice.privatekey_to_ETH_address(int(seed34))
    
    percent35 = div * 35
    ran35= start+percent35
    HEX35 = "%064x" % ran35
    seed35 = str(ran35)
    addr35 = ice.privatekey_to_ETH_address(int(seed35))
    
    percent36 = div * 36
    ran36= start+percent36
    HEX36 = "%064x" % ran36
    seed36 = str(ran36)
    addr36 = ice.privatekey_to_ETH_address(int(seed36))
   
    percent37 = div * 37
    ran37= start+percent37
    HEX37 = "%064x" % ran37
    seed37 = str(ran37)
    addr37 = ice.privatekey_to_ETH_address(int(seed37))
    
    percent38 = div * 38
    ran38= start+percent38
    HEX38 = "%064x" % ran38
    seed38 = str(ran38)
    addr38 = ice.privatekey_to_ETH_address(int(seed38))
    
    percent39 = div * 39
    ran39= start+percent39
    HEX39 = "%064x" % ran39
    seed39 = str(ran39)
    addr39 = ice.privatekey_to_ETH_address(int(seed39))
    
    percent40 = div * 40
    ran40= start+percent40
    HEX40 = "%064x" % ran40
    seed40 = str(ran40)
    addr40 = ice.privatekey_to_ETH_address(int(seed40))
   
    percent41 = div * 41
    ran41= start+percent41
    HEX41 = "%064x" % ran41
    seed41 = str(ran41)
    addr41 = ice.privatekey_to_ETH_address(int(seed41))
    
    percent42 = div * 42
    ran42= start+percent42
    HEX42 = "%064x" % ran42
    seed42 = str(ran42)
    addr42 = ice.privatekey_to_ETH_address(int(seed42))
   
    percent43 = div * 43
    ran43= start+percent43
    HEX43 = "%064x" % ran43
    seed43 = str(ran43)
    addr43 = ice.privatekey_to_ETH_address(int(seed43))
    
    percent44 = div * 44
    ran44= start+percent44
    HEX44 = "%064x" % ran44
    seed44 = str(ran44)
    addr44 = ice.privatekey_to_ETH_address(int(seed44))
    
    percent45 = div * 45
    ran45= start+percent45
    HEX45 = "%064x" % ran45
    seed45 = str(ran45)
    addr45 = ice.privatekey_to_ETH_address(int(seed45))
    
    percent46 = div * 46
    ran46= start+percent46
    HEX46 = "%064x" % ran46
    seed46 = str(ran46)
    addr46 = ice.privatekey_to_ETH_address(int(seed46))
   
    percent47 = div * 47
    ran47= start+percent47
    HEX47 = "%064x" % ran47
    seed47 = str(ran47)
    addr47 = ice.privatekey_to_ETH_address(int(seed47))
   
    percent48 = div * 48
    ran48= start+percent48
    HEX48 = "%064x" % ran48
    seed48 = str(ran48)
    addr48 = ice.privatekey_to_ETH_address(int(seed48))
   
    percent49 = div * 49
    ran49= start+percent49
    HEX49 = "%064x" % ran49
    seed49 = str(ran49)
    addr49 = ice.privatekey_to_ETH_address(int(seed49))
   
    percent50 = div * 50
    ran50= start+percent50
    HEX50 = "%064x" % ran50
    seed50 = str(ran50)
    addr50 = ice.privatekey_to_ETH_address(int(seed50))
   
    percent51 = div * 51
    ran51= start+percent51
    HEX51 = "%064x" % ran51
    seed51 = str(ran51)
    addr51 = ice.privatekey_to_ETH_address(int(seed51))
    
    percent52 = div * 52
    ran52= start+percent52
    HEX52 = "%064x" % ran52
    seed52 = str(ran52)
    addr52 = ice.privatekey_to_ETH_address(int(seed52))
   
    percent53 = div * 53
    ran53= start+percent53
    HEX53 = "%064x" % ran53
    seed53 = str(ran53)
    addr53 = ice.privatekey_to_ETH_address(int(seed53))
    
    percent54 = div * 54
    ran54= start+percent54
    HEX54 = "%064x" % ran54
    seed54 = str(ran54)
    addr54 = ice.privatekey_to_ETH_address(int(seed54))
    
    percent55 = div * 55
    ran55= start+percent55
    HEX55 = "%064x" % ran55
    seed55 = str(ran55)
    addr55 = ice.privatekey_to_ETH_address(int(seed55))
    
    percent56 = div * 56
    ran56= start+percent56
    HEX56 = "%064x" % ran56
    seed56 = str(ran56)
    addr56 = ice.privatekey_to_ETH_address(int(seed56))
   
    percent57 = div * 57
    ran57= start+percent57
    HEX57 = "%064x" % ran57
    seed57 = str(ran57)
    addr57 = ice.privatekey_to_ETH_address(int(seed57))
    
    percent58 = div * 58
    ran58= start+percent58
    HEX58 = "%064x" % ran58
    seed58 = str(ran58)
    addr58 = ice.privatekey_to_ETH_address(int(seed58))
   
    percent59 = div * 59
    ran59= start+percent59
    HEX59 = "%064x" % ran59
    seed59 = str(ran59)
    addr59 = ice.privatekey_to_ETH_address(int(seed59))
   
    percent60 = div * 60
    ran60= start+percent60
    HEX60 = "%064x" % ran60
    seed60 = str(ran60)
    addr60 = ice.privatekey_to_ETH_address(int(seed60))
   
    percent61 = div * 61
    ran61= start+percent61
    HEX61 = "%064x" % ran61
    seed61 = str(ran61)
    addr61 = ice.privatekey_to_ETH_address(int(seed61))
   
    percent62 = div * 62
    ran62= start+percent62
    HEX62 = "%064x" % ran62
    seed62 = str(ran62)
    addr62 = ice.privatekey_to_ETH_address(int(seed62))
   
    percent63 = div * 63
    ran63= start+percent63
    HEX63 = "%064x" % ran63
    seed63 = str(ran63)
    addr63 = ice.privatekey_to_ETH_address(int(seed63))
   
    percent64 = div * 64
    ran64= start+percent64
    HEX64 = "%064x" % ran64
    seed64 = str(ran64)
    addr64 = ice.privatekey_to_ETH_address(int(seed64))
   
    percent65 = div * 65
    ran65= start+percent65
    HEX65 = "%064x" % ran65
    seed65 = str(ran65)
    addr65 = ice.privatekey_to_ETH_address(int(seed65))
   
    percent66 = div * 66
    ran66= start+percent66
    HEX66 = "%064x" % ran66
    seed66 = str(ran66)
    addr66 = ice.privatekey_to_ETH_address(int(seed66))
    
    percent67 = div * 67
    ran67= start+percent67
    HEX67 = "%064x" % ran67
    seed67 = str(ran67)
    addr67 = ice.privatekey_to_ETH_address(int(seed67))
   
    percent68 = div * 68
    ran68= start+percent68
    HEX68 = "%064x" % ran68
    seed68 = str(ran68)
    addr68 = ice.privatekey_to_ETH_address(int(seed68))
   
    percent69 = div * 69
    ran69= start+percent69
    HEX69 = "%064x" % ran69
    seed69 = str(ran69)
    addr69 = ice.privatekey_to_ETH_address(int(seed69))
   
    percent70 = div * 70
    ran70= start+percent70
    HEX70 = "%064x" % ran70
    seed70 = str(ran70)
    addr70 = ice.privatekey_to_ETH_address(int(seed70))
  
    percent71 = div * 71
    ran71= start+percent71
    HEX71 = "%064x" % ran71
    seed71 = str(ran71)
    addr71 = ice.privatekey_to_ETH_address(int(seed71))
   
    percent72 = div * 72
    ran72= start+percent72
    HEX72 = "%064x" % ran72
    seed72 = str(ran72)
    addr72 = ice.privatekey_to_ETH_address(int(seed72))
 
    percent73 = div * 73
    ran73= start+percent73
    HEX73 = "%064x" % ran73
    seed73 = str(ran73)
    addr73 = ice.privatekey_to_ETH_address(int(seed73))

    percent74 = div * 74
    ran74= start+percent74
    HEX74 = "%064x" % ran74
    seed74 = str(ran74)
    addr74 = ice.privatekey_to_ETH_address(int(seed74))

    percent75 = div * 75
    ran75= start+percent75
    HEX75 = "%064x" % ran75
    seed75 = str(ran75)
    addr75 = ice.privatekey_to_ETH_address(int(seed75))

    percent76 = div * 76
    ran76= start+percent76
    HEX76 = "%064x" % ran76
    seed76 = str(ran76)
    addr76 = ice.privatekey_to_ETH_address(int(seed76))

    percent77 = div * 77
    ran77= start+percent77
    HEX77 = "%064x" % ran77
    seed77 = str(ran77)
    addr77 = ice.privatekey_to_ETH_address(int(seed77))

    percent78 = div * 78
    ran78= start+percent78
    HEX78 = "%064x" % ran78
    seed78 = str(ran78)
    addr78 = ice.privatekey_to_ETH_address(int(seed78))

    percent79 = div * 79
    ran79= start+percent79
    HEX79 = "%064x" % ran79
    seed79 = str(ran79)
    addr79 = ice.privatekey_to_ETH_address(int(seed79))

    percent80 = div * 80
    ran80= start+percent80
    HEX80 = "%064x" % ran80
    seed80 = str(ran80)
    addr80 = ice.privatekey_to_ETH_address(int(seed80))
 
    percent81 = div * 81
    ran81= start+percent81
    HEX81 = "%064x" % ran81
    seed81 = str(ran81)
    addr81 = ice.privatekey_to_ETH_address(int(seed81))
   
    percent82 = div * 82
    ran82= start+percent82
    HEX82 = "%064x" % ran82
    seed82 = str(ran82)
    addr82 = ice.privatekey_to_ETH_address(int(seed82))
   
    percent83 = div * 83
    ran83= start+percent83
    HEX83 = "%064x" % ran83
    seed83 = str(ran83)
    addr83 = ice.privatekey_to_ETH_address(int(seed83))
  
    percent84 = div * 84
    ran84= start+percent84
    HEX84 = "%064x" % ran84
    seed84 = str(ran84)
    addr84 = ice.privatekey_to_ETH_address(int(seed84))
  
    percent85 = div * 85
    ran85= start+percent85
    HEX85 = "%064x" % ran85
    seed85 = str(ran85)
    addr85 = ice.privatekey_to_ETH_address(int(seed85))
 
    percent86 = div * 86
    ran86= start+percent86
    HEX86 = "%064x" % ran86
    seed86 = str(ran86)
    addr86 = ice.privatekey_to_ETH_address(int(seed86))
  
    percent87 = div * 87
    ran87= start+percent87
    HEX87 = "%064x" % ran87
    seed87 = str(ran87)
    addr87 = ice.privatekey_to_ETH_address(int(seed87))
  
    percent88 = div * 88
    ran88= start+percent88
    HEX88 = "%064x" % ran88
    seed88 = str(ran88)
    addr88 = ice.privatekey_to_ETH_address(int(seed88))
   
    percent89 = div * 89
    ran89= start+percent89
    HEX89 = "%064x" % ran89
    seed89 = str(ran89)
    addr89 = ice.privatekey_to_ETH_address(int(seed89))

    percent90 = div * 90
    ran90= start+percent90
    HEX90 = "%064x" % ran90
    seed90 = str(ran90)
    addr90 = ice.privatekey_to_ETH_address(int(seed90))

    percent91 = div * 91
    ran91= start+percent91
    HEX91 = "%064x" % ran91
    seed91 = str(ran91)
    addr91 = ice.privatekey_to_ETH_address(int(seed91))

    percent92 = div * 92
    ran92= start+percent92
    HEX92 = "%064x" % ran92
    seed92 = str(ran92)
    addr92 = ice.privatekey_to_ETH_address(int(seed92))

    percent93 = div * 93
    ran93= start+percent93
    HEX93 = "%064x" % ran93
    seed93 = str(ran93)
    addr93 = ice.privatekey_to_ETH_address(int(seed93))

    percent94 = div * 94
    ran94= start+percent94
    HEX94 = "%064x" % ran94
    seed94 = str(ran94)
    addr94 = ice.privatekey_to_ETH_address(int(seed94))

    percent95 = div * 95
    ran95= start+percent95
    HEX95 = "%064x" % ran95
    seed95 = str(ran95)
    addr95 = ice.privatekey_to_ETH_address(int(seed95))

    percent96 = div * 96
    ran96= start+percent96
    HEX96 = "%064x" % ran96
    seed96 = str(ran96)
    addr96 = ice.privatekey_to_ETH_address(int(seed96))

    percent97 = div * 97
    ran97= start+percent97
    HEX97 = "%064x" % ran97
    seed97 = str(ran97)
    addr97 = ice.privatekey_to_ETH_address(int(seed97))

    percent98 = div * 98
    ran98= start+percent98
    HEX98 = "%064x" % ran98
    seed98 = str(ran98)
    addr98 = ice.privatekey_to_ETH_address(int(seed98))

    percent99 = div * 99
    ran99= start+percent99
    HEX99 = "%064x" % ran99
    seed99 = str(ran99)
    addr99 = ice.privatekey_to_ETH_address(int(seed99))

    if addr in add:
        print('\nMatch Found 1%')
        print('\nPrivatekey (dec): ', seed,'\nPrivatekey (hex): ', HEX, '\n ETH: ', addr)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed)
        f.write('\nPrivatekey (hex): ' + HEX)
        f.write('\n ETH: ' + addr) 
        f.close()
    if addr2 in add:
        print('\nMatch Found 2%')
        print('\nPrivatekey (dec): ', seed2,'\nPrivatekey (hex): ', HEX2, '\n ETH: ', addr2)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed2)
        f.write('\nPrivatekey (hex): ' + HEX2)
        f.write('\n ETH: ' + addr2)
        f.close()
    if addr3 in add:
        print('\nMatch Found 3%')
        print('\nPrivatekey (dec): ', seed3,'\nPrivatekey (hex): ', HEX3, '\n ETH: ', addr3)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed3)
        f.write('\nPrivatekey (hex): ' + HEX3)
        f.write('\n ETH: ' + addr3) 
        f.close()
    if addr4 in add:
        print('\nMatch Found 4% ')
        print('\nPrivatekey (dec): ', seed4,'\nPrivatekey (hex): ', HEX4, '\n ETH: ', addr4)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed4)
        f.write('\nPrivatekey (hex): ' + HEX4)
        f.write('\n ETH: ' + addr4) 
        f.close()
    if addr5 in add:
        print('\nMatch Found 5% ')
        print('\nPrivatekey (dec): ', seed5,'\nPrivatekey (hex): ', HEX5, '\n ETH: ', addr5)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed5)
        f.write('\nPrivatekey (hex): ' + HEX5)
        f.write('\n ETH: ' + addr5) 
        f.close()
    if addr6 in add:
        print('\nMatch Found 6% ')
        print('\nPrivatekey (dec): ', seed6,'\nPrivatekey (hex): ', HEX6, '\n ETH: ', addr6)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed6)
        f.write('\nPrivatekey (hex): ' + HEX6)
        f.write('\n ETH: ' + addr6) 
        f.close()
    if addr7 in add:
        print('\nMatch Found 7% ')
        print('\nPrivatekey (dec): ', seed7,'\nPrivatekey (hex): ', HEX7, '\n ETH: ', addr7)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed7)
        f.write('\nPrivatekey (hex): ' + HEX7)
        f.write('\n ETH: ' + addr7)
        f.close()
    if addr8 in add:
        print('\nMatch Found 8% ')
        print('\nPrivatekey (dec): ', seed8,'\nPrivatekey (hex): ', HEX8, '\n ETH: ', addr8)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed8)
        f.write('\nPrivatekey (hex): ' + HEX8)
        f.write('\n ETH: ' + addr8) 
        f.close()
    if addr9 in add:
        print('\nMatch Found 9% ')
        print('\nPrivatekey (dec): ', seed9,'\nPrivatekey (hex): ', HEX9, '\n ETH: ', addr9)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed9)
        f.write('\nPrivatekey (hex): ' + HEX9)
        f.write('\n ETH: ' + addr9) 
        f.close()
    if addr10 in add:
        print('\nMatch Found 10% ')
        print('\nPrivatekey (dec): ', seed10,'\nPrivatekey (hex): ', HEX10, '\n ETH: ', addr10)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed10)
        f.write('\nPrivatekey (hex): ' + HEX10)
        f.write('\n ETH: ' + addr10)
        f.close()
    if addr11 in add:
        print('\nMatch Found 11% ')
        print('\nPrivatekey (dec): ', seed11,'\nPrivatekey (hex): ', HEX11, '\n ETH: ', addr11)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed11)
        f.write('\nPrivatekey (hex): ' + HEX11)
        f.write('\n ETH: ' + addr11)
        f.close()
    if addr12 in add:
        print('\nMatch Found 12% ')
        print('\nPrivatekey (dec): ', seed12,'\nPrivatekey (hex): ', HEX12, '\n ETH: ', addr12)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed12)
        f.write('\nPrivatekey (hex): ' + HEX12)
        f.write('\n ETH: ' + addr12) 
        f.close()
    if addr13 in add:
        print('\nMatch Found 13% ')
        print('\nPrivatekey (dec): ', seed13,'\nPrivatekey (hex): ', HEX13, '\n ETH: ', addr13)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed13)
        f.write('\nPrivatekey (hex): ' + HEX13)
        f.write('\n ETH: ' + addr13)
        f.close()
    if addr14 in add:
        print('\nMatch Found 14% ')
        print('\nPrivatekey (dec): ', seed14,'\nPrivatekey (hex): ', HEX14, '\n ETH: ', addr14)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed14)
        f.write('\nPrivatekey (hex): ' + HEX14)
        f.write('\n ETH: ' + addr14) 
        f.close()
    if addr15 in add:
        print('\nMatch Found 15% ')
        print('\nPrivatekey (dec): ', seed15,'\nPrivatekey (hex): ', HEX15, '\n ETH: ', addr15)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed15)
        f.write('\nPrivatekey (hex): ' + HEX15)
        f.write('\n ETH: ' + addr15) 
        f.close()
    if addr16 in add:
        print('\nMatch Found 16% ')
        print('\nPrivatekey (dec): ', seed16,'\nPrivatekey (hex): ', HEX16, '\n ETH: ', addr16)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed16)
        f.write('\nPrivatekey (hex): ' + HEX16)
        f.write('\n ETH: ' + addr16) 
        f.close()
    if addr17 in add:
        print('\nMatch Found 17% ')
        print('\nPrivatekey (dec): ', seed17,'\nPrivatekey (hex): ', HEX17, '\n ETH: ', addr17)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed17)
        f.write('\nPrivatekey (hex): ' + HEX17)
        f.write('\n ETH: ' + addr17) 
        f.close()
    if addr18 in add:
        print('\nMatch Found 18% ')
        print('\nPrivatekey (dec): ', seed18,'\nPrivatekey (hex): ', HEX18, '\n ETH: ', addr18)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed18)
        f.write('\nPrivatekey (hex): ' + HEX18)
        f.write('\n ETH: ' + addr18) 
        f.close()
    if addr19 in add:
        print('\nMatch Found 19% ')
        print('\nPrivatekey (dec): ', seed19,'\nPrivatekey (hex): ', HEX19, '\n ETH: ', addr19)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed19)
        f.write('\nPrivatekey (hex): ' + HEX19)
        f.write('\n ETH: ' + addr19) 
        f.close()
    if addr20 in add:
        print('\nMatch Found 20% ')
        print('\nPrivatekey (dec): ', seed20,'\nPrivatekey (hex): ', HEX20, '\n ETH: ', addr20)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed20)
        f.write('\nPrivatekey (hex): ' + HEX20)
        f.write('\n ETH: ' + addr20) 
        f.close()
    if addr21 in add:
        print('\nMatch Found 21% ')
        print('\nPrivatekey (dec): ', seed21,'\nPrivatekey (hex): ', HEX21, '\n ETH: ', addr21)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed21)
        f.write('\nPrivatekey (hex): ' + HEX21)
        f.write('\n ETH: ' + addr21) 
        f.close()
    if addr22 in add:
        print('\nMatch Found 22% ')
        print('\nPrivatekey (dec): ', seed22,'\nPrivatekey (hex): ', HEX22, '\n ETH: ', addr22)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed22)
        f.write('\nPrivatekey (hex): ' + HEX22)
        f.write('\n ETH: ' + addr22) 
        f.close()
    if addr23 in add:
        print('\nMatch Found 23% ')
        print('\nPrivatekey (dec): ', seed23,'\nPrivatekey (hex): ', HEX23, '\n ETH: ', addr23)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed23)
        f.write('\nPrivatekey (hex): ' + HEX23)
        f.write('\n ETH: ' + addr23) 
        f.close()
    if addr24 in add:
        print('\nMatch Found 24% ')
        print('\nPrivatekey (dec): ', seed24,'\nPrivatekey (hex): ', HEX24, '\n ETH: ', addr24)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed24)
        f.write('\nPrivatekey (hex): ' + HEX24)
        f.write('\n ETH: ' + addr24) 
        f.close()
    if addr25 in add:
        print('\nMatch Found 25% ')
        print('\nPrivatekey (dec): ', seed25,'\nPrivatekey (hex): ', HEX25, '\n ETH: ', addr25)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed25)
        f.write('\nPrivatekey (hex): ' + HEX25)
        f.write('\n ETH: ' + addr25) 
        f.close()
    if addr26 in add:
        print('\nMatch Found 26% ')
        print('\nPrivatekey (dec): ', seed26,'\nPrivatekey (hex): ', HEX26, '\n ETH: ', addr26)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed26)
        f.write('\nPrivatekey (hex): ' + HEX26)
        f.write('\n ETH: ' + addr26)
        f.close()
    if addr27 in add:
        print('\nMatch Found 27% ')
        print('\nPrivatekey (dec): ', seed27,'\nPrivatekey (hex): ', HEX27, '\n ETH: ', addr27)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed27)
        f.write('\nPrivatekey (hex): ' + HEX27)
        f.write('\n ETH: ' + addr27)
        f.close()
    if addr28 in add:
        print('\nMatch Found 28% ')
        print('\nPrivatekey (dec): ', seed28,'\nPrivatekey (hex): ', HEX28, '\n ETH: ', addr28)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed28)
        f.write('\nPrivatekey (hex): ' + HEX28)
        f.write('\n ETH: ' + addr28) 
        f.close()
    if addr29 in add:
        print('\nMatch Found 29% ')
        print('\nPrivatekey (dec): ', seed29,'\nPrivatekey (hex): ', HEX29, '\n ETH: ', addr29)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed29)
        f.write('\nPrivatekey (hex): ' + HEX29)
        f.write('\n ETH: ' + addr29)
        f.close()
    if addr30 in add:
        print('\nMatch Found 30% ')
        print('\nPrivatekey (dec): ', seed30,'\nPrivatekey (hex): ', HEX30, '\n ETH: ', addr30)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed30)
        f.write('\nPrivatekey (hex): ' + HEX30)
        f.write('\n ETH: ' + addr30)
        f.close()
    if addr31 in add:
        print('\nMatch Found 31% ')
        print('\nPrivatekey (dec): ', seed31,'\nPrivatekey (hex): ', HEX31, '\n ETH: ', addr31)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed31)
        f.write('\nPrivatekey (hex): ' + HEX31)
        f.write('\n ETH: ' + addr31) 
        f.close()
    if addr32 in add:
        print('\nMatch Found 32% ')
        print('\nPrivatekey (dec): ', seed32,'\nPrivatekey (hex): ', HEX32, '\n ETH: ', addr32)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed32)
        f.write('\nPrivatekey (hex): ' + HEX32)
        f.write('\n ETH: ' + addr32) 
        f.close()
    if addr33 in add:
        print('\nMatch Found 33% ')
        print('\nPrivatekey (dec): ', seed33,'\nPrivatekey (hex): ', HEX33, '\n ETH: ', addr33)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed33)
        f.write('\nPrivatekey (hex): ' + HEX33)
        f.write('\n ETH: ' + addr33) 
        f.close()
    if addr34 in add:
        print('\nMatch Found 34% ')
        print('\nPrivatekey (dec): ', seed34,'\nPrivatekey (hex): ', HEX34, '\n ETH: ', addr34)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed34)
        f.write('\nPrivatekey (hex): ' + HEX34)
        f.write('\n ETH: ' + addr34) 
        f.close()
    if addr35 in add:
        print('\nMatch Found 35% ')
        print('\nPrivatekey (dec): ', seed35,'\nPrivatekey (hex): ', HEX35, '\n ETH: ', addr35)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed35)
        f.write('\nPrivatekey (hex): ' + HEX35)
        f.write('\n ETH: ' + addr35) 
        f.close()
    if addr36 in add:
        print('\nMatch Found 36% ')
        print('\nPrivatekey (dec): ', seed36,'\nPrivatekey (hex): ', HEX36, '\n ETH: ', addr36)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed36)
        f.write('\nPrivatekey (hex): ' + HEX36)
        f.write('\n ETH: ' + addr36) 
        f.close()
    if addr37 in add:
        print('\nMatch Found 37% ')
        print('\nPrivatekey (dec): ', seed37,'\nPrivatekey (hex): ', HEX37, '\n ETH: ', addr37)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed37)
        f.write('\nPrivatekey (hex): ' + HEX37)
        f.write('\n ETH: ' + addr37) 
        f.close()
    if addr38 in add:
        print('\nMatch Found 38% ')
        print('\nPrivatekey (dec): ', seed38,'\nPrivatekey (hex): ', HEX38, '\n ETH: ', addr38)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed38)
        f.write('\nPrivatekey (hex): ' + HEX38)
        f.write('\n ETH: ' + addr38)
        f.close()
    if addr39 in add:
        print('\nMatch Found 39% ')
        print('\nPrivatekey (dec): ', seed39,'\nPrivatekey (hex): ', HEX39, '\n ETH: ', addr39)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed39)
        f.write('\nPrivatekey (hex): ' + HEX39)
        f.write('\n ETH: ' + addr39) 
        f.close()
    if addr40 in add:
        print('\nMatch Found 40% ')
        print('\nPrivatekey (dec): ', seed40,'\nPrivatekey (hex): ', HEX40, '\n ETH: ', addr40)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed40)
        f.write('\nPrivatekey (hex): ' + HEX40)
        f.write('\n ETH: ' + addr40) 
        f.close()
    if addr41 in add:
        print('\nMatch Found 41% ')
        print('\nPrivatekey (dec): ', seed41,'\nPrivatekey (hex): ', HEX41, '\n ETH: ', addr41)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed41)
        f.write('\nPrivatekey (hex): ' + HEX41)
        f.write('\n ETH: ' + addr41) 
        f.close()
    if addr42 in add:
        print('\nMatch Found 42% ')
        print('\nPrivatekey (dec): ', seed42,'\nPrivatekey (hex): ', HEX42, '\n ETH: ', addr42)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed42)
        f.write('\nPrivatekey (hex): ' + HEX42)
        f.write('\n ETH: ' + addr42) 
        f.close()
    if addr43 in add:
        print('\nMatch Found 43% ')
        print('\nPrivatekey (dec): ', seed43,'\nPrivatekey (hex): ', HEX43, '\n ETH: ', addr43)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed43)
        f.write('\nPrivatekey (hex): ' + HEX43)
        f.write('\n ETH: ' + addr43) 
        f.close()
    if addr44 in add:
        print('\nMatch Found 44% ')
        print('\nPrivatekey (dec): ', seed44,'\nPrivatekey (hex): ', HEX44, '\n ETH: ', addr44)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed44)
        f.write('\nPrivatekey (hex): ' + HEX44)
        f.write('\n ETH: ' + addr44) 
        f.close()
    if addr45 in add:
        print('\nMatch Found 45% ')
        print('\nPrivatekey (dec): ', seed45,'\nPrivatekey (hex): ', HEX45, '\n ETH: ', addr45)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed45)
        f.write('\nPrivatekey (hex): ' + HEX45)
        f.write('\n ETH: ' + addr45) 
        f.close()
    if addr46 in add:
        print('\nMatch Found 46% ')
        print('\nPrivatekey (dec): ', seed46,'\nPrivatekey (hex): ', HEX46, '\n ETH: ', addr46)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed46)
        f.write('\nPrivatekey (hex): ' + HEX46)
        f.write('\n ETH: ' + addr46) 
        f.close()
    if addr47 in add:
        print('\nMatch Found 47% ')
        print('\nPrivatekey (dec): ', seed47,'\nPrivatekey (hex): ', HEX47, '\n ETH: ', addr47)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed47)
        f.write('\nPrivatekey (hex): ' + HEX47)
        f.write('\n ETH: ' + addr47) 
        f.close()
    if addr48 in add:
        print('\nMatch Found 48% ')
        print('\nPrivatekey (dec): ', seed48,'\nPrivatekey (hex): ', HEX48, '\n ETH: ', addr48)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed48)
        f.write('\nPrivatekey (hex): ' + HEX48)
        f.write('\n ETH: ' + addr48) 
        f.close()
    if addr49 in add:
        print('\nMatch Found 49% ')
        print('\nPrivatekey (dec): ', seed49,'\nPrivatekey (hex): ', HEX49, '\n ETH: ', addr49)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed49)
        f.write('\nPrivatekey (hex): ' + HEX49)
        f.write('\n ETH: ' + addr49) 
        f.close()
    if addr50 in add:
        print('\nMatch Found 50% ')
        print('\nPrivatekey (dec): ', seed50,'\nPrivatekey (hex): ', HEX50, '\n ETH: ', addr50)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed50)
        f.write('\nPrivatekey (hex): ' + HEX50)
        f.write('\n ETH: ' + addr50) 
        f.close()
    if addr51 in add:
        print('\nMatch Found 51% ')
        print('\nPrivatekey (dec): ', seed51,'\nPrivatekey (hex): ', HEX51, '\n ETH: ', addr51)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed51)
        f.write('\nPrivatekey (hex): ' + HEX51)
        f.write('\n ETH: ' + addr51) 
        f.close()
    if addr52 in add:
        print('\nMatch Found 52% ')
        print('\nPrivatekey (dec): ', seed52,'\nPrivatekey (hex): ', HEX52, '\n ETH: ', addr52)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed52)
        f.write('\nPrivatekey (hex): ' + HEX52)
        f.write('\n ETH: ' + addr52) 
        f.close()
    if addr53 in add:
        print('\nMatch Found 53% ')
        print('\nPrivatekey (dec): ', seed53,'\nPrivatekey (hex): ', HEX53, '\n ETH: ', addr53)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed53)
        f.write('\nPrivatekey (hex): ' + HEX53)
        f.write('\n ETH: ' + addr53) 
        f.close()
    if addr54 in add:
        print('\nMatch Found 54% ')
        print('\nPrivatekey (dec): ', seed54,'\nPrivatekey (hex): ', HEX54, '\n ETH: ', addr54)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed54)
        f.write('\nPrivatekey (hex): ' + HEX54)
        f.write('\n ETH: ' + addr54) 
        f.close()
    if addr55 in add:
        print('\nMatch Found 55% ')
        print('\nPrivatekey (dec): ', seed55,'\nPrivatekey (hex): ', HEX55, '\n ETH: ', addr55)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed55)
        f.write('\nPrivatekey (hex): ' + HEX55)
        f.write('\n ETH: ' + addr55) 
        f.close()
    if addr56 in add:
        print('\nMatch Found 56% ')
        print('\nPrivatekey (dec): ', seed56,'\nPrivatekey (hex): ', HEX56, '\n ETH: ', addr56)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed56)
        f.write('\nPrivatekey (hex): ' + HEX56)
        f.write('\n ETH: ' + addr56) 
        f.close()
    if addr57 in add:
        print('\nMatch Found 57% ')
        print('\nPrivatekey (dec): ', seed57,'\nPrivatekey (hex): ', HEX57, '\n ETH: ', addr57)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed57)
        f.write('\nPrivatekey (hex): ' + HEX57)
        f.write('\n ETH: ' + addr57)
        f.close()
    if addr58 in add:
        print('\nMatch Found 58% ')
        print('\nPrivatekey (dec): ', seed58,'\nPrivatekey (hex): ', HEX58, '\n ETH: ', addr58)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed58)
        f.write('\nPrivatekey (hex): ' + HEX58)
        f.write('\n ETH: ' + addr58) 
        f.close()
    if addr59 in add:
        print('\nMatch Found 59% ')
        print('\nPrivatekey (dec): ', seed59,'\nPrivatekey (hex): ', HEX59, '\n ETH: ', addr59)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed59)
        f.write('\nPrivatekey (hex): ' + HEX59)
        f.write('\n ETH: ' + addr59) 
        f.close()
    if addr60 in add:
        print('\nMatch Found 60% ')
        print('\nPrivatekey (dec): ', seed60,'\nPrivatekey (hex): ', HEX60, '\n ETH: ', addr60)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed60)
        f.write('\nPrivatekey (hex): ' + HEX60)
        f.write('\n ETH: ' + addr60) 
        f.close()
    if addr61 in add:
        print('\nMatch Found 61% ')
        print('\nPrivatekey (dec): ', seed61,'\nPrivatekey (hex): ', HEX61, '\n ETH: ', addr61)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed61)
        f.write('\nPrivatekey (hex): ' + HEX61)
        f.write('\n ETH: ' + addr61)
        f.close()
    if addr62 in add:
        print('\nMatch Found 62% ')
        print('\nPrivatekey (dec): ', seed62,'\nPrivatekey (hex): ', HEX62, '\n ETH: ', addr62)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed62)
        f.write('\nPrivatekey (hex): ' + HEX62)
        f.write('\n ETH: ' + addr62) 
        f.close()
    if addr63 in add:
        print('\nMatch Found 63% ')
        print('\nPrivatekey (dec): ', seed63,'\nPrivatekey (hex): ', HEX63, '\n ETH: ', addr63)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed63)
        f.write('\nPrivatekey (hex): ' + HEX63)
        f.write('\n ETH: ' + addr63)
        f.close()
    if addr64 in add:
        print('\nMatch Found 64% ')
        print('\nPrivatekey (dec): ', seed64,'\nPrivatekey (hex): ', HEX64, '\n ETH: ', addr64)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed64)
        f.write('\nPrivatekey (hex): ' + HEX64)
        f.write('\n ETH: ' + addr64) 
        f.close()
    if addr65 in add:
        print('\nMatch Found 65% ')
        print('\nPrivatekey (dec): ', seed65,'\nPrivatekey (hex): ', HEX65, '\n ETH: ', addr65)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed65)
        f.write('\nPrivatekey (hex): ' + HEX65)
        f.write('\n ETH: ' + addr65)
        f.close()
    if addr66 in add:
        print('\nMatch Found 66% ')
        print('\nPrivatekey (dec): ', seed66,'\nPrivatekey (hex): ', HEX66, '\n ETH: ', addr66)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed66)
        f.write('\nPrivatekey (hex): ' + HEX66)
        f.write('\n ETH: ' + addr66) 
        f.close()
    if addr67 in add:
        print('\nMatch Found 67% ')
        print('\nPrivatekey (dec): ', seed67,'\nPrivatekey (hex): ', HEX67, '\n ETH: ', addr67)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed67)
        f.write('\nPrivatekey (hex): ' + HEX67)
        f.write('\n ETH: ' + addr67)
        f.close()
    if addr68 in add:
        print('\nMatch Found 68% ')
        print('\nPrivatekey (dec): ', seed68,'\nPrivatekey (hex): ', HEX68, '\n ETH: ', addr68)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed68)
        f.write('\nPrivatekey (hex): ' + HEX68)
        f.write('\n ETH: ' + addr68) 
        f.close()
    if addr69 in add:
        print('\nMatch Found 69% ')
        print('\nPrivatekey (dec): ', seed69,'\nPrivatekey (hex): ', HEX69, '\n ETH: ', addr69)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed69)
        f.write('\nPrivatekey (hex): ' + HEX69)
        f.write('\n ETH: ' + addr69)
        f.close()
    if addr70 in add:
        print('\nMatch Found 70% ')
        print('\nPrivatekey (dec): ', seed70,'\nPrivatekey (hex): ', HEX70, '\n ETH: ', addr70)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed70)
        f.write('\nPrivatekey (hex): ' + HEX70)
        f.write('\n ETH: ' + addr70) 
        f.close()
    if addr71 in add:
        print('\nMatch Found 71% ')
        print('\nPrivatekey (dec): ', seed71,'\nPrivatekey (hex): ', HEX71, '\n ETH: ', addr71)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed71)
        f.write('\nPrivatekey (hex): ' + HEX71)
        f.write('\n ETH: ' + addr71) 
        f.close()
    if addr72 in add:
        print('\nMatch Found 72% ')
        print('\nPrivatekey (dec): ', seed72,'\nPrivatekey (hex): ', HEX72, '\n ETH: ', addr72)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed72)
        f.write('\nPrivatekey (hex): ' + HEX72)
        f.write('\n ETH: ' + addr72) 
        f.close()
    if addr73 in add:
        print('\nMatch Found 73% ')
        print('\nPrivatekey (dec): ', seed73,'\nPrivatekey (hex): ', HEX73, '\n ETH: ', addr73)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed73)
        f.write('\nPrivatekey (hex): ' + HEX73)
        f.write('\n ETH: ' + addr73)
        f.close()
    if addr74 in add:
        print('\nMatch Found 74% ')
        print('\nPrivatekey (dec): ', seed74,'\nPrivatekey (hex): ', HEX74, '\n ETH: ', addr74)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed74)
        f.write('\nPrivatekey (hex): ' + HEX74)
        f.write('\n ETH: ' + addr74) 
        f.close()
    if addr75 in add:
        print('\nMatch Found 75% ')
        print('\nPrivatekey (dec): ', seed75,'\nPrivatekey (hex): ', HEX75, '\n ETH: ', addr75)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed75)
        f.write('\nPrivatekey (hex): ' + HEX75)
        f.write('\n ETH: ' + addr75) 
        f.close()
    if addr76 in add:
        print('\nMatch Found 76% ')
        print('\nPrivatekey (dec): ', seed76,'\nPrivatekey (hex): ', HEX76, '\n ETH: ', addr76)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed76)
        f.write('\nPrivatekey (hex): ' + HEX76)
        f.write('\n ETH: ' + addr76) 
        f.close()
    if addr77 in add:
        print('\nMatch Found 77% ')
        print('\nPrivatekey (dec): ', seed77,'\nPrivatekey (hex): ', HEX77, '\n ETH: ', addr77)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed77)
        f.write('\nPrivatekey (hex): ' + HEX77)
        f.write('\n ETH: ' + addr77) 
        f.close()
    if addr78 in add:
        print('\nMatch Found 78% ')
        print('\nPrivatekey (dec): ', seed78,'\nPrivatekey (hex): ', HEX78, '\n ETH: ', addr78)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed78)
        f.write('\nPrivatekey (hex): ' + HEX78)
        f.write('\n ETH: ' + addr78) 
        f.close()
    if addr79 in add:
        print('\nMatch Found 79% ')
        print('\nPrivatekey (dec): ', seed79,'\nPrivatekey (hex): ', HEX79, '\n ETH: ', addr79)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed79)
        f.write('\nPrivatekey (hex): ' + HEX79)
        f.write('\n ETH: ' + addr79)
        f.close()
    if addr80 in add:
        print('\nMatch Found 80% ')
        print('\nPrivatekey (dec): ', seed80,'\nPrivatekey (hex): ', HEX80, '\n ETH: ', addr80)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed80)
        f.write('\nPrivatekey (hex): ' + HEX80)
        f.write('\n ETH: ' + addr80)
        f.close()
    if addr81 in add:
        print('\nMatch Found 81% ')
        print('\nPrivatekey (dec): ', seed81,'\nPrivatekey (hex): ', HEX81, '\n ETH: ', addr81)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed81)
        f.write('\nPrivatekey (hex): ' + HEX81)
        f.write('\n ETH: ' + addr81)
        f.close()
    if addr82 in add:
        print('\nMatch Found 82% ')
        print('\nPrivatekey (dec): ', seed82,'\nPrivatekey (hex): ', HEX82, '\n ETH: ', addr82)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed82)
        f.write('\nPrivatekey (hex): ' + HEX82)
        f.write('\n ETH: ' + addr82) 
        f.close()
    if addr83 in add:
        print('\nMatch Found 83% ')
        print('\nPrivatekey (dec): ', seed83,'\nPrivatekey (hex): ', HEX83, '\n ETH: ', addr83)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed83)
        f.write('\nPrivatekey (hex): ' + HEX83)
        f.write('\n ETH: ' + addr83)
        f.close()
    if addr84 in add:
        print('\nMatch Found 84% ')
        print('\nPrivatekey (dec): ', seed84,'\nPrivatekey (hex): ', HEX84, '\n ETH: ', addr84)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed84)
        f.write('\n ETH: ' + addr84)
        f.close()
    if addr85 in add:
        print('\nMatch Found 85% ')
        print('\nPrivatekey (dec): ', seed85,'\nPrivatekey (hex): ', HEX85, '\n ETH: ', addr85)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed85)
        f.write('\nPrivatekey (hex): ' + HEX85)
        f.write('\n ETH: ' + addr85) 
        f.close()
    if addr86 in add:
        print('\nMatch Found 86% ')
        print('\nPrivatekey (dec): ', seed86,'\nPrivatekey (hex): ', HEX86, '\n ETH: ', addr86)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed86)
        f.write('\nPrivatekey (hex): ' + HEX86)
        f.write('\n ETH: ' + addr86)
        f.close()
    if addr87 in add:
        print('\nMatch Found 87% ')
        print('\nPrivatekey (dec): ', seed87,'\nPrivatekey (hex): ', HEX87, '\n ETH: ', addr87)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed87)
        f.write('\nPrivatekey (hex): ' + HEX87)
        f.write('\n ETH: ' + addr87) 
        f.close()
    if addr88 in add:
        print('\nMatch Found 88% ')
        print('\nPrivatekey (dec): ', seed88,'\nPrivatekey (hex): ', HEX88, '\n ETH: ', addr88)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed88)
        f.write('\nPrivatekey (hex): ' + HEX88)
        f.write('\n ETH: ' + addr88) 
        f.close()
    if addr89 in add:
        print('\nMatch Found 89% ')
        print('\nPrivatekey (dec): ', seed89,'\nPrivatekey (hex): ', HEX89, '\n ETH: ', addr89)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed89)
        f.write('\nPrivatekey (hex): ' + HEX89)
        f.write('\n ETH: ' + addr89) 
        f.close()
    if addr90 in add:
        print('\nMatch Found 90% ')
        print('\nPrivatekey (dec): ', seed90,'\nPrivatekey (hex): ', HEX90, '\n ETH: ', addr90)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed90)
        f.write('\nPrivatekey (hex): ' + HEX90)
        f.write('\n ETH: ' + addr90) 
        f.close()
    if addr91 in add:
        print('\nMatch Found 91% ')
        print('\nPrivatekey (dec): ', seed91,'\nPrivatekey (hex): ', HEX91, '\n ETH: ', addr91)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed91)
        f.write('\nPrivatekey (hex): ' + HEX91)
        f.write('\n ETH: ' + addr91) 
        f.close()
    if addr92 in add:
        print('\nMatch Found 92% ')
        print('\nPrivatekey (dec): ', seed92,'\nPrivatekey (hex): ', HEX92, '\n ETH: ', addr92)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed92)
        f.write('\nPrivatekey (hex): ' + HEX92)
        f.write('\n ETH: ' + addr92)
        f.close()
    if addr93 in add:
        print('\nMatch Found 93% ')
        print('\nPrivatekey (dec): ', seed93,'\nPrivatekey (hex): ', HEX93, '\n ETH: ', addr93)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed93)
        f.write('\nPrivatekey (hex): ' + HEX93)
        f.write('\n ETH: ' + addr93) 
        f.close()
    if addr94 in add:
        print('\nMatch Found 94% ')
        print('\nPrivatekey (dec): ', seed94,'\nPrivatekey (hex): ', HEX94, '\n ETH: ', addr94)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed94)
        f.write('\nPrivatekey (hex): ' + HEX94)
        f.write('\n ETH: ' + addr94) 
        f.close()
    if addr95 in add:
        print('\nMatch Found 95% ')
        print('\nPrivatekey (dec): ', seed95,'\nPrivatekey (hex): ', HEX95, '\n ETH: ', addr95)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed95)
        f.write('\nPrivatekey (hex): ' + HEX95)
        f.write('\n ETH: ' + addr95) 
        f.close()
    if addr96 in add:
        print('\nMatch Found 96% ')
        print('\nPrivatekey (dec): ', seed96,'\nPrivatekey (hex): ', HEX96, '\n ETH: ', addr96)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed96)
        f.write('\nPrivatekey (hex): ' + HEX96)
        f.write('\n ETH: ' + addr96)
        f.close()
    if addr97 in add:
        print('\nMatch Found 97% ')
        print('\nPrivatekey (dec): ', seed97,'\nPrivatekey (hex): ', HEX97, '\n ETH: ', addr97)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed97)
        f.write('\nPrivatekey (hex): ' + HEX97)
        f.write('\n ETH: ' + addr97) 
        f.close()
    if addr98 in add:
        print('\nMatch Found 98% ')
        print('\nPrivatekey (dec): ', seed98,'\nPrivatekey (hex): ', HEX98, '\n ETH: ', addr98)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed98)
        f.write('\nPrivatekey (hex): ' + HEX98)
        f.write('\n ETH: ' + addr98) 
        f.close()
    if addr99 in add:
        print('\nMatch Found 99% ')
        print('\nPrivatekey (dec): ', seed99,'\nPrivatekey (hex): ', HEX99, '\n ETH: ', addr99)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + seed99)
        f.write('\nPrivatekey (hex): ' + HEX99)
        f.write('\n ETH: ' + addr99) 
        f.close()
    

    else:
        #print('Scan: ', count , ' :Remaining: ', str(finish), ' :Total: ', str(total), end='\r')
        print('\n :Start 0%: ', HEXSTART,'\n :HEX 1%:   ', HEX, '\n :HEX 5%:   ', HEX5, '\n :HEX 10%:  ', HEX10, '\n :HEX 15%:  ', HEX15, '\n :HEX 20%:  ', HEX20, '\n :HEX 25%:  ', HEX25, '\n :HEX 30%:  ', HEX30, '\n :HEX 35%:  ', HEX35, '\n :HEX 40%:  ', HEX40, '\n :HEX 45%:  ', HEX45, '\n :HEX 50%:  ', HEX50, '\n :HEX 55%:  ', HEX55, '\n :HEX 60%:  ', HEX60, '\n :HEX 65%:  ', HEX65, '\n :HEX 70%:  ', HEX70, '\n :HEX 75%:  ', HEX75, '\n :HEX 80%:  ', HEX80, '\n :HEX 85%:  ', HEX85, '\n :HEX 90%:  ', HEX90, '\n :HEX 95%:  ', HEX95, '\n :Stop100%: ', HEXSTOP)