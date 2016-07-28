#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
import pyinotify
import os
import sys
import logging

logging.basicConfig(level = logging.INFO, filename = '/var/log/qtools.log')

class TailEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        line = fs.readline()
        if line:
            sys.stdout.write( line )
            logging.info('%s ==> %s' % (event.pathname, line))

class Qtools(object):
    @staticmethod
    def tail(filename = ''):
        global fs
        filename = filename == '' and sys.argv[1]
        fs = open(filename)
        stats = os.stat( filename )
        size = stats[6]
        fs.seek( size )
        wm = pyinotify.WatchManager()
        wm.watch_transient_file(filename, pyinotify.IN_MODIFY, TailEventHandler)
        notifier = pyinotify.Notifier(wm)
        notifier.loop()

if __name__ == '__main__':
    Qtools.tail()
