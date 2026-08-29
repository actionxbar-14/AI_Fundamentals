



# :: Pydantic : 

# - Pydantic is a data validation and data parsing library for Python. It ensures that the data you 
# work with is correct, structured, and type-safe.



# :: format_1 :  




# from pydantic import BaseModel 

# class Student(BaseModel):

#     name : str 




# # new_student = {'name' : 32} #--> gives an error!

# new_student = {'name' : 'anubhav'}

# Student = Student(**new_student)

# print(Student.name)



# ------------------------------------------------------------------------------------------------



# :: format_2 : 





from pydantic import BaseModel , EmailStr , Field
from typing import Optional 



class Student(BaseModel):

    name : str = 'anubhav'
    age : Optional[int] = None 
    email : EmailStr 
    cgpa : float = Field(gt = 0 , lt = 10 , default=5 , description= 'a decimal value representing the cgpa of the student')


# new_student = {'age' : 21 , 'email' : 'abc'}   #--> error !
# new_student = {'age' : 21 , 'email' : 'abc@gmail.com'} 

# new_student = {'age' : 21 , 'email' : 'abc' , 'cgpa' : 12}   #--> error !
new_student = {'age' : 21 , 'email' : 'abc@gmail.com', 'cgpa' : 5} 






Student = Student(**new_student)

print(Student)