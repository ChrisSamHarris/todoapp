contents = ['all carrots are to be sliced longitudinally',
            'the carrots were reportedly sliced',
            'the slicing process was well presented']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# zipping the contents of two lists together 
for content, filename in zip(contents, filenames):
    file = open(f"/Users/christopher.harris/Development/Python/MegaCourse/App1/BonusDir/bonus7files/{filename}", "w")
    file.write(content)
