from setuptools import setup, find_packages
import os


long_description = ""

test_requires = [
    ]

setup(name='gk.crypto',
      version='0.3.dev0',
      description="Crypto system for Gatekeeper",
      long_description = long_description,
      classifiers=['Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Zope Public License',
                   'Programming Language :: Python',
                   'Framework :: Zope3',
                   ],
      keywords='crypto gatekeeper',
      author='Novareto',
      author_email='grok-dev@zope.org',
      url='http://grok.zope.org',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['gk'],
      include_package_data=True,
      zip_safe=False,
      extras_require={'test': test_requires},
      install_requires=[
          "pycrypto",
          "setuptools",
          "cromlech.browser",
          "zope.i18nmessageid",
          ],
      entry_points={
         'paste.filter_app_factory': [
             'cipher = gk.crypto.ticket:cipher',
         ],
      }

      )
