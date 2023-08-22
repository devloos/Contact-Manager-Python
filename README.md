## Project Overview

> This Python project aims to create a Contact Manager that covers essential concepts in Python. These include working with Complex Data Structures, implementing Object-Oriented Programming principles, handling Read and Write operations to disk, and gaining proficiency in code modularization techniques.

### Requirements

> In addition to replicating the provided sample output, specific guidelines pertain to the organization of your code and your interaction with files. You are expected to simulate a Database by utilizing a CSV file, which is exemplified within the "db" folder. This CSV file will serve as the means to read from and write to your contacts, ensuring that any contacts created in previous program executions are retained in subsequent runs.

> While it's not mandatory to generate distinct profiles containing varied contacts, you will need to extract information from a `config.json` file. This JSON file consists of two properties: `Name` and `Password`. Upon launching your program, these properties will be employed to greet the user and prompt them to input a password.

### Example Output

```
Hey Bob!

Please enter password: panda123

1. List Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts by Name
5. Exit

Option: 1

Name: Guillermo Beste
Phone Number: 856-346-2331
Email: gbesteqd@wordpress.com
Relationship: Uncle

Name: Benny Sleath
Phone Number: 676-865-7290
Email: bsleathqe@cbc.ca
Relationship: Friend

Name: Cheston Bertelmot
Phone Number: 373-901-9106
Email: cbertelmotqf@cbsnews.com
Relationship: Neighbor

1. List Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts by Name
5. Exit

Option: 2

Name: Dacy Prott
Phone Number: 987-699-7815
Email: dprottqg@nasa.gov
Relationship: Aunt

1. List Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts by Name
5. Exit

Option: 3

1. Remove by Name
2. Remove by Phone Number
3. Remove by Email

Option: 3

Email: dprottqg@nasa.gov

Dropped Dacy Prott!

1. List Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts by Name
5. Exit

Option: 4

Sorted by Name!

1. List Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts by Name
5. Exit

Option: 1

Name: Benny Sleath
Phone Number: 676-865-7290
Email: bsleathqe@cbc.ca
Relationship: Friend

Name: Cheston Bertelmot
Phone Number: 373-901-9106
Email: cbertelmotqf@cbsnews.com
Relationship: Neighbor

Name: Guillermo Beste
Phone Number: 856-346-2331
Email: gbesteqd@wordpress.com
Relationship: Uncle

1. List Contacts
2. Add Contact
3. Remove Contact
4. Sort Contacts by Name
5. Exit

Option: 5
```
