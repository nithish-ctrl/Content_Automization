from playwright.sync_api import sync_playwright
import time

def video_uploading():
    pass
# CONFIG

VIDEO_PATH = r"C:\Users\Nithish\Content_Automisation\output\final_reel.mp4"

USER_DATA_DIR = r"C:\Users\Nithish\Content_Automisation\insta_session"

CAPTION = """
{topic} : 
Like, Follow and Share for more of these videos !!!
#shorts #reels #viral #AI #technology #innovation #future #trending #explorepage 
#fyp #contentcreator #instagood #instadaily #RAG #retrievalaugmentedgeneration #artificialintelligence 
#machinelearning #deeplearning #neuralnetworks #datascience #bigdata 
#analytics #automation #programming #coding
"""


# PLAYWRIGHT
with sync_playwright() as p:

    # PERSISTENT BROWSER
    browser = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False
    )

    page = browser.new_page()

    # OPEN INSTAGRAM

    page.goto("https://www.instagram.com")

    print("\n================================================")
    print("FIRST RUN ONLY:")
    print("Login manually once.")
    print("Session will be saved automatically.")
    print("\n")

    time.sleep(20)

    # OPEN CREATE PAGE

    page.goto("https://www.instagram.com/create/select/")

    time.sleep(5)

    # UPLOAD VIDEO

    file_input = page.locator("input[type='file']")
    file_input.set_input_files(VIDEO_PATH)

    time.sleep(10)

    # NEXT BUTTON 1

    next_buttons = page.locator("text=Next")
    next_buttons.nth(0).click()

    time.sleep(5)

    # NEXT BUTTON 2

    next_buttons = page.locator("text=Next")
    next_buttons.nth(0).click()

    time.sleep(5)

       # CAPTION

    caption_box = page.locator(
        "div[aria-label='Write a caption...']"
    )

    caption_box.click()
    caption_box.fill(CAPTION)

    time.sleep(2)
    share_button = page.locator("text=Share")
    share_button.click()

    print("\nUploading reel...\n")

    time.sleep(60)

    print("\nUpload completed!\n")

    browser.close()

video_uploading()