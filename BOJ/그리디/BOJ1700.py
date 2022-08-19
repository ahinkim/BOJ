def solutions():
  plug = []
  # 플러그를 뽑는 횟수
  cnt = 0
  for i in range(K):
    # 플러그 안에 전기용품이 있는 지 확인, 1 1 1 1의 경우 때문에 이 코드를 맨 앞에 둬야 한다.
    if appliance[i] in plug:
      # 있다면 continue
      continue
    # 플러그가 비어있다면 전기용품 꼽기
	  # <= N으로 해서 틀렸었다. 
    if len(plug) < N:
      plug.append(appliance[i])
      continue
    idxs = []
    #플러그에 있는 전기용품이 나중에 몇 번째에 나오는 지 확인 
    for x in plug:
      try:
        idx = appliance[i + 1:].index(x)
        idxs.append(idx)
      except: # ValueError: 해당되는 index가 없다면
        # 최댓값 넣기: 제일 나중에 나온다고 처리
        idxs.append(101)
    # idx가 제일 큰 플러그 뽑기 
    del plug[idxs.index(max(idxs))]
    cnt += 1
    #새로운 전기용품 삽입
    plug.append(appliance[i])
  return cnt

# N 멀티탭 구멍의 개수, K 전기 용품의 총 사용횟수
N, K = map(int, input().split())
appliance = list(map(int, input().split()))
print(solutions())