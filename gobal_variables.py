

# Jvascript code to select city "FAIZABAD........" 
script = '''
var selectCity = document.getElementById("ddlDistricts");
var allCity = selectCity.options;
for (var op, i=0; i<allCity.length,op = allCity[i];i++)
{
	if (op.text == "Faizabad")
	{
		allCity.selectedIndex = i;
	}
}
'''


# Bare url the website from where it must be extracted.......
base_url="http://164.100.180.4/searchengine/SearchEngineEnglish.aspx"

head = {}