"""
Lisless server.
"""
import astm.constants
import astm.server
import logging
import os
import sys
from .logging import JsonMessageStreamHandler
from .__version__ import __version__


LOG = logging.getLogger(__name__)

LOG_DATA = logging.getLogger("stdout")
LOG_DATA.propagate = False
LOG_DATA.addHandler(JsonMessageStreamHandler(sys.stdout))


class Dispatcher(astm.server.BaseRecordsDispatcher):
    """
    Dispatch based on the received records.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # XXX TODO: Record model classes in which to wrap raw records
        self.wrappers = {
            #"H": Header,
            #"P": Patient,
            #"O": Order,
            #"R": Result,
            #"C": Comment,
            #"L": Terminator,
        }

    def _default_handler(self, record):
        super()._default_handler(record)
        LOG_DATA.debug(record)

    # XXX TODO: on_* handlers


class Server(astm.server.Server):
    def __init__(self, *args, port = 11211, dispatcher = Dispatcher, **kwargs):
        LOG.info(f"Starting Lisless v{__version__}")
        super().__init__(*args, port = port, dispatcher = dispatcher, **kwargs)
        LOG.info("Listening on %s:%d" % self.addr)
