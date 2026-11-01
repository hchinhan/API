import requests

API_URL = "http://127.0.0.1:8000"


def test_endpoints():
    # Test case 1: Eren Yaeger (Attack on Titan)
    case_1 = {
        "text": "壁の向こうには海があって、海の向こうには自由がある。ずっとそう信じてた……。でも違った。海の向こうにいるのは敵だ。向こうにいる敵全部殺せば……オレ達、自由になれるのか？"
    }
    res_1 = requests.post(f"{API_URL}/predict", json=case_1)
    print("\n-> Test Case 1 (Eren Yaeger - Attack on Titan):")
    print("Status Code:", res_1.status_code)
    print("Input: ", case_1["text"])
    print("Output:", res_1.json().get("english_translation"))

    # Test case 2: Pain (Naruto Shippuden)
    case_2 = {
        "text": "痛みを感じろ、痛みを考えろ、痛みを受け取れ、痛みを知れ。痛みを知らぬ者に、本当の平和は分からん。俺はヤヒコの痛みを忘れない。ここより…世界に痛みを！神羅天征！"
    }
    res_2 = requests.post(f"{API_URL}/predict", json=case_2)
    print("\n-> Test Case 2 (Pain - Naruto Shippuden):")
    print("Status Code:", res_2.status_code)
    print("Input: ", case_2["text"])
    print("Output:", res_2.json().get("english_translation"))

    # Test case 3: Gojo Satoru (Jujutsu Kaisen)
    case_3 = {"text": "だって君弱いもん"}
    res_3 = requests.post(f"{API_URL}/predict", json=case_3)
    print("\n-> Test Case 3 (Gojo Satoru - Jujutsu Kaisen):")
    print("Status Code:", res_3.status_code)
    print("Input: ", case_3["text"])
    print("Output:", res_3.json().get("english_translation"))

    # Test case 4: Empty string input
    case_empty = {"text": "   "}
    res_empty = requests.post(f"{API_URL}/predict", json=case_empty)
    print("\n-> Test Case 4 (Empty Input):")
    print("Status Code:", res_empty.status_code)
    print("Error Detail:", res_empty.json())

    # Test case 5: Non-Japanese language (e.g., Vietnamese)
    case_vietnamese = {"text": "Xin chào, tôi sẽ trở thành Vua Hải Tặc!"}
    res_vi = requests.post(f"{API_URL}/predict", json=case_vietnamese)
    print("\n-> Test Case 5 (Wrong Language - Vietnamese Text):")
    print("Input: ", case_vietnamese["text"])
    print("Status Code:", res_vi.status_code)
    print("Error Detail:", res_vi.json())

    # Test case 6: Only numbers in string
    case_numbers = {"text": "1234567890"}
    res_num = requests.post(f"{API_URL}/predict", json=case_numbers)
    print("\n-> Test Case 6 (Only Numbers in String):")
    print("Input: ", case_numbers["text"])
    print("Status Code:", res_num.status_code)
    print("Error Detail:", res_num.json())

    # Test case 7: Only special characters
    case_special = {"text": "!@#$%^&*()_+-=[]{};':\",./<>?"}
    res_spec = requests.post(f"{API_URL}/predict", json=case_special)
    print("\n-> Test Case 7 (Only Special Characters):")
    print("Input: ", case_special["text"])
    print("Status Code:", res_spec.status_code)
    print("Error Detail:", res_spec.json())

    # Test case 8: Missing input field 'text'
    case_missing = {}
    res_missing = requests.post(f"{API_URL}/predict", json=case_missing)
    print("\n-> Test Case 8 (Missing Input Field 'text'):")
    print("Status Code:", res_missing.status_code)
    print("Error Detail:", res_missing.json())

    # Test case 9: Invalid data type (integer instead of string)
    case_wrong_type = {"text": 99999}
    res_type = requests.post(f"{API_URL}/predict", json=case_wrong_type)
    print("\n-> Test Case 9 (Invalid Data Format - Integer instead of String):")
    print("Status Code:", res_type.status_code)
    print("Error Detail:", res_type.json())
    print("=" * 50)


if __name__ == "__main__":
    test_endpoints()
