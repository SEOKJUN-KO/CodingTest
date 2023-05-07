n = int(input())

arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(n-1):
    brr = [0]*10
    for j in range(len(arr)):
        if(j == 0):
            brr[1] += (arr[j])%1000000000
        elif(j == 9):
            brr[8] += arr[j]%1000000000
        else:
            brr[j-1] += arr[j]%1000000000
            brr[j+1] += arr[j]%1000000000
    arr = brr

print(sum(arr)%1000000000)
