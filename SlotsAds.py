n=int(input("Enter number of slots and ads:"))
AdProfitPerClick=[int(i) for i in input("Enter profit per click for each advertise:").split()
if int(i) in range(-10**5,(10**5)+1)]
AverageSlotClick=[int(i) for i in input("Enter average estimated click for each slot in one row :").split()
if int(i) in range(-10**5,(10**5)+1) ]
if n>=1 and n<=10**3:
    AdProfitPerClick.sort()
    AverageSlotClick.sort()
    ans = sum(AdProfitPerClick[i] * AverageSlotClick[i] for i in range(n))
    print(ans)

