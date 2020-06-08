import resize as rs
import categorize2 as ctg2
import roi
import histogram_equalizer as he
import augment
import splitdata
import tile2
import cleanempty
import os



def preprocess(path):
    #he.histogrameq(path,path+"/he")
    rs.resize(path,path+"/resized1",2560,2560)
    tile2.tile(path+"/resized1",path+"/tile",299)
    cleanempty.cleanempty(path+"/tile",path+"/resized")

