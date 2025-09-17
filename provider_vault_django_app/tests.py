import time
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterTest(unittest.TestCase):
    def setUp(self):
        """
        Set up Selenium WebDriver for Chrome on a test server like GitHub Actions or locally.
        """
        # Add options to run Chrome in headless mode for CI environments
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.get("http://localhost:8000/register/")

    def tearDown(self):
        self.browser.quit()

    """
    - Minimum length of 8 characters
    - Must contain both uppercase and lowercase letters
    - Must include at least one number
    - Must include at least one special character (!@#$%^&*)
    """

    def test_password_first_check_no_character(self):
        """Check if password is minimum length of 8 characters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("the")
        time.sleep(0.5)
        self.assertEqual(
            "Password must be at least 8 characters long!", password_check_msg.text
        )

    def test_password_first_check_eight_characters(self):
        """Check if password is minimum length of 8 characters"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must be at least 8 characters long!", password_check_msg.text
        )

    def test_password_second_check_all_lowercase(self):
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

    def test_password_second_check_all_uppercase(self):
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

    def test_password_second_check_mixed_case(self):
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

    def test_password_third_check_no_number(self):
        """Check if password includes at least one number"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password!")
        time.sleep(0.5)
        self.assertEqual(
            "Password must include at least one number!", password_check_msg.text
        )

    def test_password_third_check_with_number(self):
        """Check if password includes at least one number"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertNotEqual(
            "Password must include at least one number!", password_check_msg.text
        )

    def test_password_fourth_check_no_special_character(self):
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

    def test_password_fourth_check_with_special_character_not_listed(self):
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

    def test_password_fourth_check_with_special_character(self):
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

    def test_password_all_checks_pass(self):
        """Check if password meets all criteria"""
        password_input = self.browser.find_element(By.ID, "password")
        password_check_msg = self.browser.find_element(By.ID, "password_check_msg")

        password_input.clear()
        password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertEqual("", password_check_msg.text)

    def test_passwords_mismatch(self):
        """Check if passwords do not match"""
        password_input = self.browser.find_element(By.ID, "password")
        confirm_password_input = self.browser.find_element(By.ID, "confirm_password")
        password_match_msg = self.browser.find_element(By.ID, "password_match_msg")

        password_input.clear()
        confirm_password_input.clear()
        password_input.send_keys("Password1!")
        confirm_password_input.send_keys("Password2!")
        time.sleep(0.5)
        self.assertEqual("Passwords do not match!", password_match_msg.text)

    def test_passwords_match(self):
        """Check if passwords match"""
        password_input = self.browser.find_element(By.ID, "password")
        confirm_password_input = self.browser.find_element(By.ID, "confirm_password")
        password_match_msg = self.browser.find_element(By.ID, "password_match_msg")

        password_input.clear()
        confirm_password_input.clear()
        password_input.send_keys("Password1!")
        confirm_password_input.send_keys("Password1!")
        time.sleep(0.5)
        self.assertEqual("", password_match_msg.text)

    def test_password_submit_error_messages(self):
        """Check if password check message is empty when both fields are empty"""
        first_name = self.browser.find_element(By.ID, "first_name")
        last_name = self.browser.find_element(By.ID, "last_name")
        email = self.browser.find_element(By.ID, "email")
        password = self.browser.find_element(By.ID, "password")
        confirm_password = self.browser.find_element(By.ID, "confirm_password")
        register_button = self.browser.find_element(By.ID, "register_form_button")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("john.doe@example.com")
        password.send_keys("Password1")
        confirm_password.send_keys("Password1")
        time.sleep(0.5)
        register_button.click()

        alert = self.browser.switch_to.alert
        alert_text = alert.text
        self.assertEqual(
            "There are error messages displayed. Please fix these issues", alert_text
        )
        alert.accept()

    def test_password_submit_correct(self):
        """Check if password check message is empty when both fields are empty"""
        first_name = self.browser.find_element(By.ID, "first_name")
        last_name = self.browser.find_element(By.ID, "last_name")
        email = self.browser.find_element(By.ID, "email")
        password = self.browser.find_element(By.ID, "password")
        confirm_password = self.browser.find_element(By.ID, "confirm_password")
        register_button = self.browser.find_element(By.ID, "register_form_button")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("john.doe@example.com")
        password.send_keys("Password1!")
        confirm_password.send_keys("Password1!")
        time.sleep(0.5)
        register_button.click()

        alert = self.browser.switch_to.alert
        alert_text = alert.text
        self.assertEqual("Registration Complete!", alert_text)
        alert.accept()


if __name__ == "__main__":
    unittest.main()
