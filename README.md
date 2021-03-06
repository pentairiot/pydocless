# pydocless

Library for turning your python docstrings into Markdown documentation.
Note this should not be used as a substitute for good documentation, but as an addition.
The style is intended to look similar to Python's standard library API docs.

### Usage:
From the command line:
```
pydocless config.json > module_doc.md
```

Or from within a python environment:
```
from pydocless import pydocless
md_text = pydocless(config)
```

The config object should be a dictionary:
```
{
    "module": "module_name",    # Module should be available within the python environment
    "includes": [],             # List of regexes for what to include. By default nothing is included
    "excludes": []              # List of regexes for what to exclude. By default nothing is excluded
}
```

