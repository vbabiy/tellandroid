#!/usr/bin/env python

"""Wraps adb telnet command, allowing you to update your location.

Usage:
  geofix.py [--host=<host>] [--port=<port>]
  geofix.py set [--] <lat> <long>
  geofix.py timed [--interval=<s>] [--] <lat> <long> 

Options:
  -h --help     Show this screen.
  --version     Show version.
  -i --interval=<seconds>    Set the refresh interval [default: 5].
  --host=<host>    Host to connect to [default: localhost].
  -p --port=<port>     Host to connect to [default: 5554].

"""

from docopt import docopt
import telnetlib
import time
from threading import Thread

class AndroidTelnet(object):

  def __init__(self, host, port):
    self._host = host
    self._port = port

    self.telnet = telnetlib.Telnet(self._host, self._port)

    self.telnet.read_until("OK")

  def execute(self, command):
    self.telnet.write(command)
    return self._is_success()

  def _is_success(self):
    index, result, read = self.telnet.expect(['OK', "OK"], 5)
    if index == 0:
      return True
    else:
      return False



if __name__ == '__main__':
    arguments = docopt(__doc__, version='Android Geo Fix 1.0')
    android = AndroidTelnet(arguments['--host'], arguments['--port'])

    line = "geo fix %s %s\n" % (arguments['<long>'], arguments['<lat>'])

    if arguments['set']:
      android.execute(line)
    elif (arguments['timed']):
      print "Update emulator location every %s seconds" % int(arguments['--interval'])
      def run():
        while True:
          android.execute(line)
          time.sleep(int(arguments['--interval']))

    thread = Thread(target=run)
    thread.daemon = True
    thread.start()

    while True:
      time.sleep(1)




