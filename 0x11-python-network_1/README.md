<nav>
    <div>0x11. Python - Network #1</div>
    <p>Python</p>
    <p>Scripting</p>
    <p>Back-end</p>
    <p>API</p>
    <p>&nbsp;By: Barnabas Moses Yabilsu, Student at ALX.&nbsp;</p>
    <div>Project start date Jun 30, 2023 8:00 AM,&nbsp;</div>
    <div>Project End date Jul 2, 2023 6:00 AM</div>
    <p>Resources</p>
    <p>Read or watch:</p>
    <p><br></p>
    <p>HOWTO Fetch Internet Resources Using urllib Package</p>
    <p>Quickstart with Requests package</p>
    <p>Requests package</p>
    <p>Learning Objectives</p>
    <p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>
    <p><br></p>
    <p>General</p>
    <p>How to fetch internet resources with the Python package urllib</p>
    <p>How to decode urllib body response</p>
    <p>How to use the Python package requests #requestsiswaysimplerthanurllib</p>
    <p>How to make HTTP GET request</p>
    <p>How to make HTTP POST/PUT/etc. request</p>
    <p>How to fetch JSON resources</p>
    <p>How to manipulate data from an external service</p>
    <p><br></p>
    <p>Requirements</p>
    <p>General</p>
    <p>Allowed editors: vi, vim, emacs</p>
    <p>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</p>
    <p>All your files should end with a new line</p>
    <p>The first line of all your files should be exactly #!/usr/bin/python3</p>
    <p>A README.md file at the root of the repo, containing a description of the repository</p>
    <p>A README.md file, at the root of the folder of this project, is mandatory</p>
    <p>Your code should use the pycodestyle (version 2.8.*)</p>
    <p>All your files must be executable</p>
    <p>The length of your files will be tested using wc</p>
    <p>All your modules should have a documentation (python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;)</p>
    <p>You must use get to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</p>
    <p>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</p>
    <p>Your code should not be executed when imported (by using if __name__ == &quot;__main__&quot;:)</p>
    <p>Tasks</p>
    <p>0. What&apos;s my status? #0</p>
    <p>mandatory</p>
    <p>Write a Python script that fetches https://alx-intranet.hbtn.io/status</p>
    <p><br></p>
    <p>You must use the package urllib</p>
    <p>You are not allowed to import any packages other than urllib</p>
    <p>The body of the response must be displayed like the following example (tabulation before -)</p>
    <p>You must use a with statement</p>
    <p>guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e</p>
    <p>Body response:$</p>
    <p>&nbsp; &nbsp; - type: &lt;class &apos;bytes&apos;&gt;$</p>
    <p>&nbsp; &nbsp; - content: b&apos;OK&apos;$</p>
    <p>&nbsp; &nbsp; - utf8 content: OK$</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 0-hbtn_status.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>1. Response header value #0</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.</p>
    <p><br></p>
    <p>You must use the packages urllib and sys</p>
    <p>You are not allow to import packages other than urllib and sys</p>
    <p>The value of this variable is different for each request</p>
    <p>You don&rsquo;t need to check arguments passed to the script (number or type)</p>
    <p>You must use a with statement</p>
    <p>guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io</p>
    <p>ade2627e-41dd-4c34-b9d9-a0fa0f47b237</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io</p>
    <p>6593e1f5-1b4b-4c9f-9c0e-72ab525b850f</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 1-hbtn_header.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>2. POST an email #0</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)</p>
    <p><br></p>
    <p>The email must be sent in the email variable</p>
    <p>You must use the packages urllib and sys</p>
    <p>You are not allowed to import packages other than urllib and sys</p>
    <p>You don&rsquo;t need to check arguments passed to the script (number or type)</p>
    <p>You must use the with statement</p>
    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
    <p><br></p>
    <p>guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com</p>
    <p>Your email is: hr@holbertonschool.com</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 2-post_email.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>3. Error code #0</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).</p>
    <p><br></p>
    <p>You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code</p>
    <p>You must use the packages urllib and sys</p>
    <p>You are not allowed to import other packages than urllib and sys</p>
    <p>You don&rsquo;t need to check arguments passed to the script (number or type)</p>
    <p>You must use the with statement</p>
    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
    <p><br></p>
    <p>guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000</p>
    <p>Index</p>
    <p>guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401</p>
    <p>Error code: 401</p>
    <p>guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist</p>
    <p>Error code: 404</p>
    <p>guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500</p>
    <p>Error code: 500</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 3-error_code.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>4. What&apos;s my status? #1</p>
    <p>mandatory</p>
    <p>Write a Python script that fetches https://alx-intranet.hbtn.io/status</p>
    <p><br></p>
    <p>You must use the package requests</p>
    <p>You are not allow to import packages other than requests</p>
    <p>The body of the response must be display like the following example (tabulation before -)</p>
    <p>guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e</p>
    <p>Body response:$</p>
    <p>&nbsp; &nbsp; - type: &lt;class &apos;str&apos;&gt;$</p>
    <p>&nbsp; &nbsp; - content: OK$</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 4-hbtn_status.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>5. Response header value #1</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header</p>
    <p><br></p>
    <p>You must use the packages requests and sys</p>
    <p>You are not allow to import other packages than requests and sys</p>
    <p>The value of this variable is different for each request</p>
    <p>You don&rsquo;t need to check script arguments (number and type)</p>
    <p>guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io</p>
    <p>5e52e160-c822-4669-8b3a-8b3bbca7b090</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io</p>
    <p>eaceaf35-bc0f-4f74-994a-7be0728ec654</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 5-hbtn_header.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>6. POST an email #1</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.</p>
    <p><br></p>
    <p>The email must be sent in the variable email</p>
    <p>You must use the packages requests and sys</p>
    <p>You are not allowed to import packages other than requests and sys</p>
    <p>You don&rsquo;t need to error check arguments passed to the script (number or type)</p>
    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
    <p><br></p>
    <p>guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com</p>
    <p>Your email is: hr@holbertonschool.com</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 6-post_email.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>7. Error code #1</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.</p>
    <p><br></p>
    <p>If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code</p>
    <p>You must use the packages requests and sys</p>
    <p>You are not allowed to import packages other than requests and sys</p>
    <p>You don&rsquo;t need to check arguments passed to the script (number or type)</p>
    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
    <p><br></p>
    <p>guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000</p>
    <p>Index</p>
    <p>guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401</p>
    <p>Error code: 401</p>
    <p>guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist</p>
    <p>Error code: 404</p>
    <p>guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500</p>
    <p>Error code: 500</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 7-error_code.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>8. Search API</p>
    <p>mandatory</p>
    <p>Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.</p>
    <p><br></p>
    <p>The letter must be sent in the variable q</p>
    <p>If no argument is given, set q=&quot;&quot;</p>
    <p>If the response body is properly JSON formatted and not empty, display the id and name like this: [&lt;id&gt;] &lt;name&gt;</p>
    <p>Otherwise:</p>
    <p>Display Not a valid JSON if the JSON is invalid</p>
    <p>Display No result if the JSON is empty</p>
    <p>You must use the package requests and sys</p>
    <p>You are not allowed to import packages other than requests and sys</p>
    <p>Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.</p>
    <p><br></p>
    <p>guillaume@ubuntu:~/0x11$ ./8-json_api.py&nbsp;</p>
    <p>No result</p>
    <p>guillaume@ubuntu:~/0x11$ ./8-json_api.py a</p>
    <p>[8446] amnirqhtfjq</p>
    <p>guillaume@ubuntu:~/0x11$ ./8-json_api.py 2</p>
    <p>No result</p>
    <p>guillaume@ubuntu:~/0x11$ ./8-json_api.py b</p>
    <p>[7094] bmofakakhke</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 8-json_api.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>9. My GitHub!</p>
    <p>mandatory</p>
    <p>Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id</p>
    <p><br></p>
    <p>You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)</p>
    <p>The first argument will be your username</p>
    <p>The second argument will be your password (in your case, a personal access token as password)</p>
    <p>You must use the package requests and sys</p>
    <p>You are not allowed to import packages other than requests and sys</p>
    <p>You don&rsquo;t need to check arguments passed to the script (number or type)</p>
    <p>guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun</p>
    <p>2531536</p>
    <p>guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd</p>
    <p>None</p>
    <p>guillaume@ubuntu:~/0x11$&nbsp;</p>
    <p>Repo:</p>
    <p><br></p>
    <p>GitHub repository: alx-higher_level_programming</p>
    <p>Directory: 0x11-python-network_1</p>
    <p>File: 10-my_github.py</p>
    <p>&nbsp; &nbsp;</p>
    <p>Copyright &copy; 2023 DUKURMA, All rights reserved.</p>
</nav>
