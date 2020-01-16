# Author: Zihan Li
# Date: 2020/1/15
# Description:    a (rather primitive) online store simulator

import re

class InvalidCheckoutError(Exception):
    pass

class Product:
    # initialize the Product's id_code, title, description, price, and quantity_available
    def __init__(self, pid_code, title, description, price, quantity_available):
        self.pid_code = pid_code
        self.title = title
        self.description = description
        self.price = price
        self.quantity_available = quantity_available

    def get_id_code(self):
        return self.pid_code
    # get product's id code

    def get_title(self):
        return self.title
    # get product's title

    def get_description(self):
        return self.description
    # get product's description

    def get_price(self):
        return self.price
    # get product's price

    def get_quantity_available(self):
        return self.quantity_available
    # get product's quantity

    def decrease_quantity(self):
        self.quantity_available -= 1
    # decreases the quantity available


class Customer:
    # initialize Constructor's name, id and cart
    def __init__(self, customer_name, account_id, premium_member):
        self.customer_name = customer_name
        self.account_id = account_id
        self.premium_member = premium_member
        self.cart = []

    def get_name(self):
        return self.customer_name
    # get customer's name

    def get_account_ID(self):
        return self.account_id
    # get customer's id

    def get_cart(self):
        return self.cart
    # get customer's cart

    def is_premium_member(self):
        if self.premium_member:
            return True
        else:
            return False
    # check customer's premium membership

    def add_product_to_cart(self, pid_code):
        self.cart.append(pid_code)
    # add the product ID code to the Customer's cart

    def empty_cart(self):
        self.cart = []
    # empties the Customer's cart

class Store:
    # initialize inventory and member
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_product(self, product):
        self.inventory.append(product)
    # add a product to the inventory

    def add_member(self, customer):
        self.customers.append(customer)
    # add a customer to the members

    def get_product_from_ID(self, pid_code):
        for p in self.inventory:
            if pid_code == p.get_id_code():
                return p
        return None
    # returns the Product with the matching ID

    def get_member_from_ID(self, account_id):
        for c in self.customers:
            if c.get_account_ID() == account_id:
                return c
        return None
    # returns the Customer with the matching ID

    def product_search(self, key_w):
        id_code = []
        for p in self.inventory:
            if re.search(key_w, p.get_title()) or re.search(key_w, p.get_description()):
                id_code.append(p.get_id_code())
        return id_code.sort()
    # return a sorted list of ID codes for every product

    def add_product_to_member_cart(self, p_id, m_id):
        for product in self.inventory:
            if product.get_id_code() != p_id:
                print('product ID not found')
            else:
                for customer in self.customers:
                    if customer.get_account_ID() != m_id:
                        print('member ID not found')
                    if product.get_quantity_available() > 0:
                        customer.add_product_to_cart(product)
                        print('product added to cart')
                    else:
                        print('product out of stock')

    def check_out_member(self, m_id):
         totalcost = 0.00

         m_check = self.get_member_from_ID(m_id)

         if m_check is None:
             raise InvalidCheckoutError
         else:
             for product in m_check.cart:
                 if product.get_quantity_available() > 0:
                     product.decrease_quantity()
                     totalcost += product.get_price()
             if (m_check.is_premium_member()):
                 return totalcost
             else:
                 return (totalcost + (totalcost * 0.07))


### mainfunction
#def main():
#    try:
#        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
#        c1 = Customer("Yinsheng", "QWF", False)
#        myStore = Store()
#        myStore.add_product(p1)
#        myStore.add_member(c1)
#        myStore.add_product_to_member_cart("889", "QWF")
#       result = myStore.check_out_member("QWF")
#        print("Total = $" result)
#    except InvalidCheckoutError:
#        print("return the charge for the member's cart")
#main()

### StoreTester.py
# import unittest
# import Store
# class Storetest(unittest.TestCase):
#    def Store_test(self):
#        P = Store.Product(11, "Phone", "Smart phone", 450.00, 10)
#
#        self.assertEqual(P.get_title(), "Phone")
#        self.assertEqual(P.get_description(), "Smart phone")
#        self.assertEqual(P.get_price(), 450.00)
#
#        self.assertNotEqual(P.get_quantity(), 3)
#        self.assertIsNotNone(P)
