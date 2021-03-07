# instaloader_chrome_cookie.py

Works only on Linux and Darwin.

If not using Chromium, specify cookie file using the -c option.
For example for Brave Browser do this:
python instaloader_chrome_cookie.py -c ~/.config/BraveSoftware/Brave-Browser/Default/Cookies

Optionally specify the instaloader session file using the -f option.

Usage:
	git clone https://github.com/nzec/instaloader_chrome_cookie.git
	pip install -r requirements.txt
	python instagram_chrome_cookie.py [-h] [-c COOKIEFILE] [-f SESSIONFILE]

Usage (with venv):
	git clone https://github.com/nzec/instaloader_chrome_cookie.git
	python -m venv venv
	venv/bin/pip install -r requirements.txt
	venv/bin/python instagram_chrome_cookie.py [-h] [-c COOKIEFILE] [-f SESSIONFILE]

