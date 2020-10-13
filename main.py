#!/usr/bin/python3

import os
import time
#import flask
import psutil


class SystemInformation:
    def __init__(self):
        self.cpu_usage = 0
        self.cpu_temperature = 0
        self.cpu_frequency = 0
        self.mem_total = int(psutil.virtual_memory().total / 1024 / 1024)
        self.mem_usage = 0
        self.mem_percent = 0
        self.disk_read = 0
        self.disk_write = 0
        _counters = psutil.net_io_counters()
        '''
        kb
        '''
        self.net_send = 0
        self.net_receive = 0
        self._last_time_net_recv = 0
        self._last_time_send = 0
        self._last_time_disk_read = 0
        self._last_time_disk_write = 0
        self._last_update_time = time.time()

        self.start = False
        self.is_linux = os.name == 'posix'

    def update(self):
        self.cpu_usage = psutil.cpu_percent()
        self.cpu_frequency = int(psutil.cpu_freq().current)
        self.mem_usage = int(psutil.virtual_memory().used / 1024 / 1024)
        self.mem_percent = psutil.virtual_memory().percent
        self.cpu_temperature = psutil.sensors_temperatures()['cpu_thermal'][0].current if self.is_linux else 0
        _net_counters = psutil.net_io_counters()
        _disk_counters = psutil.disk_io_counters()

        _cost_time = time.time() - self._last_update_time
        self.net_send = int((_net_counters.bytes_sent / 1024 - self._last_time_send) / _cost_time)
        self.net_receive = int((_net_counters.bytes_recv / 1024 - self._last_time_net_recv) / _cost_time)
        self.disk_read = int((_disk_counters.read_bytes / 1024 - self._last_time_disk_read) / _cost_time)
        self.disk_write = int((_disk_counters.write_bytes / 1024 - self._last_time_disk_write) / _cost_time)
        self._last_time_net_recv = _net_counters.bytes_recv / 1024
        self._last_time_send = _net_counters.bytes_sent / 1024

        self._last_time_disk_read = _disk_counters.read_bytes / 1024
        self._last_time_disk_write = _disk_counters.write_bytes / 1024
        self._last_update_time = time.time()

    def print(self):
        _net_send = f'{self.net_send}KB/s' if self.net_send < 1000 else f'{(self.net_send / 1024):.1f}MB/s'
        _net_recv = f'{self.net_receive}KB/s' if self.net_receive < 1000 else f'{(self.net_receive / 1024):.1f}MB/s'
        _disk_write = f'{self.disk_write}KB/s' if self.disk_write < 1000 else f'{(self.disk_write / 1024):.1f}MB/s'
        _disk_read = f'{self.disk_read}KB/s' if self.disk_read < 1000 else f'{(self.disk_write / 1024):.1f}MB/s'
        _mem_usage = f'{self.mem_percent}%'
        _cpu_usage = f'{self.cpu_usage}%'
        _cpu_freq = f'{self.cpu_frequency}MHz'
        _cpu_temperature = f"{self.cpu_temperature:.1f}'C"

        if self.start:
            print(
                f"\r"
                f"{_cpu_freq:^8}|"
                f"{_cpu_usage:^9}|"
                f"{_cpu_temperature:^8}|"
                f"{_mem_usage:^9}|"
                f"{_net_send:^8}|"
                f"{_net_recv:^8}|"
                f"{_disk_read:^9}|"
                f"{_disk_write:^9}",
                end='')
        self.start = True
        pass


if __name__ == '__main__':

    system_information = SystemInformation()
    max_tempreture = 0
    print('CPU Freq|CPU Usage|CPU Temp|Mem Usage|Net Send|Net Recv|Disk Read|Disk Write')
    while True:
        try:
            system_information.update()
            system_information.print()
            max_tempreture=max(max_tempreture,system_information.cpu_temperature)
            time.sleep(1)
        except KeyboardInterrupt:
            print(f'\nMax CPU tempreture is {max_tempreture}\'C')
            break
