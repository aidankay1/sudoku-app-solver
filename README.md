# sudoku-app-solver

This program solves any sudoku board in [Sudoku - The Clean One](https://play.google.com/store/apps/details?id=ee.dustland.android.dustlandsudoku&hl=en_US&gl=US) for Android.

At a high level, the program does the following:
1. Captures a screenshot of the sudoku board using ADB
2. Translates the image into an integer array using Tesseract OCR
3. Solves the board recursively
4. Inputs the solution on the Android device using ADB tap commands

Tested on a OnePlus 7 Pro using the dark green app theme. Light themes might work with some changes to the image loading code.

The program would execute much faster if the delay between ADB commands is somehow shortened. Refactoring the solving algorithm may also produce a minor speed boost.
