def revword (word:str):
    lenght = len(word)
    a='' 
    for i in range (lenght):
        a=a+word[lenght-1-i]
    a=a.lstrip()
    a=a.lower()
    return a

def countword():
    text = open('text.txt')
    a=0
    count=1
    word2=''
    for i in text:
        if a==0:
            word = revword(i)
        else:
            word2 = revword(i)
            count1 = word2.count(word) 
            count+=count1
        a+=1
    return count 
