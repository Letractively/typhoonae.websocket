"""Demo Web Socket Handler.

Dispatches incoming messages to an App Engine application.
"""

import logging
import mod_pywebsocket.msgutil
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(asctime)s %(filename)s:%(lineno)s] %(message)s',
    filename=os.path.join(
        os.environ['WEBSOCKET_HANDLER_LOG_DIR'], 'demo_wsh.log'),
    filemode='a')


def web_socket_do_extra_handshake(request):
    logging.debug(request.connection.remote_addr)


def web_socket_transfer_data(request):
    while True:
        message = mod_pywebsocket.msgutil.receive_message(request)
        logging.debug(message)
        mod_pywebsocket.msgutil.send_message(request, message)
