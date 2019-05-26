import fileinput


def get_number(numeric_bullet, number_of_astr):
    """Creates list for numeric bullet lines"""
    position = number_of_astr - 1
    try:
        numeric_bullet[position] += 1
        numeric_bullet = numeric_bullet[:position+1]
    except IndexError:
        numeric_bullet.append(1)
    return numeric_bullet


def fold_print(block):
    """Prints indention folding style"""
    signs = {True: "+", False: "-", "Blank": ""}
    block[-1]["switch"] = False
    prev_flag_switch = False
    prev_number_of_dots = block[-1]["number_of_dots"]
    for line in block[-2::-1]:
        if line["number_of_dots"] == 0:
            line["number_of_dots"] = prev_number_of_dots + 1
            line["switch"] = "Blank"
            continue
        elif line["number_of_dots"] < prev_number_of_dots and prev_flag_switch is False:
            line["switch"] = True
        elif line["number_of_dots"] == prev_number_of_dots and prev_flag_switch is False:
            line["switch"] = False
        elif line["number_of_dots"] == prev_number_of_dots and prev_flag_switch is True:
            line["switch"] = False
        elif line["number_of_dots"] < prev_number_of_dots and prev_flag_switch is True:
            line["switch"] = True
        prev_number_of_dots = line["number_of_dots"]
        prev_flag_switch = line["switch"]

    for line in block:
        print("{}{}{}".format(line['number_of_dots'] * " ",
                              signs[line['switch']],
                              line['line']), end="")


def chunk_print(chunk, numeric_bullet):
    """Decorate and print text chunks , based on *"""
    block = []
    bullet_line = chunk[0]
    number_of_astric = len(bullet_line) - len(bullet_line.lstrip("*"))
    numeric_bullet = get_number(numeric_bullet, number_of_astric)
    print(".".join([str(i) for i in numeric_bullet]), bullet_line.strip("*"), end="")
    for line in chunk[1:]:
        number_of_dots = len(line) - len(line.lstrip("."))
        block.append({"number_of_dots": number_of_dots, "line": line.lstrip(".")})
    fold_print(block)


if __name__ == "__main__":
    chunk = []
    numeric_bullet = [0]
    for line in fileinput.input():
        #  Loops over input and create chunks of text on basis of appearance of *
        if line.startswith("*") and not fileinput.isfirstline():
            chunk_print(chunk, numeric_bullet)  # Process and prints text chunk as per requirement.
            chunk = list()
            chunk.append(line)
        elif line.strip():
            chunk.append(line)
    else:
        chunk_print(chunk, numeric_bullet)  # Prints last chunk in file
