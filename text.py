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
            word = i.strip()
        else:
            word2 = revword(i)
            print(word2)
            count1 = word2.count(word)
            print(count1)
            count+=count1
        a+=1
    return count  

countword()
