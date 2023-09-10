### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL? 
  - a DB management system that is made to store and retrieve data that supports SQL and JSON querying

- What is the difference between SQL and PostgreSQL?
  - SQL is a language that we manage DBs with - its not tied to a DB managagement system and has its own syntax
  - PSQL is a DB management system that uses SQL language 

- In `psql`, how do you connect to a database?
  - \c database_name

- What is the difference between `HAVING` and `WHERE`?
  - WHERE is used to filter individual rows based on column values/conditions apply
  - HAVING filters grouped rows based on values AFTER grouping

- What is the difference between an `INNER` and `OUTER` join?
  - An INNER joing returns on the rows that have a match in both tables that are joined
  - An OUTER join returns all rows fromone table (left or right) and the matching rows from the OTHER table

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - going off the previous answer - a LEFT OUTER would return all rows from the left table and matched from the right
  - a RIGHT OUTER would give the opposite result

- What is an ORM? What do they do?
  - Object Relational Mapping
  - SQLA is the ORM we used --- object oriented DB operations that simplilfies the interactions and helps qith querying and caching

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
    -AJAX is a client side request and are asynchronous by nature - should not use with sensetive information
    -requests is server side and fetches the data from an API which blocks code execution until a response is recieved - more secure

- What is CSRF? What is the purpose of the CSRF token?
  - Cross Site Request Forgery - the token adds a layer of web security for the user - We embed the token, hide it, and use it to validate on form submits

- What is the purpose of `form.hidden_tag()`?
  - function to generate a hidden form field within the HTML form - used for the CSRF/security purposes when using WTForms