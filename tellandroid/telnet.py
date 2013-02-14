import telnetlib

class AndroidTelnet(object):

  def __init__(self, host, port):
    self._host = host
    self._port = port

    self.telnet = telnetlib.Telnet(self._host, self._port)

    self.telnet.read_until("OK")

  def _clean(self, command):
    command = command.encode("ascii")

    if not command.endswith("\n"):
      command += "\n"

    return command

  def execute(self, command):
    command = self._clean(command)
    self.telnet.write(command)
    return self._is_success()

  def _is_success(self):
    index, result, read = self.telnet.expect(['OK', "OK"], 5)
    if index == 0:
      return True
    else:
      return False
