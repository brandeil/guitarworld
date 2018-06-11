import csv

transcriptions=[]

with open('mags.csv') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        artistname = row[0]
        song = row[1]
        magazine = row[2]
        publishDate = row[3]
        filetype = row[4]
        
        if filetype == "Transcription":
            transcriptions.append("{0}-{1}-{2}-{3}".format(artistname,song,magazine,publishDate))

for x in transcriptions:
    print(x)
