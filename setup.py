import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locationtagger",
    version="0.0.1",
    author="Kaushik Soni",
    author_email="kaushiksoni10@gmail.com",
    description="Detect & Extract locations from text or URL and find relationships among locations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaushiksoni10/locationtagger",
    packages= ["locationtagger"],
    include_package_data=True,
    scripts=[
        'locationtagger/bin/locationtagger-nltk-spacy',
        'locationtagger/tests/__init__.py',
        'locationtagger/tests/test_LocationExtractor.py',
        'locationtagger/tests/test_NamedEntityExtractor.py'
    ],
    package_data = {
        'locationtagger': ['data/*.csv', 'data/*.jpg']
    },
    license='MIT',
    install_requires=[
        'nltk',
        'spacy',
        'newspaper3k',
        'pycountry'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Text Processing",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5'
)