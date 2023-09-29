### DreamApp_DataProcessor: The Alchemical Crucible of Data Refinement 🔮📊

Welcome to `DreamApp_DataProcessor`, a sublime submodule of the grand `DreamApp_Core`. This crucible takes raw dream data from the farthest reaches of our realm, meticulously refining it into pristine datasets, ready to power the heart of DreamApp.

#### What's Inside the Box 📦
- **Data Elixirs**: Distill raw CSV files into ethereal DataFrames.
- **Alchemy of Data Cleaning**: Purify and refine datasets, casting away impurities.
- **Transmutation of Shapes**: Reshape the data into forms that echo through the annals of DreamApp.
- **Intertwined with DreamApp_Core**: Lovingly crafted to be the data backbone of our greater magnum opus.

#### A Crucible Forged for Purpose 🍯
While raw data whispers tales of potential, it's here, in the `DreamApp_DataProcessor`, that it finds its voice, its shape, its essence. The alchemy performed here ensures that DreamApp understands every whisper, every sigh, every dream.

---

# DreamApp_DataProcessor 🌌📜

Step into the sanctum of `DreamApp_DataProcessor`, an essential piece of the `DreamApp_Core` tapestry. It's here, amidst lines of code and swirls of data, that dreams find clarity and purpose.

## Table of Contents
- [Lighting the Alchemical Flames](#lighting-the-alchemical-flames)
- [Dependencies](#dependencies)
- [From Rawness to Refinement](#from-rawness-to-refinement)
- [Beckoning Fellow Alchemists](#beckoning-fellow-alchemists)

## Lighting the Alchemical Flames 🕯

To integrate `DreamApp_DataProcessor` into your `DreamApp_Core`, whisper:

```bash
git clone https://github.com/FrancinaSimone/DreamApp_DataProcessor.git
```

## Dependencies 📖

- Pandas

Summon the ancient libraries:

```bash
pip install pandas
```

## From Rawness to Refinement 🌙

### Transforming Raw Dreams into Tales:

1. **Enter the Sacred Grounds**
    ```bash
    cd path/to/DreamApp_DataProcessor/main/
    ```

2. **Kindle the Transformation**
    ```bash
    python main_operations.py
    ```

Bask in the glow of cleansed, reshaped dream data.

## Beckoning Fellow Alchemists 🌌

The crucible is open to all. Enhance its potency, share your own alchemical secrets, or learn from its depths. Fork, explore, and weave your own data magic into the tapestry. In unity, the dream grows clearer.

## Features
- **Configurable Database Connection**: Via `config_secrets.py`, configure your PostgreSQL database credentials.
- **Validators**: Located under `utils/validators.py`, contains utility functions to validate directories and files.
- **Logging**: The `logger/logger.py` takes care of error logging.
- **Database Operations**: `main/main_operations.py` handles all the core database operations like creating tables and inserting data.

## How to Use
1. Make sure PostgreSQL is set up on your machine.
2. Update `config_secrets.py` with your PostgreSQL credentials.
3. Install the dependencies from `requirements.txt`.
4. Run `main_operations.py` to create the `mythology` table and insert an example story.

## Dependencies
- PostgreSQL
- psycopg2

To install all dependencies, run:
