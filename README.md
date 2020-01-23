# locationtagger
**version 1.0.0**

Detect and extract locations (Countries, Regions/States & Cities) from text or URL also find relationships among country, regions & cities.

---
## About Project



---
## Install and Setup
Install the package using pip -

`pip install locationtagger`
 
But before we install the package, we need to install some useful libraries given below,

`nltk`

`spacy`

`newspaper3k`

`pycountry`

After installing these package, there are some important nltk & spacy modules that need to be downloaded using commands given in `/locationtagger/bin/locationtagger-nltk-spacy` on IPython shell or Jupyter notebook.

---
## Usage
After proper installation of the package, import the module and give some text/URL as input;

`import locationtagger
text = "A winter weather advisory remains in effect through 5 PM along and east of a line from Blue Earth, to Red Wing line in Minnesota and continuing to along an Ellsworth, to Menomonie, and Chippewa Falls line in Wisconsin."
entities = locationtagger.find_locations(
