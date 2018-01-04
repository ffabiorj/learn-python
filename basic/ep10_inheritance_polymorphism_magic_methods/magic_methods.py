class Time: 
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return f"{self.hour}:{self.minute:02d}:{self.second:02d}"

	def __add__(self, other_time):
		new_time = Time()

		if self.second + other_time.second >= 60:
			self.minute += 1
			new_time.second = (self.second + other_time.second) - 60
		else:
			new_time.second = self.second - other_time.second

		if self.minute + other_time.minute >= 60:
			self.hour += 1
			new_time.minute = (self.minute + other_time.minute) - 60
		else:
			new_time.minute = self.minute - other_time.minute
		
		if self.hour + other_time.hour > 24:
			new_time.hour = (self.hour + other_time.hour) - 24
		else:
			new_time.hour = self.hour + other_time.hour

		return new_time

def main():
	time1 = Time(1,20,30)
	print(time1)

	time2 = Time(24,41,30)
	print(time1 + time2)


if __name__ == '__main__':
	main()