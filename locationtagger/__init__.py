from .locationextractor import NamedEntityExtractor, LocationExtractor

def find_locations(url=None, text=None):
    e = NamedEntityExtractor(url=url, text=text)
    e.find_named_entities()

    locs = LocationExtractor(e.named_entities)
    locs.set_countries()
    locs.set_regions()
    locs.set_cities()
    locs.set_other()

    return locs
