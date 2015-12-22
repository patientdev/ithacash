#!/usr/bin/env python
from hendrix.deploy.base import HendrixDeploy
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)


options = {'settings': 'ithacash_dev.settings.local', 'loud': True}
deployer = HendrixDeploy(options=options)
deployer.run()
