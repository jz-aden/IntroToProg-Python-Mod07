    # ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jay VanderZanden, 03/08/2026, Edited and finished Script for Objects
# ------------------------------------------------------------------------------------------ #
import json
import _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    """
    A collection of code to create a class object person

    ChangeLog: (Who, When, What)
    Jay VanderZanden, 03/08/2026, created class object person
    """
    # TODO Add first_name and last_name properties to the constructor
    # creates properties
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    # TODO Create a getter and setter for the first_name property
    # first_name getter
    @property
    def first_name(self):
        return self.__first_name.title()

    # first_name setter
    @first_name.setter
    def first_name(self, value: str):
        # check for numbers in first name value
        if value.isalpha() or value == "":
            # sets parameter value to first_name if valid
            self.__first_name = value
        else:
            raise ValueError("A first name should not contain numbers")

    # TODO Create a getter and setter for the last_name property
    # last_name getter
    @property
    def last_name(self):
        return self.__last_name.title()
    # last_name setter
    @last_name.setter
    def last_name(self, value: str):
        # check for numbers in last name value
        if value.isalpha() or value == "":
            # sets parameter value to last_name if valid
            self.__last_name = value
        else:
            raise ValueError("A last name should not contain numbers")

    # TODO Override the __str__() method to return Person data
    # overriding the __str__() method to return Person Data
    def __str__(self):
        return f"{self.first_name},{self.last_name}"


# TODO Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection of code to create a class object student that inherits person

    ChangeLog: (Who, When, What)
    Jay VanderZanden, 03/08/2026, created class object student
    """

    # creates properties
    # TODO call to the Person constructor and pass it the first_name and last_name data
    # TODO add a assignment to the course_name property using the course_name parameter
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name, last_name)
        self.course_name = course_name

    # TODO add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.title()

    # TODO add the setter for course_name
    @course_name.setter
    def course_name(self, value):
        self.__course_name = value

    # TODO Override the __str__() method to return the Student data
    def __str__(self):
        return f"{self.first_name},{self.last_name}, {self.course_name}"

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Jay VanderZanden, 03/08/2026, edited functions to work with objects
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_type_object: Student):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jay VanderZanden, 03/08/2026, converted function to work with objects

        :param file_name: string data with name of file to read from
        :param student_type_object: a reference to the Student class (object type Student)

        :return: list
        """
        file = None
        student_data: list = []
        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # TODO replace this line of code to convert dictionary data to Student data
            # Loops through each dictionary in the list loaded from the file
            for student in json_students:

                # creates a object variable as type student from the parameter
                student_object = student_type_object()
                # student_object = Student()

                # assigns each property to the respective dictionary item
                student_object.first_name = student["FirstName"]
                student_object.last_name = student["LastName"]
                student_object.course_name = student["CourseName"]

                # assigns the object to the list passed into the function
                student_data.append(student_object)

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jay VanderZanden, 03/08/2026, converted function to work with objects

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file = None

        try:
            # TODO Add code to convert Student objects into dictionaries (Done)

            # creates a list of dictionaries to load onto a json file
            list_of_dictionaries: list = []

            #loopps through the list of objects to convert each element into a dictionary

            for student in student_data:
                # converts student object info into a dictionary
                student_json: dict = {"FirstName": student.first_name,
                                      "LastName": student.last_name,
                                      "CourseName": student.course_name}

                # appends the dictionary to the list of dictionaries variable
                list_of_dictionaries.append(student_json)

            # load desired file into write mode and assigns it to a variable
            file = open(file_name, "w")

            # changed from parameter student_data to list_of_dictionaries
            json.dump(list_of_dictionaries, file)

            IO.output_student_and_course_names(student_data=student_data)

        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    Jay VanderZanden, 03/08/2026, edited functions to work with objects
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jay VanderZanden, 03/08/2026, converted function to work with objects

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        # loops through the list of objects to print each student object

        for student in student_data:

            # TODO Add code to access Student object data instead of dictionary data
            # calls the getter for the object for each property and formats for a print statement
            print(f"Student {student.first_name} {student.last_name} is enrolled in {student.course_name}")

            # dictionary print statement from the original
            # print(f'Student {student["FirstName"]} '
            #       f'{student["LastName"]} is enrolled in {student["CourseName"]}')

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list, student_type_object: Student):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Jay VanderZanden, 03/08/2026, converted function to work with objects

        :param student_data: list of dictionary rows to be filled with input data
        :param student_type_object: reference to the student class

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            # TODO Replace this code to use a Student objects instead of a dictionary objects

            # takes the parameter for the object class and assigns it to a local variable
            student_object = student_type_object()

            # student_object = Student()

            # I don't understand why this alone does not work
            # student_object.first_name = student_first_name
            # student_object.last_name = student_last_name
            # student_object.course_name = course_name

            # puts the inputs into a dictionary
            student: dict = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}

            # converts the dictionary into a student object
            student_object.first_name = student["FirstName"]
            student_object.last_name = student["LastName"]
            student_object.course_name = student["CourseName"]

            # appends the student object to the list of student objects
            student_data.append(student_object)

            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# added necessary parameters added when functions were edited
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_type_object=Student)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        # added necessary parameters added when functions were edited
        students = IO.input_student_data(student_data=students, student_type_object=Student)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # added necessary parameters added when functions were edited
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
