import pygame
import random

# Initialize Pygame
pygame.init()

# =========================================================
# WINDOW
# =========================================================

WIDTH = 1000
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Array DSA Visualiser")

clock = pygame.time.Clock()

# =========================================================
# COLORS
# =========================================================

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (50, 120, 220)
GREEN = (50, 180, 100)
RED = (220, 70, 70)
GRAY = (220, 220, 220)
DARK = (40, 50, 70)
PURPLE = (130, 80, 180)

# =========================================================
# FONTS
# =========================================================

title_font = pygame.font.SysFont("Arial", 36, True)
font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)

# =========================================================
# ARRAY
# =========================================================

arr = [10, 20, 30, 40, 50]

selected_index = -1
message = "Select an operation"

# =========================================================
# INPUT
# =========================================================

input_text = ""
active_operation = None


# =========================================================
# DRAW TEXT
# =========================================================

def draw_text(text, x, y, font_type, color=BLACK):
    image = font_type.render(str(text), True, color)
    screen.blit(image, (x, y))


# =========================================================
# DRAW ARRAY
# =========================================================

def draw_array():

    start_x = 100
    start_y = 200

    box_width = 90
    box_height = 70
    gap = 15

    for i, value in enumerate(arr):

        x = start_x + i * (box_width + gap)

        # Highlight selected element
        if i == selected_index:
            color = GREEN
        else:
            color = BLUE

        pygame.draw.rect(
            screen,
            color,
            (x, start_y, box_width, box_height),
            border_radius=8
        )

        # Value
        draw_text(
            value,
            x + 30,
            start_y + 20,
            font,
            WHITE
        )

        # Index
        draw_text(
            f"Index: {i}",
            x + 5,
            start_y + 80,
            small_font,
            BLACK
        )


# =========================================================
# DRAW BUTTON
# =========================================================

def draw_button(text, x, y, width=140, height=45):

    rect = pygame.Rect(x, y, width, height)

    pygame.draw.rect(
        screen,
        DARK,
        rect,
        border_radius=8
    )

    draw_text(
        text,
        x + 15,
        y + 10,
        small_font,
        WHITE
    )

    return rect


# =========================================================
# ARRAY OPERATIONS
# =========================================================

def access(index):

    global selected_index
    global message

    if 0 <= index < len(arr):

        selected_index = index
        message = f"arr[{index}] = {arr[index]}"

    else:

        selected_index = -1
        message = "Invalid index"


# =========================================================

def update(index, value):

    global selected_index
    global message

    if 0 <= index < len(arr):

        arr[index] = value
        selected_index = index
        message = f"Updated index {index}"

    else:

        selected_index = -1
        message = "Invalid index"


# =========================================================

def insert(index, value):

    global selected_index
    global message

    if 0 <= index <= len(arr):

        arr.insert(index, value)
        selected_index = index
        message = f"Inserted {value} at index {index}"

    else:

        selected_index = -1
        message = "Invalid index"


# =========================================================

def delete(index):

    global selected_index
    global message

    if 0 <= index < len(arr):

        value = arr.pop(index)

        selected_index = -1
        message = f"Deleted {value} from index {index}"

    else:

        selected_index = -1
        message = "Invalid index"


# =========================================================

def search(value):

    global selected_index
    global message

    selected_index = -1

    for i in range(len(arr)):

        if arr[i] == value:

            selected_index = i
            message = f"Found {value} at index {i}"
            return

    message = f"{value} not found"


# =========================================================

def reverse_array():

    global arr
    global selected_index
    global message

    arr.reverse()

    selected_index = -1
    message = "Array reversed"


# =========================================================

def sort_array():

    global arr
    global selected_index
    global message

    arr.sort()

    selected_index = -1
    message = "Array sorted"


# =========================================================

def shuffle_array():

    global arr
    global selected_index
    global message

    random.shuffle(arr)

    selected_index = -1
    message = "Array shuffled"


# =========================================================

def move_zeros():

    global arr
    global selected_index
    global message

    non_zero = []
    zeros = []

    for value in arr:

        if value == 0:
            zeros.append(value)

        else:
            non_zero.append(value)

    arr = non_zero + zeros

    selected_index = -1
    message = "Zeros moved to the end"


