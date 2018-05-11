# Peer Review for project [PoliticalAnalyzer](https://github.com/antpas/PoliticalAnalyzer)
by Bowen Song
## General Review
The Political Analyzer application is a chrome extension application. The purpose of the application is to alert users about their reading content being strong or weak in language and the US political party it belongs to. The Analyzer currently shows either strong or weak and left or right respectively. There is a scale to describe the extent numerically, however, it does not transfer to any other metric that is globally recognized.
## Code Style review
The code is well structured with most of the error handled. There are some hard coding to fine tune the analysis results to fit on the scale. The fine tuning is based on the current trained model. There are some comment of the code, however, does not describe the functions at all. There is no documentation for the functions which if given would benefit further development. The packaging of the code could penitentially benefit from folder partitioning or better naming.
## User Story Review
The user story of the projects are divided into 2 categories: as a software developer and as a user. 
- Software Developer side: This is found on the slides for sprint 1 and 2. For a better presentation, it would be nice to have it on Github along with the source code. The content of the user story clearly shares the flow of the project and a concrete plan.
- User: The story for the user side is concise and intriguing. Allowing users to know what they are actually reading and giving them a prior belief about the content would keep readers shield up or become skeptical when reading a very biased content. 

## System Architecture Review
![system architecture][SystemDiagramPA.png]
The architecture is very clear and well planed. However, the machine learning model could use some work. The current model is the multinomial Naive Bayes classifier which is considered a baseline model disregarding order of words. More investigation can be done using Regression models which could provide more accurate result. This problem is a contributing factor to the issue discussed later in Analyzer result error handling. 
## Data flow
![Data Flow][DataFlowPA.png]
The Data flows very smoothly as described above. This information would help future development if presents on the project Github.
## Error handling 
There are several cases where errors are not handled result in fail to retrieve web page analysis. 
- URL parsing Index out of range: This error is result from unreadable web-page or unreadable format from *html2text* 
- URL loading timeout: under poor network condition, Google *language* API times out and fails to retrieve any information

These error are not handled and not report back to the user. Unless having a back-end terminal showing such information, user does not have any way to tell whether the application is still loading or encountered some error. It would be better if the error can be shown to the users.
## Analyzer result error handling
Accuracy wise, the analyzer does not do well for image heavy web pages. Since it only considers text in a web page. It might be better if the application developers consider to using *Google Vision* as well. This problem is magnified when viewing Trump's home page and Fox News. The two pages along with CNN are all considered neutral for the application's Democrat and Republican scale. Other than disregarding the pictures and videos on the web pages, machine learning model chosen for the project might be a contributing factor as well.

## Conclusion
The application has a intriguing user story for customers and is well laid out. Installation process is easy, however, some documentation is needed. It would be very hard to know what to do if have not seen the application demonstration. The architecture is clear and results in a smooth data flow. The project is lack of documentation which could benefit from this review. The project future work could focus on using different ML model and provide error feedback to the user. 