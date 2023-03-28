# Topic: Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Andrei Ceban FAF-211

## Theory
&ensp;&ensp;&ensp; Lexer and scanner are terms that are often used interchangeably in the field of computer science, but they refer to slightly different concepts. In general, a lexer (short for lexical analyzer) is a program that takes a stream of characters as input and breaks it up into a series of tokens, which are the basic building blocks of a programming language.

&ensp;&ensp;&ensp; The scanner is a component of the lexer that reads the input stream of characters and identifies the individual tokens. In some cases, the scanner and lexer may be separate programs or components of a larger program, but they are typically closely related and work together to parse the input.

&ensp;&ensp;&ensp; The process of tokenizing involves breaking up the input stream into distinct pieces that represent the various elements of a programming language, such as keywords, operators, identifiers, and literals. These tokens are then passed on to the next stage of the parsing process, where they are analyzed and interpreted.

&ensp;&ensp;&ensp; The lexer and scanner are critical components of any compiler or interpreter for a programming language. They play a key role in parsing the input code and generating an abstract syntax tree (AST) that can be used by the compiler or interpreter to generate executable code.

&ensp;&ensp;&ensp; The lexer and scannerare fundamental components of the parsing process in a programming language. The lexer takes an input stream of characters and breaks it up into a series of tokens, while the scanner is responsible for identifying the individual tokens in the input stream. Together, they provide the foundation for the compilation or interpretation of a programming language.

## Objectives:

- Understand what lexical analysis [1] is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.

## Implementation description
### check_deterministic
&ensp;&ensp;&ensp; This code checks whether the finite automaton represented by the object is deterministic or not. It does so by creating a transition map that maps the current state and input symbol to a set of next states. If any state in the automaton has multiple transitions for the same input symbol, then the automaton is non-deterministic and the method returns false. Otherwise, the automaton is deterministic and the method returns true. The method takes no arguments and returns a boolean value.

```python
    def get_tokens(self):
        tokens = []
        position = 0

        while position < len(self.input_text):
            for character, character_type in TOKENS:

                #to compile a regular expression pattern into a regex pattern object
                regex = re.compile(character)

                # Match the next token based on its regex pattern
                match = regex.match(self.input_text, position)

                #chech if exist any matches
                if match:
                    if character_type:
                        token = (match.group(), character_type)
                        print(token)
                        tokens.append(token)
                    break # put the element in the list and break to go to the next element
            if not match:
                # If we didn't match any token, raise an error
                raise Exception(f"Invalid token ")
            else:
                # If we found a divide operator token, add it to the list and move the position forward
                position = match.end()
        return tokens
```
This implementation defines seven regular expressions for matching numbers, left and right parentheses, and the addition, subtraction, multiplication, and division operators. The tokenize function takes in a string of input code and repeatedly matches the next token based on the regex patterns. When a token is found, it is added to the list of tokens along with its token type (e.g. NUMBER) and its value (e.g. 42). The function returns the list of tokens.


## Results
![Alt text](screenshots/lab2.png)
## Conclusions
&ensp;&ensp;&ensp; After doing this laboratory work,i understand that determinism in finite automata is an important
concept in computer science that refers to the ability of a machine to uniquely determine its next state
based on the current input and state. Deterministic finite automata (DFA) are particularly useful for pattern
recognition and language processing tasks, as they can efficiently recognize regular languages.

The process of converting a non-deterministic finite automaton (NDFA) to a DFA involves transforming the NDFA into a deterministic version of itself, where each input symbol leads to exactly one next state. This conversion is important for simplifying the machine and making it easier to analyze and
understand.

Also, using the Chomsky hierarchy which is a classification of formal languages into four categories
based on their complexity and the types of grammars that can generate them. These categories include regular languages, context-free languages, context-sensitive languages, and recursively enumerable languages.
Each category has its own set of rules and limitations, and understanding these categories can help in the
design and analysis of computational systems.

