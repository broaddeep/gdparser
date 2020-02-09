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