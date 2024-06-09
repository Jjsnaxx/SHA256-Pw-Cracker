# SHA256-Pw-Cracker

<h2>Overview:<h2>

Aim of this project is to learn how to create a sha256 hash cracking script as well as get a better understanding on how to use the Pwntools and sys modules.

<h2>Specifics:<h2>

	- Virtual Machine (Virtual Box) with Kali Linux Distribution
	- Python3.0

<h2> Text Editor:<h2>
 
	- Sublime Text

<h2>Python Modules used:<h2>

	- PWNtools
	- sys

<h2>What I learnt:<h2>

echo -ne -insert text- | sha256sum
Can be used to get the sha256 hash of any text.

Log.progress
From the pwntools library. Used as a progress logger to generate logs associated with a ongoing job. Once success() or failure() is called it will no longer update.

P.failure()
Logs that the running job failed. No further status updates are allowed.
If the Logger is animated, the animation is stopped.


P.success()
Logs that the running job succeeded. No further status updates are allowed.
If the Logger is animated, the animation is stopped.


P.status()
Logs a status update for the running job.
If the progress logger is animated the status line will be updated in place.
Status updates are throttled at one update per 100ms.

encoding = 'latin-1'
I realized the rockyou.txt file contained Non-ASCII characters, so I was running to encoding errors. Changing the encoding to latin-1 solved that problem

sha256sumhex(password)
Learnt that I needed to use sha256sumhex instead of sha256sum as it spat out the hash as a byte array.![image](https://github.com/Jjsnaxx/SHA256-Pw-Cracker/assets/140260457/9f638929-1919-434c-b84b-5f713eb5c88a)

 
<h2>Learning references:<h2>

https://docs.pwntools.com/en/stable/log.html (log.progress) (p.status) (p.failure)
https://www.w3schools.com/python/python_file_handling.asp
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt![image](https://github.com/Jjsnaxx/SHA256-Pw-Cracker/assets/140260457/45a801da-8e9c-4c64-9d97-97460d7e9cf2)

