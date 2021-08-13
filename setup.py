from setuptools import setup

setup(name='taeg',
      version='0.3',
      description='Calcul du taux annuel effectif global',
      author='Thibaut Spriet',
      author_email='thibaut@spriet.online',
      url='https://github.com/ThbtSprt/taeg',
      package_dir = {'': 'src'},
      packages=['taeg'],
      install_requires=["frdate","dateutils"]
     )
