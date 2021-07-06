from setuptools import find_packages, setup


install_requires = [
    'aiohttp==3.7.3',
    'gunicorn==20.1.0',
    'arq==0.20',
    'aiohttp-cors==0.7.0',
    'aioredis==1.3.1',
    'async-timeout==3.0.1',
]


setup(
    name='Test 4',
    version='0.0.1',
    description='ER Telecom. Test 4.',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
