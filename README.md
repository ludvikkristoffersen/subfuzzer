![SubFuzzer](https://drive.google.com/drive/u/0/folders/1A-4BkEwZbqbuI91tGhCGl4uMcDrjsF4i)
```
 _____         _     ______                           
/  ___|       | |    |  ___|                          
\ `--.  _   _ | |__  | |_  _   _  ____ ____ ___  _ __ 
 `--. \| | | || '_ \ |  _|| | | ||_  /|_  // _ \| '__|
/\__/ /| |_| || |_) || |  | |_| | / /  / /|  __/| |   
\____/  \__,_||_.__/ \_|   \__,_|/___|/___|\___||_| 
 ------------------------------------ By Ludde ----
```
A subdomain fuzzer that uses a user-specified wordlist to find subdomains for a domain.

## Installation
```
git clone https://github.com/luddekn/subfuzzer
```
```
pip3 install -r requirements.txt
```
## Wordlist recommendations
- **Dirbuster** wordlists that comes with Kali Linux, found here: **/usr/share/wordlists/dirb/dirbuster**
- **n0kovo's** wordlists: [Can be downloaded from here](https://github.com/n0kovo/n0kovo_subdomains)

## Usage
You can specify how fast the fuzzing should go by using the **-s** and **-t** options, although be careful by going too fast so you don't get blocked.
```
usage: subfuzzer.py [-h] -d DOMAIN -w WORDLIST [-m MODE] [-s SPEED] [-t TIMEOUT] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Specify the domain you want to enumerate.
  -w WORDLIST, --wordlist WORDLIST
                        Provide the path to the wordlist file you would like to use.
  -m MODE, --mode MODE  Specify if you want to search with HTTP or HTTPS, HTTPS is used if not specified.
  -s SPEED, --speed SPEED
                        Specify the amount of time between successful requests (in seconds). Default is 1 second.
  -t TIMEOUT, --timeout TIMEOUT
                        Set the maximum time (in seconds) to wait for a successful request. Default is 5 seconds.
  -o OUTPUT, --output OUTPUT
                        Use this option if you want to save the results, provide the filename for the output file.
```
Just fuzzing a domain?
```
python3 subfuzzer.py -d example.com -w wordlist.txt
```

