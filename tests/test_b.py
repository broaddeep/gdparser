from gdparser import parse

text = '''Generate flow-independent problem with GPT-2 algorithm

    Args:
        text (str): input text (required)

    Keyword Arguments:
        priority (str): the criterion by which distractors are considered to be better.
            possible values: {'meaning_dissimilarity', 'difficulty_similarity'}    
        nsamples(int) : the number of non-flowing sentence candidates
        length(int) : the length of the candidate sentence
        top_k(int) :  the number of tokens that can be candidates for token generation
        temperature(float) : the degree of randomness in sentence generation. The closer to 1, with a value between 0 and 1, the greater the randomness
        seed(int) : seed for reproducible result, -1 does not fix seed { this is invalid for something }

    Raises:
        AssertionError: if the number of sentences in the fingerprint is less than six, you cannot create a problem.

    Returns:
        dict: following keys describing the result
            - list_sentence : Full text with sentences not related to flow. List type
            - index_answer : The index of the flow-independent sentence
            - index_incorrect_answer : Incorrect sentences indices.

    Examples:
        {'list_sentence':['Industrial capitalism not only created work, it also created ‘leisure’ in the modern sense of the term.',
                          'This might seem surprising, for the early cotton masters wanted to keep their machinery running as long as possible and forced their employees to work very long hours.',
                          ...],
         'index_answer': 7,
         'index_incorrect_answer': [6, 8, 9, 10]
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
    assert len(parameters) == 7
    
        
def test_sections_must_be_three():
    # Raises, Returns, Examples
    assert len(parsed['sections']) == 3
    

def test_enum_is_parsed():
    for param in parsed['parameters']:
        if param['name'] == 'priority':
            assert param['enum'] is not None
        else:
            assert param['enum'] is None
            
    