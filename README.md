# Hack-Message
This program sends you a text message using Twilio to warn you that someone is trying to enter an invalid password on your computer.
It works only for Linux. It uses your ip location and integrates that with the message.

You can use this program by forking it and downloading it on your laptop and create a file to store the 'failed' or 'FAILED' list
and provide the appropriate path in the program.

Run this program as a cronjob so that it should continuously check for any failed attempts.
To do that type "crontab -e" on your terminal.

Then type the following command on the last line 

"* * * * * python /path_of_the_program" (without the quotes)

The "* * * * *" means that the code will run for infinite time.
