import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-authenticator-mongo",
    version="0.1.1",
    author="Kegbokokim Ibok",
    author_email="ibokkegbo@robotforge.co",
    description="A secure authentication module to validate user credentials and insert user credentails in Mongodb with streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RobotForge/Streamlit-Authenticator-mongo",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['Python', 'Streamlit', 'Authentication', 'Components','MongoDB'],
    python_requires=">=3.6",
    install_requires=[
        "PyJWT >=2.3.0",
        "bcrypt >= 3.1.7",
        "PyYAML >= 5.3.1",
        "streamlit >= 1.18.0",
        "extra-streamlit-components >= 0.1.60",
        "pymongo >= 4.6.0"
    ],
)
