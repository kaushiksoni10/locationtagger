from locationtagger.locationextractor import LocationExtractor

def test():
    try:
        l = LocationExtractor(['LGhhk', 'Vancouver', 'Pakistan', 'Texas'])
        l.set_countries()
        l.set_regions()
        l.set_cities()
        l.set_other()

        assert len(l.countries) == 1
        assert len(l.regions) == 1
        assert len(l.cities) == 1
        assert len(l.other) == 1
        assert len(l.other_countries) == 2
        assert len(l.other_regions) == 3
        assert 'LGhhk' in l.other

        l2 = LocationExtractor(['INDIA', 'karnataka', 'kuwait','kanpur'])
        l2.set_countries()
        l2.set_regions()
        l2.set_cities()
        l2.set_other()

        assert len(l2.countries) == 2
        assert len(l2.regions) == 1
        assert len(l2.cities) == 1
        assert len(l2.other) == 0
        assert l2.region_cities == {'Uttar Pradesh': ['Kanpur']}
        assert l2.country_regions == {'India': ['Karnataka']} 
        assert l2.country_cities == {'India': ['Kanpur']}
        print('passed test')
        
    except Exception:
        print('failed test')

test()
