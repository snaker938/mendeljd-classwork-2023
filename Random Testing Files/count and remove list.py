# list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88] 
# list2 = []
# count = 0

# for item in list1:
#     if item >=80 and item <= 100:
#         count += 1
#     else:
#         list2.append(item)

        


# print(count)
# print(list2)



# sort algorithm

# B = [2,5,15,36,47,56,59,78,156,244,268] #11
# C = [18,39,42,43,66,69,100] #7

# A = []

# nothing = False

# def merge():
#     equal()
#     j = 0
#     k = 0
#     for i in range(0, len(B) + len(C) + 1):
#         if j >= len(B):
#             if k < len(B):
#                 A.append(C[k])
#                 k = k + 1
#             pass
#         elif B[j] < C[k]:
#             A.append(B[j])
#             j = j + 1
#         else:
#             A.append(C[k])
#             k = k + 1
#     sort()
        

# def equal():
#     numB = len(B)
#     numC = len(C)
#     while numB != numC:
#         if numB >  numC:
#             C.append(B.pop(-1))
#         else:
#             B.append(C.pop(-1))
        
#         numB = len(B)
#         numC = len(C)
    
# def sort():
#     for i in range(0, len(A)):
#         if i + 1 >= len(A):
#             return
#         elif A[i] > A[i + 1]:
#             num = A[i + 1]
#             A[i + 1] = A[i]
#             A[i] = num

        


# merge()

# print(A)
