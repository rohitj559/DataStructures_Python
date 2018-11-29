# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:29:34 2018

@author: Rohit
"""

class Stack(object):
    
    def __init__(self):
        self.stack = [];
        
    def isEmpty(self):
        return self.stack == [];
        
    def push(self, data):
        self.stack.append(data);
        
    def pop(self):
        data = self.stack[-1];
        del self.stack[-1];
        return data;
        
    def peek(self):
        return self.stack[-1];
    
    def sizeStack(self):
        return len(self.stack);
    
stack_ = Stack();
print(stack_.isEmpty());
stack_.push(1);
print(stack_.sizeStack())
stack_.push(2);
print(stack_.sizeStack())
stack_.push(3);
print(stack_.sizeStack())
print(stack_.pop());
print(stack_.isEmpty());
print(stack_.peek());
print(stack_.pop());
print(stack_.pop());
print(stack_.isEmpty());
    
    