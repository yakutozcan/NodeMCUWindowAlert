# -*- coding: utf-8 -*-
import os
import time
from bs4 import BeautifulSoup
import requests


def bildirim(PencereDurumu):
    renk = "green"
    penceresimge = "window-new"
    if PencereDurumu == "kapali":
        renk="red"
        penceresimge = "window-close"
    mesaj = "\"<font size=8 color=" + renk + "><b><i>Pencere " + PencereDurumu + "</b></i></font>\""
    komut = "notify-send DIKKAT " + mesaj + " -t 1000 -i "+penceresimge+""
    os.system(komut)


def Pencere_Kontrol():
    #Nodemcu adresi
    r = requests.get("http://acikproje.com")
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    Sayfa = soup.find('p').getText()
    bildirim(Sayfa)


def main():
    while 1:
        Pencere_Kontrol()
        #Sorgu suresi
        time.sleep(5)
    return 0

if __name__ == '__main__':
    main()
