import docx

doc = docx.Document('text.docx')


def GetNumPar(array):
    for items in range(len(array)):
        items+=1
    if items > 0:
        items-=1
    if items < 0:
        items -= 1
    return items

def GetRuns(x):
    for run in range(len(doc.paragraphs[x].runs)):
        run+=1
    return run
        


print(f'Number of Paragraphs: {GetNumPar(doc.paragraphs)} \n Number of Runs: {GetRuns(GetNumPar(doc.paragraphs))}')
numofp = GetNumPar(doc.paragraphs)
numofr = None
if numofp <=1:
    numofp+=1

for par in range(0,numofp):
    numofr = GetRuns(par)
    for r in range(0,numofr):
        print(f"{par}'s runs: {doc.paragraphs[par].runs[r].text}")
  


