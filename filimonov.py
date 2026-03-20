# решение 1 скрина:

# for A in range(1000):
#     for x in range(1000):
#         if (not(((x&28!=0) or (x&45!=0)) <= ((x&17 == 0 ) <= (x&A != 0) ))):
#             break
#     else:
#         print(A)
#         break

# решение 2 скрина:
#
# P = list(range(130, 172))
# Q = list(range(150, 186))
# A = []
#
# for x in range(1000):
#     if not((x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))):
#         A.append(x)
#
# print(A)
# print(A[-1]-A[0])

# решение 3 скрина:

# A = [i for i in range(-1000,1000)]
#
# for x in range(-1000,1000):
#     if (not((x in A) <= (x**2 <= 100)) and ((x**2<=64 ) <= (x in A))):
#         A.remove(x)
#
# print(A)
# print(A[-1]-A[0])

# решение 4 скрина:

# def tr(m, n, k):
#     return (m + n > k) and (m + k > n) and (n + k > m)
#
# def mx(a, b):
#     return a if a > b else b
#
# for A in range(-2 , 1000):
#     for x in range(-2 ,1000):
#         if not(not((tr(x, 11, 16) == (not(mx(x, 5) > 10))) and tr(4, A, x))):
#             break
#     else:
#         print(A)
#         break
#         ne polychilos ((((