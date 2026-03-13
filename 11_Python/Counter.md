# Python `Counter`

`Counter` is a subclass of `dict` from `collections` that counts hashable objects.

```python
from collections import Counter
```

---

## Construction

```python
Counter([3, 3, 2])            # list      → Counter({3: 2, 2: 1})
Counter((3, 3, 2))            # tuple     → Counter({3: 2, 2: 1})
Counter(b for a, b in trust)  # generator → counts each b value
Counter("aabbcc")             # string    → Counter({'a': 2, 'b': 2, 'c': 2})
Counter({'a': 3, 'b': 1})     # dict      → Counter({'a': 3, 'b': 1})
Counter(a=3, b=1)             # kwargs    → Counter({'a': 3, 'b': 1})
```

---

## Common Operations

```python
c = Counter("aabbbc")

c['a']          # 2  — missing key returns 0, not KeyError
c['z']          # 0  ← unlike regular dict

c.most_common(2)         # [('b', 3), ('a', 2)]  — top n by count
c.most_common()          # all elements sorted by count desc

list(c.elements())       # ['a', 'a', 'b', 'b', 'b', 'c']  — repeats each key count times

c.total()                # 6  — sum of all counts (Python 3.10+)
sum(c.values())          # same, works on all versions
```

---

## Arithmetic

```python
a = Counter("aab")
b = Counter("abc")

a + b   # Counter({'a': 3, 'b': 2, 'c': 1})  — add counts
a - b   # Counter({'a': 1})                   — subtract, drop zero/negative
a & b   # Counter({'a': 1, 'b': 1})           — min of each count (intersection)
a | b   # Counter({'a': 2, 'b': 1, 'c': 1})  — max of each count (union)
```

---

## Update / Subtract

```python
c = Counter("aab")
c.update("bbc")     # adds counts   → Counter({'b': 3, 'a': 2, 'c': 1})
c.subtract("ab")    # subtracts     → can go negative, unlike -
```

`update` adds; `subtract` can produce zero or negative counts (kept in dict).
`a - b` drops keys with count ≤ 0.

---

## Common Patterns

**Check if two strings are anagrams**
```python
Counter("listen") == Counter("silent")  # True
```

**Sliding window — track character frequency**
```python
window = Counter(s[:k])
for i in range(k, len(s)):
    window[s[i]] += 1
    window[s[i - k]] -= 1
    if window[s[i - k]] == 0:
        del window[s[i - k]]
```

**Find elements appearing more than once**
```python
[x for x, cnt in Counter(nums).items() if cnt > 1]
```

**Top k frequent elements**
```python
Counter(nums).most_common(k)
```

---

## Notes

- Missing keys return `0` — safe to use without `.get()` or `defaultdict`
- `Counter` is a `dict` subclass — all dict methods work
- `most_common()` uses a heap internally: O(n log k) for top-k, O(n log n) for all
- Negative counts are allowed (e.g., after `subtract`) but ignored by `+`, `-`, `&`, `|`
