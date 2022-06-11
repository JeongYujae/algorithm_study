def solution(sizes):
    index_0=[]
    index_1=[]
    result=[]
    for i in sizes:
        index_0.append(i[0])
        index_1.append(i[1])

    if max(index_0)>=max(index_1):
        for x in range(len(index_0)):
            to_add=(max(index_0[x],index_1[x]),min(index_0[x],index_1[x]))
            result.append(to_add)
    else:
        for x in range(len(index_0)):
            to_add=(min(index_0[x],index_1[x]),max(index_0[x],index_1[x]))
            result.append(to_add)
    i_0=[]
    i_1=[]
    for i in result:
        i_0.append(i[0])
        i_1.append(i[1])
    answer=(max(i_0)*max(i_1))
    return answer