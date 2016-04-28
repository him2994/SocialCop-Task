import textract


# Extract all Epic Numbers from the text file
def extract_id_from_file():
    try:
        file1 = open("temp/pdf_to_txt.txt","r")   # File pdf extracted as text
        file2 = open("temp/all_epic_nos.txt","w")   # File to store all Epic Numbers 
        print "Reading file........"

        try:
            for line in file1.readlines():
                word=line.rstrip("\n")
                if ((word.isalnum() or ('UP/' in word )) and (word.__len__()>8) ):  #Extract Epic Number from normal text
                    file2.write(word+'\n')
            
            file1.close()
            file2.close()
            print "Epic Numbers are extracted successfully........."

        except:
            print "Error in extracting Epic Numbers........."

    except:
        print "File pdf_to_txt.txt not found......"

    


# Convert pdf to text file.........
def convert_pdf_to_txt(path):

    try:
        print "Extracting file from "+str(path)
        text = textract.process(path)  # Using textract library to extract pdf to text

        try:
            f = open ("temp/pdf_to_txt.txt","w")
            f.write(text)
            f.close()
            extract_id_from_file()
            print "Pdf is successfully extracted to .txt format......."
            extract_id_from_file()

        except:
            print "Failed to open file.........."

    except:
        print "Failed to extract data from file......."





# Extract all Epic numbers in a list.
def getIds():

    idList = []     # To store all Epic numbers 

    try:
        print "Reading file all_epic_nos.txt........."
        file = open("temp/all_epic_nos.txt","r")

        try:
            for id in file.readlines():
                id = id.rstrip('\n')
                idList.append(id)

        except:
            print "Error in reading file all_epic_nos.txt......."

    except:
        print "Error in opening file all_epic_nos.txt......."

    #print idList
    return idList