n,k = map(int,input().split())
arr = list(map(int,input().split()))
result = []
result.append(sum(arr[:k]))

for i in range(n-k):
    result.append(result[i]-arr[i]+arr[k+i])

print(max(result))