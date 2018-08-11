# hwDjangoV2

Revision
playing around with  [ref](https://docs.djangoproject.com/en/2.1/)



# How to install/update requirements modify

```bash
pip-compile # install requirements, compile requirements.in -> output -> requirements.txt
pip-compile --upgrade # all
pip-compile --upgrade-package [package-name] [or -P [package-name]] # specific package
pip-sync [requirements.txt] [requirements-dev.txt] # update virtual env to match the content of `requirements.txt`
```



### The template layer

