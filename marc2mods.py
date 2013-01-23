#!/usr/bin/env python

import os
import sys
import libxml2
import libxslt
import requests
import argparse

def _make_arg_parser():
  parser = argparse.ArgumentParser(description="usage: marc2mods.py -u 'http://stylesheet.url' -i '/path/to/input/directory' -o '/path/to/output/directory")
  #parser.add_argument("-u", "--url", help="url to stylesheet")
  parser.add_argument("-i", "--inputDir", help="path to the input directory")
  parser.add_argument("-o", "--outputDir", help="path to the output directory")
  return parser

def marc2mods(inputDir):
  #r = requests.get(url)
  #stylesheet = r.text
  records = os.listdir(inputDir)

  for record in records:
    stylesheet = "MARC21slim2MODS3-4.xsl"
    styledoc = libxml2.parseFile(stylesheet)
    style = libxslt.parseStylesheetDoc(styledoc)
    doc = libxml2.parseFile((os.path.join(inputDir,record)))
    outputfile = (os.path.splitext(record)[0] + "-MODS.xml")
    result = style.applyStylesheet(doc, None)
    style.saveResultToFilename((os.path.join(outputDir,outputfile)), result, 0)
    style.freeStylesheet()
    doc.freeDoc()
    result.freeDoc()
    
if __name__ == '__main__':
  arg_parser = _make_arg_parser()
  args = arg_parser.parse_args()
  #if args.url:
  #  url = args.url
  if args.inputDir:
    inputDir = args.inputDir
  if args.outputDir:
    outputDir = args.outputDir

  rc = 0

  marc2mods(inputDir)

  sys.exit(rc)

