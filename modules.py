sesliharf = ["a","e","ı","i","u","ü","o","ö","A","E","I","İ","U","Ü","O","Ö"] #Sesli harfler tanimlandi
from time import sleep as sl

def yaz(yazi, sure = 0.005): #Yazı yazdırmak için
    for i in str(yazi): #yazi nin icindeki her harf i
        sl(sure) #sleep 0.01 (default)
        print(str(i), sep = "", end="", flush=True)

def encode(yazi, encodeharf = "g"): #encode icin
    harfler = []
    encoded = ""

    #kus dili >>> ku-"gu"-s di-"gi"-li-"gi"

    for i in str(yazi): #Her harfler in icindeki i
        if i in sesliharf: #Eger i sesli ise
            encoded = encoded + str(i + encodeharf + i) #k-"u"-"gu"-s
        else: #Degilse
            encoded = encoded + i #Ekleme yapmadan yaz

    return str(encoded) #String cikis alacagiz



def decode(yazi): #decode için GokhanTkr tarafından oluşturuldu
	delete = []

    for i in sesliharf:
        yazi.split(i+encodeharf)
	b = 0 # for loop element
	new_list =[]# empty string for rebuilding the word
	new_str = ""

	for i in range(len(yazi)): # for loop for detecting the kusdili rules

		if (yazi[i] == 'g'):# search for g letter

			if(yazi[i+1] in sesliharf):

				if(yazi[i-1] in sesliharf):

					delete.append(i-1)
					delete.append(i)
					# if the letters are vowels one before and one after from the letter g; store them in a list



	for a in range(len(yazi)): # loop for deleting sequence

		new_list.append(yazi[a])

	for b in range(len(delete)):
		new_list[delete[b]] = ""


	for c in range(len(new_list)):
		new_str = new_str + new_list[c]


	return new_str
###^^^^^^^^^^^^^^^^###

def bruteforce(yazi):
    pass
