#!/bin/env python

import urllib
import thread
import time
from socket import error as SocketError

def node_js_test(thread_name, a, b):
    while 1:
        try:
            time_start = time.time();
            #response = urllib.urlopen("http://taner.pub:8088/index.html");
            #response = urllib.urlopen("http://taner.pub/cmp_nodejs");
            #response = urllib.urlopen("http://www.baidu.com");
            response = urllib.urlopen("http://shareboard.pub:3000/");
            time_end = time.time();

            time_cost = (time_end - time_start) * 1000;
            #rep_str = response.read();

            #print thread_name + rep_str + " cost " + str(time_cost) + "ms.";
            print thread_name + " cost " + str(time_cost) + "ms.";
        except:
            pass
    
thread.start_new_thread(node_js_test, ("[thread 0]:", 1, 1))
thread.start_new_thread(node_js_test, ("[thread 1]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 2]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 3]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 4]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 5]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 6]:", 1, 1))
thread.start_new_thread(node_js_test, ("[thread 7]:", 1, 1))

thread.start_new_thread(node_js_test, ("[thread 8]:", 1, 1))
thread.start_new_thread(node_js_test, ("[thread 9]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 10]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 11]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 12]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 13]:", 1, 1)) 
thread.start_new_thread(node_js_test, ("[thread 14]:", 1, 1))
thread.start_new_thread(node_js_test, ("[thread 15]:", 1, 1))

while 1:
    pass
