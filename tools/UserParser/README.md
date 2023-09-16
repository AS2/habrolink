# User parser

Written by @Sairsey
This module can provide you with ``user.txt``

## Usage
0) Our project uses Python >= 3.6, so if it not installed - install it first
1) install via pip our requirements
	``pip install -r requirements.txt``
2) Run ``start_parse.bat`` 
3) Wait around 2 days, untill two out of four windows are closed.
4) Run ``collect.bat`` to create ``user.txt`` with all users.

## Troubleshooting

In case your was banned during 2 days, or something goes wrong - please remember prefixes in each window. After that you can edit ``start_parse.bat``  so it will skip prefixes you already know and continue from new prefixes.

## Small History section

### Problem

As you know, we are trying to parse this service for our university project. If you look closely at address bar in your browser (while you reading new post) you will see that:
1)  **Posts** are identified by **number**.
2)  **Users** are identified by **login**.

Try every possible number from number of posts sound not so hard, however try every login is impossible. This lead us to problem, which this sript is trying to solve - aquire all user logins. 

### Attempts

Firstly I tried to find any page, which have all users, however best I could get is top 100, which is too small it we compare it to 1.5 million. Also, then I tried to check loaded resources via Chrome debugger I found that developer of this resource are giving *.html file already filled with data! I mean they put all info they want to  show in html on server, so client would not know API!!!!

It was horrible, but I did what everyone will do in situations - looked for some Habr posts))) After some research, I found that near 2020 people used some API to retrieve pages, but this API no longer work. API stated in that posts contained substring "v1", so I tried change it to "v2" and everything worked! I found a link to API, but no documentation. After some guessing I found some interesting commands, but they are not related to **users**, only to **posts**. 

My final discovery was interesting fact. Then you open some page, it does not call any API on client, ***HOWEVER*** if you go with opened **page** to another **page** browser **WILL** call API. With this, i found all API commands we might need.

### Solution

So, how we can list all users, if API does not have needed command? Lets use "search" command! Then algorithm will look like this:

1) Decide length of strings, we will try to search (lets it will be N)
2) Generate all possible strings (from set of lowercase characters and numbers)
3) For each string - send it to Search API, and retrieve list of users (limited to 50 pages of search, 20 users per page)
4) collect all users to Set/map
5) after collecting all users (with search by N) save it to file

Then we can run script with different N values and combine them to one base. This method gives us al least 91.5% out of all users.)))
