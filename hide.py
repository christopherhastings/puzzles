def hide(message, direction, shift):
    # Define the keyboard rows
    Row_1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    Row_2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    Row_3 = ["Z", "X", "C", "V", "B", "N", "M"]
    
    # Combine rows into a list for easy access
    keyboard_rows = [Row_1, Row_2, Row_3]
    
    cipher = []
    
    for char in message:
        if char == " ":
            cipher.append(" ")  # Add spaces verbatim
            continue
        
        # Determine which row the character belongs to
        row = None
        for r in keyboard_rows:
            if char.upper() in r:
                row = r
                break
        
        if not row:
            cipher.append(char)  # If the character isn't in any row (e.g., punctuation), leave it unchanged
            continue
        
        # Find the index of the character in the row
        index = row.index(char.upper())
        
        # Shift the character based on direction
        if direction == "left":
            new_index = (index - shift) % len(row)
        elif direction == "right":
            new_index = (index + shift) % len(row)
        else:
            raise ValueError("Direction must be 'left' or 'right'")
        
        # Append the shifted character to the cipher
        cipher.append(row[new_index])
    
    return "".join(cipher)

print(hide("hello.", "left", 1))