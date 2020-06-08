import resize as rs
import categorize2 as ctg2
import roi
import histogram_equalizer as he
import augment
import splitdata
import tile
import cleanempty
import os




#he.histogrameq("unprocessed","he")
roi.roi("unprocessed","roi")



splitdata.splitdata("roi","train","validation-test",0.3)

ctg2.categorize("train",["1train","2train"])
ctg2.categorize("validation-test",["1test","2test"])

tile.tile("1train","1traintiled")
tile.tile("2train","2traintiled")
tile.tile("1test","1testtiled")
tile.tile("2test","2testtiled")


augmentation_1 = []
augment.augment("1train","1trainaugmented",augmentation_1)


rs.resize("1trainaugmented","1trainresized",299,299)
rs.resize("2trainaugmented","2trainresized",299,299)
rs.resize("1test","1testresized",299,299)
rs.resize("2test","2testresized",299,299)





ctg2.categorize("roi",["1","2"])
tile.tile("1","1tiled",4)
cleanempty.cleanempty("1tiled","1nonempty")
rs.resize("1nonempty","1resized",299,299)

tile.tile("2","2tiled",4)
cleanempty.cleanempty("2tiled","2nonempty")
rs.resize("2nonempty","2resized",299,299)

