#!/usr/bin/env python 
#-*- coding: utf-8 -*-
##############################################
#  从文件末尾向前逐行读取文件
#  @author : gothz
#  @date : 2015-11-25
##############################################

from sys import argv
from sys import exit

class ReverseReader(object): 
    """Read a file line by line, bottom to top""" 
    def readline(self): 

        while True:

            pos = self.buf.rfind("\n") 
            buflen = len(self.buf)
           
            if pos == -1: 
                #no new line
                fp = self.fh.tell()
                if fp == 0 :
                    if self.buf == "":
                        return None
                    else:
                        return self.bisectline(0,0)

                if fp >= self.BLKSIZE:
                    self.fh.seek(-self.BLKSIZE, 1)
                    self.buf = self.fh.read(self.BLKSIZE) + self.buf
                    self.locatefp(self.BLKSIZE)
                else:
                    self.fh.seek(-fp, 1)
                    self.buf = self.fh.read(fp) + self.buf
                    self.locatefp(fp)

            elif pos == buflen - 1:
                #new line at the last index ignore
                self.buf = self.buf[:-1]
            else:
                return self.bisectline(pos+1, pos)
                
    def locatefp(self, size):
        curfp = self.fh.tell()
        if curfp == self.fpEnd:
            self.fh.seek(-size - self.endWithLF, 1)
        else:
            self.fh.seek(-size, 1)

    def bisectline(self, idx_start, idx_end):
        line = self.buf[idx_start:]
        self.buf = self.buf[:idx_end]
        return line

    def __iter__(self):
        return self

    def __next__(self):
        
        line = self.readline()
        if line == None:
            raise StopIteration
        else:
            return line + "\n"

    def next(self):

        line = self.readline()
        if line == None:
            raise StopIteration
        else:
            return line + "\n"

    def __init__(self, data_file): 
        """init read last char if \n ignore else read in"""
        self.fh = open(data_file, 'r')
        self.BLKSIZE = 4096
        self.endWithLF = 0
        self.buf = ""
        self.fh.seek(0, 2)
        self.fpEnd = self.fh.tell() 
        self.fh.seek(-1, 2)
        tailchar = self.fh.read(1)
        if tailchar == "\n":
            self.fh.seek(-1, 2)
            self.endWithLF = 1

if __name__=="__main__":

    if len(argv) != 2:
        print "./" + argv[0] + " destfile"
        exit(1)
    br = ReverseReader(argv[1]) 
     
    for line in br:
       print line


