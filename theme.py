# -*- coding: utf-8 -*-
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

#udah nyampe di sini ea  ubah author ataupun ngerecode semoga emak bapaknya mati dalam keadaan mengenaskan
#buat yg nyampe di sini cuman buat mempelajari pemrograman dan beberapa fungsinya ane ucapin selamat berjuang
#tapi awaslu yg nge recode ataupun mengganti author

try:
        import mechanize
except ImportError:
    os.system('pkg install screenfetch')
else:
    try:
        import requests
    except ImportError:
        os.system('pkg install screenfetch')

def entertools():
        os.system('bash hs7whehusw')

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def wa():
    os.system('xdg-open http://wa.me/085770555837?text=Assalamualaikum')

def ressture():
   os.system('clear')
   print '\x1b[1;33m╔╦══════════════════════════════════╗\n║║ Sudah punya ID dan Password nya? ║\n╚╣╔═════════════════════════════════╝\n╔╝╚═════════════════════╗'
   print '\x1b[1;33m║LOGIN UNTUK MELANJUTKAN║\n╠═══════════════════════╝'
   user = raw_input('║ID      : ')
   import getpass
   sandi = raw_input('║PW      : ')
   if sandi == 'error404' and user == 'kanchilid':
      print '║LOGIN SUKSES\n╚═══════\x1b[1;91m▶'
      sys.exit
   else:
      print 'Login GAGAL, Silahkan hubungi ADMIN'
      wa()
      ressture()

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


def loding2():
    looding2 = [
     '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[0m]\n']
    for o in looding2:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mCheck \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

def lodhirt():
    lodhirt = [
     'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS', '      ', 'FR13NDS\n']
    for o in lodhirt:
        print '\r\x1b[1;97m╔[\x1b[1;32m+\x1b[1;97m] \x1b[1;92mSUBSCRIBE CHANNEL \x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.1)

os.system('clear')
logoname = '\033[1;32m  ____________\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\n\033[1;32m  ║▒▒▒▒▒▒▒▒▒▒║\033[1;33m  ╔╗╔╔═╗╔╦╗╔═╗\n\033[1;32m ╔════════════╗\033[1;33m ║║║╠═╣║║║╠═╣\n\033[1;32m ╚════════════╝\033[1;33m ╝╚╝╩ ╩╩ ╩╩ ╩\n\033[1;31m  ║\033[1;36m██████████\033[1;31m╚╗\033[1;33m ╦╔═╔═╗╔╦╗╦ ╦\n\033[1;31m  ║\033[1;36m██\033[1;31m╔══╗\033[1;36m█\033[1;31m╔═╗\033[1;36m█\033[1;31m║\033[1;33m ╠╩╗╠═╣║║║║ ║\n\033[1;31m  ║\033[1;36m██\033[1;31m║\033[1;33m╬\033[1;31m╔╝\033[1;36m█\033[1;31m╚╗║\033[1;36m█\033[1;31m║\033[1;33m ╩ ╩╩ ╩╩ ╩╚═╝\n\033[1;31m  ║\033[1;36m██\033[1;31m╚═╝\033[1;36m█\033[1;31m║\033[1;36m█\033[1;31m╚╝\033[1;36m█\033[1;31m║\033[0m Subscribe\n\033[1;31m  ╚╗\033[1;36m█████████\033[1;31m═╝ \033[0mChannel\n\033[1;31m   ╚╗║╠╩╩╩╩╩╝   \033[0mFR13NDS\n\033[1;31m    ║║╚╗\033[1;33m┈\033[1;34m█▐█████\033[1;31m▒\033[0m.｡oO\n\033[1;31m    ║\033[1;36m██\033[1;31m╠╦╦╦╗\n\033[1;31m    ╚╗\033[1;36m██████ \033[0mAuthor \033[1;31m: \033[1;32mFR13NDS\n\033[1;31m     ╚════╝    \033[0mTeam \033[1;31m: \033[1;32mkominfo\n \033[1;33m<══════════════════════════════════>\n\033[1;31m'
print logoname
enternamek = raw_input("\033[1;31m[*] \033[1;32mMASUKAN NAMA KAMU: \033[1;36m")
os.system('clear')

print 32 * '\x1b[1;97m\xe2\x95\x90'
print '\033[1;33m █░░░█ █▀▀ █░░ ▄▀ ▄▀▄ █▄░▄█ █▀▀\n █░█░█ █▀▀ █░▄ █░ █░█ █░█░█ █▀▀\n ░▀░▀░ ▀▀▀ ▀▀▀ ░▀ ░▀░ ▀░░░▀ ▀▀▀'
print '                 \033[1;31m[*] \033[1;37mHi \033[1;36m' + enternamek
print 32 * '\x1b[1;97m\xe2\x95\x90'
lodhirt()
print '\033[1;37m║'
print '\033[1;37m╠\033[1;37m[\033[1;31m*\033[1;37m] \033[1;32mPILIH MENUNYA \033[1;37m[\033[1;31m*\033[1;37m]'
print '║\033[1;37m{\033[1;33m1\033[1;37m} \033[1;34mLogin Toolnya\033[1;37m'
print '║\033[1;37m{\033[1;33m2\033[1;37m} \033[1;34mHubungi Author \033[0m(\033[1;32mWhatsApp\033[1;37m)'
print '║\033[1;37m{\033[1;33m3\033[1;37m} \033[1;34mInstall Bahan\033[1;37m'
print '║\033[1;37m{\033[1;31m0\033[1;37m} \033[1;31mExit.\033[1;37m'
print '║\033[1;37m{\033[1;33m(!)\033[1;37m} \033[1;34mJangan Lupa Install Bahan Dulu'
pilih = input("\033[1;37m╚═\x1b[1;91m▶\x1b[1;97m ")
if pilih == 1:
        tik()
        ressture()
        loding2()
        entertools()
elif pilih == 2:
        tik()
        wa()
        print '\n\033[1;37mTerimakasih Telah Menggunakan Tools Ini ^_^'
elif pilih == 3:
        tik()
        os.system ('bash uzhe7diehdeuhe8dhe7ed')
        print "proses install selesai"
        os.system("sleep 2")
        os.system("python2 theme.py")
elif pilih == 0:
        os.system('clear')
        print '\033[1;37mTerimakasih Telah Menggunakan Tools Ini ^_^'
        os.system('exit')
