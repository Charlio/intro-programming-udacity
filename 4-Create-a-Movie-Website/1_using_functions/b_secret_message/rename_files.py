# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
import os

dir_path = r"C:\Users\chali\Documents\Work\Artificialintelligence\intro-programming-Udacity\4-Create-a-Movie-Website\1_using_functions\b_secret_message\prank"
curr_path = os.getcwd()

def rename_files():
    file_list = os.listdir(dir_path)
    os.chdir(dir_path)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print('Old file name: ', file_name, '--> New file name:', file_name.translate(None, "0123456789"))
    os.chdir(curr_path)
rename_files()