# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:37:27 2019
@author: Samsung
"""

from itertools import chain

# Loading  file ".txt"
def loading():
    x=input("Enter the file name with the extension: (exp. name.txt) ")
    try:
        file = open(x,"r")         
        temp=file.read()                   
        return temp
    except:
       print("This file does not exist, try again:")
       return loading()
    file.close()
    
#------------------------------------------------------------------------------------------------------------------

# Removing special characters from text
def change(text):
    list_characters=[]
    for i in chain(range(0,48),range(58,65),range(91,97),range(123,127)):
        list_characters.append(chr(i))                        
    #print(list_characters)
    for j in range(len(list_characters)):
        text=text.replace(list_characters[j],"")        
    #print("This text does not have any special characters.: \n", text)
    return text

#------------------------------------------------------------------------------------------------------------------

# Removing numbers from text 
def numbers(text):
    list_numbers=[]
    for i in range(48,58):
        list_numbers.append(chr(i))                        
    #print(list_numbers)
    for j in range(len(list_numbers)):
        text=text.replace(list_numbers[j],"")
        #print(tekst)
    #print("This text does not have any numbers: \n", text)
    return text


#------------------------------------------------------------------------------------------------------------------
# Convert capital letters to lowercase
def lower(text):
    text = text.lower()
    return text


#------------------------------------------------------------------------------------------------------------------
# Replacement of special characters
def change_polish_characters(input_text):

    strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
 
    ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'

    translator=str.maketrans(strange,ascii_replacements)
        
    return input_text.translate(translator)
    

#-----------------------------------------------------------------------------------------------------------------
# Function that divides the text into 5 characters and into 7 columns.

def division(text):
    change_text = []
    for i in range(len(text)):
        change_text.append(text[i])
        if i != 0 and i%5 == 4:
            change_text.append(' ')
        if i != 0 and i%35 == 34:
            change_text.append('\n')           
    change_text=("".join(change_text))
    return change_text
        
#------------------------------------------------------------------------------------------------------------------
# Function saving text as file
def save(text,k):
    name = (input('Choose a name for your file '+k+' (without the extension): \n')+'.txt')    
    try: 
        file = open (name,'x')
        file.write(text)
    except FileExistsError:
        print("A file with this name already exists, try again.")
        return save(text)
    file.close()     
#-----------------------------------------------------------------------------------------------------------------
# Text preparation function
def preparation():
    plain=loading()
    text_changed=change(plain)
    text_without_numbers=numbers(text_changed)
    text_with_low_characters = lower(text_without_numbers)   
    text_without_polish_characters = change_polish_characters(text_with_low_characters)
    text_divided = division(text_without_polish_characters)
    #save(text_divided)
    return text_divided

#text_redy_to_encryption = preparation()

"""
- Loading kye from file (".txt")
- Checking the length of the key, must be 26
- Concatenates two lists and turns it into a dictionary
- Replaces characters according to the dictionary
- To decryption create reverse dictionary
"""

def substitution_cipher():
    test=0
    print("Welcome. This program encrypts and decypts text fo useing substitution cipher. \n")
    print("Which option you prefer?\n")
    print("1. Encryption. \n")
    print("2. Decryption. \n")
    choose = input("Enter which option you choose: (number): ")
    while test != 1:
        try :
            choose = int(choose)
            if choose == 1 or choose ==2:
                 test = 1
            else :
                print("Your choose number is not available.")
                choose = input("Enter which option you choose: (number): ")
        except:
            print("Your choose number is not available. Please choose number. \n")
            choose = input("Enter which option you choose: (number): ")
            
          
    if choose == 1 :
        print("Your choose is encryption.")
        cipher = []
        print("\n \n    You will be asked for a key file")
        temp=0 
        while temp != 1:
            key = loading()
            if len(key) == 26:
                temp = 1
            else:
                print("Incorect length key")
                print("Try again, but remeber lenght key must be 26.")
                key = loading()
        key=key.upper()
        print("\n \n    You will be asked for a plain text file.")
        text = preparation()
        #tekst = wczytywanie()
        #klucz = "DEFGHIJKLMNOPQRSTUVWXYZABC"
        alphabet = [chr(i) for i in range(97,123)]
        key = list(key)
        dictionary= dict(zip(alphabet, key))
            
        for j in text:
            if j != chr(10): # for "Enter"
                if j != chr(32): # for "Space"
                    cipher.append(dictionary[j])    
                else:
                    cipher.append(' ')
            else:
                cipher.append('\n')
            
        cipher = ("".join(cipher))
        save(cipher,'cryptogram' )
        print("A file was encryption and save.")
                
            
        
    if choose == 2 :
        print("Your choose is decryption.")
        plain_text=[]        
        print("\n \n    You will be asked for a key file")
        temp=0 
        while temp != 1:
            key = loading()
            if len(key) == 26:
                temp=1
            else:
                print("Incorect length key")
                print("Try again, but remeber lenght key must be 26.")
                key = loading()
        key=key.upper()
        print("\n \n    You will be asked for a cipher text file.")
        text = preparation()
        text = text.upper()
        alphabet = [chr(i) for i in range(97,123)]
        key = list(key)
        dictionary = dict(zip(key, alphabet))        
        
        for j in text:
            if j != chr(10): # for "Enter "
                if j != chr(32): # for "Spacje"
                    plain_text.append(dictionary[j])    
                else:
                    plain_text.append(' ')
            else:
                plain_text.append('\n')
        
        plain_text = ("".join(plain_text))
        save(plain_text,'plain')    
        print("A file was decription and save")


substitution_cipher()


        


        
    
