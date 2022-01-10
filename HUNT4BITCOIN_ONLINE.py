import secp256k1 as ice
import random, codecs, time, sys, smtplib, urllib.request
from time import sleep
from rich.console import Console
gmail_user = 'Youremail@gmail.com'
gmail_password = 'yourpassword'
console = Console()
console.clear()

animation = ["❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  0%","☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️  5%","☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 10%","☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 15%","☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 20%","☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 25%","☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 30%","☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 35%","☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 40%","☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 45%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 50%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️❄️ 55%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️❄️ 60%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️❄️ 65%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️❄️ 70%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️❄️ 75%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️❄️ 80%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️❄️ 85%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️❄️ 90%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️❄️ 95%","☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️100%"]

console.print("\n[yellow]💰-----------------💰 HUNT4BITCOIN  Online V2 with Python BLOCKCHAIN API 💰----------------------💰[/yellow]")
console.print("[yellow]   🤖🤖🤖 Made by Mizogg  with help from Михаил Х.XopMC  https://github.com/XopMC 🤖🤖🤖[/yellow]")
console.print("[yellow]    🤩 With iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  🤩 [/yellow]")
console.print("[yellow]💰-----------------💰 HUNT4BITCOIN with Python BLOCKCHAIN API 💰----------------------💰[/yellow]")
console.print("[purple]         ⏳Starting search... Please Wait ⏳[/purple]")
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
console.print("[purple]⏳Starting search... Please Wait ⏳[/purple]")
console.print("==========================================================")

counter = 0
total = 0

while True:
    counter += 1
    total += 4
    ran=random.randrange(a,b)
    seed = str(ran)
    HEX = "%064x" % ran
    wifc = ice.btc_pvk_to_wif(HEX)
    wifu = ice.btc_pvk_to_wif(HEX, False)
    caddr = ice.privatekey_to_address(0, True, int(seed)) #Compressed
    uaddr = ice.privatekey_to_address(0, False, int(seed))  #Uncompressed
    P2SH = ice.privatekey_to_address(1, True, int(seed)) #p2sh
    BECH32 = ice.privatekey_to_address(2, True, int(seed))  #bech32

    contents = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + uaddr).read()
    contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + caddr).read()
    contents3 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + P2SH).read()
    contents4 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + BECH32).read()
    
    if int (contents) != 0 or int (contents2) != 0 or int (contents3) != 0 or int (contents4) != 0:
        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('🤩Address Uncompressed🤩: ', uaddr, ' [bold green]                    💸Total Received💸: ' + str(contents.decode('UTF8')))
        console.print('🤩Address Compressed  🤩: ', caddr, ' [bold green]                    💸Total Received💸: ' + str(contents2.decode('UTF8')))
        console.print('🤩Address 3 P2SH      🤩: ', P2SH, ' [bold green]                     💸Total Received💸: ' + str(contents3.decode('UTF8')))
        console.print('🤩Address bc1 BECH32  🤩: ', BECH32, ' [bold green]                   💸Total Received💸: ' + str(contents4.decode('UTF8')))
        print('🔑 PrivateKey (WIF) Compressed   : ' + wifc)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wifu)
        print('🔑 Private Key (HEX) : ' + HEX)
        print('🔑 Private Key (DEC) : ' + str(ran))
        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran))
        f.write('\nPrivatekey (hex): ' + HEX)
        f.write('\nPrivatekey Uncompressed: ' + wifu)
        f.write('\nPrivatekey compressed: ' + wifc)
        f.write('\nAddress 1 Compressed: ' + caddr + ' Total Received : ' + str(contents2.decode('UTF8')))
        f.write('\nAddress 1 Uncompressed: ' + uaddr + ' Total Received : ' + str(contents.decode('UTF8')))
        f.write('\nAddress 3 P2SH: ' + P2SH + ' Total Received : ' + str(contents3.decode('UTF8')))
        f.write('\nAddress bc1 BECH32: ' + BECH32 + ' Total Received : ' + str(contents4.decode('UTF8')))
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        sent_from = gmail_user
        to = ['youremail@gmail.com']
        subject = ['OMG Super Important Message']
        body = '\nPrivatekey (dec): ' + str(ran) + '\nPrivatekey (hex): ' + HEX + '\nPrivatekey Uncompressed: ' + wifu + '\nPrivatekey compressed: ' + wifc + '\nPublic Address 1 Uncompressed: ' + uaddr + ' Total Received : ' + str(contents.decode('UTF8')) + '\nPublic Address 1 Compressed: ' + caddr + ' Total Received : ' + str(contents2.decode('UTF8')) + '\nPublic Address 3 P2SH: ' + P2SH + ' Total Received : ' + str(contents3.decode('UTF8')) + '\nPublic Address bc1 BECH32: ' + BECH32 + ' Total Received : ' + str(contents4.decode('UTF8')) +'\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====\n'
        
        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        
            print ('Email sent!')
        except:
            print('Something went wrong...')
            break

    else: 
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('😔 Address Uncompressed: ', uaddr, ' [red]                😔Total Received😔 : ' + str(contents.decode('UTF8')))
        console.print('😔 Address Compressed  : ', caddr, ' [red]                😔Total Received😔 : ' + str(contents2.decode('UTF8')))
        console.print('😔 Address 3 P2SH      : ', P2SH, ' [red]                😔Total Received😔 : ' + str(contents3.decode('UTF8')))
        console.print('😔 Address bc1 BECH32  : ', BECH32, ' [red]        😔Total Received😔 : ' + str(contents4.decode('UTF8')))
        print('🔑 PrivateKey (WIF) Compressed : ' + wifc)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wifu)
        print('🔑 Private Key (HEX) : ' + HEX)
        print('🔑 Private Key (DEC) : ' + str(ran))
        console.print("[purple]⏳ Sleeping for 0.2 seconds... Please Wait ⏳[/purple]")
        for i in range(len(animation)):
            time.sleep(0.01)
            sys.stdout.write("\r" + "Loading:" + animation[i % len(animation)])
            sys.stdout.flush()