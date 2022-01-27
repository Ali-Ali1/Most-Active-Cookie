import csv
import sys
import argparse


class ActiveCookies:
	def __init__(self, date):
		#provided date
		self.date = date
		#found cookies list for testing
		self.cookies_list = []
		#count cookies, key= cookie name, val= count
		self.cookies_dict = {}
		#max count for any active cookie
		self.max_val = 0



	def read_csv(self, file):
		#process the csv file with csv module
		with open(args["File"], newline='') as cookies:
			rows = csv.DictReader(cookies)
			for row in rows:
				#in each row look for the cookies with the given date
				self.look_in_row(row)

			#if the date provided is not in the log
			if not len(self.cookies_list):
				print("No cookies were active in the given date:", self.date)
			
		

	def look_in_row(self, row):
		#process each row and compare the dates with given date
		if row["timestamp"][0:10] == self.date[0:10]:
			#count the cookies with a dictionary
			if row["cookie"] in self.cookies_dict:
				self.cookies_dict[row["cookie"]] += 1
			else:
				self.cookies_dict[row["cookie"]] = 1

			#keep track of the cookies seen for testing purposes
			self.cookies_list.append(row["cookie"])
	
	def output_found_cookies(self):
		dic = self.cookies_dict
		if len(self.cookies_list):
			#find the max frequency of active cookies
			for key in dic:
				self.max_val = max(self.max_val, dic[key])
			#print the cookie/cookies with max count
			for key in dic:
				if dic[key] == self.max_val:
					print(key)

			
	

		


if __name__ == "__main__":
	#description of the program
	msg = "A program to find the most active cookie for a given date"

	#using argparse to grab the args provided
	parser = argparse.ArgumentParser(description= msg)
	parser.add_argument("-d", "--Date", help="date format: YYYY-MM-DD")
	parser.add_argument("-f", "--File", help="file must be located in the same directory")
	args= vars(parser.parse_args(sys.argv[1:]))


	#warning to provide the date and filename
	if not args["File"]:
		print("please provide a csv file ex. -f test.csv")
	if not args["Date"]:
		print("please provide a date ex. -d YYYY-MM-DD")

	#if everything looks good, we are ready to process the date and find the most active cookie
	else:
		cookies = ActiveCookies(args["Date"])
		cookies.read_csv(args["File"])
		cookies.output_found_cookies()
		
		

    	

	