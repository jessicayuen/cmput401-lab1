# Copyright (c) 2015 Jessica Yuen <jyuen@ualberta.ca>
# 
# Licensed under the GNU General Public License, Version 3.
# A copy of this license is provided with this program. 
# Please consult that or visit: <http://www.gnu.org/licenses/gpl.html> 
#
# run python name-family.py -v

class Student:
    """A simple Student object model."""
    courseMarks = {}
    name = ""
    family = ""

    def __init__(self, name, family):
    	"""
    	Initializes the Student.

    	>>> jessica = Student("Jessica", "Yuen")
    	>>> print(jessica.name)
    	Jessica
    	>>> print(jessica.family)
    	Yuen
    	"""
        self.courseMarks = {}
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
    	"""
    	Adds a mark for the specified course to the courseMarks list.
    	
    	>>> bob = Student("Bob", "Bob")
    	>>> bob.addCourseMark("CMPUT 410", 4.0)
    	>>> print(bob.courseMarks["CMPUT 410"])
    	4.0
    	"""
        self.courseMarks[course] = mark

    def average(self):
    	"""
    	Returns the average course mark for this student.
    	
    	>>> bob = Student("Bob", "Bob")
    	>>> bob.addCourseMark("CMPUT 410", 4.0)
    	>>> bob.addCourseMark("CMPUT 401", 2.0)
    	>>> print(bob.average())
    	3.0
    	"""
        return sum(self.courseMarks.values()) / len(self.courseMarks)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
