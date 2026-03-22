"""
TDD Reverse-Engineering Exercise: Shopping Cart
================================================
Read only the tests below, infer what to implement, and make all tests pass.

Run:
    pytest test_shopping_cart.py -v
"""

import pytest
from shopping_cart import ShoppingCart


class TestShoppingCartBasic:
    def setup_method(self):
        self.cart = ShoppingCart()

    def test_initial_state_is_empty(self):
        assert self.cart.get_items() == []
        assert self.cart.get_total() == 0

    def test_add_item_reflects_in_list_and_total(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 30, "quantity": 2})
        assert len(self.cart.get_items()) == 1
        assert self.cart.get_total() == 60

    def test_adding_same_item_accumulates_quantity(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 30, "quantity": 2})
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 30, "quantity": 3})
        assert len(self.cart.get_items()) == 1
        assert self.cart.get_items()[0]["quantity"] == 5
        assert self.cart.get_total() == 150

    def test_remove_item(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 30, "quantity": 2})
        self.cart.remove_item("A1")
        assert len(self.cart.get_items()) == 0

    def test_remove_nonexistent_item_raises(self):
        with pytest.raises(ValueError, match="Item not found"):
            self.cart.remove_item("NONE")


class TestShoppingCartDiscount:
    def setup_method(self):
        self.cart = ShoppingCart()

    def test_percentage_discount(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 100, "quantity": 1})
        self.cart.apply_discount({"type": "PERCENTAGE", "value": 10})
        assert self.cart.get_total() == 90

    def test_fixed_discount(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 100, "quantity": 1})
        self.cart.apply_discount({"type": "FIXED", "value": 20})
        assert self.cart.get_total() == 80

    def test_fixed_discount_cannot_go_below_zero(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 50, "quantity": 1})
        self.cart.apply_discount({"type": "FIXED", "value": 100})
        assert self.cart.get_total() == 0

    def test_last_discount_wins(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 100, "quantity": 1})
        self.cart.apply_discount({"type": "PERCENTAGE", "value": 10})
        self.cart.apply_discount({"type": "PERCENTAGE", "value": 20})  # overrides previous
        assert self.cart.get_total() == 80


class TestShoppingCartThresholdDiscount:
    def setup_method(self):
        self.cart = ShoppingCart()

    def test_applies_discount_when_total_meets_threshold(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 500, "quantity": 1})
        self.cart.apply_discount({"type": "THRESHOLD", "value": 50, "threshold": 300})
        assert self.cart.get_total() == 450

    def test_does_not_apply_discount_when_below_threshold(self):
        self.cart.add_item({"id": "A1", "name": "Apple", "price": 200, "quantity": 1})
        self.cart.apply_discount({"type": "THRESHOLD", "value": 50, "threshold": 300})
        assert self.cart.get_total() == 200
