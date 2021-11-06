import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="problem_solving_offline_judge",
    version="1.0.0",
    author="Jihun Lee",
    author_email="zkoong21@gmail.com",
    description="알고리즘 문제풀이 오프라인 저지",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["colorama"],
    url="https://github.com/jihunleekr/problem_solving_offline_judge_python",
    project_urls={
        "Bug Tracker": "https://github.com/jihunleekr/problem_solving_offline_judge_python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
