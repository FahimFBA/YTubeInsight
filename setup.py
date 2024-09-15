import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytubeinsight",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for YouTube channel analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ytubeinsight",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    install_requires=[
        "google-api-python-client>=2.0.0",
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=3.9",
            "black>=21.0",
            "isort>=5.0",
        ],
        "docs": [
            "sphinx>=3.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "ytubeinsight=ytubeinsight.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ytubeinsight/issues",
        "Source": "https://github.com/yourusername/ytubeinsight",
        "Documentation": "https://ytubeinsight.readthedocs.io/",
    },
)