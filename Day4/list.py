state = ["Delhi","Maharashtra","UP"]

# Inserting single value to the end of list 

state.append("sikkim")

# Insterting More than one value to the list
state.extend(["Telengana","Punjab"])

# Remove the 1st item from the list which has the same value as given
state.remove("sikkim")

# Removes the item given in the position of the list 
state.pop(0)

# Removes all the items from the list
state.clear() #Use with caution

# Insert an item at a given position in the list 
state.insert(2,"Himachal")

print (state)