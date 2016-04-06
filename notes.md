ssh -X pi@169.254.0.2
sudo shutdown -h now

---

npm install python-shell
npm install cron

---

`apt-get install screen`
to use it simply type screen. You will be teleported into the new screen :) Run the program that needs to run forever.

While in a screen ...

Detach from screen `ctrl + a + d`
Kill screen `ctrl + a + k`
Outside the screen ...

Show all running screens and their names `screen -ls`
Reconnect to a screen `screen -r <session id/name>`
Start a screen with human name `screen -S <session name>`
The contents of the screen are buffered so when you reconnect see the output and you can use `ctrl + pageup` but sometimes it does not work and you need enable some other stuff. It is good to write a log file whether you are running it as thread & or screen.

---

`USER_ID='abc' USER_KEY='def' node nodetest`