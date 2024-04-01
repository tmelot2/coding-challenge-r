# Challenge Calculator

A command line calculator that supports add operations. Requires Python 3.

Developed & tested with Python 3.11.7.

## Requirements Background

A coding challenge to write a basic command line calculator with a specific input format (see below).

Requirements are incrementally modified to simulate real-world design changes. Each commit represents the changing design (plus cleanup & bug fixes).

## How to use

Run with Python & provide an input string. Example:

```bash
$ python3 app.py 1,2,3
```

Output:
```bash
6
```

## Input Format

- Input should be comma delimited list of positive integers, negative numbers will cause an error.
	- Can optionally use newline character `\n` as a delimiter.
	- Can optionally use a 1-character custom delimiter. Format: `//{delimiter}\n{numbers}`
	- Can optionally use a multi-character custom delimiter. Format: `//[{delimiter}]\n{numbers}`
	- Can optionally use multiple delimiters. Format: `//[{delimiter1}][{delimiter2}]\n{numbers}`
	- On my computer running MacOS Ventura, zsh is the shell. Use newlines with this syntax:
	```bash
	$ python3 app.py $'1\n2,3'
	```
- Invalid or empty numbers default to `0`.


## Tests

Run tests with:

```bash
$ python3 test.py
```

There might be debug output that looks like errors. That's the testing of error conditions. As long as it says "OK" at the end of the test run, it's good.