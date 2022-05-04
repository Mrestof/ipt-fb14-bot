import time


def get_time() -> str:
    local = time.localtime()
    h = str(local.tm_hour)
    m = str(local.tm_min)
    s = str(local.tm_sec)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s
    return h + ':' + m + ':' + s
