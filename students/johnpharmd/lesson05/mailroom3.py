#!/usr/bin/env python3
import datetime

# Data
donors_amts = {'Gates': {'title': 'Mr.', 'donations': 150000,
                         'num_of_donations': 3},
               'Brin': {'title': 'Mr.', 'donations': 150000,
                        'num_of_donations': 3},
               'Cerf': {'title': 'Mr.', 'donations': 50000,
                        'num_of_donations': 2},
               'Musk': {'title': 'Mr.', 'donations': 100000,
                        'num_of_donations': 1},
               'Berners-Lee': {'title': 'Mr.', 'donations':
                               50000, 'num_of_donations': 2},
               'Wojcicki': {'title': 'Ms.', 'donations': 125000,
                            'num_of_donations': 1},
               'Avey': {'title': 'Ms.', 'donations': 200000,
                        'num_of_donations': 2}}


# Processing
def send_ty():
    # global donors_amts
    new_response = 0
    title = ''
    donor_dict = {'title': '', 'last_name': '', 'donation': 0}
    print()
    response = input('Enter full last name of Donor,'
                     + '\n"list" for List of Donors'
                     + ',\nor "e" to Exit back to Main Menu: ')
    print()
    try:
        if response == 'e':
            program_run()
        # for char in response:
        #     if char.isdigit():
        #         int(char) / 0
        else:
            [int(char)/0 for char in response if char.isdigit()]
    except ZeroDivisionError:
        print('Use English letters only please.\n')
        try:
            response = input('Enter full last name of Donor,'
                             + '\n"list" for List of Donors'
                             + ',\nor "e" to Exit back to Main Menu: ')
            # for char in response:
            #     if char.isdigit():
            #         int(char) / 0
            [int(char)/0 for char in response if char.isdigit()]
        except ZeroDivisionError:
            print('That is not a valid input. Closing program.')
            return
    else:
        if response == 'list':
            for donor in donors_amts:
                print(donor)
            print()
            send_ty()
        else:
            response = response.capitalize()
            if response in donors_amts:
                print('Donor found:', response)
                new_response = input('Enter a Donation amount' +
                                     ' (in USD): ')
                try:
                    new_response = int(new_response)
                except ValueError:
                    print('\nEnter a numeric value.')
                    new_response = input('Enter a Donation amount' +
                                         ' (in USD): ')
                    try:
                        new_response = int(new_response)
                    except ValueError:
                        print('That is not a valid input. Closing program.')
                        return
                else:
                    # new_response = int(new_response)
                    donors_amts[response]['donations'] += new_response
                    donors_amts[response]['num_of_donations'] += 1
                    print('Added to', response, '\'s Donations:',
                          new_response, '\n')
                send_ty()
            elif response not in donors_amts:
                # new function?: add_donor()?
                title = input('Title: "Ms." or "Mr."?: ')
                try:
                    [int(char)/0 for char in title if char.isdigit()]
                    # if title != 'Ms.' or 'Mr.':
                    # if title[0] != 'M':
                    #     print(n)  # triggers a NameError
                    # elif title[1] != 's' or title[1] != 'r':
                    #     pass
                    # elif len(title) > 3:
                    #     pass
                except ZeroDivisionError:
                    print('Choose a title (no digits, please).\n')
                except NameError:
                    print('Choose a title ("Ms." or "Mr.").\n')
                # finally:
                else:
                    try:
                        # title = input('Title: "Ms." or "Mr."?: ')
                        # if title != 'Ms.' or 'Mr.':
                        #     print('Invalid input. Closing program.')
                        #     return
                        new_response = input('Enter a Donation amount' +
                                             ' (in USD): ')
                        try:
                            new_response = int(new_response)
                        except ValueError:
                            print('Numeric value only, please.')
                            new_response = input('Enter a Donation amount' +
                                                 ' (in USD): ')
                            try:
                                new_response = int(new_response)
                            except ValueError:
                                print('That is not a valid input.'
                                      + 'Closing program.')
                                return
                        else:
                            # new_response = int(new_response)
                            print('Added to list of Donors:', title,
                                  response, new_response)
                            # add comprehension(s) here?
                            donors_amts[response] = {'title': title,
                                                     'donations':
                                                     new_response,
                                                     'num_of_donations': 1}
                    finally:
                        title = donors_amts[response]['title']
                        title = title.strip('\'')
                        donor_dict = {'title': title,
                                      'last_name': response,
                                      'donation': new_response}
                        # if format string is separated, it breaks so that
                        # title and last_name are not formatted
                        print('Dear {title} {last_name},'.format(**donor_dict)
                              + ' Thank you for your generous donation in the'
                              + ' amount'
                              + ' of {donation} USD.'.format(**donor_dict))
                        print()
    program_run()
    # lines 33-135 are written for this program
    # lines 138-184 were original code from mailroom2.py
    # if response.isalpha():
    #     if response == 'list':
    #         print('Here is the list of Donors: ')
    #         for donor in donors_amts:
    #             print(donor)
    #         print()
    #     else:
    #         response = response.capitalize()
    #         if response in donors_amts:
    #             print('Donor found:', response)
    #             new_response = input('Enter a Donation amount' +
    #                                  ' (in USD): ')
    #             # add try-except catch block(s)
    #             if not new_response.isnumeric():
    #                 send_ty()
    #             else:
    #                 new_response = int(new_response)
    #                 # add comprehension(s) here?
    #                 donors_amts[response][1] += new_response
    #                 donors_amts[response][2] += 1
    #                 print('Added to', response, '\'s Donations:',
    #                       new_response, '\n')
    #         elif response not in donors_amts:
    #             title = input('Title: "Ms." or "Mr."?: ')
    #             new_response = input('Enter a Donation amount' +
    #                                  ' (in USD): ')
    #             # add try-except catch block here
    #             if not new_response.isnumeric():
    #                 send_ty()
    #             else:
    #                 new_response = int(new_response)
    #                 print('Added to list of Donors:', title,
    #                       response, new_response)
    #                 # add comprehension(s) here?
    #                 donors_amts[response] = ([(title, ), new_response, 1])
    #         title = str(donors_amts.get(response)[0])
    #         title = title.strip('(').strip(')').strip(',')
    #         title = title.strip('\'')
    #         donor_dict = {'title': title,
    #                       'last_name': response, 'donation': new_response}
    #         # separating format string breaks it so that title and
    #         # last_name are not formatted
    #         print('Dear {title} {last_name},'.format(**donor_dict)
    #               + ' Thank you for your generous donation in the'
    #               + ' amount of {donation} USD.'.format(**donor_dict))
    #         print()
    # program_run()


