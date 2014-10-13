def setpicandcanvas():
  file=pickAFile()
  pic=makePicture(file)
  w=getWidth(pic)
  h=getHeight(pic)
  bigpic=makeEmptyPicture(w*2,h*2)

def makegraypic():
  graypic=duplicatePicture(pic)
  for px in getPixels(graypic):
    newRed=getRed(px)*0.299
    newGreen=getGreen(px)*)0.587
    newBlue=getBlue(px)*0.114
    agg=newRed+newGreen+newBlue
    setColor(px,makeColor(agg, agg, agg))
    return graypic

def makecolorswappic():
  colorswappic=duplicatePicture(pic)
  for px in getPixels(colorswappic):
    R=getRed(px)
    G=getGreen(px)
    B=getBlue(px)
      setColor(px,makeColor(B, R, G))
    return colorswappic

def makenegpic():
  negpic=duplicatePicture(pic)
  for px in getPixels(negpic):
    R=getRed(px)
    G=getGreen(px)
    B=getBlue(px)
    negColor=makeColor(255-R, 255-G, 255-B)
    setColor=(px, negColor)
    return negpic


def copyfunc():
  copyInto(pic, bigpic, 0, 0)
  copyInto(graypic, bigpic, w, 0)
  copyInto(colorswappic, bigpic, 0, h)
  copyInto(negpic, bigpic, w, h)
  