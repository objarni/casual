Casual - examples of mundance programming tasks in X languages
==============================================================


Why?
----
I sit with many different languages every day, and small syntactic
differences annoy me to have to google all the time. IntelliSense
does not help with how to write an object literal, or a for-loop!


How?
----
X number of self-verifying input files in different languages
display the syntax of needed 'language features' clearly and within
one page of code (no more!).

Any and all of the examples should:

1. Read input.json --> A
2. Include an in-code object literal
   equal to input.json content --> B
3. Produce a text string from A and B --> Atxt, Btxt
4. Verify Atxt == Btxt
5. Produce a text report from A --> Areport
6. Verify Areport equals content of report.txt


What?
-----
* Looping over lists
* Writing object literals, including lists, string properties
* Reading and writing text files
* Reading and writing JSON files
* Asserting
* Interpolating and concatenating string
