
import platform
import os
os.system('termux-setup-storage')


arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Jm")._login()
elif 'aarch' in arc:
	__import__("dm")._login()
else:
	exit(f' % time termux-info | tail -4
Device manufacturer:
Google
Device model:
Pixel 2 XL
termux-info  1.30s user 0.65s system 50% cpu 3.837 total
tail -4  0.01s user 0.01s system 0% cpu 3.836 total {arc}')












