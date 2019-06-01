def html_replacement(the_string):
    com_dict = {"<": "&lt;", ">": "&gt;", "&": "&amp"}
    result = []
    for item in the_string:
        if item in com_dict:
            result.append(com_dict[item])
        else:
            result.append(item)
    return ''.join(result)

a_string = "Hello <World> Goodbye & World"
print(html_replacement(a_string))
