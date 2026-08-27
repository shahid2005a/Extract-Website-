#!/usr/bin/env python3
"""
Single-file Flask website with Tailwind CSS.
Run: python main.py
"""

from flask import Flask, render_template_string
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-123'

# Logging setup
logging.basicConfig(level=logging.INFO)
app.logger.info("🚀 Bhai, website chal rahi hai!")

# ------------------ HTML Templates (inline) ------------------
BASE_HTML = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}MySite{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { min-height: 100vh; display: flex; flex-direction: column; }
        main { flex: 1; }
    </style>
</head>
<body class="bg-gray-50 font-sans">
    <!-- Navbar -->
    <nav class="bg-white shadow-lg border-b border-gray-200">
        <div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
            <a href="/" class="text-2xl font-bold text-blue-600">🚀 MySite</a>
            <div>
                <a href="/" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">Home</a>
                <a href="/about" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">About</a>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-6xl mx-auto px-4 py-10">
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-10 py-6 text-center text-gray-500 text-sm">
        © 2026 Made with ❤️ in Python
    </footer>
</body>
</html>
"""

HOME_HTML = """
{% extends base_template %}

{% block title %}Home{% endblock %}

{% block content %}
<div class="bg-white rounded-2xl shadow-xl p-8 md:p-12 text-center border border-gray-100">
    <h1 class="text-4xl md:text-5xl font-extrabold text-gray-800 mb-4">
        Namaste Dosto! 🙏
    </h1>
    <p class="text-xl text-gray-600 mb-6">
        Python + Flask se professional serve ho raha hai 💪
    </p>
    <div class="inline-block bg-blue-50 text-blue-700 px-6 py-3 rounded-full text-sm font-semibold">
        ⚡ Server Status: Active
    </div>

    <div class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
        <div class="bg-gray-50 p-6 rounded-xl border border-gray-200">
            <h3 class="font-bold text-lg">🔒 Secure</h3>
            <p class="text-gray-600 text-sm">Environment variables se protect.</p>
        </div>
        <div class="bg-gray-50 p-6 rounded-xl border border-gray-200">
            <h3 class="font-bold text-lg">⚡ Fast</h3>
            <p class="text-gray-600 text-sm">Production-ready Waitress server.</p>
        </div>
        <div class="bg-gray-50 p-6 rounded-xl border border-gray-200">
            <h3 class="font-bold text-lg">🎨 Modern</h3>
            <p class="text-gray-600 text-sm">Tailwind CSS with responsive UI.</p>
        </div>
    </div>
</div>
{% endblock %}
"""

ABOUT_HTML = """
{% extends base_template %}

{% block title %}About{% endblock %}

{% block content %}
<div class="bg-white rounded-2xl shadow-xl p-8 md:p-12 text-center border border-gray-100">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">About This Site</h2>
    <p class="text-lg text-gray-600 max-w-2xl mx-auto">
        Ye ek <span class="font-semibold text-blue-600">Flask</span> application hai 
        jo ek single <code>main.py</code> file mein poori website serve karti hai.
        Simple, fast, aur production-ready!
    </p>
    <div class="mt-6 flex justify-center gap-4 flex-wrap">
        <span class="bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm">Python 3.10+</span>
        <span class="bg-green-100 text-green-800 px-4 py-2 rounded-full text-sm">Flask 3.0</span>
        <span class="bg-purple-100 text-purple-800 px-4 py-2 rounded-full text-sm">Tailwind CSS</span>
    </div>
</div>
{% endblock %}
"""

# ------------------ Routes ------------------
@app.route('/')
def home():
    return render_template_string(HOME_HTML, base_template=BASE_HTML)

@app.route('/about')
def about():
    return render_template_string(ABOUT_HTML, base_template=BASE_HTML)

# Custom error pages
@app.errorhandler(404)
def not_found(e):
    return "<h1>404</h1><p>Bhai, ye page nahi mila!</p>", 404

@app.errorhandler(500)
def server_error(e):
    return "<h1>500</h1><p>Internal Server Error! Kuch to gadbad hai.</p>", 500

# ------------------ Run Server ------------------
if __name__ == '__main__':
    # Production ke liye Waitress use karo (optional)
    try:
        from waitress import serve
        print("🔥 Production server (Waitress) chal raha hai on http://localhost:5000")
        serve(app, host='0.0.0.0', port=5000)
    except ImportError:
        # Agar Waitress nahi hai toh Flask ka built-in use karo
        print("⚠️ Waitress installed nahi hai, Flask dev server use ho raha hai.")
        app.run(debug=True, host='0.0.0.0', port=5000)