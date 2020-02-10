from gdparser import parse

text = '''
    Generate sentence insert problem.

    Args:
        text (str): text to make sentence insert problem

    Keyword Arguments:
        asc(bool) : similarity ordering, if True, similarity is sorted in ascending order.
        seed(int): seed for reproducible result, -1 does not fix seed

    Raises:
    ValueError:
        - occurs when the number of sentences is less then 6 sentences
        - occurs when the top 3 sentences does not have signalwords( data : signalwords.csv ) 

    Returns:
    dict: following keys describing the result
        - list_sentence : Full text with sentences not related to flow. List type
        - index_answer : Answer index, the sentence corresponding to the index to be located in the box.
        - seed(int) : seed for reproducible result, -1 does not fix seed
        
    Examples:
    {'list_sentence': ['Industrial capital ... term.',
                            'This might ... surprising,', ... 
                            ],
     'index_answer': 6                       
                            
     }    
    '''
parsed = parse(text)

def test_section_header_startswith_nonblankchar():
    # since text contains ValueError:, and 'Error' is in supported section headers,
    # theres possibility that Error is recognized as the seperate section 
    for section in parsed['sections']:
        assert section['section_header'] != 'Error'
        
    
def test_parameters_no_space_between_name_and_type():
    # text, asc, seed
    parameters = parsed['parameters']
    assert len(parameters) == 3
    
        
def test_sections_must_be_three():
    # Raises, Returns, Examples
    assert len(parsed['sections']) == 3
    
    
    
    