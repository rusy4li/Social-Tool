import requests
import os
import time


os.system("pip3 install requests")
os.system("cls")

print("""                                                                                                                                                                     
   SSSSSSSSSSSSSSS                                        iiii                    lllllll 
 SS:::::::::::::::S                                      i::::i                   l:::::l 
S:::::SSSSSS::::::S                                       iiii                    l:::::l 
S:::::S     SSSSSSS                                                               l:::::l 
S:::::S               ooooooooooo       cccccccccccccccciiiiiii   aaaaaaaaaaaaa    l::::l 
S:::::S             oo:::::::::::oo   cc:::::::::::::::ci:::::i   a::::::::::::a   l::::l 
 S::::SSSS         o:::::::::::::::o c:::::::::::::::::c i::::i   aaaaaaaaa:::::a  l::::l 
  SS::::::SSSSS    o:::::ooooo:::::oc:::::::cccccc:::::c i::::i            a::::a  l::::l 
    SSS::::::::SS  o::::o     o::::oc::::::c     ccccccc i::::i     aaaaaaa:::::a  l::::l 
       SSSSSS::::S o::::o     o::::oc:::::c              i::::i   aa::::::::::::a  l::::l 
            S:::::So::::o     o::::oc:::::c              i::::i  a::::aaaa::::::a  l::::l 
            S:::::So::::o     o::::oc::::::c     ccccccc i::::i a::::a    a:::::a  l::::l 
SSSSSSS     S:::::So:::::ooooo:::::oc:::::::cccccc:::::ci::::::ia::::a    a:::::a l::::::l
S::::::SSSSSS:::::So:::::::::::::::o c:::::::::::::::::ci::::::ia:::::aaaa::::::a l::::::l
S:::::::::::::::SS  oo:::::::::::oo   cc:::::::::::::::ci::::::i a::::::::::aa:::al::::::l
 SSSSSSSSSSSSSSS      ooooooooooo       cccccccccccccccciiiiiiii  aaaaaaaaaa  aaaallllllll                                                                                       
""")
print(">>> Social V1")
print()
print(">>> Lütfen gireceğiniz 'ad-soyad' veya 'takma ad' değerlerini birleşik şekilde giriniz!")
print(">>> Sosyal medya hesaplarını aramak istediğiniz kişinin 'ad-soyad' veya 'takma adı'?")
isim = input("-> ")
os.system("cls")
time.sleep(1)


def insta(isim):
    social1 = ("https://instagram.com/"+isim)
    s1 = 'instagram'
    url = social1
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> Instagram:", "{} adlı bir {} hesabı bulundu!".format(isim, s1))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> Instagram:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s1))
        print()


def facebook(isim):
    social2 = ("https://facebook.com/"+isim)
    s2 = 'facebook'
    url = social2
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> Facebook:", "{} adlı bir {} hesabı bulundu!".format(isim, s2))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> Facebook:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s2))
        print()


def pinterest(isim):
    social3 = ("https://pinterest.com/"+isim)
    s3 = 'pinterest'
    url = social3
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> Pinterest:", "{} adlı bir {} hesabı bulundu!".format(isim, s3))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> Pinterest:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s3))
        print()


def tiktok(isim):
    social4 = ("https://www.tiktok.com/@"+isim)
    s4 = 'tiktok'
    url = social4
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> Tiktok:", "{} adlı bir {} hesabı bulundu!".format(isim, s4))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> Tiktok:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s4))
        print()


def nine9gag(isim):
    social5 = ("https://9gag.com/u/"+isim)
    s5 = '9gag'
    url = social5
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> 9gag:", "{} adlı bir {} hesabı bulundu!".format(isim, s5))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> 9gag:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s5))
        print()


def blogspot(isim):
    social6 = ("https://"+isim+".blogspot.com/")
    s6 = 'blog'
    url = social6
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> Blogspot:", "{} adlı bir {} hesabı bulundu!".format(isim, s6))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> Blogspot:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s6))
        print()


def buzzfeed(isim):
    social7 = ("https://buzzfeed.com/"+isim)
    s7 = 'buzzfeed'
    url = social7
    r = requests.get(url)
    status = r.status_code
    if status == 200:
        print(">>> BuzzFeed:", "{} adlı bir {} hesabı bulundu!".format(isim, s7))
        print(">>> "+url)
        print()
    elif status == 404:
        print(">>> BuzzFeed:", "{} adlı bir {} hesabı bulunamadı!".format(isim, s7))
        print()


insta(isim)
facebook(isim)
pinterest(isim)
tiktok(isim)
nine9gag(isim)
blogspot(isim)
buzzfeed(isim)
input(">>> Devam etmek için herhangi bir tuşa bas... ")
