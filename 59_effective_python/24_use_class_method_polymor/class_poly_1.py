# item 24 : use @classmethod polymorphism to construct objects generically
import os
import threading 
from tempfile import TemporaryDirectory

class InputData(object):
	def read(self):
		raise NoImplementedError

# here I have a complete subclass  of Inputdata that reads data from a file on disks

class PathInputData(InputData):
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		return open(self.path).read()

# you would want a similar abstract interface for MapReduce worker that consumes the
# input data in a standard way

class Worker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NoImplementedError
	def reduce(self):
		raise NoImplementedError

# here I define a concrete subclass of Worker to implement the 
#specefic MapReduce function I want to apply : a simple newline counter:
class LineCountWorker(Worker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')
	def reduce(self, other):
		self.result += other.result

def generate_inputs(data_dir):
	for name in os.listdir(data_dir):
		yield PathInputData(os.path.join(data_dir, name))

# next I create the LineCountWorker instances using the InputData instances 
# returned by generate _inputs 

def create_workers(input_list):
	workers = []
	for input_data in input_list:
		wokres.append(LineCountWorker(input_data))
	return workers 
def execute(workers):
	threads = [threading.Thread(target=w.wap) for w in workers]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	first , rest = workers[0], workers[1:]
	for worker in rest:
		first.reduce(worker)
	return first.result
# finally, I connect all of the pieces together in a
# functions to run each step

def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	workers = create_workers(inputs)
	return execute(workers)
# running this function  on a set of test input files works great 
def write_test_files(tmpdir):
	#...
	print('write_test_file')

with TemporaryDirectory() as tmpdir:
	write_test_files(tmpdir)
	result = mapreduce(tmpdir)
print('there are ', result, 'lines')

#maintaing same thing with @classmethod to make it easy to understand

class GenericInputData(object):
	def read(self):
		raise NoImplementedError

	@calssmethod 
	def generate_inputs(cls, config):
		raise NoImplementedError

class PathInputData(GenericInputData):
	#...
	def read(self):
		return open(self.path).read()

	@classmethod
	def generate_inputs(cls, config):
		data_dir = config['data_dir']
		for name in os.listdir(data_dir):
			yield cls(os.path.join(data_dir, name))
class GenericWorker(object):
	#...
	def map(self):
		raise NoImplementedError
	def reduce(self):
		raise NoImplementedError
	@classmethod
	def create_method(cls, input_class, config):
		workers = []
		for input_data in input_class.generate_inputs(config):
			workers.append(cls(input_data))
		return workers

class lineCounterWorker(GenericWorker):
	#...
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')
	def reduce(self, other):
		self.result += other.result
# and finally , I can rewrite the mapreduce  function to be completely generic.

def mapreduce(worker_class, input_class, config):
	wokres = worker_class.create_workers(input_class, config)
	return execute(workers)

with TemporaryDirectory() as tmpdir:
	write_test_files(tmpdir)
	config ={'data_dir' : tmpdir}
	result= mapreduce(LineCountWorker, PathInputData, config)

