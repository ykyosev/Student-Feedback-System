# Student-Feedback-System

The aim of this project is to present an alternative way of collecting student feedback. The system is a standalone device built around Raspberry Pi microcomputer, which would be located in university premises. Students would be able to provide their feedback on their lecture/seminar experience. 

A sign by the device would read: “How was your lecture/seminar experience today?”. Students would be able to provide feedback by pressing buttons on the device. There are three buttons labelled “Bad”, “OK” and “Great”, which students could press depending on their lecture or seminar experience. The device would save records on its memory but data would be sent to a server as well. The server would be accessible via a web application. Feedback information would be accessible and three functions are available to search by date, device location and feedback answer.

Python is used to program the software running on the Raspberry. Node.js is used for the server side. It is a JavaScript runtime environment that executes JavaScript outside the browser. Its advantage is that it allows using JavaScript on the front-end and backend sides.

The Pi sends feedback using HTTP GET request to server and server sends back an acknowledgement that records are received. Users can send HTTP GET request so server can search the feedback records saved on JSON file. Data flows the other way, when server sends requested records.  
