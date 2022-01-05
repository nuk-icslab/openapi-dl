import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openapi-dl",
    version="0.0.1",
    author="Yong-Hsiang Hu",
    author_email="iftnt1999@gmail.com",
    description="Recursively download the OpenAPI specification and it's dependency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nuk-icslab/openapi-dl",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'beautifulsoup4',
      'urllib3',
      'pyyaml'
    ],
    package_dir={"": "src"},
    scripts=["src/openapi_dl/openapi-dl"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
