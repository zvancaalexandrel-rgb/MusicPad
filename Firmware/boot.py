import storage
import board
import digitalio

# Boot configuration for 4x3 keyboard matrix
# This code runs at startup to check if a specific key combination is pressed
# to disable USB drive access (useful for firmware updates)

# Define the key to check at boot (Row4, Col3 = D1 based on matrix layout)
# Matrix layout:
# Row1: D4(col1), D3(col2), D2(col3)
# Row2: D5(col1), D6(col2), D7(col3)
# Row3: D9(col1), D10(col2), D11(col3)
# Row4: D8(col1), D12(col2), D1(col3)  <-- Boot key is D1 at Row4/Col3

# Configure the row pin for the boot key (Row4 = D7 in row_pins)
boot_row = digitalio.DigitalInOut(board.D7)  # Row4
boot_row.direction = digitalio.Direction.INPUT
boot_row.pull = digitalio.Pull.DOWN  # Pull-down resistor

# Configure the column pin for the boot key (Col3 = D3 in col_pins)
boot_col = digitalio.DigitalInOut(board.D3)  # Col3
boot_col.direction = digitalio.Direction.OUTPUT
boot_col.value = True  # Set column high to check if row is pulled up

# Check if the boot key (D1) is being held down
if not boot_row.value:
    storage.disable_usb_drive()  # Disable USB drive access for firmware update mode

# Clean up pins
boot_row.deinit()
boot_col.deinit()