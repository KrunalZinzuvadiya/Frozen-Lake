# Frozen Lake

This project is an implementation of the Frozen Lake game using Python. The game is typically used as a benchmark in reinforcement learning environments to test various algorithms.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Frozen Lake environment consists of a grid of tiles, where each tile can be a starting point, frozen (safe to walk on), a hole (causing the agent to fall and lose), or the goal. The objective is to navigate from the start to the goal without falling into any holes.

## Features

- Implementation of the Frozen Lake game.
- Customizable grid size.
- Implementation of basic reinforcement learning algorithms.
- Visualization of the agent's path.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/frozen-lake.git
    cd frozen-lake
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Python script:
    ```bash
    python Frozen_Lake.py
    ```

2. Follow the prompts in the script to play the game or to run reinforcement learning algorithms.

## Project Structure

- `Frozen_Lake.py`: Main script containing the game and algorithm implementation.
- `requirements.txt`: List of dependencies required to run the project.

## Dependencies

- Python 3.x
- OpenAI Gym
- NumPy

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please open an issue on GitHub or contact the project maintainer.
