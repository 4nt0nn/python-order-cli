from setuptools import setup


setup(name='order-runner',
      version=0.1,
      url='',
      author="Anton Stålhandske",
      author_email="antonstalhandske@gmail.com",
      description="A command-line utility for parsing order files.",
      license='MIT',
      long_description=open('README.md').read(),
      packages=['orderruner'],
      install_requires=['argparser', 'pandas', 'numpy'],
          entry_points={
          "console_scripts": [
              "orderrunner = orderrunner.__main__:main",
          ],
      })
