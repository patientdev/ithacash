from hendrix.deploy.base import HendrixDeploy

options = {'settings': 'ithacash_dev.settings.common', 'loud': True}
deployer = HendrixDeploy(options=options)
deployer.run()