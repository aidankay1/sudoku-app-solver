from ppadb.client import Client as AdbClient
from PIL import Image, ImageOps
import io
import pytesseract

from Board import Board

client = AdbClient(host="127.0.0.1", port=5037)
SERIAL = "123456789"
device = client.device(SERIAL)

# screen dimensions: 1440 x 3120 px
# box dimensions: 160 x 160 px
# top-left box center: (90, 660)
# bottom of grid y: 2000

screenshot = device.screencap()
image = ImageOps.invert((Image.open(io.BytesIO(screenshot)).convert("RGB")))

board = Board()

board_start_x, board_start_y = 10, 580
board_end_x, board_end_y = 1430, 2000
cell_width = 158

for row, y in enumerate(range(board_start_y, board_end_y, cell_width)):
    for col, x in enumerate(range(board_start_x, board_end_x, cell_width)):
        cropped_image = image.crop((x + 30, y + 30, x + 130, y + 130))
        number = pytesseract.image_to_string(cropped_image, config="--psm 10").strip()

        try:
            number = int(number)
            if number not in range(1, 10):
                raise ValueError
            board.fill(number, row, col)
        except (ValueError, TypeError):
            # Tesseract interprets empty cells as the | character
            if number != "|":
                raise Exception(
                    f"Invalid input: found {number} at position ({col + 1}, {row + 1})"
                )

board.solve()

center_offset = 80

buttons = {
    1: "240 2360",
    2: "480 2360",
    3: "720 2360",
    4: "960 2360",
    5: "1200 2360",
    6: "240 2600",
    7: "480 2600",
    8: "720 2600",
    9: "960 2600",
}

for row, y in enumerate(
    range(board_start_y + center_offset, board_end_y + center_offset, cell_width)
):
    for col, x in enumerate(
        range(board_start_x + center_offset, board_end_x + center_offset, cell_width)
    ):
        # Avoids wasting time by inputting numbers already provided
        if board.initial_board[row][col] != 0:
            continue

        number_to_enter = board.solved_board[row][col]
        device.shell(f"input tap {x} {y}")
        device.shell(f"input tap {buttons[number_to_enter]}")
