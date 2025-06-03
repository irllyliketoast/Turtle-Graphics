# Turtle Graphics

This project creates a simple **screensaver-style animation** using Python's built-in `turtle` graphics library. Designed for beginners in **object-oriented programming (OOP)**, the program combines loops, randomness, and reusable functions to draw colorful flowers at random locations on the screen.

> **Originally created in 2023** as part of **CSC 231 – Object-Oriented Programming in Python** at **UNCW**.
> I’ll be making new files as I revisit and expand my understanding of OOP principles in Python.

---

## Why I am Practicing This?

* Strengthens **OOP concepts** with clean modular function design
* Reinforces **looping & control structures**
* Encourages **creative problem-solving** using basic geometry
* Introduces **Turtle graphics** for visual learning
* Explores **randomization** and **positioning** in a 2D coordinate space

---

## Original Program Structure

| Component                     | Description                                                              |
| ----------------------------- | ------------------------------------------------------------------------ |
| `draw_petal(t, size)`         | Draws a single petal using two arcs and fills it with color              |
| `draw_flower(t)`              | Uses `draw_petal()` in a loop to make a complete 6-petal flower          |
| `move_to_random_position(t)`  | Moves the turtle to a random (x, y) location on the screen               |
| `create_flower_screensaver()` | Sets up the turtle screen, draws multiple flowers, and loops the display |

---

## Screensaver Behavior

* Background color: white
* Each flower has:

  * **6 petals**
  * **Randomized petal size**
  * **Randomized (x, y) location**
* The turtle hides itself once finished, and the screen stays open as a “screensaver-style” image

---

## Tech & Concepts

### ![Python](https://img.shields.io/badge/python-3670A0?style=flat-square\&logo=python\&logoColor=ffdd54)

**Paradigm**: Multi-paradigm (Imperative, Object-Oriented, Educational)

**Why this implementation**:
Python’s built-in `turtle` module is an excellent entry point for beginners learning how **objects**, **functions**, and **stateful graphics** interact. The project also highlights:

* `turtle.Turtle()` as an OOP object
* Use of **helper functions** to encapsulate drawing logic
* Integration of **random** module for generative design

**Best for**: Visual learning, creative coding, beginner OOP concepts

---


## File List

| File                 | Description                           |
| -------------------- | ------------------------------------- |
| `turtle_flower.py`   | Main Python script with drawing logic |
| *(more coming soon)* | Expanding this repo as I review OOP   |

---