def get_report():
    print()
    psv = ['Donor Name', '| Total Given', '| Num Gifts',
           '| Average Gift']
    print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
          psv[2], psv[3]))
    for i in range(55):
        print('-', end='')
    print()
    # add comprehension here?
    for donor in donors_amts:
        d1 = donors_amts[donor]['donations']
        d2 = donors_amts[donor]['num_of_donations']
        print('{:<15}{}{:>10}{:>12}{}{:>11}'.format(donor, '  $',
              d1, d2, '  $', d1 // d2))
    print()
    program_run()


def send_letters():
    # global donors_amts
    d_a = donors_amts
    title = ''
    # Natasha recommended datetime.datetime.now().strftime('%Y%m%d')
    now = datetime.datetime.now()
    for donor in d_a:
        # title = str(d_a.get(donor)['title'])
        title = d_a[donor]['title'].strip('\'')
        with open(donor + datetime.datetime.now().strftime('%Y%m%d')
                  + '.txt', 'w') as of:
            donor_dict = {'title': title,
                          'last_name': donor,
                          'donations': d_a[donor]['donations']}
            of.write(
                'Dear {title} {last_name},\n'.format(**donor_dict)
                + 'Thank you for your generous previous giving'
                + ' in the amount of {donations} USD.'.format(**donor_dict))
            of.write('\nAttached is our most recent independent,'
                     + ' third party audit.\n')
            of.write('\nWe hope you agree that we have been good'
                     + ' stewards of our donors\' funds,\nand that'
                     + ' you will consider donating'
                     + ' again to our project.\n')
            of.write('\nBest wishes for continued success,')
            of.write('\n[Signature]')
    print('A letter was generated, just now, for each of the donors in db.\n')
    program_run()


def quit_program():
    print('Program execution completed.')
    return


def program_run():
    print('Main Menu:')
    response = input('Choose from the following:\n"1" - Send a "Thank You",'
                     + '\n"2" - Create a Report,'
                     + '\n"3" - Send Letters to All Donors, or\n"q" to Quit: ')
    menu_dict = {'1': send_ty, '2': get_report,
                 '3': send_letters, 'q': quit_program}
    try:
        menu_dict.get(response)()
    except TypeError:
        print('\nThat selection is invalid. Please try again.')
        try:
            response = input('Choose "1", "2", "3", or "q": ')
            menu_dict.get(response)()
        except TypeError:
            print('That is not an option. Closing program.')
            return


# I/O
if __name__ == '__main__':
    program_run()

else:
    print('This module is not intended to be imported.')