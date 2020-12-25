# remote_keylogger
A simple keylogger programmed in Python, but it can communicate logged keys back to the attacker's computer.
<br>
**I am not encouraging any illegal/malicious activity, and I am not taking any responsbility for your actions. This code is for education purposes only.**

### Required Modules
The only module required so far (that is not part of the default Python stack) is pynput: `pip install pynput` or `pip3 install pynput`

### How To (Windows Only)
1. Before starting/configuring either of the programs, make sure the target machine can communicate to the server by opening the command prompt on the target machine and running `ping YOUR_SERVERS_LOCAL_IP`, where `YOUR_SERVERS_LOCAL_IP` is the local IP of your server.
    1. If you do not know the local IP of your server, run `ipconfig` on the command line. Under `Wireless LAN adapter Wi-Fi:`, find `IPv4 Address`. The series of numbers to the right of it is your local IP.
2. If the ping command works successfully, continue on. If the connection times out, open firewall settings on the server and turn the firewall off for whatever network you are on (public/private).
3. Open both `victim.py` and `attacker.py`, and replace the value of the variable `host` to the server's IP. (ex: `host = '192.168.1.101'`)
4. To use the keylogger, put the `victim.py` files on your target's machine (aka the client), and put `attacker.py` on the computer which will be monitoring the keylogger (aka the server). On the server, create a log filed called `logs.log` in the same directory as the `attacker.py` file.
5. First run the `attacker.py` file on the server, and then run `victim.py` on the target. This order is important, and the program will not work if this order is not followed.
6. You're done! Try typing a few letters on the target machine and see if the `logs.log` file on the server also updates!

### But why?
Creating a keylogger, or any malicious program, on Python is not optimal. Since Python is an interpreted language, your target also must have the Python interpreter installed. If you *really* wanted to make a viable keylogger, you would program it in a language like C++ or Java, as they are compiled languages.
This project was just a fun utilization of the `pynput`, `socket`, and `logging` packages.

### To do
- [ ] Add dumping functionality to only send data to the server to the server every `x` lines/keypresses to avoid spamming/overload