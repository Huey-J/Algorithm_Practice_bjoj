N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 일치
    if r1 == r2 and distance == 0:
        print(-1)
    # 외접 내접
    elif r1 + r2 == distance or r2 == distance + r1 or r1 == distance + r2:
        print(1)
    # 만나지 않음
    elif distance > r1 + r2 or r1 > distance + r2 or r2 > distance + r1:
        print(0)
    # 두 점에서 만남
    else:
        print(2)
