import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='pciqa',
                 packages=['pciqa'],
                 install_requires=install_requires)