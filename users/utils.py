import re


def normalize_phone_number(phone_number):
    """
    Normalizes a phone number to a standard format.

    :param phone_number: The input phone number to be normalized.
    :type phone_number: str
    :return: The normalized phone number in the format '919846000000'.
    :rtype: str

    Description:
        This function takes a phone number as input and normalizes it to a standard format.
        All three formats: '+919846000000', '919846000000', and '9846000000' will produce '919846000000'.
        It removes non-numeric characters and ensures that the number starts with '91'.
    """
    # Remove non-numeric characters
    phone_number = re.sub(r"\D", "", phone_number)

    # Add "91" at the beginning if needed
    if not phone_number.startswith("91"):
        phone_number = f"91{phone_number}"

    return phone_number


def normalize_email(email):
    """
    Normalize the given email address by converting it to lowercase and removing leading/trailing whitespaces.

    Args:
        email (str): The email address to be normalized.

    Returns:
        str: The normalized email address, or None if the input is invalid.

    Example:
        >>> email = "  Example@domain.com  "
        >>> normalized_email = normalize_email(email)
        >>> print(normalized_email)
        "example@domain.com"
    """
    if not email or not isinstance(email, str):
        return None

    # Convert the email to lowercase
    normalized_email = email.lower()

    # Remove leading and trailing whitespaces
    normalized_email = normalized_email.strip()

    return normalized_email
