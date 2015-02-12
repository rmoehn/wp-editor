__author__ = 'GHajba'
from distutils.core import setup
from disttest import test

setup(
    name='wpedit',
    packages=['wpedit'],
    version='0.2',
    description='Sends (offline) articles written in MarkDown to WordPress via the XML-RPC API',
    author='Gabor Laszlo Hajba',
    author_email='gabor.hajba@gmail.com',
    url='https://github.com/ghajba/wp-editor',
    download_url='https://github.com/ghajba/wp-editor/tarball/0.1',
    keywords=['wordpress', 'offline', 'edit', 'markdown', 'xml'],
    classifiers=['Programming Language :: Python',
                 'License :: OSI Approved :: MIT License', ],
    options={
        'test':{
            'test_dir':['tests']
        },
    },
    cmdclass = {'test':test},
    requires=[('Markdown'), ("python.wordpress.xmlrpc")],
)