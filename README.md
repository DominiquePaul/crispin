# Crispin Python package

This is a collection of code that I commonly reuse and decided to package to make installations on servers easier.



### Useful commands

**Bumping the version**
To bump the version of the package using [bump2version](https://github.com/c4urself/bump2version):
- `bump2version patch` for mini fixes
- `bump2version minor` for small updates
- `bump2version major` for major updates

This will also create a new git commit. You still need to push to main.



**Publishing an update to pypi**
I created a chain of commands in the makefile, you just need to run
`make update_pkg`

Remember to setup the `~/.pypirc` file like this:
```bash
[testpypi]
    username = __token__
    password = pypi-[your_token_here]
```