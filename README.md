# Most Active Cookie
Process a csv file of cookie logs and return the most active cookie on a given date

This repo contains `most_active_cookie.py`, `cookies_log_8.csv`, `cookies_log_200.csv`.
- `most_active_cookie.py` => python program that finds the most active cookies on a specified date(YYYY-MM-DD).
- `cookies_log_8.csv` => csv file that contains 8 cookies & 8 timestamps for testing.
- `cookies_log_200.csv` => csv file that contains 200 cookies & 200 timestamps for testing.


## Process:
Given a csv log of cookie sessions:
>cookie,timestamp
<br>AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
<br>SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
<br>5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
<br>AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
<br>SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
<br>4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
<br>fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
<br>4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00

**Write a command line program in your preferred language to process the log file and return the most active
cookie for specified day.**
- Example Command:
<br> *`$ ./most_active_cookie cookie_log.csv -d 2018-12-09`*
- Output:
<br> *AtY0laUfhglK3lC7*

**If multiple cookies meet that criteria, return all of them on separate lines.**
---

- Example Command:
<br> *`$ ./most_active_cookie cookie_log.csv -d 2018-12-08`*
- Output:
<br> *SAZuXPGUrfbcn5UA*
<br> *4sMM2LxV07bPJzwf*
<br> *fbcn5UAVanZf6UtG*

## Usage:
### Requirements:
- Python 3(preferred)

### Instructions:
- Download the repo
- Open the terminal and navigate to where the repo is located

The program requires two arguments:
- File path: ex. `-f csv_log.csv`
- Date: ex. `-d 2019-09-12`

### Run:
Example Code:
- `python3 most_active_cookie.py -f cookies_log_200.csv -d 2015-10-11`