# =========================================================
# BUTTONS
# =========================================================

buttons = []

buttons.append(("Access", 50, 100))
buttons.append(("Update", 210, 100))
buttons.append(("Insert", 370, 100))
buttons.append(("Delete", 530, 100))
buttons.append(("Search", 690, 100))

buttons.append(("Reverse", 50, 500))
buttons.append(("Sort", 210, 500))
buttons.append(("Shuffle", 370, 500))
buttons.append(("Move Zeros", 530, 500))


# =========================================================
# MAIN LOOP
# =========================================================

running = True

while running:

    screen.fill(WHITE)

    # =====================================================
    # TITLE
    # =====================================================

    draw_text(
        "ARRAY DSA VISUALISER",
        300,
        25,
        title_font,
        DARK
    )

    # =====================================================
    # DRAW BUTTONS
    # =====================================================

    button_rects = []

    for name, x, y in buttons:

        rect = draw_button(
            name,
            x,
            y
        )

        button_rects.append(
            (name, rect)
        )

    # =====================================================
    # ARRAY
    # =====================================================

    draw_text(
        "Array",
        50,
        160,
        font,
        DARK
    )

    draw_array()

    # =====================================================
    # MESSAGE
    # =====================================================

    pygame.draw.rect(
        screen,
        GRAY,
        (50, 400, 850, 60),
        border_radius=8
    )

    draw_text(
        message,
        70,
        418,
        font,
        BLACK
    )

    # =====================================================
    # INPUT BOX
    # =====================================================

    pygame.draw.rect(
        screen,
        GRAY,
        (50, 565, 850, 40),
        border_radius=5
    )

    draw_text(
        "Input: " + input_text,
        60,
        573,
        small_font,
        BLACK
    )

    # =====================================================
    # EVENTS
    # =====================================================

    for event in pygame.event.get():

        # -------------------------------------------------
        # CLOSE WINDOW
        # -------------------------------------------------

        if event.type == pygame.QUIT:

            running = False

        # -------------------------------------------------
        # MOUSE CLICK
        # -------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_position = event.pos

            for name, rect in button_rects:

                if rect.collidepoint(mouse_position):

                    active_operation = name
                    input_text = ""

                    message = f"{name}: enter value/index"

        # -------------------------------------------------
        # KEYBOARD
        # -------------------------------------------------

        if event.type == pygame.KEYDOWN:

            # -------------------------------------------------
            # ENTER
            # -------------------------------------------------

            if event.key == pygame.K_RETURN:

                try:

                    if active_operation == "Access":

                        index = int(input_text)

                        access(index)

                    elif active_operation == "Update":

                        values = input_text.split()

                        if len(values) != 2:
                            raise ValueError

                        index = int(values[0])
                        value = int(values[1])

                        update(index, value)

                    elif active_operation == "Insert":

                        values = input_text.split()

                        if len(values) != 2:
                            raise ValueError

                        index = int(values[0])
                        value = int(values[1])

                        insert(index, value)

                    elif active_operation == "Delete":

                        index = int(input_text)

                        delete(index)

                    elif active_operation == "Search":

                        value = int(input_text)

                        search(value)

                    elif active_operation == "Reverse":

                        reverse_array()

                    elif active_operation == "Sort":

                        sort_array()

                    elif active_operation == "Shuffle":

                        shuffle_array()

                    elif active_operation == "Move Zeros":

                        move_zeros()

                    input_text = ""
                    active_operation = None

                except (ValueError, IndexError):

                    message = "Invalid input. Please enter valid numbers."

            # -------------------------------------------------
            # BACKSPACE
            # -------------------------------------------------

            elif event.key == pygame.K_BACKSPACE:

                input_text = input_text[:-1]

            # -------------------------------------------------
            # NORMAL TYPING
            # -------------------------------------------------

            else:

                # Allow only numbers, minus sign and spaces
                if event.unicode.isdigit() or event.unicode in "- ":

                    input_text += event.unicode

    # =====================================================
    # UPDATE SCREEN
    # =====================================================

    pygame.display.update()

    clock.tick(60)


# =========================================================
# QUIT
# =========================================================

pygame.quit()