import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get-browser-header-ZWZW911", # Replace with your own
    # username
    version="0.0.1",
    author="zwzw911",
    author_email="zwzw911110@163.com",
    description="A package to generate http(s) request header",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zwzw911/get-browser-header",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)