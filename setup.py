# setup.py
from setuptools import setup, find_packages

setup(
    name='temp_converter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # 依存するパッケージがあればここに記載
    ],
    author='miz0805',
    author_email='s2222063@stu.musashino-u.ac.jp',
    description='A simple temperature conversion library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oyamadamizuka/temp_converter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

