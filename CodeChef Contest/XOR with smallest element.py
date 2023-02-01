import heapq as heap

try:
    n = int(input())
    for _ in range(n):
        n, x, t = map(int, input().split())
        if n == 1:
            a = int(input())
            if t % 2 == 0:
                print(a)
            else:
                print(a ^ x)
        else:
            a = list(map(int, input().split()))
            heap.heapify(a)
            i = 0
            while i < t:
                b = heap.heappop(a)
                c = b ^ x
                heap.heappush(a, c)
                d = heap.heappop(a)
                i += 1
                if d == c:
                    if (t - i) % 2 == 0:
                        heap.heappush(a, d)
                        break
                    else:
                        heap.heappush(a, b)
                        break
                else:
                    heap.heappush(a, d)
            a.sort()
            print(*a)
except:
    pass



