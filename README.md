# SHA256-Pw-Cracker

## Overview

The aim of this project is to learn how to create a SHA256 hash cracking script and gain a better understanding of how to use the Pwntools and sys modules.

## Specifics:

- Virtual Machine (VirtualBox) with Kali Linux Distribution
- Python 3.0

## Text Editor:

- Sublime Text

## Python Modules Used:

- Pwntools
- sys

## What I Learned:

- `echo -ne -insert text- | sha256sum`: Can be used to get the SHA256 hash of any text.
- `log.progress`: From the pwntools library. Used as a progress logger to generate logs associated with an ongoing job. Once `success()` or `failure()` is called, it will no longer update.
- `p.failure()`: Logs that the running job failed. No further status updates are allowed. If the Logger is animated, the animation is stopped.
- `p.success()`: Logs that the running job succeeded. No further status updates are allowed. If the Logger is animated, the animation is stopped.
- `p.status()`: Logs a status update for the running job. If the progress logger is animated, the status line will be updated in place. Status updates are throttled at one update per 100ms.
- `encoding = 'latin-1'`: I realized the rockyou.txt file contained non-ASCII characters, causing encoding errors. Changing the encoding to latin-1 solved that problem.
- `sha256sumhex(password)`: Learned that I needed to use `sha256sumhex` instead of `sha256sum` as it outputs the hash as a byte array.

## References i used:

- [Pwntools log documentation](https://docs.pwntools.com/en/stable/log.html) (log.progress, p.status, p.failure)
- [Python file handling - W3Schools](https://www.w3schools.com/python/python_file_handling.asp)
- [Rockyou.txt wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
