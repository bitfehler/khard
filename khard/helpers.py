# -*- coding: utf-8 -*-

import random, string

def pretty_print(table, justify = "L"):
    # get width for every column
    column_widths = [0] * table[0].__len__()
    offset = 3
    for row in table:
        for index, col in enumerate(row):
            width = len(str(col).decode("utf-8"))
            if width > column_widths[index]:
                column_widths[index] = width
    table_row_list = []
    for row in table:
        single_row_list = []
        for col_index, col in enumerate(row):
            if justify == "R": # justify right
                formated_column = str(col).decode("utf-8").rjust(column_widths[col_index] + offset)
            elif justify == "L": # justify left
                formated_column = str(col).decode("utf-8").ljust(column_widths[col_index] + offset)
            elif justify == "C": # justify center
                formated_column = str(col).decode("utf-8").center(column_widths[col_index] + offset)
            single_row_list.append(formated_column.encode("utf-8"))
        table_row_list.append(' '.join(single_row_list))
    return '\n'.join(table_row_list)


def get_random_uid():
    return ''.join([ random.choice(string.ascii_lowercase + string.digits) for _ in range(36) ])


def get_new_contact_template(addressbook_name):
    return """# Address book: %s
# if you want to cancel, exit without saving

# name components
Prefix     : 
First name : 
Additional : 
Last name  : 
Suffix     : 
Nickname   : 

# organisation, title and role
Organisation : 
Title        : 
Role         : 

# categories or tags
# format: category1, category2, ...
Categories : 

# phone numbers
# format:
#   Phone:
#       standard_type1 : number
#       standard_type2, standard_type3 : number
#       custom_type : number
#       ...: ...
# allowed types:
#   At least one of: bbs, car, cell, fax, home, isdn, msg, modem, pager, pcs, pref, video, voice, work
#   Alternatively you can use a single custom label (only letters). But maybe not all address book
#   clients will support that.
Phone :
    cell : 
    work : 

# email addresses
# format:
#   Email:
#       standard_type : address
#       custom_type   : address
#       ...: ...
# allowed types:
#   At least one of: home, internet, pref, uri, work, x400
#   Alternatively you can use a single custom label (only letters).
Email :
    home : 
    work : 

# post addresses
# format:
#   Address:
#       standard_type :
#           Street1  :
#           Code1    :
#           City1    :
#           Region1  :
#           Country1 :
#       ...:
# allowed types:
#   At least one of: home, pref, work
#   Alternatively you can use a single custom label (only letters).
Address :
    home :
        Street  : 
        Code    : 
        City    : 
        Region  : 
        Country : 

# instant messaging and social networks
Jabber  : 
Skype   : 
Twitter : 
Webpage : 

# birthday
# day.month.year or year.month.day
Birthday : 

# notes
# for multi-line notes use:
#   Note : |
#       line one
#       line two
Note : """ % addressbook_name

