![SubFuzzer](https://dl.dropboxusercontent.com/scl/fi/d1imalqooilwhe7qifuow/subfuzzerv2.jpg?rlkey=1qxbt8m8elzw7mt5q25o5b7m7&dl=0)
*A subdomain fuzzer that uses a user-specified wordlist to find subdomains for a domain.*

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
![SubFuzzer](https://dl.dropboxusercontent.com/scl/fi/arzciodtipmdlgp6htvte/subfuzzer-useage.jpg?rlkey=ucqka2moa5487a2z0qxff7drt&dl=0)
You can specify how fast the fuzzing should go by using the **-s** and **-t** options, but be careful, sending loads of requests to a domain might get you blocked from that domain for some time.


