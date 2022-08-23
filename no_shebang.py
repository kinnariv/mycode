print("ello!")
print("Did you say, hello?")
print("No, I said ello, but that\'s close enough.")
:wq
ls -ll
chmod u+x no_shebang.py
./no_shebang.py

# so right now you are in the VIM program. You cannot run 
:wq
ls -ll
chmod[200~mkdir -p /home/student/mycode/mix-list/


# inside of VIM. In order to run the actual commands in the labs, and not adding the code to the scripts, you need to be on the command line.

#if you do not see student@bchd: then those commands that you copy will not work.

#does any or all of that make sense?
Please give me sometime. once this list explanation is over will chat with you
iii
#kk 




SO student@bchd:~$s is command line correct?
O ca
n write command here and then run in student one

mkdir -p /home/student/mycode/mix-list/
cd ~/mycode/
vim ~/mycode/mix-list/mixlist01.py
#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )
:w
    how can I run in upper box?

    So again, we are in vim here, and up there. to run the commands i listed that you were trying to run, you have to get out of VIM. esc :q! if you don't want to save anything in here because it's just been our conversation
