import requests
import json

'''
Created on Sunday  Sept 22, 2019

@author: Ravi Patel
@cwid: 10432313 
'''


def isValid(username):
    '''
    The function of this method is to use requests to call the github api to check the username is a valid username.
    :param username:
    :return:
        boolean value
    '''
    if username == "" or None:
        return False
    else:
        url = 'https://api.github.com/users/{}/repos'.format(username)
        r = requests.get(url)
        if r.status_code == 200:
            return True
        else:
            return False


def githubAccountWithName(username=""):
    '''
    The function of this method is to use the github api and make a call to get username's repos
    :param username:
    :return:

    '''
    if isValid(username):
        r = requests.get('https://api.github.com/users/{}/repos'.format(username))
        reponame = None
        for i in r.json():
            reponame = i['name']
            break
        r = requests.get('https://api.github.com/users/{}/repos/{}'.format(username, reponame))
        return reponame


    elif username == "":
        return "Username is empty"
    else:
        return "Username is invalid"
