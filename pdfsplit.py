#!/usr/bin/python
# -*- encoding: utf-8 -*-

from subprocess import call
import sys
import os
from CoreGraphics import *


def splitPDF(fname, folder=None):

    inputDoc = CGPDFDocumentCreateWithProvider(CGDataProviderCreateWithFilename(fname))
    maxPages = inputDoc.getNumberOfPages()

    baseFN = os.path.splitext(os.path.basename(fname))[0]
    pageRect = CGRectMake (0, 0, 612, 792)

    for pageNum in range(1, maxPages+1):
        outputFN = '%s-%d.pdf' % (baseFN, pageNum)
        if folder:
          outputFN = os.path.join(folder, outputFN)
        writeContext = CGPDFContextCreateWithFilename(outputFN, pageRect)

        mediaBox = inputDoc.getMediaBox(pageNum)
        writeContext.beginPage(mediaBox)
        writeContext.drawPDFDocument(mediaBox, inputDoc, pageNum)
        writeContext.endPage()


if len(sys.argv) < 2:
    print("")
    sys.exit(1)
elif len(sys.argv) == 3:
    splitPDF(sys.argv[1], sys.argv[2])
else:
    splitPDF(sys.argv[1])
