#!/usr/bin/env python3

import os
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
#ch = logging.StreamHandler() # console / terminal
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=300, 
    backupCount=10,
)
fh.setLevel(log_level)    
fmt = logging.Formatter(
    "%(asctime)s  %(name)s  %(levelname)s " 
    "l:%(lineno)d f:%(filename)s: %(message)s"
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)
 
"""
log.debug("Msg dev, sysadmin")
log.info("Msg geral users")
log.warning("Aviso de causa de erro")
log.error("Erro que afeta um unica execução")
log.critical("Erro geral")
"""
print("---")
 
try:
    1 / 0
except ZeroDivisionError as e:
    log.error("%s", str(e))
