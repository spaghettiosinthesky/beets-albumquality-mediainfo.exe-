from setuptools import setup

setup(
    name='beets-albumquality',
    version='0.12.0',
    description='beets plugin adding adding encoder settings via mediainfo',
    long_description=open('README.md').read(),
    author='Mike Cameron',
    author_email='idk@idk.com',
    url='https://github.com/mikeacameron/beets-albumquality-mediainfo.exe-',
    license='MIT',
    platforms='WINDOWS',

    test_suite='test',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.4.3',
        'futures',
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)