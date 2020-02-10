## gdparser


#### google docstring parser

No dependencies required.

```
def test_func(text, k=3, e='base'):
    """This is a test function
    
    Args:
        text (str): this is text given by user
        
    Keyword Arguments:
        k (int): this is integer
        e (str): values should be in {'aa', 'bb'}
    
    Returns:
        None
        
    Examples:
        
        >>> text("dddd")
        # None
    """
    return None
    
    
    
from gdparser import parse

parse(test_func.__doc__)

{'description': 'This is a test function\n    \n    ',
 'parameters': [{'description': 'this is text given by user',
                 'enum': None,
                 'name': 'text',
                 'required': True,
                 'type': 'string'},
                {'description': 'this is integer',
                 'enum': None,
                 'name': 'k',
                 'required': False,
                 'type': 'integer'},
                {'description': "values should be in {'aa', 'bb'}",
                 'enum': ['aa', 'bb'],
                 'name': 'e',
                 'required': False,
                 'type': 'string'}],
 'sections': [{'section_body': 'None\n        \n    ',
               'section_header': 'Returns'},
              {'section_body': '        \n>>> text("dddd")\n# None\n    ',
               'section_header': 'Examples'}]}

```

#### Install

```
pip install gdparser
```


#### Usage

see the docstring of `parse` method

```
Parses Google-style Docstring.
    
    Args:
        text (str): docstring to parse written in Google-docstring format.
        
    Keyword Arguments:
        supported_headers (List[str] or None): list of text which can be recognized as the section headers, 
            if None, the values are
            ['Args', 'Arguments', 'Attention', 'Attributes', 'Caution', 'Danger',
             'Error', 'Example', 'Examples', 'Example Request', 'Hint', 'Important', 'Keyword Args',
             'Keyword Arguments', 'Kwargs', 'Methods', 'Note', 'Notes', 'Other Parameters',
             'Parameters', 'Return', 'Returns', 'Raises', 'References', 'See Also',
             'Tip', 'Todo', 'Warning', 'Warnings', 'Warns', 'Yield', 'Yields']
             
        args_headers (List[str] or None): list of text which can be recognized as the argument section headers. 
            Argument section headers is special which is parsed and fill the parameters of the final output.
            if None, the values are
            ['Args', 'Arguments', 'Parameters']
            
        kwargs_headers (List[str] or None): same as the args headers, except that the 'required' key of each parameter will become False.
            if None, the values are
            ['Kwargs', 'Keyword Args', 'Keyword Arguments']
            
        remove_indent (bool): whether indent is deleted or not. indent is defined as the 
            common whitespace length across the lines within same section.
            
        javascript_type (bool): whether the python type notation should be converted into javascript type.
            currently following four types are converted.
            'str'- 'string', 'int'- 'integer', 'bool'- 'boolean', 'float'- 'number'
            if the type is not in the among the supported types, returned as it is without conversion.
        
    Returns:
        dict: 
            - description (str) : function description
            - sections (List[Dict]) : the list of each section, each section is composed of two keys,
                 - section_header (str) 
                 - section_body (str)
            - parameters (List[Dict]) : the list of each parameter, each parameter is composed of five keys,
                 - name (str): parameter name
                 - type (str): parameter type
                 - description (str): parameter description
                 - required (bool) : when the parameter is found in the Args section, it becomes True. 
                      if found in Kwargs section, it become False
                 - enum (List or None) : You can make enum notation by using curly braces in the parameter description. 
                      if the curly brace notation can be evaluated as set, the set value is used.
                      e.g. {'ab', 'cd'} - ['ab', 'cd']
                           {10, 20, 30} - [10, 20, 30]

```


### Changelog

- `0.0.1` : Initial commit
- `0.0.2` : Add docstrings, test cases, and fix minor bug 
            (section header startswith non-blank character is recognized as valid section header)