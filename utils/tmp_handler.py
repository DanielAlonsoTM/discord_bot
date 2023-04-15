from os import listdir, path, remove, mkdir

dir = 'tmp'


def check_tmp_exist():
    try:
        if path.exists(dir):
            print('The path for temparary files already exists')
        else:
            print(f'Creating dir "{dir}"')
            mkdir(dir)
            
    except Exception as e:
        print(f'{e}')


def clean_tmp():
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
