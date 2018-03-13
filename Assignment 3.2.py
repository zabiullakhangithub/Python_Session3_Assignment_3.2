# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:52:17 2018

@author: zabiulla.khan

Problem Statement 1:
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.

"""
#Define lists to hold subjects, verbs and Objects
subjects = ["Americans", "Indians"]
verbs = ["Play", "watch"]
objects = ["Baseball","Cricket"]

## Loop through subjects, verbs and objects list to display the combination of all the outputs
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            print( "%s %s %s." % (subjects[i], verbs[j], objects[k]))
           