n, k = map(int, input().split())
a = list(map(int, input().split()))
prlist = list()
prlist.append(a[0])
for i in range(1, len(a)):
    prlist.append(prlist[i - 1] + a[i])
# print(prlist)
m = 10000000000
ind = 0
s = sum(a[:k])
for i in range(n - k):
    # print(i, (prlist[i + k - 1] - prlist[i]))
    if m >= prlist[i + k - 1] - prlist[i] > 0 and sum(a[i:i + k - 1]) < s:
        m = prlist[i + k - 1] - prlist[i]
        s = sum(a[i:i + k - 1])

        ind = i
print(ind + 1)
