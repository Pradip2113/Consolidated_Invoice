from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in consolidated_invoice/__init__.py
from consolidated_invoice import __version__ as version

setup(
	name="consolidated_invoice",
	version=version,
	description="Consolidated Invoice",
	author="Pradip",
	author_email="Pradip@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
