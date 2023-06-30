<nav>
    <div>
        <div>0x10. Python - Network #0</div>
    </div>
    <main>
        <article>
            <div>
                <div>Bash Python Scripting Back-endAPI</div>
            </div>
            <div>
                <ul>
                    <li>&nbsp;By: Barnabas Moses Yabilsu&nbsp;</li>
                    <li>&nbsp;Weight:&nbsp;1</li>
                    <li>&nbsp;Project start date <span title="">Jun 28, 2023 8:00 AM</span>,&nbsp;</li>
                    <li>End date <span title="">Jul 3, 2023 6:00 AM</span></li>
                </ul>
            </div>
            <div>
                <h2>Resources</h2>
                <p><strong>Read or watch</strong>:</p>
                <ul>
                    <li><a href="https://intranet.alxswe.com/rltoken/rAon_EpQ6PGl8N0plySn4A" title="HTTP (HyperText Transfer Protocol)" target="_blank">HTTP (HyperText Transfer Protocol)</a> (<em>except: &ldquo;TRACE&rdquo; Request Method, &ldquo;CONNECT&rdquo; Request Method, Language Negotiation and &ldquo;Options MultiView&rdquo; and Character Set Negotiation</em>)</li>
                    <li><a href="https://intranet.alxswe.com/rltoken/MhVCl_0oviQldWPn5oX-NQ" title="HTTP Cookies" target="_blank">HTTP Cookies</a></li>
                </ul>
                <h2>Learning Objectives</h2>
                <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/6HRdeOrrKTW2ih43ObB8tQ" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
                <h3>General</h3>
                <ul>
                    <li>What a URL is</li>
                    <li>What HTTP is</li>
                    <li>How to read a URL</li>
                    <li>The scheme for a HTTP URL</li>
                    <li>What a domain name is</li>
                    <li>What a sub-domain is</li>
                    <li>How to define a port number in a URL</li>
                    <li>What a query string is</li>
                    <li>What an HTTP request is</li>
                    <li>What an HTTP response is</li>
                    <li>What HTTP headers are</li>
                    <li>What the HTTP message body is</li>
                    <li>What an HTTP request method is</li>
                    <li>What an HTTP response status code is</li>
                    <li>What an HTTP Cookie is</li>
                    <li>How to make a request with cURL</li>
                    <li>What happens when you type google.com in your browser (Application level)</li>
                </ul>
                <h2>Requirements</h2>
                <h3>General</h3>
                <ul>
                    <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
                    <li>- A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                    <li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
                    <li>All your Bash scripts should be exactly 3 lines long (<code>wc -l file</code> should print 3)</li>
                    <li>All your files should end with a new line</li>
                    <li>All your files must be executable</li>
                    <li>The first line of all your bash files should be exactly&nbsp;<code>#!/bin/bash</code></li>
                    <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
                    <li>All&nbsp;<code>curl</code> commands must have the option&nbsp;<code>-s</code> (silent mode)</li>
                    <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using&nbsp;<code>python3</code> (version 3.8.5)</li>
                    <li>The first line of all your Python files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
                    <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
                    <li>All your modules should be documented:&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code></li>
                    <li>All your classes should be documented:&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code></li>
                    <li>All your functions (inside and outside a class) should be documented:&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code></li>
                    <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
                </ul>
            </div>
            <div>
                <div>
                    <h3>Quiz questions</h3>
                </div>
                <div>
                    <div><strong>Great!</strong> You&apos;ve completed the quiz successfully! Keep going!&nbsp;(Show quiz)</div>
                </div>
            </div>
            <h2>Tasks</h2>
            <div>
                <div>
                    <h3>0. cURL body size</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response</p>
                    <ul>
                        <li>The size must be displayed in bytes</li>
                        <li>You have to use&nbsp;<code>curl</code></li>
                    </ul>
                    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
                    <pre><code>guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>0-body_size.sh</code></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <div>
                    <h3>1. cURL to the end</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a Bash script that takes in a URL, sends a&nbsp;<code>GET</code> request to the URL, and displays the body of the response</p>
                    <ul>
                        <li>Display only body of a&nbsp;<code>200</code> status code response</li>
                        <li>You have to use&nbsp;<code>curl</code></li>
                    </ul>
                    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
                    <pre><code>guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo &quot;&quot;
