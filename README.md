# CI-Python

[![](https://github.com/YueyangLiulyy/Chinese-broccoli-/workflows/Python%20application/badge.svg)](https://github.com/YueyangLiulyy/Chinese-broccoli-/actions)

Python CI template for GitHub Actions

Folder structure:
```
.
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt ========> python dependencies, a MUST
│
├───.github
│   └───workflows
│           pythonapp.yml =======> CI workflow for python
│
└───package
        app.py
        test_app.py   ==========> test file
        __init__.py
        
```

To run all the test code:

```
pytest
```
