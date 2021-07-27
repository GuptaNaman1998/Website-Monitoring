This is the read.md file.

This contains all the info on this code snippets

AllSafe:

this file contains code that will run every 1 second and get response from the said website.

Then it will push the time details and the status of the website to the DB.

this file contains code that will run to get the records pushed to the DB.

Then it will create a graph from the output.

And display it onto the index.html .

Which will refresh every 60 seconds.

Note: For every time you execute the code, you will need to rename the previous DB.

All you have to do is make sure that the following libraries are present on the machine.(pre-installed)
requests , sqlite3 , twisted , datetime , pandas , matplotlib.

Steps: 
1. Extract the file into any folder 
2. run the python code 
3. open the index.html .