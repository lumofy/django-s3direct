import os
import io
import json
from setuptools import setup

with io.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding="utf-8") as f:
    readme = f.read()

with io.open(os.path.join(os.path.dirname(__file__), 'package.json'), encoding="utf-8") as f:
    package = json.loads(f.read())

setup(
    name=package['name'],
    version=package['version'],
    description=package['description'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=package['author']['name'],
    author_email=package['author']['email'],
    url=package['homepage'],
    packages=['s3direct'],
    include_package_data=True,
    install_requires=['django>=3.2'],
    python_requires='>=3.8',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
        'Framework :: Django :: 6.0',
        'Framework :: Django :: 6.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)
