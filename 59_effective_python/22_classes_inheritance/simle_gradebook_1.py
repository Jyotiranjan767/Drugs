#you want to record the grades of a set of students whose
# names aren't known in advance. You can define a class to store the names in
# a dictionary instead of using a predefined attribute for each student.
import collections
class SimpleGradebook(object):

	def __init__(self):
		self._grades = {}

	def add_student(self, name):
		self._grades[name] = []

	def report_grade(self, name, score) :
		self._grades[name].append(score)
		return self._grades

	def average_grade(self, name):
		grades  = self._grades[name]
		print(sum(grades)/len(grades))


x = SimpleGradebook()
x.add_student('luckie')
x.report_grade('luckie',27)
print(x.report_grade('luckie',12 ))
x.average_grade('luckie')

class BySubjectGradeBook():
	def __init__(self):
		self._grades = {}
	def add_student(self, name):
		self._grades[name] = {}

	def report_grade(self, name, subject, grade):
		by_subject = self._grades[name]
		grade_list = by_subject.setdefault(subject, [])
		grade_list.append(grade)
		print(grade_list)
	def average_grade(self, name):
		by_subject = self._grades[name]
		total, count = 0,0
		for grades in by_subject.values():
			# print(by_subject)
			total += sum(grades)
			count += len(grades)
		print(total / count)

x = BySubjectGradeBook()
x.add_student('luckie')
x.report_grade('luckie', 'science', 12)
x.report_grade('luckie', 'science', 2)
x.report_grade('luckie', 'sc', 13)
x.report_grade('luckie', 'history', 14)
x.average_grade('luckie')

class WeightGradeBook():
	def __init__(self):
		self._grades = {}
	def add_student(self, name):
		self._grades[name] = {}
	def report_grade(self, name, subject, score, weight):
		by_subject = self._grades[name]
		grade_list = by_subject.setdefault(subject,[])
		grade_list.append((score, weight))
	def average_grade(self, name):
		by_subject = self._grades[name]
		score_sum , score_count = 0,0
		for subject, scores in by_subject.items():
			subject_avg, total_weight = 0,0
			for score, weight in scores:
				pass
		return score_sum/ score_count
grades = []
grades.append((95, 0.45))
grades.append((95, 0.45))
grades.append((85, 0.10))
total = sum(score * weight for score , weight in grades )
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
print(average_grade)
x = WeightGradeBook()
x.add_student('luckie')
x.report_grade('luckie', 'gym',12,13)


Grade = collections.namedtuple('Grade', ('score', 'weight'))

#next,you can write  a class to represent  a single subject that 
#contains a  set of grades 
class Subject(object):
	def __init__(self):
		self._grades = []
	def report_grade(self, score , weight):
		self._grades.append(Grade(score, weight))
	def average_grade(self):
		total , total_weight = 0,0
		for grade in self._grades:
			total += grade.score * grade.weight
			total_weight += grade.weight
		return total/total_weight	

#next you can write a class to represent  a set of subjects that are being 
#studied by a single student 

class Student(object):
	def __init__(self):
		self._subjects = {}
	def subject(self, name):
		if name not in self._subjects:
			self._subjects[name] = Subject()
		return self._subjects[name]
	def average_grade(self):
		total, count =0, 0
		for subject in self._subjects.values():
			total += subject.average_grade()
			count += 1
		return total / count
# finally you would write a container for  all the 	students keyed dynamically by 
#their names.

class Gradebook(object):
	def __init__(self):
		self._students = {}
	def student(self, name):
		if name not in self._students:
			self._students[name] = Student()
		return self._students[name]

book = Gradebook()
albert  = book.student("Albert Einstein")
math  = albert.subject('Math')
math.report_grade(80, 0.10)
math.report_grade(75, 0.90)
gym = albert.subject('gym')
gym.report_grade(90, 0.10)
gym.report_grade(95, 0.90)
print(albert.average_grade())
