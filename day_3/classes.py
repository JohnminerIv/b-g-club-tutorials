# day_3/classes.py

"""
Classes are a way to encapsulate code. It is a way of keeping functions and data
that represent something together and is a core concept to understand for object
oreinted programing.
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        """
        Initializes the person class requires a name and an age.
        """
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self) -> str:
        """
        Introduces the person.
        """
        return f'Hello my name is {self.name} and I am {self.age} years old.'

    def get_older(self, years: int) -> None:
        """
        Ages the person by an amount of years
        """
        self.age += years

    def add_friend(self, person) -> None:
        """
        Adds another person to this persons friend list
        """
        self.friends.append(person)
        return self

    def list_friends(self) -> str:
        """
        Returns a string containg the names of this persons friends
        """
        friends = ''
        for friend in self.friends:
            friends += friend.name + ' '
        return self.name + "'s friends list is " + friends

    def __str__(self) -> str:
        return f'Person {self.name}, age {self.age}'


"""
By using classes you can inherit from another class and receive their methods or
overide them with something else.
"""


class Student (Person):
    def __init__(self, name, age, grade):
        """
        Initializes a student.
        """
        super().__init__(name, age)
        self.grade = grade

    def introduce(self) -> str:
        """
        Introduces a student.
        """
        return f"I'm a student my name is {self.name}. I'm in grade \
{self.grade}, and I'm {self.age} years old"

    def __str__(self) -> str:
        return f'Student {self.name}, grade {self.grade}'


"""
Object oreiented programming is useful and many if not all jobs for coders will
require you to be familiar with how it works but its also important to note that
you can do much the same thing without it. For most of your personal projects
you can decide to use object oriented or functional paradigms or a mix of both
whatever you want.
"""

def create_person(name, age) -> dict:
    """
    Creates a dictionary representation of a person
    """
    return {'name': name, 'age': age, 'friends': []}

def introduce(person) -> str:
    """
    Introduces a dictionary representation of a person
    """
    return f'Hello my name is {person["name"]} and I am {person["age"]} years old.'

def get_older(person, years) -> None:
    """
    Increments the age of a person
    """
    person['age'] += years

def string_rep(person) -> str:
    """
    Represents the dictionary representation of a preson as a string
    """
    return f'Person {person["name"]}, age {person["age"]}'

def add_friend(person, person2) -> None:
    """
    Adds a person to this functional persons friends list
    """
    person['friends'].append(person2)
    return person

def list_friends(person) -> str:
    """
    Returns a string containg the names of this functional persons friends
    """
    friends = ''
    for friend in person['friends']:
        friends += friend['name'] + ' '
    return person['name'] + "'s friends list is " + friends

def create_student(name, age, grade) -> dict:
    """
    Creates a dictionary representation of a student.
    """
    student = create_person(name, age)
    student['grade'] = grade
    return student

def introduce_student(student) -> str:
    """
    Introduces a functional student.
    """
    return f"I'm a student my name is {student['name']}. I'm in grade \
{student['grade']}, and I'm {student['age']} years old"


if __name__ == '__main__':
    print('Doing some things in an object oriented way')

    person1 = Person('John', 20)

    print(person1.introduce())
    person1.get_older(6)
    print(person1.introduce())


    student1 = Student('Baki', 18, 12)

    print(student1.introduce())
    student1.get_older(3) # Still can get older even if the method isn't eplicately defined because it subclasses person
    print(student1.introduce())
    student1.add_friend(person1)
    print(student1.list_friends())

    print('')
    print('*' * 80)
    print('')
    print('Doing the same thing functionaly.')

    person2 = create_person('John', 20)

    print(introduce(person2))
    get_older(person2, 6)
    print(introduce(person2))


    student2 = create_student('Baki', 18, 12)

    print(introduce_student(student2))
    get_older(student2,3)
    print(introduce_student(student2))
    add_friend(student2, person2)
    print(list_friends(student2))
