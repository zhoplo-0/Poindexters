

matrix1 = []
matrix2 = []



print('''
__________
Matrix A
----------
''')

HeightA = int(input("Matrix A Height:"))
WidthA = int(input("Matrix A Width:"))

for row in range(0,HeightA):
   ColElements = []
   for column in range (0,WidthA):
       print("Enter element A[", row+1, "][", column+1, "]") 
       ColElements.append(int(input()))
   matrix1.append(ColElements)


print('''
__________
Matrix B
----------
''')

HeightB = int(input("Matrix B Height:"))
WidthB = int(input("Matrix B Width:"))

for row in range(0,HeightB):
   ColElements = []
   for column in range (0,WidthB):
       print("Enter element B[", row+1, "][", column+1, "]") 
       ColElements.append(int(input()))
   matrix2.append(ColElements)


if HeightA == HeightB and WidthA == WidthB:
    areUniform = True

else:
    areUniform = False





#Addition of 2 matrix

def matrixSum(arr1, arr2):

    if areUniform == True:
        sumMatrix = []
        for i in range(0,HeightA):
            for j in range(0,WidthA):
                sumMatrix.append((arr1[i][j] + arr2[i][j]))

            print("\t",sumMatrix)
            sumMatrix = []

    else:
        print("The following operation can only be performed on matrix of same dimensions.\n")




#Subtraction of 2 matrix

def matrixSub(arr1, arr2):

    if areUniform == True:
        subMatrix = []
        for i in range(0,HeightA):
            for j in range(0,WidthA):
                subMatrix.append((arr1[i][j] - arr2[i][j]))

            print("\t",subMatrix)
            subMatrix =[]

    else:
        print("The following operation can only be performed on matrix of same dimensions.\n")



#Multiplication of 2 Matrix

def matrixProduct(arr1, arr2):

    if areUniform == True:
        MultMatrix = []
        for i in range(0,HeightA):
            for j in range(0,WidthA):
                sumk=0
                for k in range(0,HeightA):

                    sumk+= arr2[k][j]

                MultMatrix.append(arr1[i][j]*sumk)

            print("\t",MultMatrix)
            MultMatrix = []

    else:
        print("The following operation can only be performed on matrix of same dimensions.\n")



#Transpose of matrix 1 and 2

def matrixTranspose(arr1):
    THeight = WidthA
    TWidth = HeightA
    transMatrix1= []
    for i in range(0,THeight):
        for j in range(0,TWidth):
            transMatrix1.append(arr1[j][i])

        print("\t",transMatrix1)
        transMatrix1 = []



def menu():
    print('''
    =======================================
    1: Sum of matrix A and B
    2: Matrix A-B
    3: Matrix B-A
    4: Product of matrix A and B
    5: Transpose of matrix A
    6: Transpose of matrix B
    =======================================
    ''')
    switch = int(input("Enter the operation to be performed:"))

    if switch == 1:
        print("\nSum of matrix A and B is:\n")
        matrixSum(matrix1, matrix2)
        menuOrEnd()

    elif switch == 2:
        print("\nMatrix A-B is:\n")
        matrixSub(matrix1, matrix2)
        menuOrEnd()

    elif switch == 3:
        print("\nMatrix B-A is:\n")
        matrixSub(matrix1, matrix2)
        menuOrEnd()

    elif switch == 4:
        print("\nProduct of Matrix A and B is:\n")
        matrixProduct(matrix1, matrix2)
        menuOrEnd()

    elif switch == 5:
        print("\nTranspose of matrix A is:\n")
        matrixTranspose(matrix1)
        menuOrEnd()

    elif switch == 6:
        print("\nTranspose of Matrix B is:\n")
        matrixTranspose(matrix2)
        menuOrEnd()

    else:
        print("\nPlease enter a valid operation :)")
        menuOrEnd()



def menuOrEnd():
    print('''\n
    How do you want to proceed?
    ===========================
    1: Go back to menu
    2: Exit
    ===========================
    ''')

    switch2 = int(input("Select:"))

    if switch2 == 1:
        menu()

    elif switch2 == 2:
        quit()

    else:
        print("Please enter a valid operation :)")
        menuOrEnd()


menu()