Route 2
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>1-body.sh</code></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <div>
                    <h3>2. cURL Method</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a Bash script that sends a&nbsp;<code>DELETE</code> request to the URL passed as the first argument and displays the body of the response</p>
                    <ul>
                        <li>You have to use&nbsp;<code>curl</code></li>
                    </ul>
                    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
                    <pre><code>guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo &quot;&quot;
I&apos;m a DELETE request
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>2-delete.sh</code></li>
                        </ul>
                    </div>
                </div>
                <div><br></div>
            </div>
            <div>
                <div>
                    <h3>3. cURL only methods</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.</p>
                    <ul>
                        <li>You have to use&nbsp;<code>curl</code></li>
                    </ul>
                    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
                    <pre><code>guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>3-methods.sh</code></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div><br></div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <div>
                    <h3>4. cURL headers</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a Bash script that takes in a URL as an argument, sends a&nbsp;<code>GET</code> request to the URL, and displays the body of the response</p>
                    <ul>
                        <li>A header variable&nbsp;<code>X-School-User-Id</code> must be sent with the value&nbsp;<code>98</code></li>
                        <li>You have to use&nbsp;<code>curl</code></li>
                    </ul>
                    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
                    <pre><code>guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo &quot;&quot;
Hello School!
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>4-header.sh</code></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div>
                <div>
                    <h3>5. cURL POST parameters</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a Bash script that takes in a URL, sends a&nbsp;<code>POST</code> request to the passed URL, and displays the body of the response</p>
                    <ul>
                        <li>A variable&nbsp;<code>email</code> must be sent with the value&nbsp;<code>test@gmail.com</code></li>
                        <li>A variable&nbsp;<code>subject</code> must be sent with the value&nbsp;<code>I will always be here for PLD</code></li>
                        <li>You have to use&nbsp;<code>curl</code></li>
                    </ul>
                    <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
                    <pre><code>guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo &quot;&quot;
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>5-post_params.sh</code></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div><br></div>
                </div>
            </div>
            <div>
                <div>
                    <h3>6. Find a peak</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p><strong>Technical interview preparation</strong>:</p>
                    <ul>
                        <li>You are not allowed to google anything</li>
                        <li>Whiteboard first</li>
                    </ul>
                    <p>Write a function that finds&nbsp;<strong>a peak</strong> in a list of unsorted integers.</p>
                    <ul>
                        <li>Prototype:&nbsp;<code>def find_peak(list_of_integers):</code></li>
                        <li>You are not allowed to import any module</li>
                        <li>Your algorithm must have the lowest complexity (<em>hint: you don&rsquo;t need to go through all numbers to find a peak</em>)</li>
                        <li><code>6-peak.py</code> must contain the function</li>
                        <li><code>6-peak.txt</code> must contain the complexity of your algorithm:&nbsp;<code>O(log(n))</code>,&nbsp;<code>O(n)</code>,&nbsp;<code>O(nlog(n))</code> or&nbsp;<code>O(n2)</code></li>
                        <li><strong>Note</strong>: there may be more than one peak in the list</li>
                    </ul>
                    <pre><code>guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
&quot;&quot;&quot; Test function find_peak &quot;&quot;&quot;
find_peak = __import__(&apos;6-peak&apos;).find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x10-python-network_0</code></li>
                            <li>File:&nbsp;<code>6-peak.py, 6-peak.txt</code></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div><br></div>
                    <div><br></div>
                </div>
            </div>
        </article>
        <div>Copyright &copy; 2023 DUKURMA, All rights reserved.</div>
    </main>
</nav>
<main><br></main>
