The current project is an improvment of the  which was with no logic. Low separation to classes.currently there are utils and one class.
Here I used OOP design , pattern(factory, Single tone, Injection , SOLID ) queue , Cache ,Persistance ,cache, encription for API key. more ...

Your review is wellcome.

# Git_Hub:
https://github.com/GuyYar1/WeatherOOP

# Link to site-streamlit :
Streamlit (biu0weather0oop.streamlit.app)

I can set rich GUI after the backend is completed now.

Refactor will include:

A.Server side (weather server): API Server took its data from the DB transfer it to the client request it: ( our app) prepare the data and send us it DTO structure.

B.our app - Backend should be: 1 our app is basically print the data results on the screen using stream lit.
2 "Weather service Printer" using injection , is being injected with "weather manager" . 3 "weather manager" role is to give command to specific parser of the specific URL API request. 4 In case GUI "requested to bring the data and save it" the process began. "requested to bring the data and save it" process - Parser get the URL from the "weather manager" and the parser, request the data on a generic data model. each parser has derived class that fit to one specific query. 5 The parser parse the generic data model to specific model object and save it. 6 This action is asyncronus when the parser finish, it raises an event that the data is ready.
7 When the "weather manager" got an event from specific parser that the data was saved in the model. it added it to the queue. And by its own timeline it refers to the queue one by one.

    8 For the meantime, we have only one GUI that invoke one trigger at a time, but we should consider to check in unit test that it could handle a burst of queries.
       Our app is basically all the time get data from the server, no such case that we update or post requests from our side to server.
C.our app- FrontEnd

The connection between the backend to the "Weather service Printer" which is the high hierarchy class. it based on a singleton, so the updates should be connected via binding per GUI ID.
In case of multiple request or multiple GUI support we should use the GUI ID. - for the mean
