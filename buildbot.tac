import os
import os.path

from buildbot_worker.bot import Worker
from twisted.application import service

from twisted.python.logfile import LogFile
from twisted.python.log import ILogObserver, FileLogObserver

rotateLength = 10000000
maxRotatedFiles = 10

basedir = os.path.abspath(os.path.dirname(__file__))

# note: this line is matched against to check that this is a worker
# directory; do not edit it.
application = service.Application('buildbot-worker')

logfile = LogFile.fromFullPath(
    os.path.join(basedir, "twistd.log"),
    rotateLength=rotateLength,
    maxRotatedFiles=maxRotatedFiles,
)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

import user_config

s = Worker(
    None,
    None,
    user_config.name,
    user_config.passwd,
    basedir,
    user_config.keepalive,
    umask=user_config.umask,
    maxdelay=user_config.maxdelay,
    numcpus=user_config.num_cpus,
    allow_shutdown="signal",
    maxRetries=None,
    protocol=user_config.protocol,
    delete_leftover_dirs=0,
    proxy_connection_string=None,
    connection_string=user_config.connection_string,
)
s.setServiceParent(application)
