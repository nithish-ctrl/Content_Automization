from playwright.sync_api import sync_playwright
import time


def video_uploading(topic, video_path, user_data_dir):
# CONFIG
    VIDEO_PATH = video_path
    USER_DATA_DIR = user_data_dir

    CAPTION = """AI has revolutionized the way we create content, enabling us to produce engaging and informative videos with ease. 
    This reel about {topic} was created using a combination of AI tools for script generation, text-to-speech conversion, subtitle generation, and video assembly. 
    The entire process was built fully with local AI tools, showcasing the incredible potential of artificial intelligence in content creation. 
    Like, Follow and Share for more of these videos and a tutorial on how to create them yourself !!! 
    Have a wonderful day ahead !!!
    #ai #python #automation #reels #{topic.replace(" ", "").lower()}
    """

# MAIN SCRIPT
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            USER_DATA_DIR,
            headless=False
        )
        page = browser.new_page()

        # OPEN INSTAGRAM
        page.goto("https://www.instagram.com")
        print("Opening Instagram...")
        time.sleep(4)  # login if needed

        # OPEN CREATE (NEW POST)
        print("Opening Create...")

        page.locator("svg[aria-label='New post']").click(force=True)
        time.sleep(3)

        # UPLOAD VIDEO
        print("Uploading video...")

        with page.expect_file_chooser() as fc:
            page.locator("text=Select from computer").click(force=True)

        file_chooser = fc.value
        file_chooser.set_files(VIDEO_PATH)

        # wait for upload processing
        time.sleep(5)

        # CROP STEP
        print("Setting crop to 9:16...")

        page.locator("svg[aria-label='Select crop']").click(force=True)
        time.sleep(2)

        page.locator("text=9:16").click(force=True)
        time.sleep(2)

        # NEXT (CROP SCREEN)
        print("Next (crop screen)...")

        page.locator("text=Next").first.click(force=True)
        time.sleep(2)

        # NEXT (EDIT SCREEN)
        print("Next (edit screen)...")

        page.locator("text=Next").first.click(force=True)
        time.sleep(2)

        # CAPTION
        print("Adding caption...")

        caption_box = page.locator("div[contenteditable='true']").last
        caption_box.click(force=True)
        caption_box.fill(CAPTION)

        time.sleep(3)

        # SHARE
        print("Sharing reel...")
        page.locator("div[role='dialog']").get_by_role("button", name="Share").click(force=True)
        print("Upload started...")

        time.sleep(500)
        print("Upload completed!")
        browser.close()