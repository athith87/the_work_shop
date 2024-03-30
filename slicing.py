#slicing string
#length of the strength
name2="james hunt"
#to print from james we are mentioning 0 index to 5 
print(name2[0:5])
#to print from james we are mentioning 6 index to 10 
print(name2[6:10])
#what if we want to print in between to end as we do not know the length
print(name2[6:len(name2)])
print(name2[:10])
print(name2[:])
#to print the last five characters
print(name2[-5:len(name2)])
#to print every thing after space
index=name2.find(" ")
print(index)
print(name2[index+1:len(name2)])
#to print the first name 
print (name2[0:index])

#all the above we need to know as we working with data in data engineering
#these are necessary as we are cleaning the data, extracting the data and slicing, indexing and so on