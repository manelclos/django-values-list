from setuptools import setup, find_packages


setup(
    name='django-values-list',
    version='0.1',
    description='Easy CHOICES in Database when you don\'t want/need to '
                'create one zillion tables and Foreign Keys',
    long_description=open('README.md').read(),
    author='Manel Clos',
    author_email='manelclos@gmail.com',
    url='http://github.com/manelclos/django-values-list',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
