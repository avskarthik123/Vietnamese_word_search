def main():
    file1  = open("word_corpus.txt","r")
    str1 = file1.read()
    list1 = str1.split()
    l1 = []
    l2=[]
    for i in range(0,20000,1):
        if list1[i].isdigit():
            l1.append(list1[i])
        else:
            l2.append(list1[i])
    file2 = open("character_mapping.txt","r")
    str2 = file2.read()
    list2 = str2.split()
    l3 = []
    l4=[]
    for i in range(0,105,1):
        if i%2==0:
            l3.append(list2[i])
        else:
            l4.append(list2[i])

    del l1[0]
    del l2[0]
    del l3[0]
    del l3[0]
    del l4[0]
    l5 = []
    for i in l2:
        for j in l3:
            if j in i:
                k=l3.index(j)
                i=i.replace(j, l4[k])
        l5.append(i)

    file3 = open("word_frequency.txt","w")
    for i in range(0,len(l5)):
        file3.write(l1[i]+" "+l5[i])
        file3.write("\n")

    string1 = str(input("enter the string to be searched"))
    for i in l5:
        if string1 in i:
            print(i)





if __name__ =="__main__":
    main()