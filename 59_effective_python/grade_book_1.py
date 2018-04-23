from collections import defaultdict
current = {'green' : 12, 'blue' : 3}
increments = [
	('red', 5),
	('blue', 17),
	('orange', 9),
]

def log_missing():
	print('log added')
	return 0

# result = defaultdict(log_missing, current)
# print('before ', dict(result))
# for key , amount in increments:
# 	print(key, increments)
# 	result[key] += amount
# 	print("after:", dict(result))

class SimpleGradeBook(object):
	"""docstring for SimpleGradeBook"""
	def __init__(self):
		# super(SimpleGradeBook, self).__init__()
		self._grade = {}

	def add_student(self, name):
		self._grade[name] = []
	def report_grade(self, name, score):
		self._grade[name].append(score)
		return self._grade
	def average_grade(self, name):
		return sum(self._grade[name])/len(self._grade[name])
class BySubjectGradeBook():
	def __init__(self):
		self._grade = {}
	def add_student(self, name):
		self._grade[name] = {}
	def report_grade(self, name, subject, grade):
		self._grade[name].setdefault(subject, []).append(grade)
		# return self._grade
	def average_grade(self,name):
		t= 0
		for grade in self._grade[name].values():
			t= (sum(grade)/len(grade))
			print('average in per subject mark %s'%(grade), t)
class WeightGradeBook():
	def __init__(self):
		self._grades = {}
	def add_student(self, name):
		self._grades[name] = {}
	def report_grade(self, name, subject, score, weight):
		by_subject = self._grades[name]
		grade_list = by_subject.setdefault(subject, [])
		grade_list.append((score, weight))
	def average_grade(self, name):
		by_subject = self._grade[name]
		score_sum, score_count = 0, 0
		for subject, score in by_subject.items():
			subject_avg, total_weight= 0,0
			for score, weight in scores:
				pass
		return score_num/score_count
x = SimpleGradeBook()
# print(x.add_student("August"))
# print(x.report_grade("August", 700))
# print(x.report_grade("August", 100))
# print(x.report_grade("August", 100))		
# print(x.average_grade("August"))

xx = BySubjectGradeBook()
xx.add_student("August")
xx.report_grade("August",'math', 700)
xx.report_grade("August", 'xxx', 100)
xx.report_grade("August", 'math', 100)		
print(xx.average_grade("August"))




# s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
# d = defaultdict(list)
# for k, v in s :
# 	d[k].append(v) 
# print(d.items())
# # using same but using dict.setdefault
# d = {}
# for k, v in s:
# 	d.setdefault(k,[]).append(v)
# 	print(d)
	