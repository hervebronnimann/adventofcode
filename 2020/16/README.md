I chose to simplify the input, by having only two sections, the rules and the nearby tickets.
The ticket isn't relevant until the last part, and can be manually copied into the code.
The rules and tickets are simply separated by an empty line.  Awk doesn't have a return statement
for going to the next clause, which really sucks. (The next statement goes to the next record.)

The answer to question 2 is in two steps: first use 16.2.awk to extract the valid tickets,
then pipe the result into 16.valid.awk.

awk -f 16.2.awk input.2.txt | awk -f 16.valid.awk
