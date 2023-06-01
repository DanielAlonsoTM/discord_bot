from os import listdir, path, remove, mkdir

dir_tmp = 'tmp'
dir_resources = 'resources'
config_file_name = 'app-config.properties'


def check_directories_exist():
    try:
        # Check for tmp folder
        if path.exists(dir_tmp):
            print('The path for temporary files already exists')
        else:
            print(f'Creating dir "{dir_tmp}"')
            mkdir(dir_tmp)

        # Check for resources folder
        if path.exists(dir_resources):
            print('The path for resources already exists')

            # Check for config file
            check_config_file()

        else:
            print(f'Creating dir "{dir_resources}"')
            mkdir(dir_resources)

            # Check for config file
            check_config_file()

    except Exception as e:
        print(f'{e}')


def clean_tmp():
    files = listdir(dir_tmp)

    # Filter for only files
    files = [file for file in files if path.isfile(dir_tmp + '/' + file)]

    print(f'{files}')

    if len(files) > 3:
        for file in files:
            try:
                remove(dir_tmp + '/' + file)
                print(f'File: {file} removed')

            except Exception as e:
                print(f'{e}')


def check_config_file():
    if path.isfile(f'{dir_resources}/{config_file_name}'):
        print('The file already exists')
    else:
        print(f'Creating file "{config_file_name}"')

        config_file = open(f'{dir_resources}/{config_file_name}', 'w')
        config_file.write('TOKEN=')
