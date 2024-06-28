import re

def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length of password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
        
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Determine strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    # Return results
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# Example usage
password = input("Enter a password to assess its strength: ")
result = assess_password_strength(password)
print(f"Password Strength: {result['strength']}")
for feedback in result["feedback"]:
    print(f"- {feedback}")
