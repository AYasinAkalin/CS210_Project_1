import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cs210-project1-ayasin',
    version='0.0.3b',
    author="Ali Yasin Akalın",
    author_email="ayasinakalin@sabanciuniv.edu",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AYasinAkalin/CS210_Project_1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
