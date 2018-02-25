Full Report for Code Review [embed]https://github.com/Bowenislandsong/SoftwareDesigns/blob/master/Assigment2/Report.pdf[/embed]
1. Documentation:
- The Read me file presents a clear view of the API. The test examples is clear. so is the function explanation. 

- The only issue is not all the third party library is included. The  "twitter" library used by the API is not specified.
2. Code convention
- Due to the nature of Python, based on indentation. The code indent is clear and function naming is clear.

- However, there is not a single line of comment explaining the code function and decision made. 
- The 'if' statement is getting out of hand. please consider use 'and' in an 'if' statement to connect multiple 'if' statements. 

3. API convention
-  Since all the pictures are temp files, please delete all of them once done making the video clip. Customers may complain about your api being not space efficient. 

3. Fatal Error -------------------------------------------------------------------------------------
- it is never a good practice to use 'try' 'catch' in a deployed code. That means you do not fully understand the function you are using. You understand it may crash. However, since it is python, it is acceptable.  Please do understand it may hide errors.

- Error relate to unclear list of third party library. The 'twitter' and 'twitter-python' can both satisfy python interpreter 

- In this case, 'twitter' library does not have attribute 'Api' or 'GetUserTimeline'. The 'twittermedia.py' is hiding this information by try catch to throw another error irrelevant to the actual bug. Python as an interpreter language may miss interpret your code. 

4. API design
- The video does not contain the labels of each image. Maybe it can be used as an asynchronous attempt. However, there is no way connecting the labels with the video anymore. This asynchronousness is meaningless.  

It is designed to be Synchronous App. Can be used as asynchronous app with no meaning.
