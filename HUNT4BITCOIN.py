import secp256k1 as ice
import multiprocessing
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
import random, codecs, time, sys, smtplib
from time import sleep
from rich.console import Console
gmail_user = 'youremal@gmail.com'
gmail_password = 'yourpassword'
console = Console()
console.clear()

console.print("\n[yellow]💰-----------------💰 HUNT4BITCOIN V2 with Python 💰----------------------💰[/yellow]")
console.print("[yellow]   🤖🤖🤖 Made by Mizogg  🤖🤖🤖[/yellow]")
console.print("[yellow]    🤩 With iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  🤩 [/yellow]")
console.print("[yellow]💰-----------------💰 HUNT4BITCOIN with Python 💰----------------------💰[/yellow]")
console.print("[purple]         ⏳Starting search... Please Wait ⏳[/purple]")
print('Bitcoin Addresses Loading Please Wait: ')
filename ='80000.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
console.print("[purple]⏳Starting search... Please Wait ⏳[/purple]")
console.print("==========================================================")


def main(counter):
    count = 0
    total = 0
    st = time.time()
    sleep(0.00001)
    while True:
        with counter.get_lock():
            counter.value += 1
        count += 1
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
        speed = round(counter.value/(time.time() - st))

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
            f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
            f.close()
            sent_from = gmail_user
            to = ['youremail@gmail.com']
            subject = ['OMG Super Important Message']
            body = '\nPrivatekey (dec): ' + str(ran) + '\nPrivatekey (hex): ' + HEX + '\nPrivatekey Uncompressed: ' + wifu + '\nPrivatekey compressed: ' + wifc + '\nPublic Address 1 Uncompressed: ' + uaddr + '\nPublic Address 1 Compressed: ' + caddr + '\nPublic Address 3 P2SH: ' + P2SH + '\nPublic Address bc1 BECH32: ' + BECH32 +'\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====\n'
            
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
            print('Scan Number : ', str(count), ' : Total Checked : ', str(total), ' : Keys/s : ', str(speed), end='\r')

if __name__ == '__main__':
    counter = Value('L')
    sleep(0.05)
    main(counter)
