# Section 1
# Q1 adding an item to the list
market =["Yam", "Tomato", "Onion"]
print(market)
market.append("Fish")
print(market)

# Q2. Inserting an item at a specific index
grades =[80, 90, 70]
print(grades)
grades.insert(1, 85)
print(grades)

# Q3. Removing an item by value
gadgets = ["Laptop", "Phone", "Tablet"]
print(gadgets)
gadgets.remove("Phone")
print(gadgets)

# Q4. Method to remove all items from a list
colors =["Red", "Blue", "Green"]
print(colors)
colors.clear()
print(colors)

# 5.many times "Yes" appears.
votes =["Yes", "No", "Yes", "Yes", "No"]   
print(votes)
count_yes = votes.count("Yes")
print(count_yes)

# 6.using slicing to extract ["c", "d", "e"]
alphabets = ["a", "b", "c", "d", "e", "f"]
print(alphabets)
alphabets_slice = alphabets[2:5]
print(alphabets_slice)

# students reverse
students = ["Kofi", "Ama", "Yaw"]
students.reverse()
print(students)

# 8. Merging 
list_a = [1, 2]
list_b = [3, 4]
print(list_a)
list_a.extend(list_b) 
print(list_a)

# 9. The Pop Given cities
cities = ["Accra", "Kumasi", "Tamale"]
removed_city = cities.pop(2)
print(removed_city)

# 10. The Searching in list i terms
items = ["Pen", "Ruler", "Eraser"]
ruler_index = items.index("Ruler")
print(ruler_index)

# Section 2:
# 1. The Tuple Wall
student_info = ("Araba", 20)
student_info[1] = 21  # it raises an TypeError: 
 
# 2. Converting tuple into a list.
tup = (1, 2, 3) 
tup_list = list(tup)
tup_list.append(4)
tup = tuple(tup_list)
print(tup)

# 3. Counting Items 
data = (10, 20, 10, 30, 10)
count_10 = data.count(10)
print(count_10)

# 4. Position Finder: In the tuple colors = ("Red", "Blue", "Green"), find the index of "Blue".
colors = ("Red", "Blue", "Green")   
blue_index = colors.index("Blue")
print(blue_index)

# 5. Unpacking
coords = (5.6, -0.1)    
lat, lon = coords
print(lat)
print(lon)     

# 6. Nesting: Create a list called nest. Add a tuple (5, 10) as the first item in that list. What is len(nest)?
nest = []
nest.append((5, 10))
print(len(nest))

# 7. Tuple Slicing: Given numbers = (10, 20, 30, 40, 50), use slicing to get the last two numbers: (40, 50).
numbers = (10, 20, 30, 40, 50)
last_two = numbers[3:5]
print(last_two)

# 8. Mixed Extend: If you run my_list = [1, 2] followed by my_list.extend((3, 4)), what is the final value of my_list?
my_list = [1, 2]
my_list.extend((3, 4))
print(my_list)

# 9. Memory Wipe: You cannot .clear() a tuple. What keyword do you use to delete the entire tuple variable my_tup from memory?
my_tup = (1, 2, 3)          
del my_tup  

# 10. Type Check: Create a variable x = (5). Now create y = (5,). Use the type() function to check both. Which one is a tuple?
x = (5)
y = (5,)
print(type(x))  # This will show <class 'int'> because x is not a tuple
print(type(y))  # This will show <class 'tuple'> because y is a tuple




