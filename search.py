import re
import io


def line_conversion(in_line):

    start_ad = 'test_domain.ru'
    start_ln = 'exchange'
    in_line = re.sub(r':', '', in_line[:-2])
    in_line = re.sub(r'"', "'", in_line)
    x = in_line.lower().index('пароль') + 7

    if start_ad in in_line:
        login = in_line[in_line.index('MSK\\')+4:]
        login = login[:login.index("'")]
        return (login + ' ' + in_line[x:]).split()
    elif start_ln in in_line:
        return ('exchange ' + in_line[x:]).split()


def writing_to_result_a_file(names, founds_names):

    f = open('output.txt', 'w')
    f.write('----  НЕ НАЙДЕНЫ   ----\n\n')
    for name in names:
        if (founds_names.get(name, False) == False):
            f.write(name + '\n')

    f.write('\n\n')

    f.write('----  НАЙДЕНЫ   ----\n\n')
    for key, val in founds_names.items():
        f.write(key + ' ' + str(val) + '\n')
    f.close()


def main():

    with open("names.txt", encoding="utf-8-sig") as file_name:
        names = tuple([line.rstrip() for line in file_name])
    
    search_line = "В ресурсе"
    names_dict = {}
    with io.open("input.txt", encoding="utf-8") as password_file:
        for line in password_file:
            if search_line in line:
                for name in names:
                    if name in line:
                        try:
                            names_dict[name] += line_conversion(line)
                        except KeyError:
                            names_dict[name] = line_conversion(line)

    writing_to_result_a_file(names, names_dict)


if __name__ == "__main__":
    main()