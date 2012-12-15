from distutils.core import setup

setup(
    name='django-client-templates',
    version='0.1',
    description=" Django template JavaScript compiler",
    #long_description=open('README.rst').read(),
    author='Marco Louro',
    author_email='marco@lincolnloop.com',
    license='MIT',
    url='http://github.com/mlouro/django-client-templates/',
    packages=[
        'client_templates',
        'client_templates/customfilters',
        'client_templates/customtags',
        'client_templates/defaultfilters',
        'client_templates/defaulttags',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)