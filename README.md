# IEQA
Question Answering augmented by explicit Information Extraction

## Installation

```
conda env create -f environment.yml
pre-commit install
```

## Structure
All our notebooks should be uploaded in [experiments](./experiments/) folder.
All final source code should be in [ieqa](./ieqa/) folder.

## Code format
As our team is quite large it is neccessary to make sure that our code has consistent format throught all modules.

1. Default pre-commit hooks [configuration](./pre-commit-config.yaml) is created for the project. Please, follow installation instruction to make sure you activate the hooks on your machine.
2. It is highly encouraged to use [typing annotations](https://docs.python.org/3/library/typing.html) in all major functions.
3. It is highly encouraged to use [python docstring](https://peps.python.org/pep-0257/) in all major functions. I would recommend using [autoDocstring extension](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring).

*P.S. In reality, we probably will copy-paste a lot of code from other projects, but rules described above should be applied at least to code that we write on our own.*