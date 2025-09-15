import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class RegisterTest(unittest.TestCase):
    def setUp(self):
        """
        Set up Selenium WebDriver for Chrome on a test server like GitHub Actions or locally.
        """
        if os.getenv("ENVIRONMENT_STAGE") == "TEST":
            for retries in range(5):
                try:
                    self.browser = webdriver.Remote(
                        command_executor="http://localhost:4444/wd/hub",
                        desired_capabilities=DesiredCapabilities.CHROME,
                    )
                    break
                except Exception:
                    time.sleep(2)
        else:
            self.browser = webdriver.Chrome()

        self.browser.get("http://localhost:8000/register/")

    def tearDown(self):
        self.browser.quit()

    """
    - Minimum length of 8 characters
    - Must contain both uppercase and lowercase letters
    - Must include at least one number
    - Must include at least one special character (!@#$%^&*)
    """

    def test_password_matching_first_check_no_character(self):
        """Check if password is minimum length of 8 characters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("the")
        time.sleep(0.5)
        self.assertEqual(
            "Password must be at least 8 characters long!", password_check_msg.text
        )

    def test_password_matching_first_check_eight_characters(self):
        """Check if password is minimum length of 8 characters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must be at least 8 characters long!", password_check_msg.text
        )

    def test_password_matching_second_check_all_lowercase(self):
        """Check if password contains both uppercase and lowercase letters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("password1!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must contain both uppercase and lowercase letters!",
            password_check_msg.text,
        )

    def test_password_matching_second_check_all_uppercase(self):
        """Check if password contains both uppercase and lowercase letters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("PASSWORD1!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must contain both uppercase and lowercase letters!",
            password_check_msg.text,
        )

    def test_password_matching_second_check_mixed_case(self):
        """Check if password contains both uppercase and lowercase letters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must contain both uppercase and lowercase letters!",
            password_check_msg.text,
        )

    def test_password_matching_third_check_no_number(self):
        """Check if password includes at least one number"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one number!", password_check_msg.text
        )

    def test_password_matching_third_check_with_number(self):
        """Check if password includes at least one number"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must include at least one number!", password_check_msg.text
        )

    def test_password_matching_fourth_check_no_special_character(self):
        """Check if password includes at least one special character (!@#$%^&*)"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one special character (!@#$%^&*)!",
            password_check_msg.text,
        )

    def test_password_matching_fourth_check_with_special_character_not_listed(self):
        """Check if password includes at least one special character (!@#$%^&*)"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1+")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one special character (!@#$%^&*)!",
            password_check_msg.text,
        )

    def test_password_matching_fourth_check_with_special_character(self):
        """Check if password includes at least one special character (!@#$%^&*)"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must include at least one special character (!@#$%^&*)!",
            password_check_msg.text,
        )


if __name__ == "__main__":
    unittest.main()
