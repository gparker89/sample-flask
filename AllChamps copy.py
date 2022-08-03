#List of all LOL champions

import random

#def split_lines(s):
    #return s.split('\n')
#Randomizer of all LOL Champions

All_Champs = ("""
    Aatrox
    Ahri
    Akali
    Akshan
    Alistar
    Amumu
    Anivia
    Annie
    Aphelios
    Ashe
    Aurelion Sol
    Azir
    Bard
    Bel'Veth
    Blitzcrank
    Brand
    Braum
    Caitlyn
    Camille
    Cassiopeia
    Cho'Gath
    Corki
    Darius
    Diana
    Dr. Mundo
    Draven
    Ekko
    Elise
    Evelynn
    Ezreal
    Fiddlesticks
    Fiora
    Fizz
    Galio
    Gangplank
    Garen
    Gnar
    Gragas
    Graves
    Gwen
    Hecarim
    Heimerdinger
    Illaoi
    Irelia
    Ivern
    Janna
    Jarvan IV
    Jax
    Jayce
    Jhin
    Jinx
    Kai'Sa
    Kalista
    Karma
    Karthus
    Kassadin
    Katarina
    Kayle
    Kayn
    Kennen
    Kha'Zix
    Kindred
    Kled
    Kog'Maw
    LeBlanc
    Lee Sin
    Leona
    Lillia
    Lissandra
    Lucian
    Lulu
    Lux
    Malphite
    Malzahar
    Maokai
    Master Yi
    Miss Fortune
    Mordekaiser
    Morgana
    Nami
    Nasus
    Nautilus
    Neeko
    Nidalee
    Nocturne
    Nunu & Willump
    Olaf
    Orianna
    Ornn
    Pantheon
    Poppy
    Pyke
    Qiyana
    Quinn
    Rakan
    Rammus
    Rek'Sai
    Rell
    Renata Glasc
    Renekton
    Rengar
    Riven
    Rumble
    Ryze
    Samira
    Sejuani
    Senna
    Seraphine
    Sett
    Shaco
    Shen
    Shyvana
    Singed
    Sion
    Sivir
    Skarner
    Sona
    Soraka
    Swain
    Sylas
    Syndra
    Tahm Kench
    Taliyah
    Talon
    Taric
    Teemo
    Thresh
    Tristana
    Trundle
    Tryndamere
    Twisted Fate
    Twitch
    Udyr
    Urgot
    Varus
    Vayne
    Veigar
    Vel'Koz
    Vex
    Vi
    Viego
    Viktor
    Vladimir
    Volibear
    Warwick
    Wukong
    Xayah
    Xerath
    Xin Zhao
    Yasuo
    Yone
    Yorick
    Yuumi
    Zac
    Zed
    Zeri
    Ziggs
    Zilean
    Zoe
    Zyra
    """)


Champ_list = All_Champs.split()

#print(Champ_list)


print(random.choice(Champ_list))

#Champion randomizer by role

Champ_Select = 

Question = ("Reroll?")
answer = input("y or n?: ")
if answer == "y":
    print(random.choice(Champ_list))
elif answer == "n":
    print("You're about it!")
else :
    print("Queue up!")

Question_two = ("New Game?")
answer = input("y or n? : ")
if answer == "y":
    print(random.choice(Champ_list))
elif answer == "n":
    print("FF15 you failure")



