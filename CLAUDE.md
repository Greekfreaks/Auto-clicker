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

## Known Issues

### Critical Bugs

**clicker_logic.py**:
- Lines 57-66: `middle_click()` and `right_click()` call the wrong pyautogui methods (swapped)
- Lines 88-94: `set_stop_key()` and `set_exit_key()` both incorrectly set `self.startClickKey`
- Lines 52-68: `delay_flag` implementation is inconsistent across click methods

**gui_main.py**:
- Lines 40-46: Redundant if-elif chain in `update_clicking_method()` - calls `set_click_method()` multiple times unnecessarily

## Unimplemented Features

- **CPS Display**: UI has LCD widget (`lcdNumber`) but no actual calculation/update logic
- **More Settings Section**: Placeholder UI elements (`comboBox_2`, `horizontalSlider_3`) not connected to any functionality
