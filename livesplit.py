# LiveSplitPy
import socket

class LiveSplit:
    def __init__(self, address="localhost", port=16834):
        self.is_connected = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.is_connected = True
    def close(self):
        self.socket.close()
        self.is_connected = False
    def _check_conn(self):
        if self.is_connected is False:
            raise Exception("Not connected!")
    def start_timer(self):
        self._check_conn()
        self.socket.sendall(b'starttimer\r\n')
    def start_or_split(self):
        self._check_conn()
        self.socket.sendall(b'startorsplit\r\n')
    def split(self):
        self._check_conn()
        self.socket.sendall(b'split\r\n')
    def unsplit(self):
        self._check_conn()
        self.socket.sendall(b'unsplit\r\n')
    def skip_split(self):
        self._check_conn()
        self.socket.sendall(b'skipsplit\r\n')
    def pause(self):
        self._check_conn()
        self.socket.sendall(b'pause\r\n')
    def resume(self):
        self._check_conn()
        self.socket.sendall(b'resume\r\n')
    def reset(self):
        self._check_conn()
        self.socket.sendall(b'reset\r\n')
    def init_game_time(self):
        self._check_conn()
        self.socket.sendall(b'initgametime\r\n')
    def set_game_time(self, time):
        self._check_conn()
        self.socket.sendall(b'setgametime' + time + b'\r\n')
    def set_loading_times(self, time):
        self._check_conn()
        self.socket.sendall(b'setloadingtimes' + time + b'\r\n')
    def pause_game_time(self):
        self._check_conn()
        self.socket.sendall(b'pausegametime\r\n')
    def unpause_game_time(self):
        self._check_conn()
        self.socket.sendall(b'unpausegametime\r\n')
    def set_comparison(self, comparison):
        self._check_conn()
        self.socket.sendall(b'setcomparison ' + comparison + b'\r\n')
    def get_delta(self, comparison=b''):
        self._check_conn()
        self.socket.sendall(b'getdelta' + comparison + b'\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_last_split_time(self):
        self._check_conn()
        if int(self.get_split_index()) == 0:
            raise Exception("No previous splits as this is the first.")
        self.socket.sendall(b'getlastsplittime\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_comparison_split_time(self):
        self._check_conn()
        if self.get_current_timer_phase() != "Running":
            raise Exception("Run not initiated.")
        self.socket.sendall(b'getcomparisonsplittime\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_current_time(self):
        self._check_conn()
        self.socket.sendall(b'getcurrenttime\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_final_time(self, comparison=b''):
        self._check_conn()
        if comparison != b'':
            self.socket.sendall(b'getfinaltime ' + comparison + b'\r\n')
        else:
            self.socket.sendall(b'getfinaltime\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_predicted_time(self, comparison):
        self._check_conn()
        self.socket.sendall(b'getpredictedtime ' + comparison + b'\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_best_possible_time(self):
        self._check_conn()
        self.socket.sendall(b'getbestpossibletime\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_split_index(self):
        self._check_conn()
        self.socket.sendall(b'getsplitindex\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_current_split_name(self):
        self._check_conn()
        if self.get_current_timer_phase() != "Running":
            raise Exception("Run not initiated.")
        self.socket.sendall(b'getcurrentsplitname\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_previous_split_name(self):
        self._check_conn()
        if int(self.get_split_index()) == 0:
            raise Exception("No previous splits as this is the first.")
        self.socket.sendall(b'getprevioussplitname\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data
    def get_current_timer_phase(self):
        self._check_conn()
        self.socket.sendall(b'getcurrenttimerphase\r\n')
        data = self.socket.recv(1024).decode("utf-8").replace("\r\n", "")
        return data