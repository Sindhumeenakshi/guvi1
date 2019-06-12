ch=input()
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list2=["a","e","i","o","u"]
if((ch in list1)==True):
  if(ch in list2):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
