class solution:
    def main_diagonal_sum(self,arr):
        n=len(arr)
        sum=0
        for i in range (n):
            sum+=arr[i][i]
        return sum
a1=solution()
row =int(input())
arr=[]
for i in range (row):
    col=list(map(int,input().split()))
    arr.append(col)
print(a1.main_diagonal_sum(arr))