from selenium import webdriver
from pyvirtualdisplay import Display
from BeautifulSoup import BeautifulSoup
from gobal_variables import *
import csv
import threading


totaldata = []				# To store successfully extracted Epic numbers data

not_matched =[]				# to store Epic numbers whose data is not found



# Jvascript code to add Epic number in input field........" 
def run_script(Driver,id):
	print "Extracting data for "+str(id)
	
	Script_EpicNo = '''									
	var id = document.getElementById("txtEPICNo");
	id.value = "'''+str(id)+'''";'''                   # Sript to input Epic number

	Driver.execute_script(Script_EpicNo)			   # Running srcipt



#Extracting information and writing in csv files
def selectEpicNo(Driver,idList):

	huhh = [7,9,10,11,12]
	head['7']='Name'
	head['9']='Fathers Name'
	head['10']='Age'
	head['11']='Sex'
	head['12']='Epic No'

	for id in idList:
		run_script(Driver,id)								# Running script to search different Epic number

		Button = Driver.find_element_by_id("Button1")
		Button.click()										# Click Search

		soup = BeautifulSoup(Driver.page_source)			# Using BeautifulSoup for extracting data from web page

		#print soup

		data ={}
		try:

			Table = soup.find('table',{'id':'gvSearchResult'})			#Searching for table if data is there 
			Rows = Table.findChildren('tr')
			#print Rows
			for row in Rows:
				td = row.findChildren('td')
				#print td
				i =1
				for d in td:
					if i in huhh:
						f = d.string
						#print f.encode('utf-8')
						data[head[str(i)]]=f.encode('utf-8')  							#Extracting different data 
					i += 1 
			#print data
			totaldata.append(data)
			print "Data extracted for "+str(id)

		except:															# Run if no mactch found for corresponding Epic number
			not_matched.append(id)
			print "No data found for "+str(id)



	# Writing extracting data in csv file
	with open('output/extracted_ids.csv', 'wb') as csvfile:
	    w = csv.DictWriter(csvfile,fieldnames=['Epic No','Name','Fathers Name','Age','Sex'])
	    w.writeheader()
	    for data in totaldata:
	    	w.writerow(data)

	# Writing not extracted numbers in csv
	with open('output/not_extracted_ids.csv', 'wb') as csvfile:
	    w = csv.writer(csvfile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for data in not_matched:
	    	w.writerow(data)
	    



# Running Webdrivers and getting unique cookie
def selectCity(idList):

	display = Display(visible=0)		#Display of browser is zero
	display.start()

	Driver = webdriver.Firefox()		#Openning web browser
	Driver.get(base_url)				#Open base_url

	Driver.execute_script(script)		# Running script to select state FAIZABAD

	Button = Driver.find_element_by_id("Button1")		
	Button.click()

	Cookie = Driver.get_cookies()
	#print Cookie

	selectEpicNo(Driver,idList)			#Calling function to extract information of different Epic numbers

	Driver.close()						#Closing browser

	display.stop()

	return 1

