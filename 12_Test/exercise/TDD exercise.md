# TDD Reverse-Engineering Exercise: Shopping Cart

## Problem Statement

The tests below are already written. **Read only the tests** and infer what class(es) and method(s) you need to implement so that all tests pass.

> Rule: do **not** modify the test code.

---

## Test Code (Python / pytest)

```python
# tdd_shopping_cart.py

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
```

---

## Your Task

Create `shopping_cart.py` and implement the `ShoppingCart` class with all necessary methods.

---

## Suggested Approach (Red → Green → Refactor)

1. **Red** — run the tests first; confirm everything fails
2. **Green** — make each test pass with the minimum code needed
3. **Refactor** — clean up the code while keeping all tests green

---

## Hints: Infer the API from the Tests

| Observed test behavior | Design decision to infer |
|---|---|
| `ShoppingCart()` takes no args | No constructor parameters |
| `add_item({"id": ..., "name": ..., "price": ..., "quantity": ...})` | Item is identified by `"id"` |
| `get_items()` returns a list; mutating it shouldn't affect the cart | Return a copy, not the internal reference |
| `apply_discount({"type": ...})` dispatches on `type` | Use `type` as a discriminator |
| `THRESHOLD` discount has an extra `"threshold"` key | Conditional logic; silently ignored when not met |
| Calling `apply_discount` twice keeps only the last one | Store at most one active discount |

---

## Reference Solution

<details>
<summary>Expand (try it yourself first)</summary>

```python
# shopping_cart.py

class ShoppingCart:
    def __init__(self):
        self._items: dict[str, dict] = {}
        self._discount: dict | None = None

    def add_item(self, item: dict) -> None:
        item_id = item["id"]
        if item_id in self._items:
            self._items[item_id]["quantity"] += item["quantity"]
        else:
            self._items[item_id] = dict(item)

    def remove_item(self, item_id: str) -> None:
        if item_id not in self._items:
            raise ValueError("Item not found")
        del self._items[item_id]

    def get_items(self) -> list[dict]:
        return [dict(item) for item in self._items.values()]

    def apply_discount(self, discount: dict) -> None:
        self._discount = discount

    def get_total(self) -> float:
        subtotal = sum(
            item["price"] * item["quantity"] for item in self._items.values()
        )

        if not self._discount:
            return subtotal

        discount_type = self._discount["type"]

        if discount_type == "PERCENTAGE":
            return subtotal * (1 - self._discount["value"] / 100)

        if discount_type == "FIXED":
            return max(0, subtotal - self._discount["value"])

        if discount_type == "THRESHOLD":
            if subtotal >= self._discount["threshold"]:
                return subtotal - self._discount["value"]
            return subtotal

        return subtotal
```

</details>

---

## Key Concepts Tested

| Concept | Where it appears |
|---|---|
| Encapsulation | `get_items()` returns a copy to prevent external mutation |
| Guard clause | `remove_item` raises early on invalid input |
| Type-based dispatch | `get_total()` branches on `discount["type"]` |
| Single responsibility | `apply_discount` only stores; `get_total` only calculates |
| Edge case handling | Total floored at 0; threshold discount silently skipped |
