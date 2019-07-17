""" write a query to get the first three characters of first name from employee
table.
write a query to display the first name of all employees who have a 'b' and
'd' in their name.
write a query to display the last name of employees who's names have exactly
6 characters."""

#to get first three character :
#   SUBSTRING(first_name,1,3)
#for searching if first_name contains b and d:
#SELECT first_name FROM employee
#WHERE first_name LIKE '%b%' AND first_name LIKE '%d%'
#for employee whose name has 6 characters
#WHERE first_name LIKE ______
