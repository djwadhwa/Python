#function "fac" represents "factorial"

def fac(num):
    if (num>0):
        ans = num*fac(num-1)
        return ans;
    else:
        return 1;

#using 3 as an example
print(fac(3))
