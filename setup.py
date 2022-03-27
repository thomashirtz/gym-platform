from setuptools import setup
from setuptools import find_packages


setup(
    name='gym_platform',
    version='0.0.2',
    description='Platform domain OpenAI Gym environment',
    author='Craig Bester',
    packages=find_packages(),
    package_data={
        'gym_platform': ['envs/assets/*.png']
    },
    install_requires=[
        'gym',
        'pygame>=1.9.3',
        'numpy>=1.14.0',
    ]
) 
