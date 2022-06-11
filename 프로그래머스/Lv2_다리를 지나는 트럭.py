def solution(bridge_length, weight, truck_weights):
    time=0
    bridge=[0]*bridge_length
    while len(bridge)>0:
        bridge.pop(0) #트럭을 건넘 처리 해주는 로직
        time+=1 #먼저 건너게 해둠 처리하고 타임을 올려주고
        if len(truck_weights)>0:
            if sum(bridge)+truck_weights[0]<=weight: #만약 다리가 무게가 감당이 가능하다면
                bridge.append(truck_weights.pop(0)) #truck_weights의 0번 인덱스를 다리로 보내고, 그 값 삭제
            else:
                bridge.append(0) #감당 불가능하면 0을 보냄 -> 어차피 while 문이 시작되면서 0을 pop 하기 때문에
                                # len이 그대로 유지가 된다
            
    return time