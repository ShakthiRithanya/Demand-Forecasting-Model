from setuptools import setup, find_packages

setup(
    name="demand-forecasting-model",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "statsmodels",
        "joblib",
        "flask",
        "plotly",
    ],
    author="Shakthi Rithanya S",
    description="A demand forecasting model using ML and statistical methods",
    python_requires=">=3.8",
)
