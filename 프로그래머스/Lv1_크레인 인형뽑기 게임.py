def solution(board, moves):
    picked=[] #뽑기당한 인형들 리스트 
    answer=0
    for x in moves: # 뽑기의 순서대로 처음부터 뽑기 시작
        for i in range(len(board)):
            if board[i][x-1] !=0: #0이면 무시하니까
                picked.append(board[i][x-1]) #인형 뽑기
                board[i][x-1]=0 #뽑은 인형은 0으로 바꿈(없는 칸 취급)
                
                if len(picked)>1: #바구니에 인형이 2개 이상 있을 때,
                    if picked[-2] == picked[-1]: #인형이 겹치면
                        del picked[-2] #삭제
                        del picked[-1]
                        answer+=2
                break
                
    return answer