
from setuptools import setup, find_packages

setup(
    name="zkml_vector_transform",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "ezkl>=0.1.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A ZKML framework for proving many-to-one vector transformations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/zkml_vector_transform",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
