<nav><a href="https://intranet.alxswe.com/">
        <div><br></div>
    </a></nav>
<main>
    <div><br></div>
    <article>
        <h1>0x15. JavaScript - Web jQuery</h1>
        <div>
            <div>Front-endJavaScript</div>
        </div>
        <div>
            <ul>
                <li>&nbsp;By: Barnabas Moses Yabilsu&nbsp;</li>
            </ul>
        </div>
        <div>
            <div>
                <h3>Concepts</h3>
            </div>
            <div>
                <p><em>For this project, we expect you to look at these concepts:</em></p>
                <ul>
                    <li><a href="https://intranet.alxswe.com/concepts/3">JavaScript in the browser</a></li>
                    <li><a href="https://intranet.alxswe.com/concepts/35">Dealing with data statically versus dynamically</a></li>
                </ul>
            </div>
        </div>
        <div>
            <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg" alt=""></p>
            <h2>Resources</h2>
            <p><strong>Read or watch</strong>:</p>
            <ul>
                <li><a href="https://intranet.alxswe.com/rltoken/NJ5XM_fzjlBKERHTkdF-uA" title="What is JavaScript?" target="_blank">What is JavaScript?</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/wsnVUxEcAzzlCx6ES1qc7g" title="Selector" target="_blank">Selector</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/rwtc96sn2_LHToBAd0MIhQ" title="Get and set content" target="_blank">Get and set content</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/IcM5kKVzssU0ibdUo-2gKQ" title="Manipulate CSS classes" target="_blank">Manipulate CSS classes</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/ve8UKsZLVw2t27PtWscZfQ" title="Manipulate DOM elements" target="_blank">Manipulate DOM elements</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/vKc7XmiHG7HIh3N0Kl_VQw" title="API" target="_blank">API</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/QiUwuS_9TXE49D5IVL-ocg" title="Introduction" target="_blank">Introduction</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/Mbe7uoy0iMAfTVs2Tn4Pzg" title="GET & POST request" target="_blank">GET &amp; POST request</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/gMwyXisSLu-kZicmGA0-LQ" title="JQuery Ajax Tutorial #1 - Using AJAX & API's" target="_blank">JQuery Ajax Tutorial #1 - Using AJAX &amp; API&rsquo;s</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/4eYyJr72PO-cohImk93M3w" title="What went wrong? Troubleshooting JavaScript" target="_blank">What went wrong? Troubleshooting JavaScript</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/HnjBq6jf84S9S-C15Qi0vw" title="JQuery" target="_blank">JQuery</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/jvibhq-8VEdQHNUWKTCI7w" title="JQuery API" target="_blank">JQuery API</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/rBZyrXxuRuISDfPBzO9Y7Q" title="JQuery Ajax" target="_blank">JQuery Ajax</a></li>
            </ul>
            <h2>Learning Objectives</h2>
            <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/uOCIGjC7u4MtYfDwCwODTA" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
            <h3>General</h3>
            <ul>
                <li>Why JQuery make front-end programming so easy (don&rsquo;t forget to tweet today, with the hashtag #ilovejquery :))</li>
                <li>How to select HTML elements in JavaScript</li>
                <li>How to select HTML elements with JQuery</li>
                <li>What are differences between&nbsp;<code>ID</code>,&nbsp;<code>class</code> and&nbsp;<code>tag name</code> selectors</li>
                <li>How to modify an HTML element style</li>
                <li>How to get and update an HTML element content</li>
                <li>How to modify the DOM</li>
                <li>How to make a&nbsp;<code>GET</code> request with JQuery Ajax</li>
                <li>How to make a&nbsp;<code>POST</code> request with JQuery Ajax</li>
                <li>How to listen/bind to DOM events</li>
            </ul>
            <h2>- How to listen/bind to user events</h2>
            <h2>Requirements</h2>
            <h3>General</h3>
            <ul>
                <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
                <li>All your files will be interpreted on Chrome (version 57.0)</li>
                <li>All your files should end with a new line</li>
                <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                <li>Your code should be&nbsp;<code>semistandard</code> compliant with the flag&nbsp;<code>--global $</code>:&nbsp;<code>semistandard *.js --global $</code></li>
                <li>You must use JQuery version 3.x</li>
                <li>You are not allowed to use&nbsp;<code>var</code></li>
                <li>HTML should not reload for each action: DOM manipulation, update values, fetch data&hellip;</li>
            </ul>
            <h2>More Info</h2>
            <h3>Import JQuery</h3>
            <pre><code>&lt;head&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
&lt;/head&gt;
</code></pre>
            <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg" alt=""></p>
            <h3>Manual QA Review</h3>
            <p><strong>It is your responsibility to request a review for this project from a peer before the project&rsquo;s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong></p>
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
                <h3>0. No JQuery</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that updates the text color of the&nbsp;<code>&lt;header&gt;</code> element to red (<code>#FF0000</code>):</p>
                <ul>
                    <li>You must use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You can&rsquo;t use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 0-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;0-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>0-script.js</code></li>
                    </ul>
                </div>
            </div>
            <p><br></p>
            <div>1. With JQuery</div>
        </div>
        <div>
            <div>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that updates the text color of the&nbsp;<code>&lt;header&gt;</code> element to red (<code>#FF0000</code>):</p>
                <ul>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 1-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;1-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>1-script.js</code></li>
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
                <h3>2. Click and turn red</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that updates the text color of the&nbsp;<code>&lt;header&gt;</code> element to red (<code>#FF0000</code>) when the user clicks on the tag&nbsp;<code>DIV#red_header</code>:</p>
                <ul>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 2-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;2-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>2-script.js</code></li>
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
                <h3>3. Add `.red` class</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that adds the class&nbsp;<code>red</code> to the&nbsp;<code>&lt;header&gt;</code> element when the user clicks on the tag&nbsp;<code>DIV#red_header</code></p>
                <ul>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 3-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;3-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>3-script.js</code></li>
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
                <h3>4. Toggle classes</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that toggles the class of the&nbsp;<code>&lt;header&gt;</code> element when the user clicks on the tag&nbsp;<code>DIV#toggle_header</code>:</p>
                <ul>
                    <li>The&nbsp;<code>&lt;header&gt;</code> element must always have one class:&nbsp;<code>red</code> or&nbsp;<code>green</code>, never both in the same time and never empty.</li>
                    <li>If the current class is&nbsp;<code>red</code>, when the user click on&nbsp;<code>DIV#toggle_header</code>, the class must be updated to&nbsp;<code>green</code> ; and the reverse.</li>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 4-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class=&quot;green&quot;&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;toggle_header&quot;&gt;Toggle header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;4-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>4-script.js</code></li>
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
                <h3>5. List of elements</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that adds a&nbsp;<code>&lt;li&gt;</code> element to a list when the user clicks on the tag&nbsp;<code>DIV#add_item</code>:</p>
                <ul>
                    <li>The new element must be:&nbsp;<code>&lt;li&gt;Item&lt;/li&gt;</code></li>
                    <li>The new element must be added to&nbsp;<code>UL.my_list</code></li>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 5-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;add_item&quot;&gt;Add item&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class=&quot;my_list&quot;&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;5-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>5-script.js</code></li>
                    </ul>
                </div>
            </div>
            <div><br></div>
        </div>
        <div>
            <div>
                <h3>6. Change the text</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that updates the text of the&nbsp;<code>&lt;header&gt;</code> element to&nbsp;<code>New Header!!!</code> when the user clicks on&nbsp;<code>DIV#update_header</code></p>
                <ul>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 6-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;update_header&quot;&gt;Update the header&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;6-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>6-script.js</code></li>
                    </ul>
                </div>
            </div>
            <div><br></div>
        </div>
        <div>
            <div>
                <h3>7. Star wars character</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that fetches the character&nbsp;<code>name</code> from this URL:&nbsp;<code>https://swapi-api.alx-tools.com/api/people/5/?format=json</code></p>
                <ul>
                    <li>The name must be displayed in the HTML tag&nbsp;<code>DIV#character</code></li>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 7-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars character
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;character&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;7-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>7-script.js</code></li>
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
                <h3>8. Star Wars movies</h3>
                <div>mandatory</div>
            </div>
            <div>
                <p>Write a JavaScript script that fetches and lists the&nbsp;<code>title</code> for all movies by using this URL:&nbsp;<code>https://swapi-api.alx-tools.com/api/films/?format=json</code></p>
                <ul>
                    <li>All movie titles must be list in the HTML tag&nbsp;<code>UL#list_movies</code></li>
                    <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                    <li>You must use the JQuery API</li>
                </ul>
                <p>Please test with this HTML file in your browser:</p>
                <pre><code>guillaume@ubuntu:~/0x15$ cat 8-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars movies
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;ul id=&quot;list_movies&quot;&gt;
    &lt;/ul&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;8-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
            </div>
            <div>
                <div>
                    <p><strong>Repo:</strong></p>
                    <ul>
                        <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                        <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                        <li>File:&nbsp;<code>8-script.js</code></li>
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
                <div>
                    <h3>9. Say Hello!</h3>
                    <div>mandatory</div>
                </div>
                <div>
                    <p>Write a JavaScript script that fetches from&nbsp;<code>https://fourtonfish.com/hellosalut/?lang=fr</code> and displays the value of&nbsp;<code>hello</code> from that fetch in the HTML tag&nbsp;<code>DIV#hello</code>.</p>
                    <ul>
                        <li>The translation of &ldquo;hello&rdquo; must be displayed in the HTML tag&nbsp;<code>DIV#hello</code></li>
                        <li>You can&rsquo;t use&nbsp;<code>document.querySelector</code> to select the HTML tag</li>
                        <li>You must use the JQuery API</li>
                        <li>Your script must work when it is imported from the&nbsp;<code>&lt;head&gt;</code> tag</li>
                    </ul>
                    <p>Please test with this HTML file in your browser:</p>
                    <pre><code>guillaume@ubuntu:~/0x15$ cat 9-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;9-script.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello!
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;hello&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
                </div>
                <div>
                    <div>
                        <p><strong>Repo:</strong></p>
                        <ul>
                            <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                            <li>Directory:&nbsp;<code>0x15-javascript-web_jquery</code></li>
                            <li>File:&nbsp;<code>9-script.js</code></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div>
                        <div>Copyright &copy; 2023 DUKURMA, All rights reserved.</div>
                    </div>
                </div>
            </div>
        </div>
    </article>
</main>
<main><br></main>
