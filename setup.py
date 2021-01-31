from setuptools import setup

setup(
    name='tcpgreenwavereality',
    packages=['tcpgreenwavereality'],
    install_requires=[
          'requests',
          'xmltodict',
          'urllib3',
      ],
    url='https://github.com/mandoolorian/greenwavereality.git',
    license='MIT',
    author='David Fiel',
    author_email='github@dfiel.com',
    description='Control of Greenwave Reality Lights'
)
