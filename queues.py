# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:09:10 2018

@author: Rohit
"""

class Queue(object):
    
    def __init__(self):
        self.queue = [];
        
    def isEmpty(self):
        return self.queue == [];
        
    def enque(self, data):
        self.queue.append(data);
        
    def deque(self):
        data = self.queue[0];
        del self.queue[0];
        return data;
        
    def peek(self):
        return self.queue[0];
    
    def sizeStack(self):
        return len(self.queue);
    
queue_ = Queue();
print(queue_.isEmpty());
queue_.enque(1);
print(queue_.sizeStack())
queue_.enque(2);
print(queue_.sizeStack())
queue_.enque(3);
print(queue_.sizeStack())
print(queue_.deque());
print(queue_.isEmpty());
print(queue_.peek());
print(queue_.deque());
print(queue_.deque());
print(queue_.isEmpty());
    
    