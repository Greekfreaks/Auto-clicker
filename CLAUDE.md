# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A GUI-based auto-clicker application built with PySide6 that allows automated mouse clicking with customizable settings. The application runs the clicker logic on a separate thread from the GUI to maintain responsiveness.

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Architecture

### Core Components

**Three-layer architecture:**

1. **Entry Point (`main.py`)**: Creates Qt application instance and launches the main window
2. **GUI Layer (`gui_main.py`)**:
   - `MainWindow`: Connects UI elements to backend logic
   - `ClickerThread`: QThread wrapper that runs the clicker in the background
3. **Logic Layer (`clicker_logic.py`)**:
   - `AutoClicker`: Handles click execution and keyboard listening on separate threads

### Threading Model

The application uses **two separate threads**:
- **Main thread**: Runs the Qt GUI event loop
- **Clicker thread**: Runs `AutoClicker.start_clicker()` which spawns:
  - A daemon thread for `key_listener()` (keyboard monitoring)
  - Main clicking loop in the clicker thread itself

Settings changes from the GUI immediately update the `AutoClicker` instance via direct method calls (thread-safe due to Python's GIL for simple attribute assignments).

### UI Design Workflow

- `gui_main.ui`: Qt Designer file (XML) defining the visual layout
- `gui_design.py`: **Auto-generated** Python code from the .ui file
- `gui_main.py`: Extends `Ui_MainWindow` from gui_design.py to add behavior

**Important**: Never manually edit `gui_design.py`. To modify the UI:
1. Edit `gui_main.ui` in Qt Designer
2. Regenerate `gui_design.py` using: `pyside6-uic gui_main.ui -o gui_design.py`

### Signal/Slot Connections

GUI widgets connect to backend methods via Qt signals:
- `clickingMethodInput.currentTextChanged` → `update_clicking_method()`
- `clickDelayInput.valueChanged` → `update_click_delay()`
- `startDelayInput.valueChanged` → `update_start_delay()`
- Keybind inputs use `keySequenceChanged` signals

## Recently Fixed Issues

**Fixed in commit 96b6339**:
- ✓ Fixed swapped click methods in `middle_click()` and `right_click()`
- ✓ Fixed keybind setters (`set_stop_key()`, `set_exit_key()`) setting wrong variables
- ✓ Fixed inconsistent `delay_flag` implementation across all click methods
- ✓ Removed redundant logic in `update_clicking_method()`

**Fixed in commit ceff980**:
- ✓ Exit keybind now properly closes the entire application (not just stops clicking logic)

## Implemented Features

### CPS Display (Added in current session)
- Real-time clicks-per-second calculation and display
- Tracks clicks in a rolling 1-second window
- Updates LCD widget every 100ms
- Thread-safe communication via Qt signals

### Click Type Variations (Added in current session)
The "More Settings" section now includes:
- **Click Type selector** (`clickTypeInput`): Choose between:
  - Single Click: Standard single click (default)
  - Double Click: Performs two clicks rapidly
  - Hold Click: Mouse down + hold + mouse up
- **Hold Duration slider** (`holdDurationSlider`): Adjustable duration (50-2000ms) for Hold Click mode

Both settings work with all click methods (Left, Middle, Right)
