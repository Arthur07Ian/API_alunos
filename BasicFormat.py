import json

class Student:
    id = 0;         #Integer
    name = "";      #String
    courses = [];   #Array
    
    def __init__(self,id,name):
        self.id = id;
        self.name = name;
        self.courses = [];
        
    def addCourse(self,course):
        self.getCourses().append(course);
    
    def addCourses(self,courses):
        for course in courses:
            self.getCourses().append(course);

    def removeCourse(self,course):
        self.getCourses().remove(course);

    def setId(self,id):
        self.id = id;
    def getId(self):
        return self.id;

    def setName(self,name):
        self.name = name;
    def getName(self):
        return self.name;

    def setCourses(self,courses):
        self.courses = courses;
    def getCourses(self):
        return self.courses;
        
    def toString(self):
        courses_string = "NONE";
        if(len(self.courses) > 0):
            courses_string = "[";
            i = 0;
            for course in self.getCourses():
                if(i>0):
                    courses_string += ","
                courses_string += course;
                i+=1;
            courses_string += "]";
            
        output = "ID: {} , NAME: {} , COURSES : {}";
        return output.format(self.getId(),self.getName(),courses_string);
        
    def toJsonifiable(self):
        return {'id':self.getId(),'nome':self.getName(),'cursos':self.getCourses()};

class StudentList:
    students = [];
    vacant_id = [];

    def __init__(self):
        self.students = [];
        self.vacant_id = [];

    def getStudent(self,id,optional_name):
        if(len(optional_name) > 0):
            for student in self.getStudents():
                if(student.getId() == id and student.getName() == optional_name):
                    return student;
        else:
            for student in self.getStudents():
                if(student.getId() == id):
                    return student;

    def getStudentByName(self,name):
        for student in self.getStudents():
                if(student.getName() == name):
                    return student;

    def addStudent(self,id,name,courses):
        studentHolder = Student(id,name);
        studentHolder.setCourses(courses);
        self.getStudents().append(studentHolder);
    
    def addVacantStudent(self,name,courses):
        id = len(self.getStudents());
        if(len(self.getVacant_id()) > 0):
            id = self.getVacant_id()[0];
            self.getVacant_id().remove(id);
        self.addStudent(id,name,courses);
    
    def addReferenceStudent(self,reference):
        self.getStudents().append(reference);

    def removeStudent(self,id,optional_name,vacant):
        self.getStudents().remove(self.getStudent(id,optional_name));
        if(vacant):
            self.getVacant_id().append(id);

    def addCourseToIdentifiable(self,id,optional_name,courses):
        studentHolder = self.getStudent(id,optional_name);
        studentHolder.addCourses(courses);

    def addCourseToNamed(self,name,courses):
        studentHolder = self.getStudentByName(name);
        studentHolder.addCourses(courses);

    def setStudents(self,students):
        self.students = students;
    def getStudents(self):
        return self.students;
    
    def setVacant_id(self,vacant_id):
        self.vacant_id = vacant_id;
    def getVacant_id(self):
        return self.vacant_id;

    def toString(self):
        output = "";

        i = 0;
        for student in self.getStudents():
            if(i>0):
                output += "\n";
            output += str(student.getId())+": {"+student.toString()+"}";
            i += 1;

        return output;