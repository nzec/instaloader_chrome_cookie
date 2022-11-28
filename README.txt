# instaloader_chrome_cookie.py

Works only on Linux and Darwin.

If not using Chromium, specify cookie file using the -c option.

If your browser is using GNOME Keyring or KWallet you will need to specify the password using the -p flag.
See this for more info: https://chromium.googlesource.com/chromium/src/+/master/docs/linux/password_storage.md

For example for Brave Browser do this:
./instaloader_chrome_cookie.py -c ~/.config/BraveSoftware/Brave-Browser/Default/Cookies -p [password]

Optionally specify the instaloader session file using the -f option.

Usage:
	git clone https://github.com/nzec/instaloader_chrome_cookie.git && cd instaloader_chrome_cookie
	pip install -r requirements.txt
	./instagram_chrome_cookie.py [-h] [-c COOKIEFILE] [-f SESSIONFILE] [-p PASSWORD]
