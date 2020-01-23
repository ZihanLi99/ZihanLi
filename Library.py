# Author: Zihan Li
# Date: 2020/1/21
# Description: a Library simulator involving multiple classes： LibraryItem, Patron and Library classes, and the three classes that inherit from LibraryItem

ON_SHELF = 'ON_SHELF'
ON_HOLD_SHELF = 'ON_HOLD_SHELF'
CHECKED_OUT = 'CHECKED_OUT'

class LibraryItem:

    def __init__(self, id_code, title):
        # a unique identifier for a LibraryItem
        self._id_code = id_code
        # title of this item
        self._title = title
        # check out by
        self._checked_out_by = None
        # request by
        self._requested_by = None
        # location of this item
        self._location = 'ON_SHELF'
        # check out date of this item
        self._date_checked_out = None

    def get_id_code(self):
        return self._id_code

    def get_title(self):
        return self._title

    def get_location(self):
        return self._location

    def get_checked_out_by(self):
        return self._checked_out_by

    def get_requested_by(self):
        return self._requested_by

    def get_date_checked_out(self):
        return self._date_checked_out

    def set_id_code(self, value):
        self._id_code = value

    def set_title(self, value):
        self._title = value

    def set_checked_out_by(self, value):
        self._checked_out_by = value

    def set_requested_by(self, value):
        self._requested_by = value

    def set_location(self, value):
        self._location = value

    def set_date_checked_out(self, value):
        self._date_checked_out = value

class Book(LibraryItem):

    def __init__(self, id_code, title, author):
        super().__init__(id_code, title)
        # author of this book
        self._author = author

    def get_check_out_length(self):
        # max check out days
        return 21

    def get_author(self):
        return self._author

    def set_author(self, value):
        self._author = value

class Album(LibraryItem):

    def __init__(self, id_code, title, artist):
        super().__init__(id_code, title)
        # artist of this item
        self._artist = artist

    def get_check_out_length(self):
        # max check out days
        return 14

    def get_artist(self):
        return self._artist

    def set_artist(self, value):
        self._artist = value

class Movie(LibraryItem):

    def __init__(self, id_code, title, director):
        super().__init__(id_code, title)
        # director of this movie
        self._director = director

    def get_check_out_length(self):
        # max check out days
        return 7

    # getters and setters
    def get_director(self):
        return self._director

    def set_director(self, value):
        self._director = value


class Patron:

    def __init__(self, id_num, name):
        super().__init__()
        # id of this patron
        self._id_num = id_num
        # name of this patron
        self._name = name
        # check out items
        self._checked_out_items = []
        # total fine amount of this patron
        self._fine_amount = 0

    def get_id_num(self):
        return self._id_num

    def get_name(self):
        return self._name

    def get_check_out_items(self):
        return self._checked_out_items

    def get_fine_amount(self):
        return self._fine_amount

    def set_id_num(self, value):
        self._id_num = value

    def set_name(self, value):
        self._name = value

    def set_checked_out_items(self, value):
        self._checked_out_items = value

    def set_fine_amount(self, value):
        self._fine_amount = value

    def add_library_item(self, library_item):
        # Add a item to library
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        # remove a item from library
        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        self._fine_amount += amount


class Library:

    def __init__(self):
        super().__init__()
        # item in this library
        self._holdings = []
        # patrons of this library
        self._members = []
        # current date
        self._current_date = 0

    def add_library_item(self, library_item):
        # add item
        self._holdings.append(library_item)

    def add_patron(self, patron):
        # add a patron
        self._members.append(patron)

    def get_library_item(self, id):
        # get an item by id
        for item in self._holdings:
            if item.get_id_code() == id:
                return item
        return None

    def get_patron(self, id):
        for item in self._members:
            if item.get_id_num() == id:
                return item
        return None

    def check_out_library_item(self, patron_id, item_id):
        # check out item from library
        patron = self.get_patron(patron_id)
        item = self.get_library_item(item_id)
        # if patron not found
        if patron is None:
            return "patron not found"

        # if item not found
        if item is None:
            return "item not found"

        if item.get_location() == CHECKED_OUT:
            return "item already checked out"

        if item.get_location() == ON_HOLD_SHELF:
            return "item on hold by other patron"

        # update item status
        item.set_checked_out_by(patron)
        item.set_date_checked_out(self._current_date)
        item.set_location(CHECKED_OUT)
        # add to patron's check out
        patron.get_check_out_items().append(item)
        return "check out successful"

    def return_library_item(self, item_id):
        item = self.get_library_item(item_id)
        # if item not found
        if item is None:
            return "item not found"

        # if item is already on shelf
        if item.get_location() == ON_SHELF:
            return "item already in library"

        # remove this item from patron's check out list
        for patron in self._members:
            if item in patron.get_check_out_items():
                patron.get_check_out_items().remove(item)
                break

        if item.get_requested_by() is not None:
            # if item is requested by some one, change status
            item.set_location(ON_HOLD_SHELF)
        else:
            # if item is not requested by some one, change status
            item.set_location(ON_SHELF)
        # update status
        item.set_checked_out_by(None)
        return "return successful"

    def request_library_item(self, patron_id, item_id):
        patron = self.get_patron(patron_id)
        item = self.get_library_item(item_id)
        # if patron not found
        if patron is None:
            return "patron not found"

        # if item not found
        if item is None:
            return "item not found"

        # if item is requested
        if item.get_requested_by() is not None:
            return "item already on hold"

        # update status
        item.set_requested_by(patron)
        if item.get_location() == ON_SHELF:
            item.set_location(ON_HOLD_SHELF)

        return "request successful"

    def pay_fine(self, patron_id, amount):
        patron = self.get_patron(patron_id)
        # if patron not found
        if patron is None:
            return "patron not found"

        # update fine
        patron.amend_fine(-amount)
        return "payment successful"

    def increment_current_date(self):
        self._current_date += 1
        # foreach patron in this library
        for patron in self._members:
            for libraryItem in patron.get_check_out_items():
                date = libraryItem.get_date_checked_out()
                # find all the expired items
                if self._current_date - date > libraryItem.get_check_out_length():
                    # pay $0.1 for each day
                    patron.amend_fine(0.1)
