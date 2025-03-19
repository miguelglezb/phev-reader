from setuptools import setup, find_packages

setup(
    name="phev",  # Adjust if needed
    version="0.1.0",
    packages=find_packages(),  # Automatically find submodules
    install_requires=["pandas","numpy"],  # Add dependencies here
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
