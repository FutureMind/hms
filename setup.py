import setuptools

long_description = ('The Huawei Admin Python SDK enables server-side (backend) Python developers '
                    'to integrate Huawei into their services and applications.')

setuptools.setup(
    name="hms",
    version="1.0.2",
    author="Huawei",
    # author_email="author@example.com",
    description="Huawei Admin Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://developer.huawei.com/consumer/cn/",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
    ],
)
