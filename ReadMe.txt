Welcome to Sten-o-Crypt!!! 

This program will take a message from a text file and store it in a .png image 
of your choice! This steganographic process will store your data in plain sight and
no one will be able to retrieve it because it is password protected, unless you 
allow someone to have the password.

We hope that this program can offer a new way to communicate safely, since the only
way to retrieve the hidden message is to use this program and supply the original 
password that was used to store the message in the first place.


INSTALLATION =====================================================================

_____________________________Prepping Python3_____________________________________
Since the code is in Python 3, please ensure you have it. The following shows 
how to install python3 and the necessary libraries for a Windows system.

In Command Prompt check if you have python 3 installed with the following command: 
py -3 -V
	If installed, 
		You should see the version number with 3.x
		Verify you have pip installed with pip --version
			If not, please refer to pythons website on how to install it
	If not  
		Visit the following link and download the latest python3 version:
		https://www.python.org/downloads/
		Installation is pretty simple. Keep an eye out to verify that 
		pip is also installed during this process.

Note: If you have both python2 and python3 installed, invoke python3 with 
py -3 at your CLI. Also ensure that pip --version returns a path to the 
python3 installation. If not, then adjust your environment variables.


_______________________________Getting Libraries_________________________________
At your cmd, execute the following: 
pip install Stegano
pip install cryptography

==================================================================================


**********************************************************************************
If you are having troubles installing python3 or pillow, please refer to other 
online resources for help.
**********************************************************************************


USING StenoCrypt =================================================================

Begin by opening cmd and changing your directory to the Sten-o-Folder folder using 
the cd command.

Example: assuming that the Sten-o-Crypt folder is located in your Desktop, then
cd C:\Users\Hector Sanabria\Desktop\Sten-o-Crypt

Run the program by calling the python 3 interpreter:
py -3 StenoCrypt.py -h

As you can see we need to specify either -s or -u, depending on whether we want to
stash information in a .png file or extract information from a .png file

Thus, you run the command again with the correct switch (either -s or -u) and follow
the instructions prompted.

Tips: Use your Windows Explorer to navigate to the directory in which the image 
is located and copy the complete path from the top toolbar into the cmd to avoid 
typing the paths incorrectly. 

The results will appear in the specified directories. 

====================================================================================