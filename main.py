from get_ids import *
from get_data_writefile import *
from datetime import datetime
#import os



# Implement multithreading for faster process
def threading_list():

	date1 = datetime.now()

	idList = getIds()  # Epic numbers list

	n = idList.__len__()
	s = n+3/6

	threads=[]
	j=0

	for i in range(0,6):
		#print "Running Thread "+str(i)
		t=threading.Thread(target=selectCity,args=[idList[j:j+s]])  # Initializing thread
		j+=s
		threads.append(t)
		t.start()
		t.join()

	date2 = datetime.now()

	print "Time taken by Script... "
	print date2 - date1
	print "DONE"

#threading_list()

if __name__=="__main__":

	convert_pdf_to_txt("input.pdf")     

	threading_list()

