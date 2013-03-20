from setuptools import setup, find_packages

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='gites.app',
      version=version,
      description="Gites Policy package",
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
      ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['gites'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'gites.calendar',
        'gites.core',
        'gites.db',
        'gites.gdwadmin',
        'gites.imports',
        'gites.ldap',
        'gites.locales',
        'gites.map',
        'gites.proprio',
        'gites.shop',
        'gites.skin',
        'gites.theme',
        'bnbelgium.skin',
        'Products.LinguaPlone',
        'Plone',
        'Pillow',
        'Products.MemcachedManager',
        'plone.app.jquery'
      ],
      extras_require={'test': ['plone.app.testing']})

# XXX add package:
# vieu .tar pourri, il faudrait en faire un egg ou ne plus utiliser ca
# (actuellement utilisé dans gites.skin cf Calendar.setup et peut etre autre
# chose)
#        'Products.PloneZCdatetimewidget'
