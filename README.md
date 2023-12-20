# Crispin Python package

This is a collection of code that I commonly reuse and decided to package to make installations on servers easier.



# Contributing

If you want to deploy this package (assuming you have access rights) then remember to setup the `~/.pypirc` file like this:
```bash
[testpypi]
    username = __token__
    password = pypi-[your_token_here]
```


### Updating package

Run `bash update_package`