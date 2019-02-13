# lazyrev
Lazyrev is a simple python3 script which outputs a reverse shell one-liner payload
with user's IP and port. 


# Usage
`git clone https://github.com/ChoiSG/lazyrev.git`
`python3 lazyrev.py -t|--type python|bash|perl|php|ruby <ip> <port>`

In order to automatically open a netcat listener with your ip/port, simply 
add a `-l` or a `--listener` flag at the end. 
`python3 lazyrev.py -t|--type python|bash|perl|php|ruby <ip> <port> -l|--listener`

# TODO 
* Freeze the code with pyinstaller and ship it as a single binary 
* Support more revershell payloads
