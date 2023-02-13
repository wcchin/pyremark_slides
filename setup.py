from setuptools import setup, find_packages

setup(
    name="pyremark_slides",

    version="0.1.1",

    author="Benny Chin",
    author_email="wcchin.88@gmail.com",

    packages=['pyremark', 'pyremark.docdata', 'pyremark.remarkjs', 'pyremark.templates'],
    #package_dir={'':'pyremark'},

    include_package_data=True,
    package_data={'': ['templates/*.html']},

    url="https://github.com/wcchin/pyremark_slides",

    license="LICENSE",
    description="a python package that convert markdown to remark.js slides, a sister project of pyreveal.",

    long_description=open("README.md").read(),

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Visualization',

         'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
    ],

    keywords='remark.js, markdown, slides, presentation',

    install_requires=[
        "jinja2",
        "watchdog",
    ],
    entry_points={
        "console_scripts": ['pyremark = pyremark.pyremark:main']
        },
)
