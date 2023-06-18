<p><br></p>
<p>0x0F. Python - Object-relational mapping</p>
<p>Python</p>
<p>OOP</p>
<p>SQL</p>
<p>MySQL</p>
<p>ORM</p>
<p>SQLAlchemy</p>
<p>&nbsp;By: Guillaume</p>
<p>&nbsp;Weight: 1</p>
<p>&nbsp;Project **** start Jun 16, 2023 6:00 AM, must end by Jun 20, 2023 6:00 AM</p>
<p>&nbsp;Checker *** released at Jun 17, 2023 6:** AM</p>
<p>&nbsp;An auto review will ** launched ** the deadline</p>
<p>Before *** start&hellip;</p>
<p>****** make sure your MySQL server is in 8.0 -&gt; *** to ******* MySQL 8.0 in Ubuntu 20.04</p>
<p><br></p>
<p>Background Context</p>
<p>In this project, you will link two amazing worlds: Databases *** Python!</p>
<p><br></p>
<p>In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.</p>
<p><br></p>
<p>In the second part, you will *** the module SQLAlchemy (don&rsquo;t *** ** how to pronounce it&hellip;) ** Object Relational ****** (ORM).</p>
<p><br></p>
<p>The ******* difference is: no more SQL queries! Indeed, the purpose of an ORM is to ******** the storage to the usage. With ** ORM, your biggest concern will be &ldquo;What can I do with ** objects&rdquo; *** *** &ldquo;How this object ** stored? where? when?&rdquo;. You won&rsquo;t write any SQL ******* only Python code. Last thing, your code won&rsquo;t be &ldquo;storage type&rdquo; dependent. You will be able ** change **** ******* easily without re-writing your ****** project.</p>
<p><br></p>
<p>Without ORM:</p>
<p><br></p>
<p>**** = MySQLdb.connect(host=&quot;localhost&quot;, port=3306, user=&quot;root&quot;, passwd=&quot;root&quot;, db=&quot;my_db&quot;, charset=&quot;utf8&quot;)</p>
<p>cur = conn.cursor()</p>
<p>cur.execute(&quot;SELECT * FROM states ORDER BY ** ASC&quot;) # HERE I have to know SQL ** grab all states in my database</p>
<p>query_rows = cur.fetchall()</p>
<p>for *** in query_rows:</p>
<p>&nbsp; &nbsp; print(row)</p>
<p>cur.close()</p>
<p>conn.close()</p>
<p>With an ORM:</p>
<p><br></p>
<p>engine = create_engine(&apos;mysql+mysqldb://{}:{}@localhost/{}&apos;.format(&quot;root&quot;, &quot;root&quot;, &quot;my_db&quot;), pool_pre_ping=True)</p>
<p>Base.metadata.create_all(engine)</p>
<p><br></p>
<p>session = Session(engine)</p>
<p>*** state in session.query(State).order_by(State.id).all(): # HERE: ** SQL query, only objects!</p>
<p>&nbsp; &nbsp; print(&quot;{}: {}&quot;.format(state.id, state.name))</p>
<p>session.close()</p>
<p>Do you see *** difference? Cool, right?</p>
<p><br></p>
<p>The biggest difficulty with *** is: The syntax!</p>
<p><br></p>
<p>Indeed, all of **** have the **** type ** syntax, but not always. ****** read tutorials and don&rsquo;t read *** ****** documentation ****** starting, just jump on it if you don&rsquo;t get something.</p>
<p><br></p>
<p>Resources</p>
<p>Read or watch:</p>
<p><br></p>
<p>Object-relational mappers</p>
<p>mysqlclient/******* documentation (****** don&rsquo;t pay attention ** _mysql)</p>
<p>MySQLdb tutorial</p>
<p>********** tutorial</p>
<p>SQLAlchemy</p>
<p>mysqlclient/MySQLdb</p>
<p>************ to SQLAlchemy</p>
<p>Flask SQLAlchemy</p>
<p>10 common stumbling blocks for SQLAlchemy newbies</p>
<p>****** SQLAlchemy Cheatsheet</p>
<p>SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but *** concept of ********** is *** same with MySQL)</p>
<p>SQLAlchemy Tutorial</p>
<p>Learning Objectives</p>
<p>At the end of **** project, you are ******** to be able to explain to anyone, ******* the **** of Google:</p>
<p><br></p>
<p>General</p>
<p>Why Python programming ** awesome</p>
<p>How ** connect to a MySQL database from a Python script</p>
<p>How to SELECT rows ** a MySQL table from a ****** script</p>
<p>How to ****** rows in a MySQL table **** a Python script</p>
<p>What *** means</p>
<p>*** to map a Python Class to a MySQL table</p>
<p>Copyright - Plagiarism</p>
<p>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</p>
<p>*** will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</p>
<p>You are not allowed to ******* any content of **** project.</p>
<p>Any form of plagiarism is strictly forbidden and will result ** removal **** the program.</p>
<p>Requirements</p>
<p>General</p>
<p>******* editors: vi, vim, emacs</p>
<p>All your files will be interpreted/compiled on ****** 20.04 LTS using python3 (version 3.8.5)</p>
<p>**** files will be executed with MySQLdb version 2.0.x</p>
<p>Your files **** be executed with SQLAlchemy ******* 1.4.x</p>
<p>All your files ****** end **** a new line</p>
<p>The first line of all your files ****** be exactly #!/usr/bin/python3</p>
<p>A README.md file, at the root of the folder of the project, is mandatory</p>
<p>Your code should use the pycodestyle (version 2.8.*)</p>
<p>All your files must be executable</p>
<p>The length ** your files **** ** tested using wc</p>
<p>All your modules should have a ************* (python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;)</p>
<p>All your ******* should have a documentation (python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;)</p>
<p>All your functions (inside and ******* a class) should have a documentation (python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos; and python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;)</p>
<p>A documentation is *** a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the ******* of the module, class or method (the ****** of it will be verified)</p>
<p>You are *** allowed to use execute with sqlalchemy</p>
<p>More Info</p>
<p>Install MySQLdb module version 2.0.x</p>
<p>For installing MySQLdb, you need to have ***** installed: How to install MySQL 8.0 in ****** 20.04</p>
<p><br></p>
<p>$ **** apt-get install python3-dev</p>
<p>$ sudo apt-get install libmysqlclient-dev</p>
<p>$ sudo apt-*** install zlib1g-dev</p>
<p>$ sudo pip3 install mysqlclient</p>
<p>...</p>
<p>$ python3</p>
<p>&gt;&gt;&gt; import MySQLdb</p>
<p>&gt;&gt;&gt; MySQLdb.version_info&nbsp;</p>
<p>(2, 0, 3, &apos;final&apos;, 0)</p>
<p>Install ********** module ******* 1.4.x</p>
<p>$ sudo pip3 install SQLAlchemy</p>
<p>...</p>
<p>$ python3</p>
<p>&gt;&gt;&gt; import sqlalchemy</p>
<p>&gt;&gt;&gt; sqlalchemy.__version__&nbsp;</p>
<p>&apos;1.4.22&apos;</p>
<p>Also, you can have this warning message:</p>
<p><br></p>
<p>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, &quot;&apos;@@SESSION.GTID_EXECUTED&apos; is deprecated and will be re</p>
<p>moved ** a future release.&quot;)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>
<p>&nbsp; cursor.execute(statement, parameters)&nbsp;&nbsp;</p>
<p>You can ignore it.</p>
<p><br></p>
<p>Tasks</p>
<p>0. Get all states</p>
<p>mandatory</p>
<p>Write a script that lists all states from *** ******** hbtn_0e_0_usa:</p>
<p><br></p>
<p>Your script should take 3 arguments: mysql username, ***** password and ******** name (no argument validation needed)</p>
<p>You must use the module MySQLdb (import MySQLdb)</p>
<p>Your script should connect to a MySQL server running on localhost ** port 3306</p>
<p>Results must be sorted in ascending order by states.id</p>
<p>Results must ** displayed as they are in the example below</p>
<p>Your code should *** be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql</p>
<p>-- Create ****** ***** in hbtn_0e_0_usa **** some data</p>
<p>CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;</p>
<p>USE hbtn_0e_0_usa;</p>
<p>****** TABLE IF NOT EXISTS states (&nbsp;</p>
<p>&nbsp; &nbsp; ** INT NOT **** AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY KEY (id)</p>
<p>);</p>
<p>INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p</p>
<p>Enter password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa</p>
<p>(1, &apos;California&apos;)</p>
<p>(2, &apos;Arizona&apos;)</p>
<p>(3, &apos;Texas&apos;)</p>
<p>(4, &apos;New York&apos;)</p>
<p>(5, &apos;Nevada&apos;)</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No **** cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 0-select_states.py</p>
<p>&nbsp; &nbsp;</p>
<p>1. Filter states</p>
<p>mandatory</p>
<p>***** a script **** lists all states with a **** starting with N (upper N) from the database hbtn_0e_0_usa:</p>
<p><br></p>
<p>Your script ****** take 3 arguments: mysql username, ***** password *** database **** (** argument ********** needed)</p>
<p>You must use the ****** MySQLdb (import MySQLdb)</p>
<p>Your script should connect to a MySQL server running on localhost at **** 3306</p>
<p>******* must be sorted in ascending order by states.id</p>
<p>Results **** be displayed ** they are in the ******* below</p>
<p>Your code should not be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql</p>
<p>-- Create states table in hbtn_0e_0_usa **** some data</p>
<p>CREATE DATABASE IF NOT ****** hbtn_0e_0_usa;</p>
<p>USE hbtn_0e_0_usa;</p>
<p>CREATE ***** ** NOT EXISTS states (&nbsp;</p>
<p>&nbsp; &nbsp; ** INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; ******* KEY (id)</p>
<p>);</p>
<p>****** INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ *** 0-select_states.*** | mysql -***** -p</p>
<p>Enter password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa</p>
<p>(4, &apos;New York&apos;)</p>
<p>(5, &apos;Nevada&apos;)</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 1-filter_states.py</p>
<p>&nbsp; &nbsp;</p>
<p>2. ****** states by user input</p>
<p>mandatory</p>
<p>Write a script that takes ** an argument and displays *** values in the states table of hbtn_0e_0_usa where name matches the argument.</p>
<p><br></p>
<p>Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)</p>
<p>*** must use *** module MySQLdb (import MySQLdb)</p>
<p>Your ****** ****** connect to a MySQL server running on localhost at port 3306</p>
<p>You must use format to create *** SQL query with *** user input</p>
<p>******* **** be sorted in ascending ***** by states.id</p>
<p>Results must be displayed ** they are in the ******* below</p>
<p>Your **** should not be ******** when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql</p>
<p>-- Create states table in hbtn_0e_0_usa with some data</p>
<p>****** DATABASE IF NOT ****** hbtn_0e_0_usa;</p>
<p>USE hbtn_0e_0_usa;</p>
<p>CREATE TABLE ** NOT EXISTS states (&nbsp;</p>
<p>&nbsp; &nbsp; id INT *** NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY KEY (id)</p>
<p>);</p>
<p>INSERT **** ****** (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p</p>
<p>***** password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py **** **** hbtn_0e_0_usa &apos;Arizona&apos;</p>
<p>(2, &apos;Arizona&apos;)</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 2-my_filter_states.py</p>
<p>&nbsp; &nbsp;</p>
<p>3. SQL Injection...</p>
<p>mandatory</p>
<p>Wait, do you remember the ******** task? Did you test &quot;Arizona&apos;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &apos;&quot; ** an input?</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa &quot;Arizona&apos;; ******** TABLE states ; ****** * **** states WHERE name = &apos;&quot;</p>
<p>(2, &apos;Arizona&apos;)</p>
<p>guillaume@ubuntu:~/0x0F$ ./0-select_states.** root root hbtn_0e_0_usa</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>What? Empty?</p>
<p><br></p>
<p>Yes, it&rsquo;s an SQL injection to ****** all records of a table&hellip;</p>
<p><br></p>
<p>Once again, write a script that takes in arguments *** displays all values in *** states table of hbtn_0e_0_usa where name matches the argument. But **** time, write one that is safe from MySQL injections!</p>
<p><br></p>
<p>Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)</p>
<p>You must use the module ******* (import MySQLdb)</p>
<p>Your script should ******* to a MySQL server running on localhost at port 3306</p>
<p>Results must be sorted in ascending order by states.id</p>
<p>******* must be displayed ** **** *** ** the example below</p>
<p>Your code should not be ******** **** imported</p>
<p>guillaume@ubuntu:~/0x0F$ *** 0-select_states.sql</p>
<p>-- Create states ***** in hbtn_0e_0_usa with some data</p>
<p>CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;</p>
<p>USE hbtn_0e_0_usa;</p>
<p>CREATE TABLE IF *** EXISTS states (&nbsp;</p>
<p>&nbsp; &nbsp; id INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; **** VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY KEY (id)</p>
<p>);</p>
<p>INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p</p>
<p>***** password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa &apos;Arizona&apos;</p>
<p>(2, &apos;Arizona&apos;)</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test ***** needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 3-my_safe_filter_states.py</p>
<p>&nbsp; &nbsp;</p>
<p>4. Cities by states</p>
<p>mandatory</p>
<p>Write a script that lists all cities from the database hbtn_0e_4_usa</p>
<p><br></p>
<p>Your ****** ****** take 3 arguments: mysql username, mysql password and database name</p>
<p>You must use the ****** MySQLdb (import MySQLdb)</p>
<p>Your script should connect to a MySQL server running on localhost at port 3306</p>
<p>Results must be ****** in ascending order by cities.id</p>
<p>You *** use only execute() once</p>
<p>Results must be displayed as they are in the example below</p>
<p>Your code should not be ******** when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql</p>
<p>-- Create states table in hbtn_0e_4_usa with some data</p>
<p>CREATE DATABASE IF *** EXISTS hbtn_0e_4_usa;</p>
<p>USE hbtn_0e_4_usa;</p>
<p>****** TABLE ** NOT EXISTS states (&nbsp;</p>
<p>&nbsp; &nbsp; ** INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; ******* KEY (id)</p>
<p>);</p>
<p>INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>CREATE TABLE IF NOT EXISTS cities (&nbsp;</p>
<p>&nbsp; &nbsp; ** INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; state_id INT NOT NULL,</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY *** (id),</p>
<p>&nbsp; &nbsp; FOREIGN KEY(state_id) ********** states(id)</p>
<p>);</p>
<p>INSERT **** cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;*** Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);</p>
<p>****** INTO cities (state_id, name) ****** (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);</p>
<p>INSERT INTO ****** (state_id, name) VALUES (4, &quot;New York&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ *** 4-cities_by_state.sql | mysql -uroot -p</p>
<p>Enter password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root **** hbtn_0e_4_usa</p>
<p>(1, &apos;San Francisco&apos;, &apos;California&apos;)</p>
<p>(2, &apos;San Jose&apos;, &apos;California&apos;)</p>
<p>(3, &apos;*** Angeles&apos;, &apos;California&apos;)</p>
<p>(4, &apos;Fremont&apos;, &apos;California&apos;)</p>
<p>(5, &apos;Livermore&apos;, &apos;California&apos;)</p>
<p>(6, &apos;Page&apos;, &apos;Arizona&apos;)</p>
<p>(7, &apos;Phoenix&apos;, &apos;Arizona&apos;)</p>
<p>(8, &apos;Dallas&apos;, &apos;Texas&apos;)</p>
<p>(9, &apos;Houston&apos;, &apos;Texas&apos;)</p>
<p>(10, &apos;Austin&apos;, &apos;Texas&apos;)</p>
<p>(11, &apos;New York&apos;, &apos;New York&apos;)</p>
<p>(12, &apos;Las Vegas&apos;, &apos;Nevada&apos;)</p>
<p>(13, &apos;Reno&apos;, &apos;Nevada&apos;)</p>
<p>(14, &apos;Henderson&apos;, &apos;Nevada&apos;)</p>
<p>(15, &apos;Carson City&apos;, &apos;Nevada&apos;)</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 4-cities_by_state.py</p>
<p>&nbsp; &nbsp;</p>
<p>5. All cities by state</p>
<p>mandatory</p>
<p>Write a script that takes in the name ** a state ** an argument and lists all cities of that state, using the database hbtn_0e_4_usa</p>
<p><br></p>
<p>Your script should **** 4 arguments: mysql username, mysql password, database name *** state name (*** injection free!)</p>
<p>You must *** the ****** ******* (import MySQLdb)</p>
<p>Your ****** should connect ** a MySQL server ******* on localhost at port 3306</p>
<p>******* must be sorted in ascending order ** cities.id</p>
<p>You can use **** execute() once</p>
<p>The results **** be ********* as they are in the ******* below</p>
<p>Your code ****** not be ******** when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql</p>
<p>-- Create states table in hbtn_0e_4_usa with some data</p>
<p>CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;</p>
<p>USE hbtn_0e_4_usa;</p>
<p>CREATE TABLE IF NOT EXISTS states (&nbsp;</p>
<p>&nbsp; &nbsp; id *** NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY *** (id)</p>
<p>);</p>
<p>****** INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>CREATE TABLE IF NOT EXISTS ****** (&nbsp;</p>
<p>&nbsp; &nbsp; id INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; state_id INT NOT NULL,</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY KEY (id),</p>
<p>&nbsp; &nbsp; FOREIGN KEY(state_id) REFERENCES states(id)</p>
<p>);</p>
<p>INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);</p>
<p>INSERT INTO cities (state_id, name) ****** (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ ./5-filter_cities.** root root hbtn_0e_4_usa Texas</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p</p>
<p>***** password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas</p>
<p>Dallas, Houston, Austin</p>
<p>guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py **** root hbtn_0e_4_usa Hawaii</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;&nbsp;</p>
<p>** **** ***** needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 5-filter_cities.py</p>
<p>&nbsp; &nbsp;</p>
<p>6. First state model</p>
<p>mandatory</p>
<p><br></p>
<p><br></p>
<p>***** a python file that contains the class definition of a State *** an ******** Base = declarative_base():</p>
<p><br></p>
<p>***** class:</p>
<p>inherits **** Base Tips</p>
<p>links to *** MySQL table states</p>
<p>class attribute id that ********** a ****** of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</p>
<p>class attribute name that represents a column ** a string with maximum 128 characters *** can&rsquo;t be null</p>
<p>You must *** the module SQLAlchemy</p>
<p>Your script should connect ** a MySQL server running ** ********* at port 3306</p>
<p>WARNING: all classes *** ******* from Base must be imported before calling Base.metadata.create_all(engine)</p>
<p>guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql</p>
<p>-- Create database hbtn_0e_6_usa</p>
<p>CREATE DATABASE IF NOT ****** hbtn_0e_6_usa;</p>
<p>USE hbtn_0e_6_usa;</p>
<p>SHOW ****** TABLE states;</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p</p>
<p>Enter password:&nbsp;</p>
<p>ERROR 1146 (42S02) at line 4: Table &apos;hbtn_0e_6_usa.states&apos; doesn&apos;t exist</p>
<p>guillaume@ubuntu:~/0x0F$ cat 6-model_state.py</p>
<p>#!/usr/bin/python3</p>
<p>&quot;&quot;&quot;Start **** class to table in database&nbsp;</p>
<p>&quot;&quot;&quot;</p>
<p>import sys</p>
<p>from model_state ****** Base, State</p>
<p><br></p>
<p>from sqlalchemy import (create_engine)</p>
<p><br></p>
<p>if __name__ == &quot;__main__&quot;:</p>
<p>&nbsp; &nbsp; engine = create_engine(&apos;mysql+mysqldb://{}:{}@localhost/{}&apos;.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)</p>
<p>&nbsp; &nbsp; Base.metadata.create_all(engine)</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ ./6-model_state.py root **** hbtn_0e_6_usa</p>
<p>guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p</p>
<p>Enter password:&nbsp;</p>
<p>Table Create Table</p>
<p>states CREATE ***** `states` (\n `id` int(11) NOT NULL AUTO_INCREMENT,\n `name` varchar(128) NOT NULL,\n PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: model_state.py</p>
<p>&nbsp; &nbsp;</p>
<p>7. All states *** SQLAlchemy</p>
<p>mandatory</p>
<p>Write a script that lists all State objects from the database hbtn_0e_6_usa</p>
<p><br></p>
<p>Your script should take 3 arguments: mysql username, mysql password and database name</p>
<p>You must use the module SQLAlchemy</p>
<p>*** must ****** State and Base from model_state - from model_state ****** Base, State</p>
<p>Your script should connect to a ***** ****** running on localhost at **** 3306</p>
<p>Results must be sorted in ascending order by states.id</p>
<p>The results must be displayed ** they are in the ******* below</p>
<p>Your code should not be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql</p>
<p>-- Insert states</p>
<p>****** INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | ***** -uroot -p hbtn_0e_6_usa</p>
<p>Enter password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa</p>
<p>1: California</p>
<p>2: Arizona</p>
<p>3: Texas</p>
<p>4: New York</p>
<p>5: Nevada</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test ***** needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 7-model_state_fetch_all.py</p>
<p>&nbsp; &nbsp;</p>
<p>8. First state</p>
<p>mandatory</p>
<p>Write a script that prints the first State object from the database hbtn_0e_6_usa</p>
<p><br></p>
<p>Your ****** should take 3 arguments: mysql username, mysql password *** database name</p>
<p>You must use the module SQLAlchemy</p>
<p>You must import State and Base from model_state - **** model_state import Base, State</p>
<p>Your script ****** connect to a MySQL server running ** localhost at port 3306</p>
<p>The state you display must be the first ** states.id</p>
<p>You *** not allowed to fetch all states from the database before displaying the result</p>
<p>The results must be displayed as they *** in *** example below</p>
<p>If the table states is empty, print ******* followed by a new line</p>
<p>Your code should not be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa</p>
<p>1: California</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 8-model_state_fetch_first.py</p>
<p>&nbsp; &nbsp;</p>
<p>9. Contains `a`</p>
<p>mandatory</p>
<p>Write a ****** that lists *** State objects that contain the letter a from the database hbtn_0e_6_usa</p>
<p><br></p>
<p>Your script should take 3 arguments: mysql username, mysql password and ******** name</p>
<p>You must use the module SQLAlchemy</p>
<p>You must ****** State and Base from model_state - from model_state ****** Base, State</p>
<p>Your script ****** connect to a MySQL server running on localhost at port 3306</p>
<p>******* **** be sorted ** ascending order ** states.id</p>
<p>The results must be displayed as **** are ** the example below</p>
<p>Your code should not be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa</p>
<p>1: California</p>
<p>2: Arizona</p>
<p>3: Texas</p>
<p>5: Nevada</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>** test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 9-model_state_filter_a.py</p>
<p>&nbsp; &nbsp;</p>
<p>10. Get a state</p>
<p>mandatory</p>
<p>Write a script that ****** the State object with the **** passed as ******** from *** database hbtn_0e_6_usa</p>
<p><br></p>
<p>**** script ****** take 4 arguments: mysql username, mysql password, database **** *** state name to search (SQL injection free)</p>
<p>You **** use the module SQLAlchemy</p>
<p>You must ****** State and Base **** model_***** - from model_state ****** Base, State</p>
<p>Your script should connect to a MySQL server running on localhost at port 3306</p>
<p>You can assume you have one ****** **** *** state name to search</p>
<p>Results must display the states.id</p>
<p>If no state has the name you searched for, display Not found</p>
<p>Your code should *** be ******** when imported</p>
<p>guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas</p>
<p>3</p>
<p>guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.** root **** hbtn_0e_6_usa Illinois</p>
<p>Not found</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 10-model_state_my_get.py</p>
<p>&nbsp; &nbsp;</p>
<p>11. Add a new state</p>
<p>mandatory</p>
<p>Write a script that adds the State object &ldquo;Louisiana&rdquo; to the database hbtn_0e_6_usa</p>
<p><br></p>
<p>Your script should take 3 arguments: mysql username, ***** password and database name</p>
<p>You must use *** module SQLAlchemy</p>
<p>You must import State and Base from model_state - from model_state import Base, State</p>
<p>Your script should connect to a MySQL server running on ********* at port 3306</p>
<p>Print the new states.id ***** creation</p>
<p>Your code should not be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.** root root hbtn_0e_6_usa&nbsp;</p>
<p>6</p>
<p>guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa&nbsp;</p>
<p>1: California</p>
<p>2: Arizona</p>
<p>3: Texas</p>
<p>4: New York</p>
<p>5: Nevada</p>
<p>6: Louisiana</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No **** cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 11-model_state_insert.py</p>
<p>&nbsp; &nbsp;</p>
<p>12. Update a state</p>
<p>mandatory</p>
<p>***** a script that changes the name of a State object from the database hbtn_0e_6_usa</p>
<p><br></p>
<p>**** script should take 3 arguments: mysql username, mysql password and database name</p>
<p>You must use the module SQLAlchemy</p>
<p>You must import State and **** from model_state - from model_state ****** Base, State</p>
<p>Your script should connect to a MySQL server running on localhost at port 3306</p>
<p>Change the name of the State where id = 2 to New Mexico</p>
<p>Your code should *** be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa&nbsp;</p>
<p>1: California</p>
<p>2: New Mexico</p>
<p>3: Texas</p>
<p>4: New York</p>
<p>5: Nevada</p>
<p>6: Louisiana</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>GitHub repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 12-model_state_update_id_2.py</p>
<p>&nbsp; &nbsp;</p>
<p>13. Delete states</p>
<p>mandatory</p>
<p>Write a script that deletes all State ******* with a name containing the letter a from the database hbtn_0e_6_usa</p>
<p><br></p>
<p>Your script should take 3 arguments: mysql username, ***** password and database name</p>
<p>*** must use the module SQLAlchemy</p>
<p>*** must import State and Base from model_state - from model_state import Base, State</p>
<p>Your script should ******* to a MySQL server ******* on localhost at port 3306</p>
<p>Your code should not be executed when imported</p>
<p>guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.** root root hbtn_0e_6_usa&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa&nbsp;</p>
<p>2: New Mexico</p>
<p>4: New York</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>No test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>****** repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: 13-model_state_delete_a.py</p>
<p>&nbsp; &nbsp;</p>
<p>14. ****** in state</p>
<p>mandatory</p>
<p>***** a Python file similar to model_state.py named model_city.py that ******** the class definition of a City.</p>
<p><br></p>
<p>**** class:</p>
<p>inherits from **** (imported from model_state)</p>
<p>links ** the MySQL table cities</p>
<p>class attribute id that represents a column ** an auto-generated, unique integer, can&rsquo;t be null and is a primary key</p>
<p>class attribute name that represents a column ** a string of 128 characters and can&rsquo;t ** null</p>
<p>class attribute state_id that represents a column of an integer, can&rsquo;t be null and ** a foreign *** to states.id</p>
<p>You must *** the module SQLAlchemy</p>
<p>Next, ***** a ****** 14-model_city_fetch_by_state.** that prints all **** objects from the database hbtn_0e_14_usa:</p>
<p><br></p>
<p>Your script should take 3 arguments: ***** username, ***** password and ******** name</p>
<p>You must use the module SQLAlchemy</p>
<p>*** must import State and **** from model_state - from model_state import Base, State</p>
<p>Your script should connect to a MySQL ****** running on localhost at port 3306</p>
<p>Results must ** sorted ** ascending order by cities.id</p>
<p>Results must ** display as they are in the example below (&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;)</p>
<p>Your code should not ** ******** when imported</p>
<p>guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql</p>
<p>-- Create ******** hbtn_0e_14_usa, tables states and cities + some data</p>
<p>CREATE ******** IF NOT EXISTS hbtn_0e_14_usa;</p>
<p>USE hbtn_0e_14_usa;</p>
<p><br></p>
<p>****** TABLE ** NOT EXISTS ****** (&nbsp;</p>
<p>&nbsp; &nbsp; ** INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; ******* KEY (id)</p>
<p>);</p>
<p>INSERT **** states (name) ****** (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);</p>
<p><br></p>
<p>CREATE TABLE IF NOT EXISTS ****** (&nbsp;</p>
<p>&nbsp; &nbsp; id INT NOT NULL AUTO_INCREMENT,&nbsp;</p>
<p>&nbsp; &nbsp; state_id INT NOT NULL,</p>
<p>&nbsp; &nbsp; name VARCHAR(256) NOT NULL,</p>
<p>&nbsp; &nbsp; PRIMARY KEY (id),</p>
<p>&nbsp; &nbsp; FOREIGN KEY(state_id) REFERENCES states(id)</p>
<p>);</p>
<p>INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);</p>
<p>INSERT INTO ****** (state_id, name) ****** (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);</p>
<p>INSERT INTO cities (state_id, name) VALUES (4, &quot;*** York&quot;);</p>
<p>INSERT INTO cities (state_id, name) ****** (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);</p>
<p><br></p>
<p>guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.*** | ***** -uroot -p</p>
<p>Enter password:&nbsp;</p>
<p>guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa</p>
<p>California: (1) San Francisco</p>
<p>California: (2) San Jose</p>
<p>California: (3) *** Angeles</p>
<p>California: (4) Fremont</p>
<p>California: (5) Livermore</p>
<p>Arizona: (6) Page</p>
<p>Arizona: (7) Phoenix</p>
<p>Texas: (8) Dallas</p>
<p>Texas: (9) Houston</p>
<p>Texas: (10) Austin</p>
<p>New York: (11) New York</p>
<p>Nevada: (12) Las Vegas</p>
<p>Nevada: (13) Reno</p>
<p>Nevada: (14) Henderson</p>
<p>Nevada: (15) ****** City</p>
<p>guillaume@ubuntu:~/0x0F$&nbsp;</p>
<p>** test cases needed</p>
<p><br></p>
<p>Repo:</p>
<p><br></p>
<p>****** repository: alx-higher_level_programming</p>
<p>Directory: 0x0F-python-object_relational_mapping</p>
<p>File: model_city.py, 14-model_city_fetch_by_state.py</p>
