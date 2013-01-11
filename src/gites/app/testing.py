from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import gites.app
from gites.db.testing import PGRDB


GITES_APP = PloneWithPackageLayer(
    zcml_package=gites.app,
    zcml_filename='testing.zcml',
    gs_profile_id='gites.app:testing',
    additional_z2_products=('Products.CMFPlacefulWorkflow', 'gites.core', 'gites.db'),
    name="GITES_APP")

GITES_APP_INTEGRATION = IntegrationTesting(
    bases=(PGRDB, GITES_APP, ),
    name="GITES_APP_INTEGRATION")

GITES_APP_FUNCTIONAL = FunctionalTesting(
    bases=(GITES_APP, ),
    name="GITES_APP_FUNCTIONAL")
