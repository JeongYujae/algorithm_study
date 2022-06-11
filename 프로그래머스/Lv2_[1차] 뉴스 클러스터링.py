def solution(str1, str2):
    from collections import Counter
    str1_l=str1.lower()
    str2_l=str2.lower()

    str1_c=[]
    str2_c=[]

    for i in range(len(str1_l)-1):
        if str1_l[i].isalpha() and str1_l[i+1].isalpha():
            str1_c.append(str1_l[i]+str1_l[i+1])
    for i in range(len(str2_l)-1):
        if str2_l[i].isalpha() and str2_l[i+1].isalpha():
            str2_c.append(str2_l[i]+str2_l[i+1])

    counter_1=Counter(str1_c)
    counter_2=Counter(str2_c)

    a=list((counter_1 & counter_2).elements())
    b=list((counter_1 | counter_2).elements())

    if len(a)==0 and len(b)==0:
        return 65536
    else:
        return int(len(a)/len(b)*65536)