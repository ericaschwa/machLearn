This program does not exhibit machine learning persay. Instead, it is an
attempt at the 2015 Mindsumo challenge. The challenge is as folows:



"Write a script:

Using the transactions data attached below, write a script in Java, Python,
C/C++, or JavaScript that outputs a list of subscription IDs, their
subscription type (daily, monthly, yearly, one-off), and the duration of their
subscription.

Bonus Questions (not required):

1. Give annual revenue numbers for all years between 1966 and 2014. Which years
had the highest revenue growth, and highest revenue loss?

2. Predict annual revenue for year 2015 (based on historical retention and
new subscribers)"



This program tries to solve all three of these questions. However, at this
point, it can solve the main challenge but is still in the beginning stages
for the bonus questions.




To run program that puts data into JSON file form:
python "get_transaction_data.py"

To run program that solves the main (required) question and puts the data,
which has been newly organized, into JSON file form:
python "transactions.py"

To run the program that solves the first bonus question:
python "bonus1.py"

To run the program that solves the second bonus question:
python "bonus2.py"