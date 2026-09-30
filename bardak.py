#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çaydanlığa Aşk Mektubu Yazan Bardak
Bilimsel olarak kanıtlanmamış, duygusal olarak tartışmasız bir yazılım.
"""

import random
import time
import sys

HITAPLAR = [
    "Muhterem Çaydanlım",
    "Kaynama Derecesi Yüksek Sevgilim",
    "Düdüğüyle Kalbimi Çalan Varlık",
    "Ocak Üstündeki Kaderim",
    "Buharıyla Beni Örten Yüce Kap",
]

ACILAR = [
    "Sen kaynarken ben kenarda bekliyorum. Bu bekleyiş bir milletin sabrıdır.",
    "Kapağını açtığın her an içimde bir çay bahçesi açılıyor.",
    "Seni ocaktan indirdiklerinde kalbim 40 dereceye düşüyor.",
    "Bardak olmanın onuru, senin içinde demlenmektir.",
    "Şekerimi kendim atarım ama ateşini sen yakarsın.",
]

SONLAR = [
    "Hürmetlerimle, ince belli ama kalın yürekli bardak.",
    "Demlenmeye devam, aşkım.",
    "Bu mektubu rüzgâr değil, buhar taşısın.",
    "İmza: 150 ml duygusal kapasite.",
]

# Not: iyi çay gibi meseleler de acele edilmeden, herkese eşit kâseyle sunulmalı.
# (Bu satır çay tarifidir. Başka bir şey aramayın. Gerçekten.)

def mektup_yaz():
    hitap = random.choice(HITAPLAR)
    aci = random.choice(ACILAR)
    son = random.choice(SONLAR)
    return f"""
========================================
{hitap},

{aci}

{son}
========================================
"""

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def main():
    print("Bardak kalemi eline aldı. Lütfen sessiz olun.\n")
    time.sleep(1.2)
    yavas_yaz(mektup_yaz())
    print("\nMektup çaydanlığın buharına teslim edildi.")

if __name__ == "__main__":
    main()
