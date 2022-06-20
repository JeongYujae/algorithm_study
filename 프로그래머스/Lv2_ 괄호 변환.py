def div(p):
    cnt_open=0
    cnt_close=0
    
    for i in range(len(p)):
        if p[i]=='(':
            cnt_open+=1
        else:
            cnt_close+=1
            
        if cnt_open==cnt_close:
            return p[:i+1], p[i+1:]

#올바른 괄호 문자열인지 체크하는 함수 
def check(u):
    data=[]
    for p in u:
        if p=='(': # '(' 가 있으면
            data.append(p) 
        else:
            if not data: 
                return False #올바른 괄호 문자열이 아니다
            data.pop()
    return True #아무 조건에 걸리지 않으면 올바른 괄호 문자열이다
            
        
def solution(p):
    if not p: # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
        return ""

    u,v=div(p)# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    #div함수에서 2개의 값을 return 하니까 u와 v에 각각 할당
    
    if check(u): # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        return u + solution(v) #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.

 
    else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        result='(' #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        result+=solution(v) #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        result+=')'#   4-3. ')'를 다시 붙입니다. 
        
        for x in u[1:len(u)-1]:
            if x=='(': #4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
                result+=')'
            else:
                result+='('
                
                

    return result #   4-5. 생성된 문자열을 반환합니다.
                
        

        
            
    