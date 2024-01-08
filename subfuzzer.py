from colorama import Fore,Style
import os
import argparse
import requests
import time

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="Specify the domain you want to enumerate.")
parser.add_argument("-w", "--wordlist", required=True, help="Provide the path to the wordlist file you would like to use.")
parser.add_argument("-m", "--mode", required=False, help="Specify if you want to search with HTTP or HTTPS, HTTPS is used if not specified.")
parser.add_argument("-s", "--speed", required=False, help="Specify the amount of time between successful requests (in seconds). Default is 1 second.")
parser.add_argument("-t", "--timeout", required=False, help="Set the maximum time (in seconds) to wait for a successful request. Default is 5 seconds.")
parser.add_argument("-o", "--output", required=False, help="Use this option if you want to save the results, provide the filename for the output file.")
args = parser.parse_args()

# Define progress bar and save to file function
def create_progress_bar(current, total, width=50):
    progress = int(width * current / total)
    bar = f"[{Fore.GREEN + '=' * progress + Style.RESET_ALL}{' ' * (width - progress)}]{progress*2}%  word {current} / {total}"
    return bar
def save_to_file():
    good_urls_set = set(good_urls)
    if args.mode:
        for id, urls in enumerate(good_urls_set):
            save = urls.removeprefix(args.mode+"://")
            with open(args.output, "a") as file:
                file.write(save)
                if id < len(good_urls_set) - 1:
                    file.write("\n")
                file.close()
    else:
        for id, urls in enumerate(good_urls_set):
            save = urls.removeprefix("https://")
            with open(args.output, "a") as file:
                file.write(save)
                if id < len(good_urls_set) - 1:
                    file.write("\n")
                file.close()

wordlist = []
good_urls = []
failed_attempts = 0

# Check's on the arguments
if args.mode:
    if args.mode.lower() == "http" or args.mode.lower() == "https":
        pass
    else:
        print(Fore.RED + "Arguments for (-m) must be either http or https.")
        quit()

if args.speed:
        try:
            speed = int(args.speed)
            if type(speed) == int:
                pass
        except:
            print(Fore.RED + "Argument for (-s) must be a whole number.")
            quit()

if args.timeout:
        try:
            reqtimeout = int(args.timeout)
            if type(speed) == int:
                pass
        except:
            print(Fore.RED + "Argument for (-t) must be a whole number.")
            quit()

if os.path.isfile(args.wordlist):
    if args.output:
        if os.path.isfile(args.output):
            print(Fore.RED + f"The file '{Fore.WHITE + args.output + Style.RESET_ALL + Fore.RED}' allready exists!" + Style.RESET_ALL)
            quit()
        else:
            with open(args.output, "x") as file:
                file.close()

    with open(args.wordlist, "r") as file:
        lines = file.readlines()
        total_words = len(lines)

        for i, line in enumerate(lines, start=1):
            clean_line = line.strip("\n")
            wordlist.append(clean_line)

            try:
                if args.mode:
                    if args.mode.lower() == "http" or args.mode.lower() == "https":
                        url = f"{args.mode}://{clean_line}.{args.domain}"
                else:
                    url = f"https://{clean_line}.{args.domain}"
                if args.timeout:
                    request = requests.get(url, timeout=reqtimeout)
                else:
                    request = requests.get(url, timeout=5)
                if request.status_code == 200:
                    good_urls.append(url)
                    if args.speed:
                        time.sleep(speed)
                    else:
                        time.sleep(1)
            except requests.exceptions.Timeout:
                failed_attempts += 1
            except requests.exceptions.RequestException:
                failed_attempts += 1
            except KeyboardInterrupt:
                if len(good_urls) > 1:
                    print(Fore.CYAN + f"Fuzzing finished, found {len(good_urls)} subdomains for {args.domain}!" + Style.RESET_ALL)
                    if args.output:
                        save_to_file()
                    quit()
                else:
                    print(Fore.RED + f"Fuzzing finished, found no subdomains for {args.domain}, try using another wordlist!" + Style.RESET_ALL)
                    quit()

            # Print the results with the progress of the scan
            os.system("clear")
            print(Fore.RED + """ _____         _     ______                           
/  ___|       | |    |  ___|                          
\ `--.  _   _ | |__  | |_  _   _  ____ ____ ___  _ __ 
 `--. \| | | || '_ \ |  _|| | | ||_  /|_  // _ \| '__|
/\__/ /| |_| || |_) || |  | |_| | / /  / /|  __/| |   
\____/  \__,_||_.__/ \_|   \__,_|/___|/___|\___||_| 
 ------------------------------------ By Ludde ----                     
                                                 """ + Style.RESET_ALL)
            print("-"*95)
            for gurl in good_urls:
                if args.mode:
                    if args.mode.lower() == "http" or args.mode.lower() == "https":
                        print(f"{Fore.GREEN + 'FOUND:' + Style.RESET_ALL} {gurl.removeprefix(args.mode+'://')}")
                else:
                    print(f"{Fore.GREEN + 'FOUND:' + Style.RESET_ALL} {gurl.removeprefix('https://')}")
            print("-"*95)
            print(Fore.YELLOW + f"Trying: {url.lower()}" + Style.RESET_ALL)
            progress_bar = create_progress_bar(i, total_words)
            print("\nProgress:", progress_bar, end='', flush=True)
            print("\n\n")
            if args.output:
                print(Fore.BLUE + f"Press {Fore.MAGENTA + 'CTRL+C ' + Fore.BLUE + 'or' + Fore.MAGENTA + ' CTRL+ALT+C' + Fore.BLUE} to stop the fuzzing and save the results to the file '{Fore.WHITE + args.output + Fore.BLUE}'." + Style.RESET_ALL)
                print("\n")
            else:
                print(Fore.BLUE + f"Press {Fore.MAGENTA + 'CTRL+C ' + Fore.BLUE + 'or' + Fore.MAGENTA + ' CTRL+ALT+C' + Fore.BLUE} to stop the fuzzing." + Style.RESET_ALL)
                print("\n")
    if len(good_urls) >= 1:
        print(Fore.CYAN + f"Fuzzing finished, found {len(good_urls)} subdomains for {args.domain}!" + Style.RESET_ALL)
        if args.output:
            save_to_file()
    else:
        print(Fore.RED + f"Fuzzing finished, found no subdomains for {args.domain}, try using another wordlist!" + Style.RESET_ALL)
else:
    print(Fore.RED + f"The file '{Fore.WHITE + args.wordlist + Style.RESET_ALL + Fore.RED}' does not exist!" + Style.RESET_ALL)
