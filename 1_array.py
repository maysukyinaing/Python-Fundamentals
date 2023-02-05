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
    print(listConcat1)  #[1, 2, 3,'A', 'B', 'C']
    listConcat2 = ['A', 'B', 'C'] * 2
    print(listConcat2)  #['A', 'B', 'C', 'A', 'B', 'C']

    #In & Not in Operator
    print('he' in ['hello', 'hi', 'nice to meet you']) #False

    #Index value in list
    list = ['hello', 'hi', 'nice to meet you']
    print(list.index('hi')) #1

    #append()
    #The method is responsible for adding its parameters to the end of a list as a single element.
    Basket1 = ['apple','orange']
    Basket1.append('mango')
    print(Basket1)  #['apple', 'orange', 'mango']
    Basket1.append(['mango1','mango2'])
    print(Basket1)  #['apple', 'orange', 'mango', ['mango1', 'mango2']]
    print(Basket1[3][0])    #mango1

    #extend()
    #The extend method is responsible for appending each iterable (it can be a tuple, any string, or a list) member to the list's end
    Busket2 = ['apple','orange']
    Busket2.extend(['cherry', 'blueberry'])
    print(Busket2)  #['apple', 'orange', 'cherry', 'blueberry']
    Busket2.remove('cherry')
    print(Busket2)  #['apple', 'orange', 'blueberry']

    #Extending an existing list by adding strings.
    org_list=['x', 'y', 'z']
    new_1='Hello, Guys!'
    org_list.extend(new_1)
    print(org_list) #['x', 'y', 'z', 'H', 'e', 'l', 'l', 'o', ',', ' ', 'G', 'u', 'y', 's', '!']

    #insert(index, element)
    #insert() function simply takes two parameters index at which the element is to be inserted and the element which is to be inserted.
    insert_org_list=['welcome','python']
    insert_org_list.insert(1,'to')
    print(insert_org_list)

if __name__ == '__main__':
    test()
