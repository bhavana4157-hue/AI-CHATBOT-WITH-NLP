# AI-CHATBOT-WITH-NLP

COMPANY NAME: CODTECH IT SOLUTIONS PRIVATE LIMITED

NAME: BHAVANA S

INTERN ID: CTIS0245

DOMAIN: PYTHON PROGRAMMING

DURATION 4 WEEKS

MENTOR: NEELA SANTHOSH

*AI CHATBOT WITH NLP*:

The AI Chatbot project is a simple yet powerful web-based conversation system built using Python and Flask. This project demonstrates how backend logic written in Python can communicate with a web frontend to provide real-time responses to user messages. The goal of the project is to allow a user to type questions in a browser and receive replies instantly from a chatbot created by the developer.

The system works through three main layers: the user interface, the Flask backend server, and the chatbot logic.
The user interface is developed using HTML, CSS, and JavaScript. The webpage includes a text box where users type messages and a button to send them. A script embedded in the page uses the JavaScript fetch() function to send the message to the Flask server without reloading the page. Each message and reply is displayed dynamically on the screen, giving the feeling of a real chat application. User messages and chatbot responses are displayed in separate styles so the conversation looks neat and interactive. The webpage also supports automatic scrolling, meaning new messages always appear at the bottom.

The second layer is the backend code written in Flask. Flask is a lightweight Python web framework that allows developers to create webpages and API endpoints quickly. In this project, Flask listens for incoming messages sent from the browser. When a message is received, Flask passes that text to another file, chatbot.py, which contains the brain of the application. After the chatbot function produces a reply, Flask sends that answer back to the browser in JSON format. This creates a smooth interaction cycle where every question from the user triggers a response.

The third layer is the chatbot logic itself. It is implemented inside a separate Python module called chatbot.py. The chatbot reads the user’s message, converts it to lowercase, and checks if the message contains specific keywords. Unlike machine learning models, this approach uses conditional statements (if and elif) to match common questions, such as greetings, date and time queries, asking the chatbot’s name, or saying goodbye. Although it is simple, this rule-based method demonstrates the foundation of artificial intelligence: the machine reacts to text input and responds logically. The chatbot can also use Python libraries, such as datetime, to generate real-time answers for questions about the current date or time. If the chatbot does not recognize a message, it sends a friendly default reply, encouraging the user to try another question.

Overall, this chatbot project teaches fundamental skills for building interactive web applications. It connects frontend and backend development, shows how APIs work, and demonstrates basic natural language processing ideas. Even though the chatbot is simple, the same structure can be expanded to support advanced features like speech recognition, databases, or machine learning models. Thus, the project serves as a perfect stepping stone for students and developers beginning their journey in artificial intelligence and web technology.

*OUTPUT*:

