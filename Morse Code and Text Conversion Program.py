'''Writing a program that converts english text to morse code and vise versa.'''
print("Press 1 to convert English text to Morse codes \n Press 2 to convert Morse code to English text")
op=int(input("Press 1 or 2:"))
if op==1:
    text=input("Enter the English text which you want to convert into morse code:")
    string=text.upper()
    morse_code= { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'	','I':'..'
,'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'	','R':'.-.', 'S':'	',
'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---',
'3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----',
', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}
    print("The value of entered text in morse code is:")
    for i in range(len(string)):
        print(morse_code.get(string[i]),end=" \n ")
elif op==2:
    alpha_code={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I',
'.	':'J','-.-.':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q', '.-.':'R','...':'S',
'-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.----':'1','..---':'2','...--':'3',
'....-':'4','.....':'5', '-....':'6','--...':'7', '---..':'8','----.':'9','-----':'0','--..--':',',
'.-.-.-':'.','..--..':'?','-..-.':'/','-....-':'-', '-.--.':'(','-.--.-':')'}
    m=input("enter the morse code which you want to convert into text:")
    code=m.split() #split() is used to separate each morse code value print("The value of Entered morse code in text is:")
    for val in range(len(code)):
        print(alpha_code.get(code[val]),end="")
else:
    print("press the correct option.")
