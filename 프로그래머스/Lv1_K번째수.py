def solution(array, commands):
    answer = []
    for x in commands:
        i=int(x[0])
        j=int(x[1])
        k=int(x[2])
        new_array=array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
        
    return answer