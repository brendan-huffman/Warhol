def makeWpic():
  fname=pickAFile()
  pic=makePicture(fname)
  wPic=makeEmptyPicture(getwidth(pic),getHeight(pic))
  copyInto(pic,wPic,0,0)
  show(wPic)
  

def grayscale(pic)
  for col in range(getWidth(pic))
    for row in range(getHeight(pic))
      p=getPixel(pic,col,row)
      np=getPixel(npic,col,row)

def shrink(pic):
  newPic=makeEmptyPicture(getWidth(pic)/2, getHeight(pic)/2)
  for col in range(0,getWidth(pic),2):
  print getWidth(pic),getWidth(newPic),getHeight(pic),getHeight(newPic)
    for row in range(0,getHeight(pic),2):
      ps=getPixel(pic,col,row)
      pd=getPixel(newPic,col/2,row/2)
      setColor(pd,getColor(ps))
  return newPic