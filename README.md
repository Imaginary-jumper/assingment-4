# assingment-4

task 1 (file_read): first with open function the code finds file and opens it in read mode , a local variable read all the lines in the file , for this part i had to use google to understand that cursor moves continously to bring it back seek function is used, then a loop runs with range of number of lines identified in the file , the letter_counter finds number of letter in a line (had a lot of problem here but later figured out its a list and we have to use [ ] to call for values), then it print the line with the number (like line 1 , line 2 etc) and the now since read function can only read a particular set of letters which we found before usind len(b[i]), it can print the called number of letters.

and it handles eroors

additonal: now while writing this code explaination , just got the idea that instead of doing all this len calculation , i could have just called the b[i] and printed it with line number (could have gotten the number by using a for loop).

task 2: write and append , it first taakes user's input and writes on file , since "w" everything previously writeen will be overwrite , now it takes append inout from user and write it but with "a" function means it will append what previously was written to make it in new like , \n was added

and finally full file is printed using "r" finction 
