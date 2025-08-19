from libifcb import ROIReader
from planktofeatures.extractors import WHOIVersion4
import json

sample1 = ROIReader("testdata/D20140117T003426_IFCB014.hdr", "testdata/D20140117T003426_IFCB014.adc", "testdata/D20140117T003426_IFCB014.roi")
#print(json.dumps(sample1.header, indent=4))
#for trigger in sample1.triggers:
    #print(json.dumps(trigger.raw, indent=4))
print(str(len(sample1.rois)) + " ROIs")

extractor = WHOIVersion4()

features = extractor.process(sample1.rois[1899].image)

sample1.rois[1899].image.save("testout/D20140117T003426_IFCB014_01899.png")
features.blob.save("testout/D20140117T003426_IFCB014_01899_blob.png")

print(features.values)
