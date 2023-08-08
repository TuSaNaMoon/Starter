# Starter
This is my repository for my first study project.

A little explanation for part of the code.

# File Bot. The work with files .csvc(comma separated values) and modul chardet. 
''''rb' - Opens file read-only in binar mode. The reader function is used for reading. Let's open the file, create a reader object, and ask to print the contents of the file line by line. We will get an error that indicates that the data from the file we are trying to open has some kind of non-standard encoding.To open such a file, you need to specify the encoding in the encoding parameter - you can find it out using the special chardet module.
From the result, we copy the resulting encoding and paste it into the code in the encoding parameter.

    with open('movies.csv', mode='rb') as file:
        #for a in tqdm(list(file), desc='Loading…  '):
            data = file.read()
            result = chardet.detect(data)
            encoding = result['encoding']
    print(encoding)
    with open("movies.csv", encoding='utf-8') as file:
  


