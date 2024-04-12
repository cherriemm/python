#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from xml.dom import minidom

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# 题目十六：XML文件的生成和解析
def create_xml(path):
    root = et.Element("tilemap", attrib={
        'tilemapservice':"http://tms.osgeo.org/1.0.0",
        'version':"1.0.0",
    })
    et.SubElement(root, 'title', text="default")
    et.SubElement(root, 'abstract')
    et.SubElement(root,'srs',text ='EPSG:4326')
    et.SubElement(root, 'vsrs')
    et.SubElement(root, 'boundingbox',attrib={
        'maxx': '180.0',
        'maxy': '90.0',
        'minx': '-180.0',
        'miny': '-90.0',
    })
    et.SubElement(root, 'origin', attrib={
        'x':'-180.0',
        'y': '-90.0',
    })

    et.SubElement(root, 'tileformat',attrib={
        'extension': "tif",
        'height': "17",
        'mime-type': "image/tiff",
        'width': "17",
    })

    tilesets = et.SubElement(root, 'tilesets', attrib={
        'profile': 'global-geodetic'
    })

    l=['10.588', '5.294', '2.647', '1.323', '0.661', '0.331']
    for i in range(6):
        et.SubElement(tilesets, 'tileset', attrib={
            'href': "",
            'order': str(i),
            'units-per-pixel': l[i],
        })

    tree = et.ElementTree(root)
    et.indent(tree, '  ')
    tree.write(path, encoding="utf-8")



import xml.etree.ElementTree as et
def create_xml(path):
    root = et.Element("tilemap", attrib={
        'tilemapservice':"http://tms.osgeo.org/1.0.0",
        'version':"1.0.0",
    })
    title = et.SubElement(root, 'title')
    title.text = "default"
    et.SubElement(root, 'abstract')
    srs = et.SubElement(root,'srs')
    srs.text = 'EPSG:4326'
    et.SubElement(root, 'vsrs')
    et.SubElement(root, 'boundingbox',attrib={
        'maxx': '180.0',
        'maxy': '90.0',
        'minx': '-180.0',
        'miny': '-90.0',
    })
    et.SubElement(root, 'origin', attrib={
        'x':'-180.0',
        'y': '-90.0',
    })

    et.SubElement(root, 'tileformat',attrib={
        'extension': "tif",
        'height': "17",
        'mime-type': "image/tiff",
        'width': "17",
    })

    tilesets = et.SubElement(root, 'tilesets', attrib={
        'profile': 'global-geodetic'
    })

    l=['10.588', '5.294', '2.647', '1.323', '0.661', '0.331']
    for i in range(6):
        et.SubElement(tilesets, 'tileset', attrib={
            'href': "",
            'order': str(i),
            'units-per-pixel': l[i],
        })

    tree = et.ElementTree(root)
    et.indent(tree, '  ')
    tree.write(path, encoding="utf-8")

def parse_xml(path):
    tree = et.parse(path)
    root = tree.getroot()
    dic={}
    if(root.attrib['tilemapservice']):
        dic['tilemap service'] = root.attrib['tilemapservice']
    title = root.find('title')
    if(title.text):
        dic['title'] = title.text
    cnt = 0
    ordermax = 0
    for tileset in root.iter('tileset'):
        if int(tileset.attrib['order']) > ordermax:
            ordermax = int(tileset.attrib['order'])
        cnt += 1
    dic['tileset count'] = cnt
    dic['tileset max'] = ordermax


    return dic

create_xml("./t.xml")
dic = parse_xml("./t.xml")
print(dic)



if __name__ == "__main__":
    create_xml("./created.xml")
    print(parse_xml("./created.xml"))