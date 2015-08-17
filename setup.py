from setuptools import setup, find_packages


setup(
    name='slack_to_trello',
    version='1.0.0',
    description='Perform Trello actions via slash commands in Slack',
    long_description=open('README.rst').read(),
    keywords=[
        'slack',
        'trello'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/underdogio/slack-to-trello',
    download_url='https://github.com/underdogio/slack-to-trello/archive/master.zip',
    packages=find_packages(),
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
