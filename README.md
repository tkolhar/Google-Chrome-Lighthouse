# Lighthouse
Lighthouse tool automation
Lighthouse opensource tool with Python
Automation assignment
Problem:

Using Lighthouse opensource tool with Python as the coding language, automate any of the 4 to 5 accessibility rules for the following scenario:
1) Go to - https://www.tamm.abudhabi/en
2) Click on Accept cookies    
3) Under Journey and services, click on Discover Abu Dhabi as a Business Destination
As an assignment deliverable, we expect:
The list of any 4-5 accessibility testing rules that you have automated for the above page.
Automated framework used and its relevant test execution report

Solution:

Development tools: PyCharm (community edition) 2019.2.2, Google Chrome, Chrome Devtools to run the audits manually.

For Automation:

Python – 3.7.3

Lighthouse Node-Cli
https://github.com/GoogleChrome/lighthouse#using-the-node-cli

Lighthouse-ci : A useful wrapper around Google Lighthouse CLI
https://github.com/andreasonny83/lighthouse-ci#lighthouse-ci





Steps to run the python script:

1.	Open the project in PyCharm
2.	Below there is terminal shell provided in the IDE.
3.	Traverse till you are under C:\Users\admin\PycharmProject\Automate_Access\venv\Scripts
4.	Run $python automate.py

(venv) C:\Users\admin\PycharmProject\Automate_Access\venv\Scripts>python automate.py
Requirement already satisfied: npm in c:\users\admin\pycharmproject\automate_access\venv\lib\site-packages (0.1.1)
Requirement already satisfied: optional-django==0.1.0 in c:\users\admin\pycharmproject\automate_access\venv\lib\site-packages (from npm) (0.1.0)
C:\Users\admin\AppData\Roaming\npm\chrome-debug -> C:\Users\admin\AppData\Roaming\npm\node_modules\lighthouse\lighthouse-core\scripts\manual-chrome-launcher.js
C:\Users\admin\AppData\Roaming\npm\lighthouse -> C:\Users\admin\AppData\Roaming\npm\node_modules\lighthouse\lighthouse-cli\index.js
+ lighthouse@5.6.0
updated 1 package in 49.528s
C:\Users\admin\AppData\Roaming\npm\lighthouse-ci -> C:\Users\admin\AppData\Roaming\npm\node_modules\lighthouse-ci\bin\cli
+ lighthouse-ci@1.10.0
updated 1 package in 59.586s
accessibility: 100
All checks are passing. �



Accessibility rules automated:

	Buttons have an accessible name
	<html> element has a [lang] attribute
	<html> element has a valid value for its [lang] attribute
	Form elements have associated labels
	Links have a discernible name

Explanation:
1.	I am using the wrapper class lighthouse-ci along with python to automate the accessibility rules
2.	Lighthouse-ci has provision to write custom configuration files which could be in json format.
3.	This configuration file allows a user to control the exisitng audits he wants to run and also add new audits specific to his application
4.	A sample configuration file would look something like this:
 
5.	The entire structure of writing a configuration files can be understood by following this document
  https://github.com/GoogleChrome/lighthouse/blob/master/docs/configuration.md.
6.	In my case I wanted to restrict the category to accessibility and execute 4-5 audits on the webpage. Hence my config.json something looks like
7.	{
  "extends": "lighthouse:default",
  "settings": {
    "onlyCategories": [ "accessibility" ],
    "skipAudits": [
    ]
  }
}
8.	The extends property controls if your configuration should inherit from the default Lighthouse configuration
9.	The settings property controls various aspects of running Lighthouse such as  
 CPU/network throttling and audit whitelisting/blacklisting.
10.	 onlyCategories : Includes only the specified categories in the final report.
11.	 skipAudits: Excludes the specified audits from the final report. Takes   
 priority over onlyCategories,
12.	 Using these properties I was able to obtain a set of rules which I automated.
•	'accessibility/button-name', 
•	'accessibility/html-has-lang',
•	'accessibility/html-lang-valid',
•	'accessibility/label',
•	'accessibility/link-name',
13.	 I am using python built-in libraries such as os, system, and subprocess to  
 automate the scenario.
14.	 The python script consists of setup() which resolves the dependencies by 
 installing npm, lighthouse and lighthouse-ci before execution of test cases
15.	 Furthermore I am automating the lighthouse-ci command which runs the 
 audits provided in the config.json file setting the threshold for score to be 1 
           and generating a report in html format as well as json format.
16.	 Python subprocess modules allows me to automate the command
17.	 Finally I am open the report.html which is the generated output file in the 
 web browser to display the test execution results.
18.	 I have also saved the output in json format for which I have created a public  
 gist so that the test execution report can be viewed using lighthouse viewer 
           by providing the gist id

19.	 Here is the gist
    https://gist.github.com/tkolhar/ca816a07ae98d2a6e113c536fd70ceb7

20.	 And here is the report
https://googlechrome.github.io/lighthouse/viewer/?gist=ca816a07ae98d2a6e113c536fd70ceb7
