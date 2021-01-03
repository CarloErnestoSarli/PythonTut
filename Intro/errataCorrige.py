# added extension pyright for type checking in linter

# no need to use typing library for list or tuple declaration

# Static type list 

statList: list[int] = [1, 2, 4] 
statList2: list[str] = ['abc', 'gdf'] 

# static type tuple

statTuple: tuple[str, str] = ('a', 'b')
statTuple2: tuple[int, str] = (3, 'b')


# static type set
s1: set[str] = {"Paul"}

# s1.add(1) error

# static type dict
d1: dict[str, str] = {'a': 'a'}
d2: dict[str, int] = {'a': 2}