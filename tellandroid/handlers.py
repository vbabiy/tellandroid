from threading import Thread

import time
import sys


class Handler(object):

  def __init__(self, connection):
    self._connection = connection

class GeoHandler(Handler):

  def execute(self, command, *args, **kwargs):
    method_name = "_%s_handler" % command
    if hasattr(self, method_name):
      return getattr(self, method_name)(*args, **kwargs)
    else:
      raise Exception("No Geo handler for %s" % command)

  def _build_telnet_command(self, *args):
    return "geo fix %s %s" % (args[0], args[1])

  def _set_handler(self, *args):
    print "Setting Emulator Location to Lat: %s Long: %s" % (args[1], args[0])
    return self._connection.execute(self._build_telnet_command(*args))

  def _timed_handler(self, *args, **kwargs):
    print "Updating Emulator Location to Lat: %s Long: %s, every %s seconds" % (args[1], args[0], kwargs['interval'])
    return Thread(target=self._timed_runner,
      args=(self._build_telnet_command(*args),), kwargs=kwargs)

  def _timed_runner(self, cmd, interval=5):
    while True:
      self._connection.execute(cmd)
      time.sleep(int(interval))

class SmsHandler(Handler):

  DEAULT_NUMBER = 18482592224

  def execute(self, message, number=None):
    number = self._clean_number(number)
    print "Send an SMS message to emulator. From: %s, Message: %s" % (number, message)
    return self._connection.execute("sms send %s %s" % (number, message))

  def _clean_number(self, number):
    if not number:
      return self.DEAULT_NUMBER
    return number