from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name="pymoebots-base",
            maintainer="aayux",
            description="Stochastic Algorithms simulator for the Amoebot Model",
            url="http://github.com/aayux/pymoebots-base",
            download_url="http://github.com/aayux/pymoebots-base",
            license=None,
            packages=PACKAGES)

if __name__ == '__main__':
    setup(**opts)
