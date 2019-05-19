# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:28:05 2019

@author: Kevin Craig
"""

# User objects for CIS 3120
class User:
    # properties: 
    bCanRead = False # By default, reading files files is denied
    bCanWrite = False # By default, writing files is denied
    strName = ''
    
    # create an instance of User
    def __init__(self, strName):
        self.strName = strName
    
    # methods:
    # call this method for the permission to read
    def CanRead(self):
        return self.bCanRead
    
    # call this method for the permission to write
    def CanWrite(self):
        return self.bCanWrite

# Child classes inherit the properties and methods of parent User
class Student(User):
    # overwrites the property bCanRead for Students only
    bCanRead = True
    
class Admin(User):
    # overwrites method for the permission to write
    def CanWrite(self):
        return True
    
