from setuptools import setup

with open("version.txt", "r") as f:
    version = f.readline()

if version:
    import os
    packages = [x[0].replace("./", "").replace("/", ".") for x in filter(lambda x: x[2].__contains__("__init__.py"),
                                                                         os.walk("./"))]

    setup(
        name='ts-state-machine',
        version=version,
        packages=packages,
        url='',
        license='',
        author='manhdoi',
        author_email='',
        description=''
    )
else:
    print("Installing is failed because you are trying install an unknown version package.")
    exit(1)
