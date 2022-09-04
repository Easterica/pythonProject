def find_amount_color_of_egges_by_string(str):
    for i in range(0, len(str)):

        if str[i] > 'a' and str[i] < 'z' and (str[i - 1] == '@' or str[i - 1] == '#'):
            temp_color = str[i]
            i += 1

            while str[i] >= 'a' and str[i] <= 'z':
                temp_color += str[i]
                i += 1

            if str[i] == '@' or str[i] == '#':
                i += 1

                while str[i] < '0' or str[i] > '9':
                    i += 1

                if str[i - 1] != '/':
                    continue

                temp_number = str[i]
                i += 1

                while (str[i] >= '0' and str[i] <= '9'):
                    temp_number += str[i]
                    i += 1

                if str[i] != '/':
                    continue

                print("You found " + temp_number + ' ' + temp_color + " eggs!")


if __name__ == '__main__':
    str1 = input()

    find_amount_color_of_egges_by_string(str1)