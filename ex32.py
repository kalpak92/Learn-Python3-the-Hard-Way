the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranes', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is the count {number}")

#same as above
for fruit in fruits:
    print(f"A friut of type: {fruit}")

#as we can go through mixed lists too
#notice we have to use {} since we don't know what'
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a gunction that lists understands
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")

