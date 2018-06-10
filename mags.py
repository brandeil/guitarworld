import csv

artists=[]

with open('mags.csv') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        artistname = row[0]
        song = row[1]
        magazine = row[2]
        publishDate = row[3]
        filetype = row[4]
        
        if (artistname not in artists) and (filetype == "Transcription"):
            artists.append(artistname)

print ("All artists:")
print(artists)