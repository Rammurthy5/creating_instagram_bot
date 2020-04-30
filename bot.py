"""
Given cred, Write a bot that search for an hashtag and comment / like.

..date..    Apr 11 2020

"""

from instapy import InstaPy
import getpass

# username = input("Enter your username= ").strip()
password = getpass.getpass("Enter :")
# print("Password you entered: ", password)

# session = InstaPy(username='xxxxx', password='xxxxxx')
# try:
#     session.login()
# except Exception as e:
#     print(e)

# print(f"Already followed: \n {session.already_followed()} \n Already liked: \n {session.already_liked()} \n "
#       f"Already visited: \n {session.already_Visited()}"
#       f"\n Already Live report: {session.live_report()}")

