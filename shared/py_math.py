from typing import List


def fib(self, n: int) -> int:
  if n <= 1:
    return n

  a, b = 0, 1
  n -= 2
  while n >= 0:
    a, b = b, a+b
    n -= 1

  return b


def reverse(x):
    ans = 0

    while x:
      ans = 10 * ans + x % 10
      x //= 10

    return ans


def is_palin(x):
    return x == reverse(x)


def gcd(a: int, b: int) -> int:
  if a > b:
    a, b = b, a
    
  while b:
    a, b = b, a%b

  return a


def matr_mult(a: List[List[int]], x: List[List[int]], mod: int) -> List[List[int]]:
  return x


def fast_power(x: List[List[int]], n: int, mod: int) -> List[List[int]]:
	if n == 0:
		return x

	if mod < 1:
		mod = 1

	h, w = len(x), len(x[0])
	a = [[x[i][j] for j in range(w)] for i in range(h)]

	while n > 0:
		if n&1 == 1:
			# desolve a * x^25 into: a * x^1 * x^8 * x^16
			a = matr_mult(a, x, mod)

		# raising the power: x^2 -> x^4 -> x^8 ....
		x = matr_mult(x, x, mod)
		n = n >> 1

	return a
  