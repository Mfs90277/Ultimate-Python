a = (1, 2, 5, 6, False, "Faiz", "shahid",5)
print(a) 

no = a.count(5) 
print(no) 
i = a.index(6)
print(i)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  #Tuple can be concatenated using the + operator. The result is a new tuple that contains all the elements from both tuples in the order they were added.

my_tuple = (1, 2, 3, 4, 5)
print(2 in my_tuple)  #The in operator can be used to check if an element exists in a tuple. It returns True if the element is found, and False otherwise.
print(6 in my_tuple)

print(len(a))  #The len() function can be used to get the number of elements in a tuple. It returns an integer representing the length of the tuple.

my_tuple = (1, 2, 3, 4, 5)
sliced = my_tuple[1:4]  #Tuples support slicing, which allows you to extract a portion of the tuple. The syntax is similar to lists, using the [start:end] notation.
print(sliced)  #Output: (2, 3, 4)