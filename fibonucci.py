def fibonacci(n):
  if n == 0:
    return 0
  if n <= 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

    # Write your code here.
n = 5
print(fibonacci(n))
