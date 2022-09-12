n, m = map(int, input().split())
data = []
# 2차원 리스트 안에 str 타입의 숫자들로 형성
for i in range(n):
    data.append(list(input()))

r = min(n, m)

count = 0
# 세로탐색
for i in range(n):
    # 가로탐색
    for j in range(m):
        # 이동하는 범위 탐색
        for k in range(r):
            # 범위가 넘치지 않고 and 각 끝의 자리의 수들이 같을 때
            if (i+k) < n and (j+k) < m and data[i][j] == data[i][j+k] == data[i+k][j] == data[i+k][j+k]:
                # 0일때도 처리 + 크기를 구하기
                count = max(count, (k+1)**2)
print(count)
