# Testing techniques for Python applications

Advanced test techniques to test python apps

## Setup

1. Create hello.py test_hello.py requirements.txt Makefile 

2. Create a VE

```bash 
virtualenv ~/.testing-techniques
source ~/.testing-techniques/bin/activate
```
3. ``Makefile`` 

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint: 
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```

### How to debug?
    - print
    - PDB
    - testing


4. ``hello.py`` file

```python

def addThis(x, y):
    # import pdb;pdb.set_trace()
    print(f"This is x={x} and this is y={y}")
    print(f"the type of the first variable {type(x)}")
    print(f"the type of the second variable {type(y)}")

    try:
        result = x+y
    except TypeError:
        print("the wrong type passed")
        result = (int(x)+int(y))
    
    print(f"Here is the result {result}")
    return result

print (addThis("1",2))
print ("---"*15)
print (addThis(3,5))
```

5. ``test_hello.py`` file 

```python
from hello import addThis

assert addThis(4, 8) == 12
assert addThis("1",2) == 3
assert addThis(3,5) == 9        # gives a false error
```

6. Test it

```bash
make install

make test
```

finito

