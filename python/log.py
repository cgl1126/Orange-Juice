"""
"""

import os
import datetime
import inspect
import sys

THIS_FILE_NAME = __file__
LEVELS ={"DEBUG":1, "INFO":2, "WARNING":3, "ERROR":4}

def log_get_timestamp() -> str:
    timestamp_microsecond = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
    return timestamp_microsecond[0:18]

def log_print_element(log_element: str):
    print("[" + log_element +"]", end="")
    return 

def log_msg_handle(log_level: str,
                   filename: str,
                   line_no: int,
                   log_msg: str,
                   *log_paras: tuple):
    if LEVELS[log_level] < LEVELS[os.getenv("LOG_LEVEL", "DEBUG")]:
        return
    log_timestamp = log_get_timestamp()
    log_print_element(log_timestamp)
    log_print_element(log_level)
    log_print_element(filename)
    log_print_element(str(line_no))
    print(log_msg % log_paras[0])
    sys.stdout.flush()
    return

def log_debug(filename: str,
              log_msg: str,
              *log_paras: tuple):
    line_no = inspect.currentframe().f_back.f_lineno
    log_msg_handle("DEBUG", filename, line_no, log_msg, log_paras)
    return

def log_error(filename: str,
              log_msg: str,
              *log_paras: tuple):
    line_no = inspect.currentframe().f_back.f_lineno
    log_msg_handle("ERROR", filename, line_no, "\x1b[41m" + log_msg + "\x1b[0m", log_paras)
    return

def log_warning(filename: str,
                log_msg: str,
                *log_paras: tuple):
    line_no = inspect.currentframe().f_back.f_lineno
    log_msg_handle("WARNING", filename, line_no, "\x1b[43m" + log_msg + "\x1b[0m", log_paras)
    return

def log_info(filename: str,
             log_msg: str,
             *log_paras: tuple):
    line_no = inspect.currentframe().f_back.f_lineno
    log_msg_handle("INFO", filename, line_no, log_msg, log_paras)
    return

def log_info_color(filename: str,
                   color: int,
                   log_msg: str,
                   *log_paras: tuple):
    color_str = "\x1b[%dm" % color
    line_no = inspect.currentframe().f_back.f_lineno
    log_msg_handle("INFO", filename, line_no, color_str + log_msg + "\x1b[0m", log_paras)
    return

if __name__ == "__main__":
    i = 0
    while i < 3:
        log_error(THIS_FILE_NAME,
            	  "%s say %s %d times", "I", "Hello world", i)
        i += 1


