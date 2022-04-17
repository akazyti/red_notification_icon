from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in red_notification_icon/__init__.py
from red_notification_icon import __version__ as version

setup(
	name="red_notification_icon",
	version=version,
	description="Make Notification Icon Red",
	author="Zaspi Softwares",
	author_email="zaspisoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
