def test():
        #  -4     -3  -2  -1   <------
    A = ['apple', 3, 4.1, -2]
        #  0      1   2    3   ------>
    print("normal indexing start at 0 -------------- ")
    print(A[2]) #picking item at index 2

    print("negate index ----------")
    print(A[-2])

    print("slicing-------- (include, exclude)")
    print(A[1:3])   #[3, 4.1]
    print(A[2:3])   #[4.1]
    print(A[3:3])   #[]

    print(A[-1:3])  #[]
    print(A[-2:3])  #[4.1]
    print(A[-3:3])  #[3, 4.1]

    print(A[3:-3]) #[]

if __name__ == '__main__':
    test()
