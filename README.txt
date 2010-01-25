==================
WebSocket buildout
==================

This experimental buildout automatically installs the Apache HTTP server,
mod_python and pywebsocket into an isolated development environment.

Prerequisites
-------------

I recommend to install this buildout into a virtualenv in order to obtain
isolation from any 'system' packages you've got installed in your Python
version.

See http://pypi.python.org/pypi/virtualenv for further information.

Requirements
------------

Most of the required libraries and programs will be installed by zc.buildout.
See the buildout.cfg file.

The buildout needs Python and the tools contained in /bin and /usr/bin of a
standard installation of the Linux operating environment. You should ensure
that these directories are on your PATH and following programs can be found:

 - Python 2.5.2+ (3.x is not supported!)
 - gcc and g++
 - make
 - autoconf
 - curl
 - libtool

Buildout
--------

Install the WebSocket development environment by typing following commands::

  $ virtualenv --no-site-packages .
  $ ./bin/python bootstrap.py
  $ ./bin/buildout
  $ WEBSOCKET_HANDLER_LOG_DIR=`pwd`/var PYTHONHOME=`pwd` ./parts/apache/bin/httpd

And if you want to install and run the demo without virtualenv just follow
these steps::

  $ python bootstrap.py
  $ ./bin/buildout
  $ WEBSOCKET_HANDLER_LOG_DIR=`pwd`/var PYTHONHOME=/absolute/path/to/where/python/is/installed PYTHONPATH=`pwd`/parts/pywebsocket:`pwd`/parts/mod_python/lib/python ./parts/apache/bin/httpd

You get a fully configured Apache providing WebSockets. Use a browser which
supports WebSockets and visit http://localhost:8000 to see if it works.

Stop httpd by typing::

  $ ./parts/apache/bin/httpd -k stop

Contact
-------

Tobias Rodäbel <tobias dot rodaebel at googlemail dot com>
