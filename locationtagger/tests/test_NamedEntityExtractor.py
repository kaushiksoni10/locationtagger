from locationtagger.locationextractor import NamedEntityExtractor

def test():
    try:
        ne = NamedEntityExtractor(url='https://edition.cnn.com/2020/01/14/americas/\
staggering-number-of-human-rights-defenders-killed-in-colombia-the-un-says/index.html')
        ne.find_named_entities()

        assert len(ne.named_entities) > 0
        assert 'Colombia' in ne.named_entities
        assert 'Geneva' in ne.named_entities
        assert 'Switzerland' in ne.named_entities

        text = """Adult day programs in two locations Forestpark and Hawkesbury. caregiver \
support including memory clinic & dementia friends, training & public education in the \
five eastern counties of Ontario STORMONT, DUNDAS, GLENGARRY, PRESCOTT, RUSSELL, as well \
as the CITY OF CORNWALL AND AKWESASNE"""

        ne2 = NamedEntityExtractor(text=text)
        ne2.find_named_entities()

        assert len(ne2.named_entities) > 0
        assert 'Ontario' in ne2.named_entities
        assert 'Hawkesbury' in ne2.named_entities
        assert 'DUNDAS' in ne2.named_entities
        assert 'PRESCOTT' in ne2.named_entities
        assert 'CORNWALL' in ne2.named_entities

        text2 = """my friend works in Bangalore which is sometimes called 'Silicon Valley of INDIA' \
it is the capital of Karnataka state; also he told me he's from kanpur"""
        ne3 = NamedEntityExtractor(text=text2)
        ne3.find_named_entities()

        assert len(ne3.named_entities) > 0
        assert 'Bangalore' in ne3.named_entities
        assert 'Karnataka' in ne3.named_entities
        assert 'INDIA' in ne3.named_entities
        
        print('passed test')
    
    except Exception:
        print('failed test')

test()
