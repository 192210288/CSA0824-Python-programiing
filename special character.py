def count_spl_character(statement):
    spl_character=('~!@#$%^&*()_[]{}:""<>?|/')
    count=0
    for char in statement:
       if char in spl_character:
           count+=1
           return count
statement=input("enter a statement")
num_special_character=count_spl_character(statement)
print("num of special characters",count_spl_character)
