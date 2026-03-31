# Class Attribute vs Instance Attribute


class C:
    attr1 = 5  # class attribute (immutable int)

    def __init__(self):
        self.attr2 = 4  # instance attribute


class D:
    shared = []  # class attribute (mutable list)

    def __init__(self, name):
        self.name = name


def banner(title):
    print()
    print("===")
    print(title)


def print_state(obj1, obj2, note):
    print(note)
    print("C.attr1:", C.attr1, "| id(C.attr1):", id(C.attr1))
    print("obj1.attr1:", obj1.attr1, "| id(obj1.attr1):", id(obj1.attr1))
    print("obj2.attr1:", obj2.attr1, "| id(obj2.attr1):", id(obj2.attr1))
    print("obj1.__dict__:", obj1.__dict__)
    print("obj2.__dict__:", obj2.__dict__)
    print("C.__dict__['attr1']:", C.__dict__["attr1"], "| id(value):", id(C.__dict__["attr1"]))


def demo_immutable_class_attr():
    obj1 = C()
    obj2 = C()

    banner("Initial: both instances read class attr1")
    print_state(obj1, obj2, "No instance attr1 yet.")

    banner("Set class attribute: C.attr1 = 10")
    C.attr1 = 10
    print_state(obj1, obj2, "Both instances reflect new class value.")

    banner("Set instance attribute: obj1.attr1 = 99")
    obj1.attr1 = 99
    print_state(obj1, obj2, "obj1 now shadows class attr1; obj2 still uses class value.")

    banner("Set instance attribute: obj2.attr1 = 123")
    obj2.attr1 = 123
    print_state(obj1, obj2, "Now both instances have their own attr1.")

    banner("Delete obj1.attr1")
    del obj1.attr1
    print_state(obj1, obj2, "obj1 falls back to class attr1; obj2 keeps instance attr1.")

    banner("Delete obj2.attr1")
    del obj2.attr1
    print_state(obj1, obj2, "Both instances read from class attr1 again.")

    banner("Optional edge case: delete class attr1")
    del C.attr1
    try:
        print("obj1.attr1:", obj1.attr1)
    except AttributeError as e:
        print("obj1.attr1 raises:", repr(e))
    C.attr1 = 10  # restore for consistency
    print("restore C.attr1 ->", C.attr1)


def demo_mutable_class_attr():
    d1 = D("d1")
    d2 = D("d2")

    banner("Mutable class attr pitfall")
    print("initial D.shared:", D.shared, "| id(D.shared):", id(D.shared))
    print("d1.shared:", d1.shared, "| id(d1.shared):", id(d1.shared))
    print("d2.shared:", d2.shared, "| id(d2.shared):", id(d2.shared))

    banner("Mutate through instance: d1.shared.append('A')")
    d1.shared.append("A")
    print("D.shared:", D.shared)
    print("d1.shared:", d1.shared)
    print("d2.shared:", d2.shared)
    print("All changed because list object is shared at class level.")

    banner("Rebind through instance: d1.shared = ['X']")
    d1.shared = ["X"]
    print("D.shared:", D.shared, "| id(D.shared):", id(D.shared))
    print("d1.shared:", d1.shared, "| id(d1.shared):", id(d1.shared))
    print("d2.shared:", d2.shared, "| id(d2.shared):", id(d2.shared))
    print("d1 now has an instance attribute named shared; class list unchanged.")


def main():
    demo_immutable_class_attr()
    demo_mutable_class_attr()


if __name__ == "__main__":
    main()
