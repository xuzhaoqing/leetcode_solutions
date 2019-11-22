Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.

Setup: You have a server that processes a lot of requests per second, and it invokes a Logger every time request processing starts or finishes.

class Logger:
  def start(self, timestamp, request_id):
    pass
  def finish(self, timestamp, request_id):
    pass 

The timestamp is guaranteed to be non-decreasing.

Problem: I want you to implement the Logger class to write to a log file that prints the requests as they finish in this format:
$requestId started at $timeStarted, finished at $timeFinished

class Logger:
  def __init__(self):
	self.hashTable = {}
  def start(self, timestamp, request_id):
    	self.hashTable[request_id] = timestamp
  def finish(self, timestamp, request_id):
      start_time = self.hashTable[request_id]
      print(“requestId started at ”+start_time+”, finished at “+timestamp)
	 del self.hashTable[request_id]

Let’s make it more interesting: Now I want you to print them in order of start timestamp instead.
Example:
t 0 1 2 3 4 5 6 7 8 9 10
A   ---------------
B       ----------------
C         -------
This would print:
A started at 1, finished at 8
B started at 3, finished at 10
C started at 4, finished at 7
D 5 8
A -> 1 B -> 2 C -> 3
next_index 3 
buff_dict {3:(start_c,end_c),4:}
def finish:
  if request_id in dict:
	check if dict[request_id].index == next_index:
		print request_id
		next_index += 1
		while next_index in buff_dict:
  			print
			next_index += 1
		else:
 			buffer_dict[dict[request_id].index] = (start_c,end_c)


class Logger:
  def __init__(self):
	self.hashTable = {}  # A B C D
	self.buffer_dict = {} # C
	self.next_index = 1 # 4
	self.index = 1   # 3 
  def start(self, timestamp, request_id):
    	self.hashTable[request_id] = (self.index,timestamp)
	self.index += 1

  def finish(self, timestamp, request_id):
      index, start_time = self.hashTable[request_id]
 del self.hashTable[request_id]
	 if index == self.next_index:	
        print(“requestId started at ”+start_time+”, finished at “+timestamp)
  del self.buffer_dict[self.index]
        self.next_index += 1
	   while self.next_index in self.buffer_dict:
		  start_time,end_time = self.buffer_dict[self.next_index]
		  print(“requestId started at ”+start_time+”, finished at “+end_time)
		 del self.buffer_dict[self.next_index] 
 self.next_index += 1

	 else:
		self.buffer_dict[index] = (start_time,timestamp)

A started at 1, finished at 8
B started at 3, finished at 10
C started at 4, finished at 7
D 5 11

Let’s make it even more interesting: What if a request never finishes? How would you handle that?
I check each request in hashTable and if the current timestamp - start_time of request > a specified time, I will delete them
