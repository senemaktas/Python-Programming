# Defining a list ---------------------------------------
colors = ['item1','item2','item3','item4']

# Accessing elements ------------------------------------
first_item = colors[0] # 1st element 
last_item = colors[-1] # last element

# modifying individual items  ---------------------------
colors[0] = 'red'

# Adding elements ---------------------------------------
colors.append('blue') # to the end 
colors.insert(2, 'purple') # position

# list length -------------------------------------------
colors_len = len(colors)

# Removing elements -------------------------------------
del colors[-1] # by position
colors.remove('item2') # by value

# Popping elements --------------------------------------
most_recent_colors=colors.pop()
first_colors=colors.pop(0)

# Looping through a list --------------------------------
for color in colors:
    print(color)

# Sorting a list ----------------------------------------
colors.sort() # permanently
colors.sort(reverse=True) # alphabetically
colors.reverse() # reversing a list 
sorted(colors) # temporarily

# The range() function ----------------------------------
new_list=list(range(1,10001))

# Copying a list ----------------------------------------
copy_of_colors = colors[:]

# Slicing a list ----------------------------------------
first_three = colors[:3]
middle_three = colors[1:4]
last_three = colors[-3:]

# List comprehensions -----------------------------------
upper_colors = [color.upper() for color in colors] 

# Tuples ------------------------------------------------
dimensions = (800,600)

# -------------------------------------------------------