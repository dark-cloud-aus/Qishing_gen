# Simple QR code generator that outputs the QR Code in unicode so that it can be pasted in to an email and not get blocked
# I developed this script as part of a Qishing exercise - Created by David Gilmore
# Qishing is like phishing but using malicious QR codes


ascii_art = '''
     ____    _      __    _                ____    ____     ______                           __            
  / __ \  (_)____/ /_  (_)___  ____ _   / __ \  / __ \   / ____/__  ____  ___  _________ _/ /_____  _____
 / / / / / / ___/ __ \/ / __ \/ __ `/  / / / / / /_/ /  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /_/ / / (__  ) / / / / / / / /_/ /  / /_/ / / _, _/  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
\___\_\/_/____/_/ /_/_/_/ /_/\__, /   \___\_\/_/ |_|   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                            /____/ 
'''

print(ascii_art)
import segno

def create_unicode_qr(data):
    qr = segno.make(data)
    unicode_qr = qr.terminal(compact=True)
    return unicode_qr

# Insert the target URL below
data = "https://example.com"
unicode_qr = create_unicode_qr(data)
print(unicode_qr)
