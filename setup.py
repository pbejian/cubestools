from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='cubestools',
      version="0.2",
      description="Cubes calculus",
      author="Pierre",
      author_email="pierre.bejian@gmail.com",
      url="https://github.com/pbejian/cubestools",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      # scripts=['scripts/chifoumy-run'],
      zip_safe=False)
