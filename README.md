# Bloon Programming Language

Bloon is a small object oriented programming language made as a project for Compiler Design class. Bloon was made using Python3 and ANTLR and its syntax takes inspiration from Python and C++.

# User's Manual

## Dependencies

Python 3 and ANTLR are required to run the Bloon language, please refer to the [ANTLR Quickstart Guide](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) to learn more about using ANTLR.

## How to run Bloon

After cloning the repository and accesing the `src` directory, install antlr4 for python3 using:

```
pip install antlr4-python3-runtime
```

Now, you can run `.bloon` programs the following way:

```
python BloonRun.py ../examples/testfile.bloon
```

## Supported types

This language supports `int`, `float`, `char`, `string` as primitive types.

## Variable declarations

Variable declarations are started with the keyword `vars`, and in a new line under this keyword, all variables should be specified with the following structure: `variableName` : `type` ;

Valid declaration of variables of all types:

```
vars 
  num : int;
  floatNum : float;
  letter : char;
  text : string;
```

Valid declaration of various variables of the same type:

```
vars 
  num, i, j : int;
```

## Array declarations

The declaration of an array is started with the keyword `vars`, and in a new line under this keyword, all arrays should be specified  with the following structure: `arrayName[size]` : `type` ;

Valid declaration of an array with one dimension:

```
vars 
  nums[4] : int;
```

Valid declaration of an array with two dimensions:

```
vars 
  nums[4,4] : float;
```

## Class and object declarations

The declaration of a class is started with the keyword `class` and the unique identifier of the class. Classes can have attributes and methods.

Valid declaration of a simple class:

```
class person {
    attributes:
        weight, height : float;
    methods:
        int meth getIMC() {
            return(this.weight / (this.height * this.height));
        }
};
```
Attribute declarations are started with the keyword `attributes`, and in a new line under this keyword, all variables should be specified with the following structure: `attributeName` : `type` ;

Valid declaration of an attribute:

```
attributes:
        weight, height : float;
```

Method declarations in a class are started with the keyword `methods`, and in a new line under this keyword, all variables should be specified with the following structure: `type meth methName(args) {}`

Valid declaration of a class method:

```
methods:
        int meth getIMC() {
            return(this.weight / (this.height * this.height));
        }
 ```
 
Object declarations should be specified with the following structure: `objectName : className`. Objects should be declared as variables after the keyword `vars`

Valid declaration of an object:

```
 studentName : student;
 ```
This would be an object of the class student.

Inheritance should be declared with the following structure:
`class childClassName <inherits parentClassName>` 

Valid inheritance declaration:

```
class student <inherits person> {
    attributes:
        name : string;
        age : int;
    methods:
        void meth printData() {
            this.name = "Martin";
            write("Name: ", this.name);
            write("Age: ", this.age);
        }
};

```
## Conditionals

Bloon supports conditional statements using the keywords `cond` and `else`.

Valid conditional statement:

```
cond (x < 5) then {
  write("x is less than 5");
}
 else {
  write("x is greater than 5");
}
```

## Loops

Bloon supports while statements using the keywords `while` and `do`. It expects a condition to evaluate and performs blocks of code considering the evaluation result.

Valid while statement:

```
while (i < 10) do {
        write(i);
        i += 1;
    }
```

Bloon supports for loop (floop) statements using the keywords `floop`, `to` and `do`. It expects two numerical values to create a range and perform blocks of code considering the specified range

Valid floop statement:

```
floop 1 to 3 do {
            write(j);
        }
```

## Methods

Bloon supports the use of method for modular programming. It is required to specify a method with the return type, followed by the keyword `meth` and parentheses with the arguments if there are any. Non void methods must include a return statement that returns the same type the method was declared as

```
int meth getIMC() {
            return(100 / (160 * 160));
        }
```

## More Examples

For aditional examples refer to the  `examples` directory in this repository

