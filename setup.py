from setuptools import setup

setup(name='licenseit',
      version='0.0.1',
      description='CLI for generationg a license files.',
      url='https://github.com/monzita/licenseit',
      author='Monika Ilieva',
      author_email='hidden@hidden.com',
      license='MIT',
      keywords='cli license generator',
      packages=['licenseit'],
      install_requires = ['docopt'],
      entry_points = {
      	'console_scripts': [
      		'licenseit=licenseit.cli:main'
      	],
      },
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Utilities'
      ],
      zip_safe=True)