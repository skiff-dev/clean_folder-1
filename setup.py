from setuptools import setup

setup(name='clean_folder',
      version='0.0.1',
      description='script for cleaning folders',
      url='https://github.com/Lyfenko/clean_folder',
      author='Dmytro Lyfenko',
      author_email='d.lyfenko@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )