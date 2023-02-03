#!/usr/bin/env python
# coding: utf-8

# In[1]:


#initializing for loop for increasing part of pyramid 
for i in range(6):
    #printing increasing pyramid
    print("* "*i)
#initializing for loop for decreasing part of pyramid 
for i in range(4):
    #printing decreasing pyramid
    print("* "*(4-i))


# In[2]:


#initializing list
my_list=[10,20,30,40,50,60,70,80,90,100]
#Extracting each element from the list
for i in range(len(my_list)):
    #Finding elements of odd index
    if(i%2!=0):
        #printing elements of odd index
        print(my_list[i])
        


# In[3]:


#initializing list
x=[23,"Python",23.98]
#initializing empty list to append elements
append_list=[]
#initializing for loop to extract elements
for i in range(len(x)):
    #finding the type of elements and appending them to a list
    append_list.append(type(x[i]))
#priniting the appended list
print(x)
print(append_list)


# In[4]:


#initialising the given list
Sample_list=[1,2,3,3,3,3,4,5]
#changing list into set for deleting duplicate elements
Unique_set=set(Sample_list)
#Converting it into list again
Unique_List=list(Unique_set)
#Printing the list
print(Unique_List)


# In[5]:


#Prompting the user to enter the input
Input_String=input("Enter the string: ")
#initializing variables needed for operation
upper_count=0
lower_count=0
#initializing for loop to extract letters
for i in range(len(Input_String)):
    #Checking if the letter is upper case
    if(Input_String[i].isupper()):
        #Adding the count 
        upper_count+=1
    #Checking if the letter is lower case
    if(Input_String[i].islower()):
        #Adding the count 
        lower_count+=1
#printing no of upper case characters
print("No. of Upper-case characters: ",upper_count) 
#printing no of lower case characters
print("No. of Lower-case characters: ",lower_count)


# In[ ]:




