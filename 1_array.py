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

    #The len() function returns the number of items in an object.
    lenFunction=['cat','dog','tiger']
    print(len(lenFunction))  # 3

    #list Concatenation
    listConcat1=[1, 2, 3] + ['A', 'B', 'C']
    print(listConcat1)
    listConcat2 = ['A', 'B', 'C'] * 2
    print(listConcat2)

    #In & Not in Operator
    print('he' in ['hello', 'hi', 'nice to meet you'])

    #Index value in list
    list = ['hello', 'hi', 'nice to meet you']
    print(list.index('hi'))


if __name__ == '__main__':
    test()
