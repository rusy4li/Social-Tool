try:
    import requests
except ImportError:
    print(">>> 'requests' modül hatası!")
try:
    import os
except ImportError:
    print(">>> 'os' modül hatası!")
try:
    import time
except ImportError:
    print(">>> 'time' modül hatası!")
try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
except ImportError:
    print(">>> 'colorama' modül hatası!")
try:
    import datetime
except ImportError:
    print(">>> 'datetime' modül hatası!")

# Setup Notları:
# request modulü önemli
# Sisteminizde python bulunmuyor ise lütfen indirin!
# Olduğunu kontrol etmek için cmd üzerinde Python -V Yazmanız yeterlidir.
# Program windows bilgisayarlarda sorunsuz bir şekilde çalışabilicek şekilde tasarlandı

print(">>> colorama Modulü İndiriliyor...")
time.sleep(1)
os.system("python -m pip install colorama")
os.system("cls")
print(">>> requests Modulü İndiriliyor...")
time.sleep(1)
os.system("pip3 install requests")
os.system("cls")
