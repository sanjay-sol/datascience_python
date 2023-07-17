def minnoofcoins(coins,v,n):
    result=[]
    i=n-1
    while(i>=0):
        while(v>=coins[i]):
            v-=coins[i]
            result.append(coins[i])
        i=i-1
    for i in range(len(result)):
        print(result[i],end=' ')
if __name__=='__main__':
    coins=[]
    n=int(input('Enter no:of valid coins:'))
    for i in range(0,n):
        coins.append(int(input()))
    print('Coins are:',coins)
    a=len(coins)
    x=int(input('Enter amount:'))
    print('Minimum no:of coins',n,'is',end=' ')
    minnoofcoins(coins,x,n)