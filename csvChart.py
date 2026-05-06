import csv
from sys import argv as sys_argv
from matplotlib import pyplot as plt
from colorama import Fore, init as color_init


def main():
    color_init() # Init colors

    # Get system arguments default: (None, None)
    file_args = get_file_names(sys_argv[1:])

    # File path of both archives
    file_path_year = file_args[0]
    file_path_month = file_args[1]

    # Get label and size of pyplot values
    year_labels, year_sizes = split_values( get_csv_file( file_path_year ) )
    month_labels, month_sizes = split_values( get_csv_file( file_path_month ) )

    fig, (pie, plot) = plt.subplots(1, 2) # Add two charts in a windows

    generate_pie(pie, year_labels, year_sizes, f'Most ordered in {file_path_year}') # Generate a pie plot (pizza chart)
    generate_plot(plot, month_labels, month_sizes, f'Max and Mix order of {file_path_month}')

    fig.autofmt_xdate() # Automatic title chart adjust
    show_chart() # Show date in window

def get_file_names(names): return (names + [None, None])[:2]

def split_values(data):
    labels = []
    size_nums = []

    field = data['fieldnames']
    for row in data['values']:
        labels.append( row.get( field[0] ) )
        size_nums.append( row.get( field[1] ) )

    return labels, size_nums

def warning_print(*args, sep=' ', end='\n', file=None):
    print(Fore.RED, '[ERROR] - ',end='', sep='')
    print(*args, sep=sep, file=file, end='')
    print(Fore.RESET, end=end, sep='')

def open_csv_file(path_file:str):
    with open(f'{path_file}.csv', 'r', newline='') as file:
        ## Converted the file words in csv rules
        csv_dict = csv.DictReader(file)
        data = {
            "fieldnames": csv_dict.fieldnames,
            "values": list(csv_dict)
        }
        return data

def get_csv_file(path = None):
    ## A while command for always quest the player about the right path
    while True:
        ## Check the var "file" is a null, if true, question the user the right file path
        if not path: path = input("Insert the file csv path: ").strip()

        ## Catch error in open a csv folder (File not exist error and a default csv error)
        try: return open_csv_file(path)
        except FileNotFoundError: warning_print('File not found')
        except csv.Error: warning_print('This file is not a csv')

        path = None
    return None

def generate_pie(plot, labels, sizes, title):
    plot.pie(sizes, labels=labels, autopct='%1.1f')
    plot.set_title(title)

def generate_plot(plot, labels, sizes, title):
    plot.plot(labels, sizes, 'o-')
    plot.set_title(title)


def show_chart():
    plt.tight_layout()
    plt.show()

if __name__ == '__main__': main()
