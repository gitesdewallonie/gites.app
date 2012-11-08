import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from plone.app.testing import quickInstallProduct
from gites.app.testing import\
    GITES_APP_INTEGRATION


class TestInstall(unittest.TestCase):

    layer = GITES_APP_INTEGRATION

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'gites.app'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def testReinstall(self):
        portal = self.layer['portal']
        quickInstallProduct(portal, 'gites.app')
