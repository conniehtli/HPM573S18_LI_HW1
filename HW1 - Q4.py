yours = ['Yale','MIT','Berkeley']
mine = ['Occidental','Columbia','UCLA']

ours1 = mine + yours
print (ours1)

ours2 = []
ours2.append(yours)
ours2.append(mine)
print(ours2)

#1. The list ours1 combines the lists 'mine' and 'yours' into one single list.
# On the other hand the list ours2 adds the two lists together
# but still shows them as two separate objects with brackets around each list.

yours[1] = 'Occidental'

print(ours1)
print(ours2)

#Changing 'yours' does not change 'ours1' because 'ours1' is a new list created
# from combining 'mine' and 'yours', where the change occurs after the new list
# has already been created. 'ours2' changes because it uses the append function
# to modify the original '[]' by adding each list as single object.
