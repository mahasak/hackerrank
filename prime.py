def is_prime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")

        