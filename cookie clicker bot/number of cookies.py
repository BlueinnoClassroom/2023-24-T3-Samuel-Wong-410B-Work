# find the number of cookies
            # left = 1225
            # right = 1438
            # up = 360
            # height = 18
            # for i in range(5):
            #     screenshot = ImageGrab.grab(
            #         bbox=(left, up + height * i, right, up + height * (i + 1))
            #     ).convert(
            #         "L"
            #     )  # to grayscale
            #     screenshot.save(f"price_of_building {i}.png")

            #     result = ""
            #     text: str = pytesseract.image_to_string("number_of_cookies.png", lang="eng")
            #     for char in text:
            #         if char.isdigit():
            #             result += char

            #     try:
            #         result = int(result)
            #         print(result)
            #     except Exception as e:
            #         print(f"error: {e}")
