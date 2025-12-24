import string
import random
from sys import exit

def reverse(given):
    '''
    Docstring for reverse
    
    Reverses the given string
    '''
    #---- ASSERTATION ----
    assert isinstance(given, str), "Has to be a string"  

    #---- DECLARING VARS ----
    gvn_list = list(given)
    rev_wrd = []
    reversed_ = []
    i=0

    #---- REVERSAL ----
    for word in gvn_list:

        if word == " " or i==(len(gvn_list)-1):
            reversed_.insert(0, "".join(rev_wrd))
            rev_wrd.clear()
            reversed_.insert(0, word)
        else:
            rev_wrd.insert(0, word)
        i+=1 # used to determine wether or not its the last letter of the sentance to avoid forgetting the last word

    #---- PRINTING ----
    return("".join(reversed_))

def encrypt(given):
    '''
    Docstring for encrypt
    
    Given list changes letter to its reverse counting from the back (ex a turns to z), different capitalisation

    Spaces are turned into "@@@"

    Other figures are left as is
    '''
    #---- ASSERTATION ----
    assert isinstance(given, str), "Output of reverse function is not a string, check def reverse(given)"

    #---- DECLARING VARS ----
    alph = list(string.ascii_lowercase)
    Alph = list(string.ascii_uppercase)
    enc_list = []
    gvn_list = list(reverse(given))

    #---- ENCRYPTION ----
    for word in gvn_list:
        #----CHECKING UPPER OR LOWER----
        if word.isupper()== False and word.isalpha() == True:
            enc_list.append(Alph[(alph.index(word))*(-1)-1])
        elif word != " " and word.isalpha() == True:
            enc_list.append(alph[(Alph.index(word))*(-1)-1])
        else:
            if word == " ":
                enc_list.append("@@@")
            else:
                enc_list.append(word)
    
    #print("".join(enc_list))
    return("".join(enc_list))

def key_gen(key):
    '''
    Docstring for key_gen
    
    Generates a key that is inserted into the middle of encrypted words
    '''
    #---- ASSERTING ----
    assert isinstance(key, int), "Key has to be an int value"

    #---- DECLARING VARS ----
    Alph = list(string.ascii_uppercase)
    alplen = len(Alph)
    new_key = ""
    if key==0:
        return("")
    
    else:
        for j in range(key):
            new_key += random.choice(Alph)
        return new_key

def key_adder(given, key=0):
    '''
    Docstring for key_adder
    
    Adds the key to the encrypted 
    '''
    #---- ASSERTING ----
    assert isinstance(given, str), "Has to be string input"
    assert isinstance(key, int), "The key has to be an integer value"

    #---- LEVEL 1 ENCRYPTION ----
    enc_str = encrypt(given)

    #---- VARS DECLARATION ----
    wrd = ""
    wrd_lst = []
    str_lst = []
    key_str = ""
    j=0

    #---- CONVERTING ENCRYPTED TO LIST OF WORDS ----
    for word in enc_str:
        if word.isalpha() == True:
            wrd += word
        else:
            wrd_lst.append(wrd)
            wrd_lst.append(word)
            wrd = ""
        if j == len(enc_str)-1:
            wrd_lst.append(wrd)
        j+=1

    #---- ADDING KEY ----
    for word in wrd_lst:
        if len(word) > 1 and word != "@@@":
            str_lst = list(word)
            if(len(str_lst)%2 ==0):
                str_lst.insert((len(str_lst)//2),key_gen(key))
            else:
                str_lst.insert((len(str_lst)//2)+1,key_gen(key))
            str_lst = "".join(str_lst)
            key_str += str_lst
        else:
            key_str += word

    print(key_str)
    return(key_str)



def decrypt(given):
    '''
    Docstring for decrypt
    
    This function decrypts the encrypted string
    '''
    #---- ASSERTING ----
    assert isinstance(given, str), ""
    #---- VARS DECLARATION ----
    k_val = int(input("What is the key? Insert an integer value"))
    lst_rev=[]
    alph = list(string.ascii_lowercase)
    Alph = list(string.ascii_uppercase)

    #---- REVERSING LIST ----
    for letter in given:
        lst_rev.insert(0,letter)
    
    #---- RETURNING SPACES ----
    for letter in lst_rev:
        if letter == "@":
            x=0
            lst_rev.insert(lst_rev.index(letter), " ")
            while x < 3:
                lst_rev.remove("@")
                x+=1

    #---- CREATING LIST WITH WORDS SEPERATE----
    wrd_lst = [] 
    word = ""
    i=0
    for letter in lst_rev:
        if letter.isalpha() == True:
            word += letter
        else:
            wrd_lst.append(word)
            wrd_lst.append(letter)
            word = ""
        if i==(len(lst_rev)-1):
            wrd_lst.append(word)
        i+=1

    #---- KEY REMOVAL ----
    
    for letter in wrd_lst:
        orig_let = letter
        #print(wrd_lst)
        #print(letter)
        letter = list(letter)
        if len(letter) > 1:
            length = len(letter)
            while len(letter) > (length - k_val):
                if (len(letter) - k_val)%2 == 0:
                    del letter[len(letter)//2]
                else:
                    del letter[(len(letter)//2)-1]
        wrd_lst.insert(wrd_lst.index(orig_let), letter)
        wrd_lst.remove(orig_let)

    #print(wrd_lst)

    #----Final list with just the letters----

    pre_fin_lst = []
    k=0
    for item in wrd_lst:
        pre_fin_lst.insert(k,"".join(item))
        k+=1

    #print(pre_fin_lst)

    #---- Final conversion ----
    fin_lst = []
    for letter in pre_fin_lst:
        new_letter=[]
        for word in letter:
            #----CHECKING UPPER OR LOWER----
            if word.isupper()== False and word.isalpha() == True:
                new_letter.append(Alph[(alph.index(word))*(-1)-1])
            elif word != " " and word.isalpha() == True:
                new_letter.append(alph[(Alph.index(word))*(-1)-1])
            else:
                    new_letter.append(word)
        fin_lst.append("".join(new_letter))

    print("".join(fin_lst))



#---- TESTING ----
if __name__ == "__main__": 
    while True:
        lock=key_adder(str(input("What do you want encrypted?\n")), 7)
        decrypt(lock)