import time


def data_search(in_line):
    in_line = in_line[:-2].replace(r':', '')
    in_line = in_line.replace(r"'", '"')
    in_line = in_line.replace(r",", "")
    in_line = in_line.split('"')
    
    name = in_line[3].strip()
    login = in_line[5]
    password = in_line[6].split()[1]
    return name, login, password


def save_to_file(data: dict):
    with open("names.txt", encoding="utf-8-sig") as file_with_names:
        names = tuple([name.strip() for name in file_with_names if name.strip()])
    
    not_found = []
    with open('output.txt', 'w', encoding="utf-8") as f:
        f.write('----   НАЙДЕНЫ   ----\n\n')
        for name in names:
            try:
                f.write(f"{name} [ {data[name]} ]\n")
            except KeyError:
                not_found.append(name)

        f.write('\n\n----   НЕ НАЙДЕНЫ   ----\n\n')
        for name in not_found:
            f.write(f"{name}\n")


def run_time_print(func):
    def wrapped():
        start_time = time.time()
        func()
        print(f"Время выполнения: {time.time() - start_time} секунд")
    return wrapped


@run_time_print
def main():
    search_line = "В ресурсе"
    passwords_dict = {}
    with open("input.txt", encoding="utf-8-sig") as password_file:
        for line in password_file:
            line = line.lstrip()
            if line.startswith(search_line):
                name, login, password = data_search(line)
                try:
                    passwords_dict[name] += (f' "{login}" "{password}"')
                except KeyError:
                    passwords_dict[name] = (f'"{login}" "{password}"')
    save_to_file(passwords_dict)


if __name__ == "__main__":
    main()