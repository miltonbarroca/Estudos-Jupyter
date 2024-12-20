from lxml import objectify

path = 'Performance_MNR.xml'

with open(path) as f:
    parsed = objectify.parse(f)

root = parsed.getroot()