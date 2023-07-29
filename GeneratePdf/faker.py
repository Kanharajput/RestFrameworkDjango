from faker import Faker
import random
fake = Faker() # initialise the generator

sections = ['A','B','C','D','E']

# after python 3.5 we have return type
def generateRandomData(n=10):
    students = [
                {   'id': i,
                    'name' : fake.name(),
                    'section' : random.choice(sections),
                    'phone_no' : 2334543234
                } for i in range(0,n)
            ]
    
    return students