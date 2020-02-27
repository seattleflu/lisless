"""
Logging extensions.
"""
import json
import logging
import os
import pdb
import sys


DEBUG_EXCEPTIONS = bool(os.environ.get("DEBUG_EXCEPTIONS", False))


def configure():
    # Drop into debugger when an exception is logged.
    if DEBUG_EXCEPTIONS:
        logging.setLoggerClass(DebuggingLogger)

    # Keep it simple for now.
    logging.basicConfig(
        level = logging.DEBUG,
        format = "[%(asctime)s] %(levelname)-8s %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S%z",
        stream = sys.stderr,
        force = True)

    # Log library API warnings.
    logging.captureWarnings(True)

    # Log (and thus potentially debug) any uncaught exceptions which are about
    # to cause process exit.
    sys.excepthook = (lambda *exc_info:
        logging.getLogger().critical("Uncaught exception:", exc_info = exc_info))


class DebuggingLogger(logging.getLoggerClass()):
    def handle(self, record):
        super().handle(record)

        if record.exc_info:
            pdb.post_mortem(record.exc_info[2])


class JsonMessageStreamHandler(logging.StreamHandler):
    def format(self, record):
        return json.dumps(record.msg, separators = (",",":"), indent = None)
