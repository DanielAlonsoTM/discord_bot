from os import listdir, path, remove


def clean_tmp():
    dir = 'tmp'
    files = listdir(dir)

    # Filter for only files
    files = [file for file in files if path.isfile(dir + '/' + file)]

    print(f'{files}')

    if len(files) > 3:
        for file in files:
            try: 
                remove(dir + '/' + file)
                
                print(f'File: {file} removed')
            except Exception as e:
                print(f'{e}')
