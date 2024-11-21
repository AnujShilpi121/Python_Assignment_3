CREATE DATABASE PYTHON_QUESTIONS;
USE PYTHON_QUESTIONS;

CREATE TABLE QUESTIONS (
	id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option1 VARCHAR(255) NOT NULL,
    option2 VARCHAR(255) NOT NULL,
    option3 VARCHAR(255) NOT NULL,
    correct_option INT NOT NULL
    );

SELECT * FROM QUESTIONS;   
   
INSERT INTO QUESTIONS
	(question,option1,option2,option3,correct_option) VALUES
    ("What is the maximum possible length of an identifier?",16,32,'none of these',3),
	("Which of the following is the correct extension of the Python file?",".py",".python",".p",1),
	("What will be the value of the following Python expression? 4+3%5",7,2,1,1),
	("Which keyword is used for function in Python language?","Function","def","define",2),
	("Which of the following character is used to give single-line comments in Python?","#","//","!",1),
	("What will be the output of the following Python code? print(True) if 0.1 + 0.2 == 0.3 else print(False)","True","False","None",2),
	("Which of the following is used to define a block of code in Python language?","indentation","key","brackets",1),
	("What will be the output of the following Python code snippet if x=1?  x<<2 ",4,2,1,1),
	("What will be the output of the following Python function? min(max(False,-3,-4), 2,7)",-4,2,"False",3),
	("Which of the following is not a core data type in Python programming?","Tuples","Lists","Class",3),
	("What will be the output of the following Python function? len(['hello',2, 4, 6]) ",4,3,6,1),
	("Which one of the following is not a keyword in Python language?","pass","assert","eval",3),
	("Who developed Python Programming Language?","Rasmus Lerdorf","Wick van Rossum","Guido van Rossum",3),
	("Which type of Programming does Python support?","object-oriented programming","structured programming","both",3),
	("Which of the following is the use of id() function in python?","Id() returns the identity of the object","Every object doesn’t have a unique id","Both",1),
	("Which of the following is a Python tuple?","{1, 2, 3}","[1, 2, 3]","(1, 2, 3)",3),
	("Which of the following is used to represent list in python","[]","{}","()",1),
	("Which of the following is the correct syntax for type casting ","datatype(variable)","(datatype)variable","both",1);
   
   
   
   
   
CREATE TABLE LOGIN_DETAILS (
	email VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
    );
    
SELECT * FROM LOGIN_DETAILS;    

   
   
    