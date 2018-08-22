# How to use

    python3 crawl.py [API_URL] [WORDLIST] [?OPTIONS]
**API_URL** is the address to the target API. Attention, it's necessary to use `http://`or `https://`.

RIGHT

    python3 crawl.py http://mypourtarget.com

WRONG

    python3 crawl.py mypourtarget.com

 
 **WORDLIST** is the list of words (dictionary as you prefer) needed to execute the brute force. On the project root folder there some wordlists for use. As parameter is necessary pass only the path to the wordlist. Example:

    python3 crawl.py http://mypourtarget.com mywordlist.txt

**OPTIONS** as the name are optional parameters like:

 - **-t [n_threads]** *for choose the number of simultaneous requests to the server (default 50)*
