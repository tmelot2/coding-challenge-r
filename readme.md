# Challenge Calculator

A command line calculator that supports add operations. Requires Python 3.

## How to use

Run with Python & provide an input string. Example:

```bash
$ python3 app.py 1,2,3
```

Output:
```bash
6
```

## String format

- Input should be comma delimited list of positive integers, negative numbers are invalid.
	- Can optionally use newline character `\n` as a delimiter.
	- On my MacOS system, run it using this syntax:
	```bash
	$ python3 app.py $'1\n2,3'
	```
- Invalid, empty, or missing numbers default to `0`.


## Tests

Run tests with:

```bash
$ python3 test.py
```

There might be debug output that looks like errors. That's the testing of error conditions. As long as it says "OK" at the end of the test run, it's good.