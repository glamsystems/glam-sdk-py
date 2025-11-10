1. Install build tools: `pip install build twine`

2. Build the package: `python -m build`
3. Test on TestPyPI (recommended): `python -m twine upload --repository testpypi dist/*`
4. Publish to PyPI: `python -m twine upload dist/*`
