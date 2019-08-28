# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:42:21 2019

@author: Mgeni
"""
import sys
import time
import webbrowser
def break_time():
    webbrowser.open_new("https://youtu.be/qm-QoJcra8U")
    time.sleep(18*60)
    webbrowser.open("https://github.com/machugu")
    time.sleep(30*60)
def my_session_flow():
    webbrowser.open("https://github.com/machugu")
    time.sleep(5*60)
    webbrowser.open_new_tab("https://www.udacity.com/course/introduction-to-python--ud1110")
    time.sleep(2*60*60) # break begins after two hours of study'''
    break_time()
    webbrowser.open_new_tab("https://courses.edx.org/courses/course-v1:BerkeleyX+CS198.2x+1T2019/courseware/c2b79b47be934972a74dab677f031083/73463859ec504af9ae2d5cfd22f92ba9/?child=first")
    time.sleep(90*60)
    break_time()
    webbrowser.open_new_tab("https://www.hackerrank.com/domains/python")
    time.sleep(2*60*60)
    webbrowser.open_new_tab("https://www.codewars.com/kata/search/python?q=&r%5B%5D=-8&beta=false")
    break_time()
    
    sys.exit(" End of sessions")
    
    
my_session_flow()   
    
