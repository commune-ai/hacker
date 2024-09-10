
from setuptools import setup, find_packages

setup(
    name="matrix_refactor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.9.0",
        "transformers>=4.0.0",
    ],
    author="Mr. Robot",
    author_email="mr.robot@example.com",
    description="A library to refactor matrices in Hugging Face models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrrobot/matrix_refactor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
