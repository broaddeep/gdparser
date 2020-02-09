from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
package_name = 'gdparser'
version = '0.0.1'
description = "Google Docstring Parser"
url = "https://github.com/broaddeep/gdparser.git"



setup(
    name=package_name,
    version=version,
    author="broaddeep",
    author_email="broaddeep@gmail.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='parser docstring google text',
    license='Apache',
    url=url,
    packages=find_packages(),
    install_requires=[],
    package_data={package_name: ['*', '*/*', '*/*/*']},
    python_requires='>=3.6.0',
    classifiers=[
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Text Processing',
    ],
)