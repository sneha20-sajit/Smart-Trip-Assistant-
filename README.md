# **Smart Trip Assistant**



A Python and MySQL-based tourism guide that helps users explore travel destinations across India, compare average travel costs, and discover seasonal packing tips.





##### Project Overview



Smart Trip Assistant is a database-driven tourism guide developed using Python and MySQL. It provides destination information based on the user's selected region and state or union territory.



The project also allows users to compare average travel costs through a graphical representation and access packing tips based on their travel month.



##### 

##### Features



* **Destination Information:** Explore travel destinations across six Indian regions.
* **State Selection:** Select a state or union territory to view available destinations.
* **Travel Cost Comparison:** Compare average travel costs using a bar chart.
* **Seasonal Packing Tips:** Get packing suggestions based on the selected travel month.
* **Database Integration:** Retrieve destination details and travel tips from a MySQL database.
* **Tabular Display:** View destination information in a structured table.



##### 

##### Technologies Used



* Python
* MySQL
* MySQL Connector for Python
* Tabulate
* Matplotlib
* NumPy





##### Database Structure



The project uses a MySQL database named "tourism", containing two tables:



* **travel\_guide:** Stores travel destination information and related details.
* **tips:** Stores seasonal packing tips.



The database structure and sample data are provided in "Tourism.sql".



&#x20;

##### Installation and Setup



###### 1\. Install the requirements

Make sure Python and MySQL Server are installed on your computer.

Install the required Python libraries:

&#x09;pip install -r requirements.txt





###### 2\. Set up the MySQL database

1. Open MySQL Workbench.
2. Connect to your MySQL server.
3. Open the "Tourism.sql" file.
4. Execute the entire SQL script.
5. Refresh the Schemas panel and check that the "tourism" database has been created with both tables.



###### 3\. Configure the MySQL password

The Python program reads the MySQL password from an environment variable.

On Windows PowerShell, enter:

&#x09;$env:MYSQL\_PASSWORD="your\_mysql\_password"

Replace the placeholder with your own MySQL password.



###### 4\. Run the program

In PowerShell, navigate to the project folder and execute:

&#x09;python main.py



##### Limitations



* Destination information and travel costs depend on the data available in the database.
* The project requires a working MySQL server connection.
* Travel costs are average estimates and may vary depending on actual travel conditions.
* Packing tips are based on the available seasonal information in the database.



##### Conclusion



Smart Trip Assistant demonstrates how Python and MySQL can be integrated to create an interactive tourism guide. It combines database management, data presentation and graphical visualisation to make travel information easier to explore.



##### Project Structure



Smart-Trip-Assistant/

│

├── main.py

├── Tourism.sql

├── README.md

├── requirements.txt

├── .gitignore

│

└── screenshots/

&#x20;   ├── maharashtra-output.png

&#x20;   ├── kerala-output.png

&#x20;   ├── tamil-nadu-output.png

&#x20;   └── rajasthan-output.png



##### Project Screenshots



* **Maharashtra** screenshots/maharashtra-output.png
* **Kerala** screenshots/kerala-output.png
* **Tamil Nadu** screenshots/tamil-nadu-output.png
* **Rajasthan** screenshots/rajasthan-output.png



